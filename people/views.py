from django.views import generic
from people.models import Person
class PersonDetail(generic.DetailView):
    model = Person
    template_name = 'people/person.htm'
class PersonList(generic.ListView):
    model = Person
    template_name = 'people/person_list.htm'
