from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Tag, Review
from .forms import ProjectForm

# Create your views here.


def createProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects_list')
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)


def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects_list')
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)


def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects_list')
    context = {'project': project}
    return render(request, 'projects/project-delete.html', context)


def projects_by_tag(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    projects = Project.objects.filter(tags__in=[tag])
    context = {'projects': projects}
    return render(request, 'projects/projects-list.html', context)


def project(request, pk):
    currentProject = Project.objects.get(id=str(pk))
    tags = currentProject.tags.all()
    return render(request, "projects/project-detail.html", {'project': currentProject})


def projects(request):
    ProjectsList = Project.objects.all()
    return render(request, "projects/projects-list.html", {'projects': ProjectsList})
