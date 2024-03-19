
from django.shortcuts import redirect
from django.urls import reverse

class CheckUserMiddleware:

    EXCLUDED_PATHS = ['/login/', '/signup/','/', '/admin_login/',]

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__ (self,request):
        if request.path_info in self.EXCLUDED_PATHS:
            if "email" in request.session :
                if request.session['email'] != "":
                    return redirect('dashboard')

            response = self.get_response(request)
            return response
        elif "email" in request.session :
            if request.session['email'] != "":
                response = self.get_response(request)
                return response
            else:
                return redirect('home')
        else:
            return redirect('home')
        