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
        (SIMPLE, _('Simple')),
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
    def get_form(self):
        if self.form == self.SIMPLE:
            return ""
        elif self.form == self.CIRCLE:
            return "circle"
        elif self.form == self.BRAND:
            return "block"
        elif self.form == self.SPLIT_WITH_ICON:
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
    def get_size(self):
        if self.size == self.DEFAULT:
            return ""
        elif self.size == self.SMALL:
            return "sm"
        elif self.size == self.LARGE:
            return "lg"

    def __str__(self):
        return self.get_size_display()



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
    color = models.IntegerField(_('Color'),
                                  choices=COLOR_CHOICES,
                                  default=PRIMARY,
                                  )

    @property
    def get_color(self):
        if self.color == self.PRIMARY:
            return "primary"
        elif self.color == self.SECONDARY:
            return "secondary"
        elif self.color == self.SUCCESS:
            return "success"
        elif self.color == self.INFO:
            return "info"
        elif self.color == self.WARNING:
            return "warning"
        elif self.color == self.ERROR:
            # Django forms has message tags and constant error and bootstrap use danger
            return "danger"
        elif self.color == self.LIGHT:
            return "light"

    def __str__(self):
        return self.get_color_display()

class FaStyle(models.Model):
    # Font Awesome version 5. Instead of fa as a style preceding every icon style, you need
    # to pick from fas for solid, far for regular, fal for light, or fab for brand
    SOLID = 1
    REGULAR = 2
    LIGHT = 3
    BRAND = 4
    FA_STYLE_CHOICES = [
        (SOLID, _("Solid")),
        (REGULAR, _("Regular")),
        (LIGHT, _("Light")),
        (BRAND, _("Brand")),
    ]
    style = models.IntegerField(_('Icon Style'),
                                     choices=FA_STYLE_CHOICES,
                                     default=REGULAR,
                                    )

    @property
    def get_style(self):
        if self.style== self.SOLID:
            return "fas"
        elif self.style == self.REGULAR:
            return "far"
        elif self.style == self.LIGHT:
            return "fal"
        elif self.style == self.BRAND:
            return "fab"

    def __str__(self):
        return self.get_style_display()


class FaIcon(models.Model):
    # Font Awesome version 5. Instead of fa as a style preceding every icon style, you need
    # to pick from fas for solid, far for regular, fal for light, or fab for brand
    style = models.CharField(_("Style"),
                             max_length=120,
                            )

    def __str__(self):
        return self.style



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
    style = models.ForeignKey(FaStyle,
                              on_delete=models.CASCADE,
                              related_name='buttons')
    icon = models.ForeignKey(FaIcon,
                              on_delete=models.CASCADE,
                              related_name='buttons')
