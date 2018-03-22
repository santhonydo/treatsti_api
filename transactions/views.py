from django.shortcuts import render
from django.core.exceptions import SuspiciousOperation
from django.http import HttpResponse
from common.sendgrid_api import send_mail
import stripe
from django.views.decorators.csrf import csrf_exempt

# stripe.api_key = "sk_live_G0h2V0jwMQhp3SYNlpyX61A3"
stripe.api_key = "sk_test_gNQIsH7UWOchs63rkKfIPmxm"


def create_charge(req):
	try:
		param = req.POST
		amount = param.get('amount')
		source = param.get('source')
		description = param.get('description')
		if amount > 0:
			stripe.Charge.create(amount=amount, source=source, description=description, currency='usd')
			send_mail(
				from_email_str='admin@treatsti.com', 
				to_email_str='drphan@firstdoc.co', 
				cc=['anthony@firstdoc.co', 'tracy@firstdoc.co'],
				message=description,
				subject='Payment charge created'
			)
			return HttpResponse(status=200)
	except Exception as e: 
		return HttpResponse(status=400)

	return HttpResponse(status=400)


handlers = {
	'POST': create_charge
}

@csrf_exempt
def index(request):
	handler = handlers[request.method]
	if handler:
		return handler(request)
	else: 
		return HttpResponse(status=404)

