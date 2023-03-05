from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.models import User
from .models import Post
from .forms import FilterForm, PostForm
from .filters import ListingFilter


def index(request):  # home
    return render(request, 'landingpage.html', {})


def angebote(request):
    posts = Post.objects.all()
    listing_filter = ListingFilter(request.GET, queryset=posts)
    context = {
        'posts': posts,
        'listing_filter': listing_filter
    }

    return render(request, 'angebote.html', context)


def is_valid_queryparam(param):
    return param != '' and param is not None


def filter_list(request):#BootstrapFilterView(request)
    qs = Post.objects.all()
    categories = Post.category
    city = Post.city_choices
    bezirk = Post.berlin_bezirk
    weekday = Post.weekday_choices

    title_contains_query = request.GET.get('title_contains')
    categories_query = request.GET.get('category')
    city_query = request.GET.get('city')
    bezirk_query = request.GET.get('berlin_bezirk')
    weekday_query = request.GET.get('weekday')

    #Title
    if title_contains_query != '' and title_contains_query is not None:
        qs = qs.filter(title__icontains=title_contains_query)

    #category
    if is_valid_queryparam(categories_query) and categories_query != 'Choose...':
        qs = qs.filter(category__iexact=categories_query)

    #city
    if is_valid_queryparam(city_query) and city_query != 'Choose...':
        qs = qs.filter(city__iexact=city_query)

    #bezirk
    if is_valid_queryparam(bezirk_query) and bezirk_query != 'Choose...':
        qs = qs.filter(bezirk__iexact=bezirk_query)

    #weekday
    if is_valid_queryparam(weekday_query) and weekday_query != 'Choose...':
        qs = qs.filter(weekday__iexact=weekday_query)

    context = {
        'queryset': qs,
        'weekday': weekday,
        'category': categories,
        'bezirk': bezirk,
        'city': city,
    }

    return render(request, 'filtered_list.html', context)

def nutzerprofil(request):
    return render(request, 'nutzerprofil.html', {})


def vereinsmarketing(request):
    return render(request, 'vereinsmarketing.html', {})


def anzeige_new(request):

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PostForm()
    return render(request, 'anzeige_new.html', {'form': form})


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'beschreibung', 'category', 'bezirk', 'city', 'weekday', 'titelbild']

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
    template_name = 'post_detail.html'

    def postdetail(request):
        posts = Post.objects.get(pk=request.GET.get('value'))
        # return render(request, 'filter_list.html', {'item': items})
        return render(request, 'post/<int:pk>/', {'item': posts})


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    #template_name = 'post_detail.html'
    template_name = 'post_update.html'
    fields = ['title', 'beschreibung', 'category', 'bezirk', 'city', 'weekday', 'titelbild']

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
    template_name = 'post_confirm_delete.html'
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
        #title_contains = request.GET.get('title_contains')
        filtered = ListingFilter(request.GET, queryset=posts)
        filtered_posts = filtered.qs

        return render(request, self.template_name, filtered_posts)


class CreateView(TemplateView):
    template_name = 'vereinsapp/anzeige_new.html'

    def post(self, request):
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