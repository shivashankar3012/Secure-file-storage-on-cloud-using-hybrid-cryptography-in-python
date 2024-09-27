# user/middleware.py

class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Process the request here
        response = self.get_response(request)
        # Process the response here
        return response
