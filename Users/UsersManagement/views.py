from .models import User
from .serializers import UserSerializer
from rest_framework.generics import ListCreateAPIView

class UserRegister(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# TODO Create an endpoint for other services to check the validity and usability of the jwt