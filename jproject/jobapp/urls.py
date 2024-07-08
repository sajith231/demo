from django.urls import path
from . import views 


urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('job/', views.job, name='job'),
    path('about/', views.about, name='about'),
    path('signup/', views.signup_view,name='signup' ),
    path('login/', views.login_form,name='login' ),
    path('signout/', views.signout,name='signout' ),
    path('apply/<int:job_id>/', views.apply_for_job, name='apply'),
    path('success/', views.success, name='success'),
    path('readmore/', views.readmore,name='readmore' ),
    path('readmore/<int:id>/', views.readmore, name='readmore'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    
]