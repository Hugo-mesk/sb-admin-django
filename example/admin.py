from django.contrib import admin
from .models import Button, Form, Size, Color, FaStyle, FaIcon

class ButtonAdmin(admin.ModelAdmin):
    list_display = ("form", "size", "color")

admin.site.register(Button, ButtonAdmin)
admin.site.register(Form)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(FaStyle)
admin.site.register(FaIcon)
