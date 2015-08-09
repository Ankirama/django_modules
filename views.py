from django.shortcuts   import render, get_object_or_404
from django.views       import generic
from .                  import models

class TagMixin(object):
    def get_tags(self):
        return models.Tag.objects.all()

    def get_context_data(self, **kwargs):
        context = super(TagMixin, self).get_context_data(**kwargs)
        context['tags'] = self.get_tags()
        return context

class BlogIndex(TagMixin, generic.ListView):
    queryset = models.Post.objects.published()
    template_name = "blog/index.html"
    paginate_by = 2

class BlogDetail(TagMixin, generic.DetailView):
    model = models.Post
    template_name = "blog/post.html"

class TagIndex(generic.ListView):
    template_name = "blog/index.html"
    paginate_by = 5

    def get_queryset(self):
        slug = self.kwargs['slug']
        tag = models.Tag.objects.get(slug=slug)
        results = models.Post.objects.filter(tags=tag)
        return results
