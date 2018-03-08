from django.shortcuts import render
from django.core.exceptions import SuspiciousOperation
from django.http import HttpResponse
from common.firebase import firebase
from bson import ObjectId
from django.http import JsonResponse

Users = db.child("users")

def create_user(req):
	new_user = req.data
	token = ObjectId()
	setattr(new_user, 'token', ObjectId())
	Users.push(req.data)
	return JsonResponse({'token': token})

def get_user(req):
	user = Users.order_by_value('token').get(req.data.token)
	return JsonResponse(user)

handlers = {
	'POST': create_user,
	'GET': get_user
}

def index(request):
	handler = handlers[request.method]
	if handler:
		handlers(request)
	else: 
		return HttpResponse(status=404)
