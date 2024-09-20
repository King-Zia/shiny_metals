from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello),
    path('getData/', views.getData, name="getData"),
    path('process_selection/', views.process_selection, name='process_selection'),

]
