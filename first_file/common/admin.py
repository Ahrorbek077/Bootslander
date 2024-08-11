from django.contrib import admin
from common.models import Gallery, Contact, Cars, Video

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("title", )

@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    list_display = ("title", )

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject")
    list_filter = ("email", )
    search_fields = ("name", "email", "subject", "message")

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ("video", )