from django.contrib import admin
from users.models import Profile, User


class UserAdmin(admin.ModelAdmin):
    model = User,
    list_display = ["username", "email"]


admin.site.register(User, UserAdmin)
admin.site.register(Profile)
