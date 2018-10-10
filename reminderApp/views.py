import requests
from django.shortcuts import render, HttpResponse
from reminderApp.models import Events
from django.conf import settings
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages


def main_page(request):
    return render(request, 'mainPage.html')


def send_sms(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        phone = request.POST.get('phone')
        sms_username = settings.SMS_USERNAME
        sms_password = settings.SMS_PASSWORD
        request = requests.get(f'https://RayganSMS.com/SendMessageWithUrl.ashx?\
                Username={sms_username}&Password={sms_password}\
                &PhoneNumber=50005858312\
                &MessageBody={message}&RecNumber={phone}\
                &Smsclass=1')
        try:
            if request is True:
                messages.success(request, 'Your message was sent successfully')
        except exception as e:
            messages.warning(request, 'Your message was not sent,\
                please try again!!! Error:{}.format(e)')
    return render(request, 'send-sms.html')


class AccountRegister:
    def __init__(self, mobile_number, email, password, confirm_password):
        self.mobile_number = mobile_number
        self.email = email
        self._password = password
        self._confirm_password = confirm_password


class PremiumAccountRegister:
    pass
    '''
        this is a class for premium account register
        and will be used to expand the project in the future.
    '''


class User(AccountRegister):
    def __init__(self, mobile_number, email, password, confirm_password):
        super().__init__(mobile_number, email, password, confirm_password)

    def check_password(self):
        if self._password == self._confirm_password:
            pass
        else:
            print('Does not match password!!!')
            self.check_password()

    def change_password(self):
        old_password = input('Please enter old password: ')
        if old_password == self._password:
            new_password = input('Please enter new password: ')
            confirm_password = input('please repeat new password:')
            if new_password == confirm_password:
                self._password = new_password
            else:
                print('Does not match!!!')
                self.change_password()
        else:
            print('wrong password!!!')
            self.change_password()
