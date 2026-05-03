from django.urls import path, include
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.todo_list,name='todo_list'),
    path('delete/<int:id>/', views.delete,name='delete'),
    path('complete/<int:id>/', views.complete,name='complete'),
    
]