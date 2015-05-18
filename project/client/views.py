from django.shortcuts import render,redirect
from client.forms import ClientForm
from client.models import Client
from django.contrib.auth.hashers import make_password,check_password
from django.views.generic import View
from django.http import JsonResponse,Http404
import json
import requests


class IndexView(View):
    template = 'client/index.html'
    all_clients = Client.objects.all()

    def get(self,request):
        if request.session.get('id'):
            active_client_id = request.session.get('id')
            if Client.objects.filter(id=active_client_id):
                active_client = Client.objects.filter(id=active_client_id)[0]
                return render(request,self.template,{'active_client':active_client})
        return render(request, self.template)


class LoginView(View):
    template = 'client/login.html'
    empty_form = ClientForm()

    def get(self,request):
        if request.session.get('id'):
            active_client_id = request.session.get('id')
            if Client.objects.filter(id=active_client_id):
                active_client = Client.objects.filter(id=active_client_id)[0]
                return render(request,self.template,{'client_form':self.empty_form, 'active_client':active_client})
        return render(request,self.template,{'client_form':self.empty_form})

    def post(self,request):
        name = request.POST['name']
        password = request.POST['password']
        if Client.objects.filter(name=name):
            loggin_in_client = Client.objects.filter(name=name)[0]
            if check_password(password, loggin_in_client.password):
                request.session.flush()
                request.session['id'] = loggin_in_client.id
                return redirect('/gvd/play')
            return render(request, self.template, {'error':'Name and/or password incorrect.  Please try again.', 'login_form':self.empty_form})
        return redirect('/gvd/login')


class RegisterView(View):
    empty_form = ClientForm()
    template = 'client/login.html'

    def get(self,request):
        if request.session.get('id'):
            active_client_id = request.session.get('id')
            if Client.objects.filter(id=active_client_id):
                active_client = Client.objects.filter(id=active_client_id)[0]
                return render(request,self.template,{'client_form':self.empty_form,'active_client':active_client})
        return render(request,self.template,{'client_form':self.empty_form})

    def post(self,request):
        submitted_form = ClientForm(request.POST)
        if submitted_form.is_valid():
            name = submitted_form.cleaned_data.get('name')
            payload = {'name':name}
            r = requests.post(self.create_url,data=payload)
            submitted_password = submitted_form.cleaned_data.get('password')
            password = make_password(submitted_password)
            new_client = Client(name = name, password = password)
            new_client.save()
            request.session.flush()
            request.session['id'] = new_client.id
            return redirect('/gvd/play')
        return render(request,self.template,{'error':'Invalid input, please try again', 'client_form':self.empty_form})


class LogoutView(View):
    template = 'client/logout.html'

    def get(self,request):
        if request.session.get('id'):
            active_client_id = request.session.get('id')
            if Client.objects.filter(id=active_client_id):
                active_client = Client.objects.filter(id=active_client_id)[0]
                return render(request,self.template,{'active_client':active_client})
        return redirect('/gvd/index')

    def post(self,request):
        request.session.flush()
        return redirect('/gvd/index')


class PlayView(View):
    template = 'client/game.html'

    def get(self,request):
        if request.session.get('id'):
            active_client_id = request.session.get('id')
            if Client.objects.filter(id=active_client_id):
                active_client = Client.objects.filter(id=active_client_id)[0]
            return render(request,self.template,{'active_client':active_client})
        return render(request, self.template)
