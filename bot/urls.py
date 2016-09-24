from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^b'd63c0f6359f147e4e77f097465b95803a401074dd248d479e1'/?$", views.BotMessenger.as_view()),
]
