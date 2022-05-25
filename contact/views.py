from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.


def contact(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        number = request.POST.get('number')
        message = request.POST.get('message')

        data = {
            'full_name': full_name,
            'email': email,
            'subject': subject,
            'number': number,
            'message': message

        }
        message = '''
        New message: {}

        from: {}
        '''.format(data['message'], data['email'])
        send_mail(data['subject'], message, '',
         ['osarobovictors@gmail.com'])
        return HttpResponse('message has been sent')
        

    else:
        return render(request, "contact.html", {})
