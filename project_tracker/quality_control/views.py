from django.http import HttpResponse
from django.urls import reverse

def index(request):
    bugs_page_url = reverse('quality_control:bugs_page')
    features_page_url = reverse('quality_control:features_page')
    html = f"<h1>Система контроля качества</h1><a href='{bugs_page_url}'>Список всех багов</a><br/><a href='{features_page_url}'>Запросы на улучшение</a>"
    return HttpResponse(html)

def bug_list(request):
    return HttpResponse(f"<h1>Cписок отчетов об ошибках</h1>")

def features_page(request):
    return HttpResponse(f"<h1>Список запросов на улучшение</h1>")
