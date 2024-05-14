from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status

from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist

from users.v1.serializers import UserSerializer
from users.models import CustomUser


class UserRegistrationAPIView(APIView):
    """
    View for handling user registration.
    """
    serializer_class = UserSerializer
    response_data = dict()

    def post(self, request):
        """
        method will register user with given 
        username, email and password.
        param: username, email, password
        return: Response
        """

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            self.response_data = {
                    'status': 'Success',
                    'message': "User has been registered successfully."
                }
            return Response(self.response_data, status=status.HTTP_201_CREATED)
        self.response_data = {
                    'status': 'Failed',
                    'error': serializer.errors
                }
        return Response(self.response_data, status=status.HTTP_400_BAD_REQUEST)
    

class UserLoginAPIView(APIView):
    """
    View for handling user authentication
    """
    response_data = dict()

    def post(self, request):
        """
        Method will authenticate the user after validating the username and password.
        After successfull authentication api will returns a token generated. 
        for authenticated user which will be passed along with every authorized request.
        param: username, password.
        return: Response
        """
        
        username = request.data.get('username')
        password = request.data.get('password')

        user = None
        if '@' in username:
            try:
                user = CustomUser.objects.get(email=username)
            except ObjectDoesNotExist:
                pass

        if not user:
            user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            self.response_data = {
                    'status': 'Success',
                    'token': token.key
                }
            return Response(self.response_data, status=status.HTTP_200_OK)
        
        self.response_data = {
                    'status': 'Failed',
                    'error': "Invalid credentials"
                }
        return Response(self.response_data, status=status.HTTP_401_UNAUTHORIZED)
    

class UserLogoutAPIView(APIView):
    """
    User Logout View
    """
    permission_classes = [IsAuthenticated]
    response_data = dict()

    def get(self, request):
        """
        On calling the api the token of the authorized user will be deleted from the table.
        param: request
        return: Response
        """
        try:
            request.user.auth_token.delete()
            logout(request)
            self.response_data = {
                    'status': 'Success',
                    'message': "Successfully logged out."
                }
            return Response(self.response_data, status=status.HTTP_200_OK)
        except Exception as e:
            self.response_data = {
                    'status': 'Failed',
                    'error': str(e)
                }
            return Response(self.response_data, status=status.HTTP_400_BAD_REQUEST)
        