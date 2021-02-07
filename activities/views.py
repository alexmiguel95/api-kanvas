from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from django.contrib.auth import authenticate
# from rest_framework.authtoken.models import Token
from .serializers import ActivitiesSerializer
# Anotar essa parte, agora não é mais do user direto
# from .models import Activity


class ActivitiesView(APIView):
    def post(self, request):
        serializer = ActivitiesSerializer(request.data)

        if not serializer.is_valid():
            return Response(
               serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
        # ipdb.set_trace()
        # activity = Activity.objects.create(
        #     **request.data, user_id=request.user
        # )
