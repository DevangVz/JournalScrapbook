from django.http import HttpResponse,HttpRequest
from django.template import Template, Context


#No esta detectando URL Relativa
def homeHTML(request):
    path=r'C:\Users\SPARTAN PC\Documents\Proyectos_Django\JournalScrapbook\JournalScrapbook\HTML\home.html'
    homeHTMLCode = open(path)
    template = Template(homeHTMLCode.read())
    homeHTMLCode.close()
    contexto=Context()
    documento=template.render(contexto)
    return HttpResponse(documento)

