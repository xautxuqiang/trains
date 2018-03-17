from django.urls import path

from . import views

app_name = 'graph'
urlpatterns = [
    path('', views.index, name='index'),
    path('graphDisplay/', views.graph_display, name='graphDisplay'),
    path('pathLength/', views.path_length, name='pathLength'),
    path('shortestPath/', views.shortest_path, name='shortestPath'),
    path('allPath/', views.all_path, name='allPath'),
    path('lessTimes/', views.less_times, name='lessTimes'),
    path('equalTimes/', views.equal_times, name='equalTimes'),
    path('lessDistance/', views.less_distance, name='lessDistance'),
]
