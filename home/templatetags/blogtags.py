from django import template
from wagtail.users.models import UserProfile
from wagtail.users.utils import get_gravatar_url

from blog.models import BlogIndexPage, BlogPage

register = template.Library()


@register.inclusion_tag('blog/blog_index_page.html', takes_context=True,)
def last_entry(context, page):
    page_data = BlogIndexPage.objects.child_of(page).live().select_related('owner').first()
    if page_data:
        entries = BlogPage.objects.child_of(page_data).live().order_by(
            '-latest_revision_created_at').select_related('owner').order_by('-date')
        if entries:
            entries = entries[:3]
        context['blogpages'] = entries
    return context


@register.simple_tag
def user_image(user):
    user_information = UserProfile.objects.filter(user=user).first()
    if user_information and user_information.avatar:
        return user_information.avatar.url
    else:
        return get_gravatar_url(user.email)
