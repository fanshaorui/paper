# -*- coding: utf-8 -*-
from django import forms
from paper.locals import *
from captcha.fields import CaptchaField
from django.contrib.auth.models import User
class changeProfileForm(forms.Form):
	password=forms.CharField(max_length=140,widget=forms.TextInput(attrs={'placeholder':'密码','type':'password'}),error_messages=password_error_messages)
	email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'邮箱','type':'text'}),error_messages=email_error_messages)
	phonenumber=forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'电话号码','type':'text'}),error_messages=phonenumber_error_messages)
	realname=forms.CharField(max_length=140,widget=forms.TextInput(attrs={'placeholder':'真实姓名','type':'text'}),error_messages=realname_error_messages)
	selfdescription=forms.CharField(max_length=10000,widget=forms.Textarea(attrs={'placeholder':'自我介绍','type':'text'}),error_messages=selfdescription_error_messages)
	bankaccount=forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'收款账号','type':'text'}),error_messages=bankaccount_error_messages)
	bank=forms.CharField(max_length=140,widget=forms.TextInput(attrs={'placeholder':'开户银行','type':'text'}),error_messages=bank_error_messages)
	repeatpassword=forms.CharField(max_length=140,widget=forms.TextInput(attrs={'placeholder':'重复密码','type':'password'}),error_messages=password_error_messages)
	def clean_repeatpassword(self):
		if self.cleaned_data['password']==self.cleaned_data['repeatpassword']:
			return self.cleaned_data['repeatpassword']
		else:
			raise  forms.ValidationError(u"密码输入不一样,请重新输入")
class ProfileForm(forms.Form):
	name=forms.CharField(max_length=140,widget=forms.TextInput(attrs={'placeholder':'用户名','type':'text'}),error_messages=name_error_messages)
	password=forms.CharField(max_length=140,widget=forms.TextInput(attrs={'placeholder':'密码','type':'password'}),error_messages=password_error_messages)
	repeatpassword=forms.CharField(max_length=140,widget=forms.TextInput(attrs={'placeholder':'重复密码','type':'password'}),error_messages=password_error_messages)
	email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'邮箱','type':'text'}),error_messages=email_error_messages)
	phonenumber=forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'电话号码','type':'text'}),error_messages=phonenumber_error_messages)
	realname=forms.CharField(max_length=140,widget=forms.TextInput(attrs={'placeholder':'真实姓名','type':'text'}),error_messages=realname_error_messages)
	selfdescription=forms.CharField(max_length=10000,widget=forms.Textarea(attrs={'placeholder':'自我介绍','type':'text'}),error_messages=selfdescription_error_messages)
	captcha = CaptchaField()
	bankaccount=forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'收款账号','type':'text'}),error_messages=bankaccount_error_messages)
	bank=forms.CharField(max_length=140,widget=forms.TextInput(attrs={'placeholder':'开户银行','type':'text'}),error_messages=bank_error_messages)
	def clean_repeatpassword(self):
		if self.cleaned_data['password']==self.cleaned_data['repeatpassword']:
			return self.cleaned_data['repeatpassword']
		else:
			raise  forms.ValidationError(u"密码输入不一样,请重新输入")
	def clean_name(self):
		username=self.cleaned_data['name']
		is_exist=User.objects.filter(username=username).exists()
		if is_exist:
			raise forms.ValidationError(u"这个用户名已经被注册了,请换个名字")
		return username
	def clean_email(self):
		email=self.cleaned_data['email']
		is_exist=User.objects.filter(email=email).exists()
		if is_exist:
			raise forms.ValidationError(u"这个邮箱已经被注册了,请换个邮箱")
		return email
	

	