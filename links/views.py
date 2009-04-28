from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponsePermanentRedirect

from links.models import Link, LinkClick

def lookup(request, token):
    link = get_object_or_404(Link, token=token)
    
    try:
        referrer = request.META['HTTP_REFERER']
    except KeyError:
        referrer = None
    
    LinkClick.objects.create(link=link, ip=request.META['REMOTE_ADDR'], referrer=referrer)
    
    return HttpResponsePermanentRedirect(link.url)
    
def test(request):
    return HttpResponse('<a href="/1">Test me!</a>')