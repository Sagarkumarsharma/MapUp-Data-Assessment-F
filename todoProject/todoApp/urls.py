#from django.contrib import admin
from django.urls import path
#from .import views # import views
from .views import TaskCreate, TaskDetail, TaskList, TaskUpdate, TaskDelete, CustomLoginView,RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',CustomLoginView.as_view(), name = 'login-detail'),
    path('logout/',LogoutView.as_view(next_page = 'login-detail'), name = 'logout-detail'),
    path('register/',RegisterPage.as_view(), name = 'register-detail'),
    path('', TaskList.as_view(), name = 'tasks'),
    path('task1/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('create/', TaskCreate.as_view(), name='task-create'),
    path('update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
]

"""urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.taskman, name = "tasks"), 
]
 """