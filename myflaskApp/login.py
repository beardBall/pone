from flask import Flask, request, render_template   


def hello():
    print("Hello, World!")


def login(request):
    print(str(request))
    return render_template('login.html', request=request)
