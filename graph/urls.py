from django.urls import path

from . import views

app_name = 'graph'
urlpatterns = [
    path('', views.index, name='index'),
    path('graphDisplay/<str:graph>/', views.graph_display, name='graphDisplay'),
    path('pathLength/<str:graph>/', views.path_length, name='pathLength'),
    path('shortestPath/<str:graph>/', views.shortest_path, name='shortestPath'),
    path('allPath/<str:graph>/', views.all_path, name='allPath'),
    path('lessTimes/<str:graph>/', views.less_times, name='lessTimes'),
    path('equalTimes/<str:graph>/', views.equal_times, name='equalTimes'),
    path('lessDistance/<str:graph>/', views.less_distance, name='lessDistance'),
]
