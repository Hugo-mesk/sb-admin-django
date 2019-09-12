from django.contrib import admin
from .models import Button, ButtonSubGroup, ButtonGroup

# Register your models here.
class ButtonSubGroupInline(admin.TabularInline):
    model = ButtonSubGroup
    extra = 1


class ButtonInline(admin.TabularInline):
    model = Button
    extra = 1


class ButtonSubGroupAdmin(admin.ModelAdmin):
    list_display = ('sub_group', 'group')
    inlines = [ButtonInline,]


class ButtonGroupAdmin(admin.ModelAdmin):
    list_display = ('group',)
    inlines = [ButtonSubGroupInline,]


class ButtonAdmin(admin.ModelAdmin):
    list_display = ('caption', 'url', "sub_group")


admin.site.register(Button, ButtonAdmin)
admin.site.register(ButtonSubGroup, ButtonSubGroupAdmin)
admin.site.register(ButtonGroup, ButtonGroupAdmin)
