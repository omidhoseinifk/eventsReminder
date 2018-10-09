from django.shortcuts import render, HttpResponse
from reminderApp.models import Events
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def main_page(request):
    return render(request, 'mainPage.html')


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
