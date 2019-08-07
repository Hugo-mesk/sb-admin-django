# from django.utils.translation import ugettext_lazy as _
# from django.db import models
# from django.utils.text import slugify
#
# # Create your models here.
# class Page(models.Model):
#
#     title = models.CharField(verbose_name=_('title'),
#                              max_length=60)
#     menu_titles = models.CharField(verbose_name=_('menu_title'),
#                                    max_length=60)
#
#     def generate_slug(self):
#         return slugify(self.title)
#
#     slug = models.CharField(verbose_name=_('slug'),
#                             default=generate_slug,
#                             max_length=60)
