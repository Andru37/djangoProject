from django.shortcuts import render
from django.http import HttpResponse
import random


def main(request):
    return HttpResponse("Hey! It's your main view!")


def my_homepage(request):
    return HttpResponse("This is homepage my first application. It's very good.")


def my_home(request):
    return HttpResponse("This is homepage my first application.")


def article(request, article_id, name=""):
    return HttpResponse("This is an article {}. {}".format(article_id, "Name of this article is {}".format(
        name) if name else "This is unnamed article"))


def password(request, my_password=""):
    if my_password.isalnum() and len(my_password) == 8:
        return HttpResponse(f"Your password is {my_password}")
    else:
        return HttpResponse(f"Your password {my_password} is invalid")


def generate_password(request, length):
    password_list = ""
    for i in range(length):
        number = random.randint(0, 9)
        password_list = password_list + str(number)
    return HttpResponse(f"Your random password {password_list}")
