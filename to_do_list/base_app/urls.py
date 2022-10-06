from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, UserLoginView, UserRegisterView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('create/', TaskCreate.as_view(), name='task_create'),
    path('update/<int:pk>/', TaskUpdate.as_view(), name='task_update'),
    path('delete/<int:pk>/', TaskDelete.as_view(), name='task_delete')
]