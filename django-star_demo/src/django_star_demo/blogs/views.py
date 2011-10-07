from django.views.generic import DetailView
from django.views.generic import ListView

from models import Entry

class EntryDetailView(DetailView):
    model = Entry
    slug = 'title'

class EntryListView(ListView):
    model = Entry