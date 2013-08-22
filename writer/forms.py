# -*- coding: utf-8 -*-
from django import forms
class changeProfileForm(forms.Form):
	password=forms.CharField(max_length=140,widget=forms.TextInput(attrs={'placeholder':'密码','type':'password'}))
	email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'邮箱','type':'text'}))
	phonenumber=forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'电话号码','type':'text'}))
	realname=forms.CharField(max_length=140,widget=forms.TextInput(attrs={'placeholder':'真实姓名','type':'text'}))
	selfdescription=forms.CharField(max_length=10000,widget=forms.TextInput(attrs={'placeholder':'自我介绍','type':'text'}))
class ProfileForm(forms.Form):
	name=forms.CharField(max_length=140,widget=forms.TextInput(attrs={'placeholder':'用户名','type':'text'}))
	password=forms.CharField(max_length=140,widget=forms.TextInput(attrs={'placeholder':'密码','type':'password'}))
	email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'邮箱','type':'text'}))
	phonenumber=forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'电话号码','type':'text'}))
	realname=forms.CharField(max_length=140,widget=forms.TextInput(attrs={'placeholder':'真实姓名','type':'text'}))
	selfdescription=forms.CharField(max_length=10000,widget=forms.TextInput(attrs={'placeholder':'自我介绍','type':'text'}))