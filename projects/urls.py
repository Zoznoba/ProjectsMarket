from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name='projects_list'),
    path('project/<str:pk>/', views.project, name='project_detail'),
    path('create-project/', views.createProject, name="create-project"),
    path('update-project/<str:pk>', views.updateProject, name='update-project'),
    path('delete-project/<str:pk>/', views.deleteProject, name='delete-project'),
    path('tag/<slug:tag_slug>', views.projects_by_tag, name="filter_by_tag"),

]
