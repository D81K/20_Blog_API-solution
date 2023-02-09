from django.dispatch import receiver
from django.db.models.signals import pre_save
from .models import Post
from django.template.defaultfilters import slugify
import uuid


def get_random_code():
    code = str(uuid.uuid4())[:11].replace('-', '')
    return code

@receiver(pre_save, sender=Post)
def add_slug(sender, instance, **kwargs):
    if not instance.slug:
        slug_text = slugify(instance.title + ' ' + get_random_code())
        while Post.objects.filter(slug=slug_text).exists():
            slug_text = slugify(instance.title + ' ' + get_random_code())
        instance.slug = slug_text