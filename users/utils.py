from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Profile

def searchProfiles(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    profiles = Profile.objects.distinct().filter(
        Q(name__icontains = search_query)
    )
    return profiles, search_query