from django.views import generic
from issue.models import Issue, Editorial, Squiggle, UpcomingSquiggle
from datetime import datetime, timedelta

def get_current_squiggle(minimal=True):
    now = datetime.today()
    first = now + timedelta(-3)
    last = now + timedelta(2)
    s = Squiggle.objects.filter(date1__range=(first, last))
    if s.count() == 1:
        return s[0]
    elif s.count() == 2:
        if abs(s[0] - now) < abs(s[1] - now):
            return s[0]
        else:
            return s[1]
    else:
        return None
def get_upcoming_squiggles():
    now = datetime.today()
    s = UpcomingSquiggle.objects.filter(last_date__gte=now)
    return s


class IssueDetail(generic.DetailView):
    model = Issue
    template_name = 'issue/issue.htm'
class IssueList(generic.ListView):
    model = Issue
    template_name = 'issue/issue_list.htm'

class SquiggleByID(generic.DetailView):
    model = Squiggle
    template_name = 'squiggle/squiggle.htm'
class SquiggleByDate(generic.DetailView):    
    model = Squiggle
    template_name = 'squiggle/squiggle.htm'
    def get_object(self, *args, **kwargs):
        year = self.kwargs['year']
        month = self.kwargs['month']
        day = self.kwargs['day']
        return self.model.objects.get(
            date1__year=year,
            date1__month=month,
            date1__day=day)

class SquigglesByYear(generic.YearArchiveView):
    model = Squiggle
    date_field = 'date1'
    make_object_list = True
    template_name = 'squiggle/squiggle_list.htm'
# TODO: Year List, Month List


class SquiggleHome(generic.ListView):
    model = Squiggle
    queryset = Squiggle.objects.all()[:4]
    template_name = 'squiggle/squiggle_index.htm'
