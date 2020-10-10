from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from .models import Groups, Students
from .forms import StudentsForm, GroupForm
from django.contrib import messages


def index(request):
    return render(request, "base.html")


def groupsMenu(request):
    grupos = Groups.objects.all()
    return render(request, "groups.html", {"grupos": grupos})


def newGroup(request):
    form = GroupForm()
    if request.method == "POST":

        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/grupos") # /grupos/nuevo/lista
    context = {"form": form}
    return render(request, "new_group.html", context)


def updateGroup(request, pk):
    grupo = Groups.objects.get(id=pk)
    form = GroupForm(instance=grupo)
    if request.method == "POST":

        form = GroupForm(request.POST, instance=grupo)
        if form.is_valid():
            form.save()
            return redirect("/grupos")

    context = {"form": form}
    return render(request, "new_group.html", context)


def deleteGroup(request, pk):
    grupo = Groups.objects.get(id=pk)
    if request.method == "POST":
        grupo.delete()
        return redirect("/grupos")
    context = {"grupo": grupo}
    return render(request, "delete_group.html", context)


def newStudent(request):
    form = StudentsForm()
    if request.method == "POST":
        form = StudentsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Alumno agregado exitosamente! Puedes seguir agregando más alumnos.')
            return redirect("/grupos/nuevo/alumnos/") # /grupos/nuevo/alumnos

    alumnos = Students.objects.all()
    context = {"form": form, "alumnos": alumnos}
    return render(request, "new_list.html", context)


def groupList(request, pk):
    grupo = Groups.objects.get(id=pk)
    alumnos = Students.objects.filter(group=grupo).order_by("last_name")
    return render(request, "group_list.html", {"alumnos": alumnos, "grupo": grupo})

