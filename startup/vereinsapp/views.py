from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.models import User
from .models import Post#, #Category,Item
from .forms import FilterForm
from .filters import ProductFilter

def index(request):
    return render(request, 'landingpage.html', {})

def angebote(request):

    return render(request, 'angebote.html', {})

def angebotsprofil(request):

    return render(request, 'angebotsprofil.html', {})

def nutzerprofil(request):

    return render(request, 'nutzerprofil.html', {})

def vereinsmarketing(request):

    return render(request, 'vereinsmarketing.html', {})

def anzeige_new(request):

    return render(request, 'anzeige_new.html', {})



def items(request):
    items = Post.objects.get(pk=request.GET.get('value'))
    return render(request, 'filter_list.html', {'item': items})

class PostListView(ListView):
    model = Post
    template_name = 'vereinsapp/angebote.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted'] #ordering posts from latest to oldest

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'city', 'category']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'city', 'category']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self): #prevent that a user can update other users posts
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self): #prevent that a user can update other users posts
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class FilterView(TemplateView):
    template_name = 'vereinsapp/angebote.html'

    def filter(self, request): #get request
        form = FilterForm(request.GET)
        form.save()
        posts = Post.objects.all()
        title_contains = request.GET.get('title_contains')
        myFilter = ProductFilter(request.GET, queryset=posts)
        posts = myFilter.qs

        return render(request, self.template_name, posts)

    def post(self, request):
        form = FilterForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['post']
            post = form.save()
            post.save()
            form = FilterForm()
            post = form.save()
            return redirect('filter:filter')

        args = {'form': form}
        return render(request, self.template_name, args)