from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task
#for the create view
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
#revers_lazy redirect us on the certain part of our page or application
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.views import LoginView

from django.contrib.auth.forms import UserCreationForm #built-in form
from django.contrib.auth import login

class CustomLoginView(LoginView):
    template_name = 'todoApp/login.html'
    fields = '__all__'
    redirect_authenticated_user: True

    def get_success_url(self):
        return reverse_lazy('tasks')

    
    #redirect on the tasks if current user logged in
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(CustomLoginView, self).get(*args, **kwargs)    


class RegisterPage(FormView):
    template_name = 'todoApp/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')  
    
    #redirect user when the form is submitted
    def form_valid(self, form): 
        user = form.save() #when form is save so return value is gonna be the user
        if user is not None: #if user successfully created
            login(self.request, user) #then go ahead and use the login function
        return super(RegisterPage, self).form_valid(form)      
    
    #redirect on the tasks if current user has been registered
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args, **kwargs)



class TaskList(LoginRequiredMixin, ListView):  #we wanna restrict our tasklist
    model = Task  #listview requires a model or query se t
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user = self.request.user)
        context['count'] = context['tasks'].filter(complete = False).count()
        return context

    #logic for searching
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(
               title__icontains=search_input)  #__contains its loo for the string but with case-insensitive

        context['search_input'] = search_input

        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = "task"
    template_name = 'todoApp/task.html'

class TaskCreate(LoginRequiredMixin, CreateView): #create view to create a new item
    model = Task
    fields = ['title', 'description', 'complete']
    #fields = '__all__' # we wann list out all the item
    success_url = reverse_lazy('tasks')  #resolving django url names into url paths,after performing operation we have to go back on user


    def form_valid(self, form): #creation will not be override
        form.instance.user = self.request.user #logged in user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView): #to update the task
    model = Task
    fields = ['title', 'description', 'complete']
    #fields = '__all__'
    success_url = reverse_lazy('tasks')


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')








#import httpresponse
#from django.http import HttpResponse

#Create your views here.
#function base view
#def taskman(request):
#return HttpResponse("<h1>Task Man Application</h1>")