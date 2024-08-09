# Django session:

from django.shortcuts import redirect


https://docs.djangoproject.com/en/4.1/topics/http/sessions/

# Django provides full support for anonymous sessions. The session framework lets you store and retrieve arbitrary data on a per-site-visitor basis. It stores data on the server side and abstracts the sending and receiving of cookies. Cookies contain a session ID – not the data itself (unless you’re using the cookie based backend).

# Using database-backed sessions

# If you want to use a database-backed session, you need to add 
# 'django.contrib.sessions' to your INSTALLED_APPS setting.

# Already it is added in default app settings.py file in installed_apps section

While redirect to user login from views.py file under login_user()
once we check user is not None before redirect to dashboard page we need to start user session as:

def login_user(request):
    if request.method == "POST":
        a = request.POST['username']
        b = request.POST['password']
        
        user = authenticate(request, username = a, password = b)

        if user is not None:
            login(request, user)
            # Redirect to a success page.
            request.session['username'] = a
            # starting session of user and username we assign to username_id to access in program

            return redirect('dashboard')
        else:
            # display 'invalid login' error message
            messages.error(request, 'In-correct username or password!..')    
        
    return render(request, 'login.html')


# once session we create as soon as login done and before redirect to dashboard page, now suppose we want to check whether really session is started or not,

# for that purpose, in dashboard() function, where we are sending data of database to dashboard.html page,

# before render, just print() call and check session as:

@login_required(login_url='login')
def dashboard(request):

    username = request.session.get('username')

    return render(request, 'dashboard/index.html', {'username':username})


# and now in dashboard/index.html page where you want to show username as Hi, admin, you need to use username as:

    <marquee direction="up" style="height:200px;"
            onmouseover="this.stop();" onmouseout="this.start();"> 
            
            {% if user.is_authenticated %}
    
                <h3> Hello, {{ username }}</h3>

            {% endif %}
            
            <br><b>Welcome to My Portal.. </b>
    </marquee>



