from django.shortcuts import render
from django.views.generic import    (ListView,
                                     DetailView,
                                     CreateView,
                                     UpdateView,
                                     DeleteView,
                                                 )
from .models import Blog
# Create your views here.

class BlogListView(ListView):
    model = Blog
    template_name = 'blog/allblogs.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'blogs' #dictionary ko keyword jastai bhayo aba
    ordering = ['-pub_date']



class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/detail.html'
    context_object_name = 'blog' #dictionary ko keyword jastai bhayo aba

class BlogCreateView(CreateView):
    model = Blog
    fields = '__all__' #Creates form with these fields
    template_name = 'blog/blog_entry.html'
    success_url = '/blog/'

    def form_valid(self, form):
        #if any changes is to be made..its the place to write
        return super().form_valid(form)

class BlogUpdateView(UpdateView):
    model = Blog
    fields = '__all__' #Creates form with these fields
    template_name = 'blog/blog_entry.html'
    success_url = '/blog/'


    def form_valid(self, form):
        #if any changes is to be made..its the place to write
        return super().form_valid(form)

class BlogDeleteView(DeleteView): 
    model = Blog
    fields = '__all__'
    success_url='/blog/'
    template_name = 'blog/confirm_delete.html'