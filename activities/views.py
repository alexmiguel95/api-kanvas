from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import ActivitiesSerializer
from .permissions import InstructorOrFacilitadorOnly
from .models import Activity
from accounts.models import User
# import ipdb


class ActivitiesView(APIView):
    permission_classes = [IsAuthenticated, InstructorOrFacilitadorOnly]
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        serializer = ActivitiesSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
               serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        repo = request.data["repo"]
        user_id = request.data["user_id"]

        # Verificar se o user_id é do usuario logado
        user = User.objects.get(id=user_id)
        if user.username != request.user.username:
            return Response(
                {"message": "Invalid user_id"},
                status=status.HTTP_400_BAD_REQUEST
            )

        activity = Activity.objects.create(repo=repo, user_id=user)

        serializer = ActivitiesSerializer(activity)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request):
        id = request.data.get('id')
        user_id = request.data.get('user_id')
        repo = request.data.get('repo')
        grade = request.data.get('grade')

        # Verificar se os ids passados existem
        try:
            activity = Activity.objects.get(id=id)
            user = User.objects.get(id=user_id)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        activity.repo = repo
        activity.grade = grade
        activity.user_id = user
        activity.save()

        serializer = ActivitiesSerializer(activity)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
