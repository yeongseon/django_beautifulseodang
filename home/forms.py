from allauth.account.forms import *

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

class MySignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(MySignupForm, self).__init__(*args, **kwargs)

        self.fields['username'].label = "사용자이름"
        self.fields['email'].label = "이메일"
        self.fields['password1'].label = "비밀번호"
        self.fields['password2'].label = "비밀번호확인"
