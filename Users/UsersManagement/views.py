from .models import User
from .serializers import UserSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

class UserRegisterView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserProfileView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
    queryset = User.objects.filter(id='1')





# TODO Create an endpoint for other services to check the validity and usability of the jwt