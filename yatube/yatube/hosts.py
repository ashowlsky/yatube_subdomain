from django.conf import settings
from django_hosts import patterns, host


host_patterns = patterns('',
    host(r'yatube', settings.ROOT_URLCONF, name='www'),
    host(r'(\w+)', settings.CUSTOM_URLCONF, name='wildcard'),
)