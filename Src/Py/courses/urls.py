from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('<int:course_id>/', views.course_detail, name='course_detail'),
    path('create_course/', views.create_course, name='create_course'),
    path('<int:course_id>/create_section/', views.create_section, name='create_section'),
    path('<int:course_id>/create_final/', views.create_final, name='create_final'),
] 