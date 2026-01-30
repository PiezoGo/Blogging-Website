from .models import Post, Tag


def sidebar_context(request):
    return {
        'recent_sidebar_posts': Post.objects.all()[:5],
        'sidebar_tags': Tag.objects.all()[:15],
    }
