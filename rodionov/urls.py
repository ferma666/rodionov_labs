from . import views
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('admin', admin.site.urls),
    path('employees', views.Professions.as_view()),
    path('roles', views.Roles.as_view()),
    # path('categories', views.ProfessionCategories.as_view())
]
