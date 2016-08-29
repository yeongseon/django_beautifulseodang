from allauth.account.forms import LoginForm
from django import forms

class MyLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(MyLoginForm, self).__init__(*args, **kwargs)


        self.fields['login'].label = "이메일"
        self.fields['password'].label = "비밀번호"
        self.fields['remember'].label = "로그인 상태 유지"

        #self.fields['submit'].label = "로그인 상태 유지"
        # You don't want the `remember` field?
        # if 'remember' in self.fields.keys():
        #    del self.fields['remember']