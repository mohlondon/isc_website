from Users.forms import EditProfileForm
from Users.models import (
    CustomUser,
)

from .models import Commenters


def users_and_projects(request):
    if request.user.is_authenticated:
        user = CustomUser.objects.get(username=request.user)
        initials = {
            'first_name': request.user.first_name,
            "last_name": request.user.last_name,
            "email": request.user.email,
            "gender": request.user.gender,
            "username": request.user.username
        }
        return {
            'User': user,
            'comments': Commenters.objects.all(),
            'EditProfile': EditProfileForm(instance=request.user.profile, initial=initials)
        }
    return ''
