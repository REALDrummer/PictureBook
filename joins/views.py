from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from .forms import EmailForm, JoinForm
from .models import Join

def home(request):
	#print request.POST["email"], request.POST["email_2"]
#	form = EmailForm(request.POST or None)

# This is using regular django forms
#	if form.is_valid():
#		email = form.cleaned_data['email']
#		new_join, created = Join.objects.get_or_create(email = email)
#		print new_join, created
#		print new_join.timestamp
#		if created:
#			print "This object was created"

#this is using model forms
	form = JoinForm(request.POST or None)
	if form.is_valid():
		new_join = form.save(commit = False) 
		#we might do somehting here
		email = form.cleaned_data['email']
		password = hash(form.cleaned_data['password'])
		
		new_join_old, created = Join.objects.get_or_create(email = email, password = password)
		#new_join.save()
		messages.success(request, 'Your account has been successfully created.')

	context = {"form": form}
	template = "home.html"
	return render(request, template, context)


