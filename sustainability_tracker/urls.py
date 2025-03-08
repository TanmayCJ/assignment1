from django.contrib import admin
from django.urls import path
from actions import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/actions/', views.get_actions),
    path('api/actions/add/', views.add_action),
    path('api/actions/<int:action_id>/', views.update_action),
    path('api/actions/<int:action_id>/delete/', views.delete_action),
]