from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render

def cache_test(request):
    # Set a value in the cache
    cache.set('my_key', 'Hello, World!', timeout=60)
    
    # Get the value from the cache
    value = cache.get('my_key', 'Key not found')

    return HttpResponse(f'Cache value: {value}')
