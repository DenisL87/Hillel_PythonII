from django.shortcuts import render, redirect

from .forms import NewForm
from tasks import send_mail_to_admin


def email_reminder(request):
    if request.method == 'POST':
        form = NewForm(request.POST)
        if form.is_valid():
            subject = 'Reminder'
            email = form.cleaned_data['email']
            reminder = form.cleaned_data['reminder']
            datetime = form.cleaned_data['datetime']
            send_mail_to_admin.apply_async((subject, reminder, email), eta=datetime)
            # messages.add_message(request, messages.SUCCESS, 'Message sent')
            return redirect('email_reminder')
    else:
        form = NewForm()
    return render(request, 'reminder.html', {'form': form})
