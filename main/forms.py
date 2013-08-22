# -*- coding: utf-8 -*-
from django import forms
from paper.locals import name_error_messages,password_error_messages
class LoginForm(forms.Form):
	name=forms.CharField(max_length=140,widget=forms.TextInput(attrs={'placeholder':'用户名','type':'text'}),error_messages=name_error_messages)
	password=forms.CharField(max_length=140,widget=forms.TextInput(attrs={'placeholder':'密码','type':'password'}),error_messages=password_error_messages)