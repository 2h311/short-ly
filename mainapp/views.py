from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.http.response import Http404

from mainapp.models import ShortLinks

# Create your views here.
def index(request):
	if request.method == 'POST':
		object_ = ShortLinks.objects.create(full_link=request.POST['link'])
		return render(request, 'mainapp/index.html', {'short_link': f"{settings.DOMAIN}{object_.short_link}"})
	return render(request, 'mainapp/index.html')

def handle_link(request, short_link):
	try:
		query = get_object_or_404(ShortLinks, short_link=short_link)
		return redirect(query.full_link)
	except (KeyError, ShortLinks.DoesNotExist, Http404):
		return render(request, 'mainapp/index.html', {'error_message': ""})


