from django.http import HttpResponse

def index(request):
    return HttpResponse("Sveiks no Projects aplikācijas!")