from django.db import models
from django.utils.translation import gettext_lazy as _

# As django docs sugest define CHIOCES by suitably-named constant
# Field with restricted choices only are good when you need predefined filter

class Form(models.Model):
    #
    SIMPLE = "SP"
    CIRCLE = "CB"
    SPLIT_WITH_ICON = "SBI"
    BRAND = "BB"
    FORM_CHOICES = [
        (CIRCLE, _('Circle')),
        (BRAND, _('Brand')),
        (SPLIT_WITH_ICON, _('Split if Icon')),
    ]

    form = models.CharField(_("Form"),
                            max_length= 3,
                            choices= FORM_CHOICES,
                            default= SIMPLE,
                            )

    @property
    def bootstrap_form(self):
        if self.form == SIMPLE:
            return ""
        elif self.form == CIRCLE:
            return "circle"
        elif self.form == BRAND:
            return "block"
        elif self.form == SPLIT_WITH_ICON:
            return "icon-split"

    def __str__(self):
        return self.get_form_display()


class Size(models.Model):

    DEFAULT = "DB"
    SMALL = "SB"
    LARGE = "LG"
    SIZE_CHOICES = [
        (DEFAULT, _("Default")),
        (SMALL, _("Small")),
        (LARGE, _("Large")),
    ]

    size = models.CharField(_("Size"),
                            max_length=3,
                            choices=SIZE_CHOICES,
                            default=DEFAULT,
                            )
    @property
    def bootstrap_size(self):
        if self.sub_group.sub_group == DEFAULT:
            return ""
        elif self.sub_group.sub_group == SMALL:
            return "sm"
        elif self.sub_group.sub_group == LARGE:
            return "lg"

    def __str__(self):
        return self.get_sub_group_display()



class Color(models.Model):

    PRIMARY = 1
    SECONDARY = 2
    SUCCESS = 3
    INFO = 4
    WARNING = 5
    ERROR = 6
    LIGHT = 7
    COLOR_CHOICES = [
        (PRIMARY, _("Primary")),
        (SECONDARY, _("Secondary")),
        (SUCCESS, _("Success")),
        (INFO, _("Info")),
        (WARNING, _("Warning")),
        (ERROR, _("Error")),
        (LIGHT, _("Light")),
    ]
    bootstrap_color = models.IntegerField(_('Color'),
                                          choices=COLOR_CHOICES,
                                          default=PRIMARY,
                                          )

    @property
    def bootstrap_color(self):
        if self.color == PRIMARY:
            return " btn-primary"
        elif self.color == SECONDARY:
            return " btn-secondary"
        elif self.color == SUCCESS:
            return " btn-success"
        elif self.color == INFO:
            return " btn-info"
        elif self.color == WARNING:
            return " btn-warning"
        elif self.color == ERROR:
            # Django forms has message tags and constant error and bootstrap use danger
            return " btn-danger"
        elif self.color == LIGHT:
            return " btn-light"


class FaIcon(models.Model):
    # Font Awesome version 5. Instead of fa as a style preceding every icon style, you need
    # to pick from fas for solid, far for regular, fal for light, or fab for brand
    SOLID = 1
    REGULAR = 2
    LIGHT = 3
    BRAND = 4
    FAICON_CHOICES = [
        (SOLID, _("Default")),
        (REGULAR, _("Small")),
        (LIGHT, _("Large")),
        (BRAND, _("Large")),
    ]
    icon_style = models.IntegerField(_('Icon Style'),
                                     choices=FAICON_CHOICES,
                                     default=REGULAR,
                                    )

    @property
    def fa_icon(self):
        if self.sub_group.group.group == SOLID:
            return "fas"
        elif self.sub_group.group.group == REGULAR:
            return "far"
        elif self.bootstrap_color == LIGHT:
            return "fal"
        elif self.bootstrap_color == BRAND:
            return "fab"


# Create your models here.
class Button(models.Model):

    caption = models.CharField(max_length=20, blank=True)
    # Button normaly some operation by POST in some href="url"
    # Just for illustration it will be set in database
    # you should use get_absolute_url in your model
    href = models.CharField(max_length=120, blank=True)

    # As django docs sugest define CHIOCES by suitably-named constant
    form = models.ForeignKey(Form,
                              on_delete=models.CASCADE,
                              related_name='buttons')
    size = models.ForeignKey(Size,
                              on_delete=models.CASCADE,
                              related_name='buttons')
    color = models.ForeignKey(Color,
                              on_delete=models.CASCADE,
                              related_name='buttons')
    fa_icon = models.ForeignKey(FaIcon,
                              on_delete=models.CASCADE,
                              related_name='buttons')
