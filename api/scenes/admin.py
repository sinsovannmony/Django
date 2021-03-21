from django.contrib import admin
from .models import Word, Scene, Percentage, Bookmark, Understood, PointToApprove
# Register your models here.
admin.site.register(Word)
admin.site.register(Scene)
admin.site.register(Percentage)
admin.site.register(Bookmark)
admin.site.register(Understood)
admin.site.register(PointToApprove)

