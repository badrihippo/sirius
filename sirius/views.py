from django.shortcuts import render_to_response
from issue.views import get_current_squiggle, get_upcoming_squiggles
def home(request):
    return render_to_response('base.html',{
        'csquig':get_current_squiggle(),
        'upcoming_squiggles': get_upcoming_squiggles()})
