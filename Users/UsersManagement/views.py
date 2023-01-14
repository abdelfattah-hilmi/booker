from .models import User
from .serializers import UserSerializer
from rest_framework.generics import CreateAPIView

class UserRegister(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer