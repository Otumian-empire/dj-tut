from django.shortcuts import render, HttpResponse, redirect


def home(request, username='No user'):
    title = "Home"
    username = request.GET['username']
    
    return render(
        request, 'accounts/home.html', {
            'title' : title,
            'username' : username})
    
    
def login(request):
    title = "Login"
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        if username and password:
            return redirect('/accounts/?username=' + str(username), username=username)
            
    return render(
        request, 'accounts/login.html', {
            'title': title})


