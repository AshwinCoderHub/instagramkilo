""" Creating application
    """
from django.apps import AppConfig


class UserConfig(AppConfig):
    """
         Creating  User configuration

    Args:
        AppConfig (_type_): _description_
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "user"
