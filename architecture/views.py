from django.shortcuts import render,get_object_or_404
from .models import Architecture
# Create your views here.
def architecture_detail(request, id):
    architecture = get_object_or_404(Architecture, id=id)
    context = {}
    context['architecture'] = architecture
    return render(request,"architecture_detail.html", context)


def architecture_list(request):
    architectures = Architecture.objects.all()
    context = {}
    context['architectures'] = architectures
    return render(request,"architecture_list.html", context)


def test(request,id):
    context = {}
    return render(request,"test.html",context)
