from django.shortcuts import render, redirect

from .models import Record

def index(request):
    return redirect('login')


def stat(request):
    """ show stat of learning record. """
    context = {
        'stat_today': Record.get_today_stat(),
        'stat_seven_days': Record.get_seven_days_stat(),
        'stat_this_year': Record.get_this_year_stat(),
    }
    return render(request, 'record/stat.html', context=context)