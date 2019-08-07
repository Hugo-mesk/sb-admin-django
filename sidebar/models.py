from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class SidebarPlace(models.Model):
    # for illustrate the use of choices hard cooded
    SIDEBAR_GROUP_CHOICES = (("INT",_('Interface')), ("ADO",_('Addons')))
    group = models.CharField(verbose_name=_("Sidebar Group"),
                              max_length=3,
                              choices=SIDEBAR_GROUP_CHOICES
                            )

    subgroup = models.CharField(verbose_name=_('title'),
                             max_length=60)


class Page(models.Model):
    # get_slug is a funcition to generate slug you may use a property
    # intent to have ability to edit the slug

    # in future it can be implemnted in JS to auto update the field

    def get_slug(self):
        return slugify(self.title)

    title = models.CharField(verbose_name=_('title'),
                             max_length=60)
    menu_title = models.CharField(verbose_name=_('title'),
                             max_length=60)
    slug = models.CharField(verbose_name=_('slug'),
                            default=get_slug,
                            max_length=60)
    sidebar = models.ForeignKey(SidebarItem,
                              on_delete=models.PROTECT,
                              related_name='pages',
                              )

    def get_absolute_url(self):
        return reverse('sidebar:page', kwargs={'slug': self.slug})
