from django.db import models
from django.utils.translation import gettext_lazy as _

GROUP = ()

# Create your models here.
class Button(models.Model):

    caption = models.CharField(max_length=20, blank=True)
    # As django docs sugest define CHIOCES by suitably-named constant
    CIRCLE_BUTTONS = "CB"
    FACEBOOK_BUTTONS = "FB"
    GOOGLE_BUTTONS = "GB"
    SPLIT_BT_ICON = "SBI"
    BUTTON_GROUP_CHOICES = [
        (CIRCLE_BUTTONS, _('Circle Buttons')),
        (FACEBOOK_BUTTONS, _('Facebook Buttons')),
        (GOOGLE_BUTTONS, _('Google Buttons')),
        (SPLIT_BT_ICON, _('Split Buttons if Icon')),
    ]
    group = models.CharField(
        max_length=3,
        choices=BUTTON_GROUP_CHOICES,
        default=CIRCLE_BUTTONS,
    )
    DEFAULT_BUTTON = "DB"
    SMALL_BUTTON = "SB"
    LARGE_BUTTON = "LG"
    BUTTON_SUBGROUP_CHOICES = [
        (DEFAULT_BUTTON, _("Default Buttons")),
        (SMALL_BUTTON, _("Small Buttons")),
        (LARGE_BUTTON, _("Large Buttons")),
    ]
    sub_group = models.CharField(
        max_length=3,
        choices=BUTTON_SUBGROUP_CHOICES,
        default=DEFAULT_BUTTON,
    )
    PRIMARY_BUTTON = "btn-primary"
    SECONDARY_BUTTON = "btn-secondary"
    SUCCESS_BUTTON = "btn-success"
    INFO_BUTTON = "btn-info"
    WARNING_BUTTON = "btn-warning"
    DANGER_BUTTON = "btn-danger"
    LIGHT_BUTTON = "btn-light"
    BUTTON_FORM_CHOICES = [
        (PRIMARY_BUTTON, _("Primary Button")),
        (SECONDARY_BUTTON, _("Secondary Button")),
        (SUCCESS_BUTTON, _("Success Button")),
        (INFO_BUTTON, _("Info Button")),
        (WARNING_BUTTON, _("Warning Button")),
        (DANGER_BUTTON, _("Danger Button")),
        (LIGHT_BUTTON, _("Light Button")),
    ]
    bootstrap_color = models.CharField(
        max_length=15,
        choices=BUTTON_FORM_CHOICES,
        default=PRIMARY_BUTTON,
    )

    @property
    def bootstrap_form(self):
        if self.group == CIRCLE_BUTTONS:
            return bootstrap_form = "btn-circle"
        elif self.group == FACEBOOK_BUTTONS
            return bootstrap_form = "btn-facebook btn-block"
        elif self.group == GOOGLE_BUTTONS:
            return bootstrap_form = "btn-google btn-block"

        elif self.group == SPLIT_BT_ICON:
            return bootstrap_form = "btn-icon-split"

    @property
    def bootstrap_size():
        if self.sub_group == DEFAULT_BUTTON:
            return bootstrap_form = ""
        elif self.sub_group == SMALL_BUTTON:
            return bootstrap_form = "btn-sm"
        elif self.sub_group == LARGE_BUTTON:
            return bootstrap_form = "btn-lg"

    @property
    def fa_icon():
        if self.group == FACEBOOK_BUTTONS:
            return fa_icon = "fab fa-facebook-f fa-fw"
        elif self.group == GOOGLE_BUTTONS:
            return fa_icon = "fab fa-google fa-fw"
        elif self.bootstrap_color == PRIMARY_BUTTON:
            return fa_icon = "fas fa-flag"
        elif self.bootstrap_color == SECONDARY_BUTTON:
            return fa_icon = "fas fa-arrow-right"
        elif self.bootstrap_color == SUCCESS_BUTTON:
            return fa_icon = "fas fa-check"
        elif self.bootstrap_color == INFO_BUTTON:
            return fa_icon = "fas fa-info-circle"
        elif self.bootstrap_color == WARNING_BUTTON:
            return fa_icon = "fas fa-exclamation-triangle"
        elif self.bootstrap_color == DANGER_BUTTON:
            return fa_icon = "fas fa-trash"
