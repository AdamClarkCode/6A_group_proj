import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','group_project_6A.settings')

import django
django.setup()
from oneWordStory.models import Story, Word, UserProfile

def populate():
    
    users = [
        {'username': 'Jason', 'password': 'jasonspassword'},
        {'username': 'Zack', 'password': 'zackspassword'},
        {'username': 'Billy', 'password': 'billyspassword'},
        {'username': 'Trini', 'password': 'trinispassword'},
        {'username': 'Kimberly', 'password': 'kimberlyspassword'},
        {'username': 'Tommy', 'password': 'tommyspassword'}
    ]
        
    stories = [
        {'title': 'The Man and the Dog', 'author': users[0], 'likes':5},
        {'title': 'School Dance', 'author': users[1], 'likes':7},
        {'title': 'Garden of Goodness', 'author': users[2], 'likes':2},
        {'title': 'The Pirate Attack', 'author': users[3], 'likes':3},
        {'title': 'Billy the Snake', 'author': users[4], 'likes':11},
        {'title': '3 Old Men', 'author': users[5], 'likes':6}
    ]
       
    words = [
        {'story': stories[0], 'userProfile': users[0], 'content': 'There'},
        {'story': stories[0], 'userProfile': users[1], 'content': 'once'},
        {'story': stories[0], 'userProfile': users[0], 'content': 'was'},
        {'story': stories[0], 'userProfile': users[2], 'content': 'a'},
        {'story': stories[0], 'userProfile': users[1], 'content': 'cat'},
           
        {'story': stories[1], 'userProfile': users[1], 'content': 'At'},
        {'story': stories[1], 'userProfile': users[4], 'content': 'the'},
        {'story': stories[1], 'userProfile': users[0], 'content': 'dance'},
        {'story': stories[1], 'userProfile': users[4], 'content': 'we'},
        {'story': stories[1], 'userProfile': users[1], 'content': 'danced'},
            
        {'story': stories[2], 'userProfile': users[2], 'content': 'Garden'},
        {'story': stories[2], 'userProfile': users[5], 'content': 'Garden'},  

        {'story': stories[3], 'userProfile': users[3], 'content': 'Pirates'},
        {'story': stories[3], 'userProfile': users[0], 'content': 'ate'},   
        {'story': stories[3], 'userProfile': users[3], 'content': 'my'},
        {'story': stories[3], 'userProfile': users[0], 'content': 'cake'},  
        
        {'story': stories[4], 'userProfile': users[4], 'content': 'Billy'},
        {'story': stories[4], 'userProfile': users[0], 'content': 'was'},   
        {'story': stories[4], 'userProfile': users[5], 'content': 'looking'},
        {'story': stories[4], 'userProfile': users[1], 'content': 'for'},  
        {'story': stories[4], 'userProfile': users[4], 'content': 'his'},
        {'story': stories[4], 'userProfile': users[3], 'content': 'friends'},   
        {'story': stories[4], 'userProfile': users[2], 'content': 'but'},
        {'story': stories[4], 'userProfile': users[4], 'content': 'died'},  
        
        {'story': stories[5], 'userProfile': users[5], 'content': '3'},  
        {'story': stories[5], 'userProfile': users[0], 'content': 'blind'},
        {'story': stories[5], 'userProfile': users[4], 'content': 'men'},   
        {'story': stories[5], 'userProfile': users[5], 'content': 'wearing'},
        {'story': stories[5], 'userProfile': users[2], 'content': 'pink'},  
    ]
      
    for user in users:
        add_user(user['username'],user['password'])
    for story in stories:
        add_story(story['title'], story['author'], story['likes'])
    for word in words:
        add_word(word['story'], word['userProfile'], word['content'])
    
def add_user(username,password):
    u = UserProfile.objects.get_or_create(user.username=username)[0]
    u.user.password = password
    u.save()
    return u
def add_story(title,author,likes):
    s = Story.objects.get_or_create(title=title)[0]
    s.author = author
    s.likes = likes
    s.save()
    return s
def add_word(story,userProfile,content):
    w = Word.objects.get_or_create()[0]
    w.story = story
    w.userProfile = userProfile
    w.content = content
    w.save()
    return w
        
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
