from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from educational_service.authentication.serializers import UserRegisterSerializer


class UserRegistrationView(APIView):
    authentication_classes = []
    serializer_class = UserRegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)