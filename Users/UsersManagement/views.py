from .models import User
from .serializers import UserSerializer, CustomTokenObtainPairSerializer
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
class UserRegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserProfileView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    
    def get_queryset(self):
        user_id = self.request.user.__dict__["id"]

        return User.objects.filter(id=user_id)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

# TODO Create an endpoint for other services to check the validity and usability of the jwt
# TODO create update destroy api-view