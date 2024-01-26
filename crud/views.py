from django.shortcuts import render
from django.views.generic import TemplateView

# TopViewをビューとして使用して、関連するURLにアクセスすると "signin.html" テンプレートが表示されるようになる。
class TopView(TemplateView):
    template_name = "signin.html"
