from django.contrib import admin
from django.contrib.sites.models import Site
from logger.models import Publication, Bookmark, Friendship

class AdminPublication(admin.ModelAdmin):
    list_display = ('text datetime publisher'.split())

class AdminBookmark(admin.ModelAdmin):
    list_display = ('publication', 'owner')

class AdminFriendship(admin.ModelAdmin):
    list_display = ('who',)

admin.site.unregister(Site)
admin.site.register(Publication, AdminPublication)
admin.site.register(Bookmark, AdminBookmark)
admin.site.register(Friendship, AdminFriendship)
