from .models import ProfileConsultant
from .models import ProfileUser
from .forms import UserProfileForm
from .forms import ConsultantProfileForm

def get_profile_user(request):
    profile = None
    if request.user.is_consultant:
        if hasattr(request.user, 'profileconsultant'):
            profile = request.user.profileconsultant
        else:
            profile = ProfileConsultant.objects.create(user=request.user)
    else:
        if hasattr(request.user, 'profileuser'):
            profile = request.user.profileuser
        else:
            profile = ProfileUser.objects.create(user=request.user)
    return profile

def get_profile_or_none(request):
    profile = None
    if request.user.is_consultant:
        if hasattr(request.user, 'profileconsultant'):
            profile = request.user.profileconsultant
    else:
        if hasattr(request.user, 'profileuser'):
            profile = request.user.profileuser
    return profile

def get_profile_forms(request):
    if request.user.is_consultant:
        form = ConsultantProfileForm
    else:
        form = UserProfileForm
    return form

def get_template_profile(request):
    if request.user.is_consultant:
        urlredirect = "users/profile.html"
    else:
        urlredirect = "users/profile_user.html"
    return urlredirect


def get_profile_context(request):
    context = {}
    if hasattr(request.user, 'profileuser'):
        height = request.user.profileuser.height 
        heightm= request.user.profileuser.height / 100
        weight = request.user.profileuser.weight
        imd = weight / (heightm * heightm)
        diver = 2
        if (request.user.profileuser.sex == "M"):
            diver = 4
        idealweight = (height - 100) - (height-150)/diver
        waterNormal = weight/450*14
        context = {'imd':round(imd, 2), 'idealWeight':round(idealweight,2), 'waterNormal':round(waterNormal,2)}
    return context
