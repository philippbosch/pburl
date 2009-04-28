from django.contrib import admin

from links.models import Link, LinkClick

class LinkClickInline(admin.TabularInline):
    model = LinkClick
    extra = 0

class LinkAdmin(admin.ModelAdmin):
    inlines = [
        LinkClickInline
    ]
    list_display = (
        'token',
        'link',
        'added',
    )

admin.site.register(Link, LinkAdmin)
