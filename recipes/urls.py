from django.urls import path
from recipes.views import home
from recipes import views



urlpatterns = [
    path('', home),
    # no django so de por o <id> serve como parmetro para o recipes
    path('recipes/<int:id>/', views.recipes),
]
