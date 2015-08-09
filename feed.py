from django.contrib.syndication.views   import Feed
from .models                            import Post

class LatestPosts(Feed):
    title = "Q Blog"
    link = "/feed/"
    description = "Latest Posts of Q"

    def items(self):
        return Post.objects.published()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description
