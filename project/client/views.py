from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from interface.forms import lientForm
from client.models import Client
from django.contrib.auth.hashers import make_password,check_password
from django.views.generic import View
from django.http import JsonResponse,Http404
import json
import requests


class IndexView(View):
    template = 'interface/index.html'
    all_clients = Client.objects.all()

    def get(self,request):
        if request.session.get('key'):
            active_client_key = request.session.get('key')
            if Client.objects.filter(key=active_client_key):
                active_client = Client.objects.filter(key=active_client_key)[0]
                return render(request,self.template,{'active_client':active_client})
        return render(request, self.template)


class LoginView(View):
    template = 'interface/login.html'
    empty_form = ClientForm()

    def get(self,request):
        if request.session.get('key'):
            active_client_key = request.session.get('key')
            if Client.objects.filter(key=active_client_key):
                active_client = Client.objects.filter(key=active_client_key)[0]
                return render(request,self.template,{'client_form':self.empty_form, 'active_client':active_client})
        return render(request,self.template,{'client_form':self.empty_form})

    def post(self,request):
        name = request.POST['name']
        password = request.POST['password']
        if Client.objects.filter(name=name):
            loggin_in_client = Client.objects.filter(name=name)[0]
            if check_password(password, loggin_in_client.password):
                request.session.flush()
                request.session['key'] = loggin_in_client.key
                return redirect('/interface/my_page')
            return render(request, self.template, {'error':'Name and/or password incorrect.  Please try again.', 'login_form':self.empty_form})
        return redirect('/interface/login')


class RegisterView(View):
    empty_form = lientForm()
    template = 'interface/login.html'
    create_url = 'http://127.0.0.1:8000/api/create_client'

    def get(self,request):
        if request.session.get('key'):
            active_client_key = request.session.get('key')
            if Client.objects.filter(key=active_client_key):
                active_client = Client.objects.filter(key=active_client_key)[0]
                return render(request,self.template,{'client_form':self.empty_form,'active_client':active_client})
        return render(request,self.template,{'client_form':self.empty_form})

    def post(self,request):
        submitted_form = lientForm(request.POST)
        if submitted_form.is_valid():
            name = submitted_form.cleaned_data.get('name')
            payload = {'name':name}
            r = requests.post(self.create_url,data=payload)
            submitted_password = submitted_form.cleaned_data.get('password')
            password = make_password(submitted_password)
            new_client = Client(name = name, password = password, key = r.json()['new_client']['key'])
            new_client.save()
            request.session.flush()
            request.session['key'] = new_client.key
            return redirect('/interface/my_page')
        return render(request,self.template,{'error':'Invalid input, please try again', 'client_form':self.empty_form})


class LogoutView(View):
    template = 'interface/logout.html'

    def get(self,request):
        if request.session.get('key'):
            active_client_key = request.session.get('key')
            if Client.objects.filter(key=active_client_key):
                active_client = Client.objects.filter(key=active_client_key)[0]
                return render(request,self.template,{'active_client':active_client})
        return redirect('/interface/index')

    def post(self,request):
        request.session.flush()
        return redirect('/interface/index')
#
# class ClientView(View):
#     template = 'interface/account.html'
#
#     def get(self,request):
#         if request.session.get('key'):
#             active_client_key = request.session.get('key')
#             if Client.objects.filter(key=active_client_key):
#                 active_client = Client.objects.filter(key=active_client_key)[0]
#                 return render(request,self.template,{'active_client':active_client})
#         return redirect('/interface/login')
#
# class AllActivityView(View):
#     all_todos_url = 'http://127.0.0.1:8000/api/get_all/'
#
#     def get(self,request):
#         if request.session.get('key'):
#             active_client_key = request.session.get('key')
#             if Client.objects.filter(key=active_client_key):
#                 active_client = Client.objects.filter(key=active_client_key)[0]
#                 r = requests.get(self.all_todos_url+active_client_key)
#                 full_activity_dict = r.json()['all_todos']
#                 return JsonResponse({'todos':[(activity['activity'],activity['status'],activity['created_at']) for activity in full_activity_dict]})
#
# class CreateActivity(View):
#     create_todo_url = 'http://127.0.0.1:8000/api/create_todo/'
