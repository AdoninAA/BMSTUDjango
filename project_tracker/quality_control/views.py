from django.http import HttpResponse
from django.urls import reverse

from django.views import View
from django.views.generic import DetailView

from .models import BugReport, FeatureRequest


def index(request):
    bugs_page_url = reverse('quality_control:bugs_list')
    features_page_url = reverse('quality_control:features_list')
    html = f"<h1>Система контроля качества</h1><a href='{bugs_page_url}'>Список всех багов</a><br/><a href='{features_page_url}'>Запросы на улучшение</a>"
    return HttpResponse(html)


def bug_list(request):
    bugs = BugReport.objects.all()
    bugs_html = '<h1>Список bug report</h1><ul>'
    for bug in bugs:
        bugs_html += f'<li>{bug.title}<br/>Статус: {bug.status}<br/><a href="{bug.id}/">Детали бага {bug.id}</a></li>'
    bugs_html += '</ul>'
    return HttpResponse(bugs_html)


def feature_list(request):
    features = FeatureRequest.objects.all()
    features_html = '<h1>Список запросов на улучшение</h1><ul>'
    for feature in features:
        features_html += f'<li>{feature.title}<br/>Статус: {feature.status}<br/><a href="{feature.id}/">Детали улучшения {feature.id}</a></li>'
    features_html += '</ul>'
    return HttpResponse(features_html)


def bug_detail(request, bug_id):
    return HttpResponse(f"<h1>Детали бага {bug_id}</h1>")


def feature_id_detail(request, feature_id):
    return HttpResponse(f"<h1>Детали улучшения {feature_id}</h1>")


class IndexView(View):
    def get(self, request, *args, **kwargs):
        bugs_page_url = reverse('quality_control:bugs_list')
        features_page_url = reverse('quality_control:features_list')
        html = f"<h1>Система контроля качества</h1><a href='{bugs_page_url}'>Список всех багов</a><br/><a href='{features_page_url}'>Запросы на улучшение</a>"
        return HttpResponse(html)


class BugsDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        bug = self.object
        response_html = f"<h1>Детали бага {bug.id}</h1><h2>{bug.title}</h2><p>{bug.description}<p/>"
        response_html += f'<p>Статус: {bug.status}</p>'  # <ul>'
        response_html += f'<p>Приоритет: {bug.priority}</p>'
        response_html += f'<p>Cвязанный проект: {bug.project}</p>'
        response_html += f'<p>Cвязаная задачи: {bug.task}</p>'
        return HttpResponse(response_html)


class FeaturesDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'feature_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        feature = self.object
        response_html = f"<h1>Детали бага {feature.id}</h1><h2>{feature.title}</h2><p>{feature.description}<p/>"
        response_html += f'<p>Статус: {feature.status}</p>'  # <ul>'
        response_html += f'<p>Приоритет: {feature.priority}</p>'
        response_html += f'<p>Cвязанный проект: {feature.project}</p>'
        response_html += f'<p>Cвязаная задачи: {feature.task}</p>'
        return HttpResponse(response_html)
