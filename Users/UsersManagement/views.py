from .models import User
from .serializers import UserSerializer
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

class UserRegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserProfileView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    
    def get_queryset(self):
        user_id = self.request.user.__dict__["id"]

        return User.objects.filter(id=user_id)





# TODO Create an endpoint for other services to check the validity and usability of the jwt
# TODO create update destroy api-view