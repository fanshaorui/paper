# -*- coding: utf-8 -*-
from django import forms
from paper.locals import email_error_messages,password_error_messages,phonenumber_error_messages,name_error_messages
from captcha.fields import CaptchaField
from django.contrib.auth.models import User
class ProfileForm(forms.Form):
	name=forms.CharField(max_length=140,widget=forms.TextInput(attrs={'placeholder':'用户名','type':'text'}),error_messages=name_error_messages)
	password=forms.CharField(max_length=140,widget=forms.TextInput(attrs={'placeholder':'密码','type':'password'}),error_messages=password_error_messages)
	email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'邮箱','type':'text'}),error_messages=email_error_messages)
	phonenumber=forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'电话号码','type':'text'}),error_messages=phonenumber_error_messages)
	captcha = CaptchaField()
	repeatpassword=forms.CharField(max_length=140,widget=forms.TextInput(attrs={'placeholder':'重复密码','type':'password'}),error_messages=password_error_messages)
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
class changeProfileForm(forms.Form):
	password=forms.CharField(max_length=140,widget=forms.TextInput(attrs={'placeholder':'密码','type':'password'}),error_messages=password_error_messages)
	email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'邮箱','type':'text'}),error_messages=email_error_messages)
	phonenumber=forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'电话号码','type':'text'}),error_messages=phonenumber_error_messages)
	repeatpassword=forms.CharField(max_length=140,widget=forms.TextInput(attrs={'placeholder':'重复密码','type':'password'}),error_messages=password_error_messages)
	def clean_repeatpassword(self):
		if self.cleaned_data['password']==self.cleaned_data['repeatpassword']:
			return self.cleaned_data['repeatpassword']
		else:
			raise  forms.ValidationError(u"密码输入不一样,请重新输入")
	