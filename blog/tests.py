from django.test                import TestCase
from .models                    import Post
from django.core.urlresolvers   import reverse


def create_post(title, slug, published=True):
    """
    Create a post with specific title and slug and published (boolean)
    """
    return Post.objects.create(title=title, slug=slug, published=published)
    
class PostMethodTests(TestCase):
    def test_absoluse_url_exist(self):
        """
        test if get_absolue_url return right url
        """
        post = Post.objects.create(slug='test_slug')
        self.assertEqual(post.get_absolute_url(), reverse('blog:detail', args=(post.slug,)))

    def test_create_unpublished(self):
        """
        create an unpublished post and check if it's not displayed
        """
        create_post('test no published', 'test_no_published', False)
        self.assertEqual(Post.objects.all().count(), 1)
        self.assertEqual(Post.objects.published().count(), 0)

    def test_create_published(self):
        """
        create a published post and check if it's displayed
        """
        create_post('test published', 'test_published')
        self.assertEqual(Post.objects.all().count(), 1)
        self.assertEqual(Post.objects.published().count(), 1)

class PostViewTests(TestCase):
    def test_feed_url(self):
        response = self.client.get(reverse('blog:feed'))
        self.assertIn("xml", response['Content-Type'])
