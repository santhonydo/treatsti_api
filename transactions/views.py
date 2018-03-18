from django.shortcuts import render
from django.core.exceptions import SuspiciousOperation
from django.http import HttpResponse

import stripe

stripe.api_key = "sk_live_G0h2V0jwMQhp3SYNlpyX61A3"

def create_charge(req):
	try:
		stripe.Charge.create(amount=req.amount, source=req.source, description=req.description, currency='usd')
		return HttpResponse(status=200)
	except: 
		return HttpResponse(status=400)

handlers = {
	'POST': create_charge
}

def index(request):
	handler = handlers[request.method]
	if handler:
		handlers(request)
	else: 
		return HttpResponse(status=404)

