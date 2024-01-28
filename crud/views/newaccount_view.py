from django.shortcuts import render
from django.views.generic import CreateView
from ..models.user import User

# TopViewをビューとして使用して、関連するURLにアクセスすると "signin.html" テンプレートが表示されるようになる。
class NewaccountView(CreateView):
    template_name = "newaccount.html"
    model = User
    fields = ['email', 'password',]