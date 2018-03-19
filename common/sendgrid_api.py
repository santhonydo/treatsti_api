import sendgrid
import os
print sendgrid
print sendgrid.SendGridAPIClient
sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('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'))

def send_mail (from_email_str, to_email_str, subject=None, message=None, html=None, cc=None):
	
	if html:
		content = [{
			"type": "text/html",
			"value": html
		}]
	else:
		content = [
			{
				"type":"text/plain",
				"value": message
			}
		]

	cc_emails = [{'email': email} for email in cc] if cc else []

	data = {
	  	"personalizations": [
		    {
		      	"to": [{
		          	"email": from_email_str
		        }],
		      	"subject": subject,
	  			"cc": cc_emails,
		    },
	  	],
	  	"from": {
	    	"email": to_email_str
	  	},
	  	"content": content,
	}

	response = sg.client.mail.send.post(request_body=data)
	return response
