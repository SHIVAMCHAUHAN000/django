from django.urls import path, re_path
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
    re_path(r'^regex/(?P<username>[a-zA-Z0-9_]+)/$', views.regex, name='regex'),  # Regex path for username
    path('index/',views.indexpage),
    path('about/', views.aboutme),  
]