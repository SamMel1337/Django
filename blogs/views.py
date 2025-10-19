from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import BlogPost

# Список постов
class BlogListView(ListView):
    model = BlogPost
    template_name = 'blogs/blog_list.html'
    context_object_name = 'posts'
    queryset = BlogPost.objects.filter(published=True)

# Детальный просмотр поста с увеличением счетчика просмотров
class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blogs/blog_detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        # Увеличение счетчика просмотров
        self.object.views_count += 1
        self.object.save(update_fields=['views_count'])
        return response

# Создание нового поста
class BlogCreateView(CreateView):
    model = BlogPost
    fields = ['title', 'content', 'published']
    template_name = 'blogs/blog_create.html'

    def get_success_url(self):
        return self.object.get_absolute_url()

# Обновление поста
class BlogUpdateView(UpdateView):
    model = BlogPost
    fields = ['title', 'content', 'published']
    template_name = 'blogs/blog_form.html'

    def get_success_url(self):
        return self.object.get_absolute_url()

# Удаление поста с подтверждением
class BlogDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blogs/blog_confirm_delete.html'
    success_url = reverse_lazy('blogs:blog_list')
