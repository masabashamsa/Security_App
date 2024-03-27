from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.middleware.csrf import get_token
from django.contrib.auth.decorators import login_required

def welcome(request):
    return render(request, 'welcome.html')

#def vulnerable_query(request):
 #   if request.method == 'GET':
  #      search_query = request.GET.get('query', '')
   #     with connection.cursor() as cursor:
    #        # Execute raw SQL query using the correct table name
     #       cursor.execute("SELECT * FROM your_app_name_user WHERE username = %s", [search_query])
      #      users = cursor.fetchall()
      #  return render(request, 'vulnerable_query.html', {'users': users})


def vulnerable_query(request):
    if request.method == 'GET':
        search_query = request.GET.get('query', '')
        # Use Django's ORM to perform the query
        users = User.objects.filter(username=search_query)
        return render(request, 'vulnerable_query.html', {'users': users})



#def vulnerable_change_password(request):
    #if request.method == 'POST':
     #   user_id = request.POST.get('user_id')
      #  new_password = request.POST.get('new_password')
       # user = User.objects.get(id=user_id)
        #user.set_password(new_password)
        #user.save()
        #return render(request, 'password_changed.html')
    #return render(request, 'vulnerable_change_password.html')


def vulnerable_change_password(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        new_password = request.POST.get('new_password')

        # Validate if the user has permission to change the password
        # You might want to implement additional permission checks here
        try:
            user = User.objects.get(id=user_id)
            user.set_password(new_password)
            user.save()
            return render(request, 'changed_password.html')
        except User.DoesNotExist:
            return render(request, 'invalid_user.html')  # Handle invalid user ID
    else:
        return render(request, 'vulnerable_change_password.html')
    