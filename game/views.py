from django.shortcuts import render, redirect
from .forms import EntryForm
from django.contrib import messages
from .hangman_main import new_game, show_current_word
import datetime


def home_view(request):
    return render(request, 'game/home.html', {})

def contact_view(request):
     return render(request, 'game/contact.html', {'date': datetime.datetime.now().strftime('%A, %d %B %Y' )})

# checker = 1
def entry_view(request):
    if request.method == 'POST':
            my_form = EntryForm(request.POST)
            if my_form.is_valid():
                letter = my_form.cleaned_data.get('your_guess')
                result = new_game(letter)
                if result[-1] == 'Done !':
                     checker = True
                else:
                     checker = False
                return render(request, 'game/entry.html', {'my_form' : EntryForm(), 'data': result, 'checker': checker})
                     
            else:
                messages.error(request, f"{request.error}")
                return redirect('home')
    else:
        messages.info(request, """
    The hangman is about to hang this word,
        save the word by guessing it letter-by-letter
        """)
        messages.info(request, '\\\_("_")_//   Help Me!')

        return render(request, 'game/entry.html',{'my_form' : EntryForm(), 'starter': show_current_word()})
    