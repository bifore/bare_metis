from django.conf import settings


class SubDomainRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        subdomain = request.META['HTTP_HOST']
        if subdomain in settings.REDIRECTED_SUBDOMAIN:
            request.urlconf = settings.REDIRECTED_SUBDOMAIN[subdomain]
        response = self.get_response(request)
        return response
