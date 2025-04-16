from django.shortcuts import render ,get_object_or_404

from .models import Formation,FormationRegister,Modules
from students.models import Student

def affichage_formation(request):
    if request.user.is_authenticated:
        student = Student.objects.get(user = request.user)
        modules_formations = FormationRegister.objects.filter(student = student)
        formations = []   # Liste de liste de formation dans chaque module dont l'etudiant inscrit
        for module_formation in modules_formations:
            formations.append(Formation.objects.filter(module=module_formation))

        context = {"formations":formations}
        return render(request ,"students/affichage_formation.html",context)
    context = "Vous n'êtes pas inscrit"
    return render(request,'formation/accueil.html',context)


def formation_views(request):
    formations = Formation.objects.all()
    context = {
        'formations': formations,
    }
    return render(request, 'formations/formation.html', context)

def formation_module_detail(request,module_id):
    module = get_object_or_404(Modules,pk=module_id)
    context = {'module_de_formation':module}
    return render(request,'formation/formation_detail.html',context)

def formation_detail(request, formation_id):
    formation = get_object_or_404(Formation, id=formation_id)
    context = {
        'formation': formation,
    }
    return render(request, 'formations/formation_detail.html', context)
