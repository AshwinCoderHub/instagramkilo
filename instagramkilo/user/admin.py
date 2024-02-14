"""_summary_ admin Class
    """
from django.contrib import admin
from user.models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    """import admin

    Args:
        admin (_type_): _description_
    """


admin.site.register(User, UserAdmin)
