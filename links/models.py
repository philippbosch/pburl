from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from links.baseconv import base36

def get_next_token():
    i = 35 # reserve the one-letter URLs
    while True:
        i=i+1
        try:
            token = base36.from_decimal(i)
            link = Link.objects.get(token=token)
        except:
            break
    return token

class Link(models.Model):
    token = models.CharField(max_length=200, unique=True, default=get_next_token)
    url = models.URLField(verbose_name=_("URL"), unique=True)
    added = models.DateTimeField(auto_now_add=True)
    lastmod = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return "%s => %s" % (self.get_absolute_url(), self.url)
    
    def get_absolute_url(self):
        return reverse('link_token_lookup', kwargs = { 'token': self.token })
    
    def link(self):
        return """<a href="%(short_url)s">%(long_url)s</a>""" % { 'short_url': self.get_absolute_url(), 'long_url': self.url }
    link.allow_tags = True

class LinkClick(models.Model):
    link = models.ForeignKey(Link)
    datetime = models.DateTimeField(auto_now=True, verbose_name=_("Timestamp"))
    ip = models.IPAddressField(verbose_name=_("IP"))
    referrer = models.CharField(max_length=255, blank=True, null=True)
