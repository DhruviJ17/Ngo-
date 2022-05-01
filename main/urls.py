from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('admin/<str:pk>', views.admin, name='admin'),
    path('requirementform/<str:pk>', views.requirementform, name='requirementform'),
    path('ngo_list/', views.ngo_list, name='ngo_list'),
    path('summary/<str:pk>', views.summary, name='summary'),
    path('tabular/<str:pk>', views.tabular, name='tabular'),
    path('user/<str:pk>', views.user_requirements, name='user'),
    path('user/<str:pk>/<str:cat>', views.user_requirements_category, name='user_category'),
    path('donation/<str:pk>', views.donation, name='donation'),
    # path('logout', views.logoutUser, name='logout'),
]
