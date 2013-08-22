# -*- coding: utf-8 -*-
from django import forms
class LoginForm(forms.Form):
	name=forms.CharField(max_length=140,widget=forms.TextInput(attrs={'placeholder':'用户名','type':'text'}))
	password=forms.CharField(max_length=140,widget=forms.TextInput(attrs={'placeholder':'密码','type':'password'}))