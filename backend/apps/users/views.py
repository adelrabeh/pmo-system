from common.mixins import SecureModelViewSet
from .models import User
from .serializers import UserSerializer
class UserViewSet(SecureModelViewSet):
    queryset = User.objects.all().order_by("id")
    serializer_class = UserSerializer
    search_fields = ["username", "email", "full_name_ar"]
