from django.shortcuts import render
# Create your views here.

rooms = [
    {'id': 1, 'name': 'General Cafe'},
    {'id': 2, 'name': 'Meet and Greet'},
    {'id': 3, 'name': 'Tech Talk'},
    {'id': 4, 'name': 'Gaming Arena'},
    {'id': 5, 'name': 'Movie Buffs'},
    {'id': 6, 'name': 'Music Lounge'},
    {'id': 7, 'name': 'Book Club'},
    {'id': 8, 'name': 'Fitness Corner'},
    {'id': 9, 'name': 'Foodie Haven'},
    {'id': 10, 'name': 'Travel Diaries'},
    {'id': 11, 'name': 'Artists\' Alley'},
    {'id': 12, 'name': 'Mindful Retreat'},
    {'id': 13, 'name': 'Study Group'},
    {'id': 14, 'name': 'Pet Park'},
    {'id': 15, 'name': 'Science Lab'},
    {'id': 16, 'name': 'Coding Hub'},
    {'id': 17, 'name': 'Entrepreneurs\' Exchange'},
    {'id': 18, 'name': 'DIY Workshop'},
    {'id': 19, 'name': 'Sports Field'},
    {'id': 20, 'name': 'Meme Central'}
]


def home(request):
    context = {'rooms': rooms}
    return render(request, "base/home.html", context)

def room(request):
    return render(request, "base/room.html")