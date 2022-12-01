from django.http import HttpResponse

def home(request):
   text = """<h1>Hello world cambio 1.0.6</h1>"""
   return HttpResponse(text)
