"""views for the user api"""
from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from user.serializers import(
    UserSerializer,
    AuthTokenSerializer,
)


class CreateUserView(generics.CreateAPIView):
    """create user in the system"""
    """createAPIView handles http post requests thats designed for
    creating objects in the db"""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """create new auth token for user"""
    serializer_clas = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """RetrieveUpdateAPIView is proided by the django rest frameowrk to provide
    funtionailty needed for retreiving and updating objets in the database """
    """Manage authenticated user"""
    serializer_class = UserSerializer
    authentcation_classes = [authentication.TokenAuthentication]
    """"permission classes we jknow who the user is what is it that user
    is allowed to do in our system? Want user to be authenticated. no other
    restrictions"""
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """retrieve and reutrn authenticated user"""
        """when user is auth the user object is assigned to the request object
        available in the view"""
        return self.request.user