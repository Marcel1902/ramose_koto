from django.shortcuts import render ,get_object_or_404

from .models import Formation

def formation_views(request):
    formations = Formation.objects.all()
    context = {
        'formations': formations,
    }
    return render(request, 'formations/formation.html', context)

def formation_detail(request, formation_id):
    formation = get_object_or_404(Formation, id=formation_id)
    context = {
        'formation': formation,
    }
    return render(request, 'formations/formation_detail.html', context)
