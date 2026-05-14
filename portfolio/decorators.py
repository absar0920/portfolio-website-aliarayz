from functools import wraps
from django.core.cache import cache
from django.http import JsonResponse


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        return x_forwarded_for.split(',')[0].strip()
    return request.META.get('REMOTE_ADDR')


def rate_limit(max_requests, period):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            ip = get_client_ip(request)
            cache_key = f'ratelimit:{ip}:{period}'

            cache.add(cache_key, 0, timeout=period)
            count = cache.incr(cache_key)

            if count > max_requests:
                return JsonResponse(
                    {'status': 'error', 'message': 'Too many submissions. Please try again later.'},
                    status=429,
                )

            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator
