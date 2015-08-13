from django.db                  import models
from django.core.urlresolvers   import reverse
from django_markdown.models     import MarkdownField

class Tag(models.Model):
    slug = models.SlugField(max_length=200, unique=True)

    def __unicode__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse("blog:tagIndex", kwargs={"slug": self.slug})

class PostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(published=True)

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    description_image = models.ImageField(upload_to='images/%Y/%m/%d/')
    description = MarkdownField()
    published = models.BooleanField(default=False)
    
    body = MarkdownField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag)

    objects = PostQuerySet.as_manager()

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})

    # used to define plural name and ordering posts
    class Meta:
        verbose_name = 'blog post'
        verbose_name_plural = 'blog posts'
        ordering = ['-date_created']

    def __unicode__(self):
        return u'%s' % self.title
