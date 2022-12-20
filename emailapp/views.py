from django.shortcuts import render

from datetime import datetime

from .utils import send_email_with_html_body

# Create your views here.



def create_view(request, *args, **kwargs):
    """ This view help to create and account for testing sending mails."""
    cxt = {}
    if request.method == "POST":
        email = request.POST.get('email')

        subjet = "Test Email"
        template = 'email.html'
        context = {
            'date': datetime.today().date,
            'email': email
        }

        receivers = [email]

        has_send = send_email_with_html_body(
            subjet=subjet,
            receivers=receivers,
            template=template,
            context=context
            )

        if has_send:
           cxt =  {"msg":"mail envoyee avec success."}
        else:
            cxt = {'msg':'email envoie echoue.'}

    return render(request, 'index.html', cxt)       