from kalchakra_app import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('personality/', views.personality_view, name='personality'),
]
