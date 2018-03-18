from django.shortcuts import render
from django.core.exceptions import SuspiciousOperation
from django.http import HttpResponse
from common.sendgrid import send_mail
import stripe

stripe.api_key = "sk_live_G0h2V0jwMQhp3SYNlpyX61A3"

def create_charge(req):
	try:
		stripe.Charge.create(amount=req.amount, source=req.source, description=req.description, currency='usd')
		send_mail(
			from_email_str='admin@treatsti.com', 
			to_email_str='drphan@firstdoc.co', 
			cc=['anthony@firstdoc.co', 'tracy@firstdoc.co']
			message=description,
			subject='Payment charge created'
		)
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

