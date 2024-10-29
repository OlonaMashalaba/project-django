from django.urls import path
from . import views

app_name = 'candidates'

urlpatterns = [
    path('', views.home, name='home'),
    path('candidates/', views.candidate_list, name='candidate_list'),
    path('candidates/<int:candidate_id>/', views.candidate_detail, name='candidate_detail'),
]


