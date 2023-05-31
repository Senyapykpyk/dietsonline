from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from users.models import ProfileConsultant, SiteUser
from django.db.models import Prefetch
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'home/index.html', {})


@login_required
def dietolog_list(request):
    # dietologs_profile = SiteUser.objects.prefetch_related(
    #     Prefetch(
    #         "profileconsultant",
    #         queryset=ProfileConsultant.objects.filter(is_activate=True),
    #         to_attr="profileconsultant_activate",
    #     )
    # )
    # dietologs_profile = SiteUser.objects.select_related("profileconsultant").filter(is_activate=True)
    dietologs_profile = ProfileConsultant.objects.filter(is_activate=True)
    context = {'diet_profile':dietologs_profile}
    return render(request, 'home/dietolog_list.html', context)

@login_required
def dietolog_profile(request, dietolog_id):
    dietolog_obj = get_object_or_404(ProfileConsultant, is_activate=True, user_id=dietolog_id)
    return render(request, "users/profile_id.html", {"dietolog": dietolog_obj})


def calc_bzhu(request):
    return render(request, "home/calc_bzhu.html")
def about(request):
    return HttpResponse('<h1>about</h1>')
# Create your views here.
