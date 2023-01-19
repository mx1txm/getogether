from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.models import User
from .models import Post
from .forms import FilterForm, PostForm, AnzeigeForm
from .filters import ProductFilter


def index(request):  # home
    return render(request, 'landingpage.html', {})


def angebote(request):
    context = {
        'posts': Post.objects.all
    }
    return render(request, 'angebote.html', context)


def angebotsprofil(request):
    return render(request, 'angebotsprofil.html', {})


def nutzerprofil(request):
    return render(request, 'nutzerprofil.html', {})


def vereinsmarketing(request):
    return render(request, 'vereinsmarketing.html', {})


def anzeige_new(request):
    #form = PostForm()

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PostForm()
    return render(request, 'anzeige_new.html', {'form': form})

#new
def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = AnzeigeForm(request.POST)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, 'anzeige_new.html', context)


def list_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["dataset"] = AnzeigeForm.objects.all()

    return render(request, 'angebote.html', context)

#new end

def items(request):
    items = Post.objects.get(pk=request.GET.get('value'))
    # return render(request, 'filter_list.html', {'item': items})
    return render(request, 'angebotsprofil.html', {'item': items})


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'category', 'weekday']
    print("Inside PostCreateView")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostListView(ListView):
    model = Post
    template_name = 'vereinsapp/angebote.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']  # ordering posts from latest to oldest

    def get_queryset(self):
        qs = self.model.objects.all()
        print(qs)

        return render(self.template_name, qs)



class PostDetailView(DetailView):
    model = Post


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'category', 'weekday']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):  # prevent that a user can update other users posts
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):  # prevent that a user can update other users posts
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class FilterView(TemplateView):
    template_name = 'vereinsapp/angebote.html'

    def filter(self, request):  # get request
        form = FilterForm(request.GET)
        form.save()
        posts = Post.objects.all()
        title_contains = request.GET.get('title_contains')
        myFilter = ProductFilter(request.GET, queryset=posts)
        posts = myFilter.qs

        return render(request, self.template_name, posts)


class CreateView(TemplateView):
    template_name = 'vereinsapp/anzeige_new.html'
    print("Inside Create View")

    def post(self, request):
        print("Inside def post")
        form = PostForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['post']
            post = form.save()
            post.save()
            form = PostForm()
            post = form.save()
            return redirect('post:posts')

        args = {'form': form}
        return render(request, self.template_name, args)
