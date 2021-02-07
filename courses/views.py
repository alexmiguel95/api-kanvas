from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Course
from accounts.models import User
from .serializers import CourseSerializer
from rest_framework import status
from .permissions import InstructorOnly


class CourseView(APIView):
    permission_classes = [InstructorOnly]
    # queryset = Course.objects.none()
    authentication_classes = [TokenAuthentication]

    """ Criar um novo curso."""
    def post(self, request):
        serializer = CourseSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        # Crie um curso se ele já não existir.
        course, is_created_course = Course.objects.get_or_create(
            name=request.data["name"]
        )

        if is_created_course:
            serializer = CourseSerializer(course)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(
            {"message": f"{request.data['name']} already exists"},
            status=status.HTTP_400_BAD_REQUEST
        )

    def get(self, request):
        queryset = Course.objects.all()
        serializer = CourseSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CourseUpdateView(APIView):
    permission_classes = [IsAuthenticated, InstructorOnly]
    authentication_classes = [TokenAuthentication]

    def put(self, request):
        course_id = request.data.get('course_id')
        user_ids = request.data.get('user_ids')

        if not isinstance(course_id, int):
            return Response(
                {"message": "Enter the course id"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if not isinstance(user_ids, list):
            return Response(
                {"message": "Enter the list of student ids"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            course = Course.objects.get(id=course_id)
        except ObjectDoesNotExist:
            return Response(
                {
                    "message":
                        f"Course id {request.data['course_id']} not exist"
                },
                status=status.HTTP_404_NOT_FOUND
            )

        # Verificar se todos os IDs passados existem
        users = []
        for user_id in user_ids:
            try:
                user = User.objects.get(id=user_id)
                users.append(user)
            except ObjectDoesNotExist:
                return Response(
                    {'message': f'Student id {user_id} not exist'},
                    status=status.HTTP_404_NOT_FOUND
                )

        # Fazer a o relacionamento N:N
        for user in users:
            course.user_set.add(user)

        # Apagar todas as associações entre Users e Courses que não estão na
        # lista user_ids.
        associated_users = course.user_set.all()
        for user in associated_users:
            if user.id not in user_ids:
                course.user_set.remove(user)

        serializer = CourseSerializer(course)
        return Response(serializer.data, status=status.HTTP_200_OK)
