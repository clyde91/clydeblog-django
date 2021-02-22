from django import forms
from django.contrib import auth
from django.contrib.auth.models import User


class LoginForm(forms.Form):  # 表单类
    username = forms.CharField(label="用户名", widget=forms.TextInput(attrs={"class": "form-control", }))
    password = forms.CharField(label="密码", widget=forms.PasswordInput(attrs={"class": "form-control", }))

    def clean(self):
        username = self.cleaned_data["username"]
        password = self.cleaned_data["password"]

        user = auth.authenticate(username=username, password=password)
        if user is None:  # 验证用户
            raise forms.ValidationError("用户名或者密码不正确")
        else:
            self.cleaned_data["user"] = user
        return self.cleaned_data


class RegForm(forms.Form):
    username = forms.CharField(label="用户名", widget=forms.TextInput(attrs={"class": "form-control", }))
    email = forms.EmailField(label="邮箱", widget=forms.TextInput(attrs={"class": "form-control", }), required=False)
    password = forms.CharField(label="密码", widget=forms.PasswordInput(attrs={"class": "form-control", }), required=False)
    password_c = forms.CharField(label="确认密码", widget=forms.PasswordInput(attrs={"class": "form-control", }), required=False)

    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.filter(username=username):
            raise forms.ValidationError("用户名存在")
        return username  # return就是把这错误信息return的地方

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email):
            raise forms.ValidationError("邮箱存在")
        return email

    def clean_password_c(self):
        password = self.cleaned_data["password"]
        password_c = self.cleaned_data["password_c"]
        if password != password_c:
            raise forms.ValidationError("两次输入不一致")
        return password_c

