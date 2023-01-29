from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView

from trainer.models import Trainer


class HomeTemplateView(TemplateView):
    template_name = 'home/home.html'  # specificam calea catre pagina .html pentru aceasta clasa

def search(request):
    search = request.GET.get('search')
    if search:
        all_entries = Trainer.objects.filter(Q(course__icontains=search) | Q(first_name__icontains=search)) # cu si & iar cu not cu exclude
    else:
        all_entries = Trainer.objects.all()

    return render(request, 'search.html', {'entries': all_entries})


