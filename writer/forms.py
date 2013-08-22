# -*- coding: utf-8 -*-
from django import forms
from paper.locals import *
class changeProfileForm(forms.Form):
	password=forms.CharField(max_length=140,widget=forms.TextInput(attrs={'placeholder':'密码','type':'password'}),error_messages=password_error_messages)
	email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'邮箱','type':'text'}),error_messages=email_error_messages)
	phonenumber=forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'电话号码','type':'text'}),error_messages=phonenumber_error_messages)
	realname=forms.CharField(max_length=140,widget=forms.TextInput(attrs={'placeholder':'真实姓名','type':'text'}),error_messages=realname_error_messages)
	selfdescription=forms.CharField(max_length=10000,widget=forms.TextInput(attrs={'placeholder':'自我介绍','type':'text'}),error_messages=selfdescription_error_messages)
class ProfileForm(forms.Form):
	name=forms.CharField(max_length=140,widget=forms.TextInput(attrs={'placeholder':'用户名','type':'text'}),error_messages=name_error_messages)
	password=forms.CharField(max_length=140,widget=forms.TextInput(attrs={'placeholder':'密码','type':'password'}),error_messages=password_error_messages)
	email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'邮箱','type':'text'}),error_messages=email_error_messages)
	phonenumber=forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'电话号码','type':'text'}),error_messages=phonenumber_error_messages)
	realname=forms.CharField(max_length=140,widget=forms.TextInput(attrs={'placeholder':'真实姓名','type':'text'}),error_messages=realname_error_messages)
	selfdescription=forms.CharField(max_length=10000,widget=forms.TextInput(attrs={'placeholder':'自我介绍','type':'text'}),error_messages=selfdescription_error_messages)