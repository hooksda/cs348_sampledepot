from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render, redirect

from Accounts.forms import LoginForm, RegisterForm, uploadForm
from sampledepotapp.models import Music, SampledepotappUsers, Genre, Comments
User = get_user_model()

def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password1")
        password2 = form.cleaned_data.get("password2")
        first = form.cleaned_data.get("first")
        last = form.cleaned_data.get("last")
        #try:
        user = User.objects.create_user(username, email, password)
        new_user = SampledepotappUsers.objects.create(user_id = str(hash(username))[1:5],username = username, first_name = first, last_name = last)
        new_user.save()
        if user != None:
            login(request, user = user)
            return redirect("/")
        else:
            request.session['register_error'] = 1 # 1 == True
    return render(request, "forms.html", {"form": form})

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user != None:
            # user is valid and active -> is_active
            # request.user == user
            login(request, user = user)
            return redirect("/")
        else:
            # attempt = request.session.get("attempt") or 0
            # request.session['attempt'] = attempt + 1
            # return redirect("/invalid-password")
            request.session['invalid_user'] = 1 # 1 == True
    return render(request, "forms.html", {"form": form})

def logout_view(request):
    logout(request)
    # request.user == Anon User
    return redirect("/login")

def profile_view(request):
    #form= FormNewUser(request.POST or None)
    #if form.is_valid():
    #    form.save()                      
    #context= {'New User': form }
    user = request.user.username
    users = SampledepotappUsers.objects.filter(username = user)
    muse = Music.objects.filter(sampledepotappusers__in = users)
    count_of = Music.objects.count()
    if users.get(username = user).music != None:
        return render(request, 'profile.html', {'users': users, 'music':muse, 'count': count_of})
    else:
        return render(request, 'profile.html', {'users': users, 'music': None, 'count': 0})

def upload_view(request):
    form = uploadForm(request.POST or None)
    if form.is_valid():
        title = form.cleaned_data.get("title")
        genre = form.cleaned_data.get("genre")
        if len(Genre.objects.filter(label = genre).values_list('genre')) == 0:
            g = Genre.objects.create(label = genre)
            g.save()
        user = request.user.username
        au_id = SampledepotappUsers.objects.filter(username = user)[0]
        #comment_new = Comments.objects.create(comment_id = str(hash(title))[1:5], music_id = str(hash(title))[1:5])
        #comment_new.save()
        new_music = Music.objects.create(title = title, genre = Genre.objects.filter(label = genre)[0], sampledepotappusers = au_id)
        #person =  SampledepotappUsers.objects.filter(username__in = user)[0]
        #person.music.add(music = new_music)
        new_music.save()
        #person.save()

    return render(request, "forms.html", {"form": form})
