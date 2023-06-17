from django.views.generic import ListView, DetailView, \
    CreateView, UpdateView, DeleteView

from .models import Post
from .filters import PostFilter
from .forms import PostForm


class PostList(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    ordering = ['-id']
    paginate_by = 10


class PostSearch(ListView):
    model = Post
    template_name = 'post_search.html'
    context_object_name = 'posts_search'
    ordering = ['-id']
    paginate_by = 10

    def get_filter(self):
        return PostFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        qs = self.get_filter().qs
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        filter = self.get_filter()
        context['filter'] = filter

        filter_params = ""
        for f_name in [str(k) for k in filter.filters]:
            if f_name in filter.data:
                filter_params += f"&{f_name}={filter.data[f_name]}"
        context['filter_params'] = filter_params

        return context


# class PostDetail(DetailView):
#     model = Post
#     template_name = 'post.html'
#     context_object_name = 'post'


class PostDetail(DetailView):
    template_name = 'flatpages/post_detail.html'
    queryset = Post.objects.all()


class PostCreateView(CreateView):
    template_name = 'flatpages/post_create.html'
    form_class = PostForm


class PostUpdateView(UpdateView):
    template_name = 'flatpages/post_create.html'
    form_class = PostForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDeleteView(DeleteView):
    template_name = 'flatpages/post_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'