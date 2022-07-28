from django.urls import path, re_path

from .views import *

urlpatterns = [
	path('', index, name='index'),
	# re_path('result/*', index, name='index'),
	path('<short_link>/', handle_link, name='handle'),
]