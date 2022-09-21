from django.shortcuts import render

from django_app.models import Post
#from django.http import HttpResponse  #comment out it because we are using render
# Create your views here.

#import class base views
from django.views.generic import (ListView, 
                                  DetailView, 
                                  CreateView,
                                  UpdateView,
                                  DeleteView,
                                  )

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

#dummy data
"""posts = [

    {
        'Author': 'Sagar Kumar Sharma',
        'Title' : 'Blog Post 1',
        'Content' : 'First Post Content',
        'Date_Posted' : 'September 5, 2022'
    },
    {
        'Author': 'Sumit Pundir',
        'Title' : 'Blog Post 2',
        'Content' : 'Second Post Content',
        'Date_Posted' : 'September 7, 2022'
    }
]
we dont need of dummy data so we can comment out it
"""


#create function for routing 
def home(request):
    #return HttpResponse('<h1>Home Blog</h1> ')
    context = {
        'posts': Post.objects.all() #addiing posts through database not by dummy data
        #'posts' : posts
    }
    return render(request, 'django_app/home.html', context)  #request a argument by the help of django shortcut
    #still render function will return httpresponse in the background


#class based view
class PostListView(ListView):
    model = Post
    template_name = 'django_app/home.html' #'<app>/<model>_<viewtype>.html'
    context_object_name = 'posts'
    ordering = ['-Date_Posted']

class PostDetailView(DetailView):  #go to on an individual post
    model = Post


#create a post
class PostCreateView( LoginRequiredMixin, CreateView ):
    model = Post
    fields = ['Title', 'Content']    
    
    def form_valid(self, form):
        form.instance.Author = self.request.user
        return super().form_valid(form)  #form valid method on our parent class


#update a post
class PostUpdateView( LoginRequiredMixin, UserPassesTestMixin, UpdateView ):
    model = Post
    fields = ['Title', 'Content']    
    
    def form_valid(self, form):
        form.instance.Author = self.request.user
        return super().form_valid(form)  #form valid method on our parent class
   
    def test_func(self):
        post = self.get_object() #current post that we trying to update
        if self.request.user == post.Author: #current user author of the post
            return True
        return False



class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):  # delete view
    model = Post
    success_url = '/'
    
    def test_func(self):
        post = self.get_object() #current post that we trying to delete
        if self.request.user == post.Author: #current user author of the post
            return True
        return False


def about(requests):
    #return HttpResponse('<h3>Hello Welcome to the About Page</h3>')
    return render(requests, 'django_app/about.html',{'title':'ABOUT'})

  