from django.urls import path
from . import views
app_name='todoapp'
urlpatterns = [
    path('',views.add,name='add'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('list/',views.listtask.as_view(),name='list'),
    path('detail/<int:pk>/',views.taskdetails.as_view(),name='detail'),
    path('cbvupdate/<int:pk>/',views.taskupdate.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.deletetask.as_view(),name='cbvdelete'),
]