from django.urls import path
from . import views
urlpatterns = [
    path('hello/', views.hellofunction, ),
    path('why/', views.mydictionary),
    path('list/', views.listfunction),
    path('showname/<str:name>', views.showname),
    path('sum/<int:a>/<int:b>/', views.sum),
    path('getval/', views.getval),
    path('add/', views.add),
    path('calculator/', views.calculator),
    path('json/', views.json),  # Added path for JSON response
    path('apidata/', views.apidata),  # Added path for API data
]