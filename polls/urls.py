from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'), 
    path('view_user/', views.view_user, name='view_user'),
    path('view_questions/', views.view_questions, name='view_questions'),
    path('conduct_poll/<int:question_id>/', views.conduct_poll, name='conduct_poll'),  # Update this line
    path('vote/<int:question_id>/', views.vote, name='vote'),
    path('view_results/', views.view_results, name='view_results'),
    path('view_results_single/<int:question_id>/', views.view_results_single, name='view_results_single'),
]
