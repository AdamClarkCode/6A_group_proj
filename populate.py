import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','group_project_6A.settings')

import django
django.setup()
from oneWordStory.models import Story, Word, UserProfile
from django.contrib.auth.models import User

def populate():
    
    users = [
        {'username': 'Jason', 'password': 'jasonspassword'},
        {'username': 'Zack', 'password': 'zackspassword'},
        {'username': 'Billy', 'password': 'billyspassword'},
        {'username': 'Trini', 'password': 'trinispassword'},
        {'username': 'Kimberly', 'password': 'kimberlyspassword'},
        {'username': 'Tommy', 'password': 'tommyspassword'}
    ]
    
    i=0 
    userData = {}
    
    for user in users:
        u = add_user(user['username'],user['password'])
        up = add_userProfile(u)
        userData[i] = up
        i+=1
        
    stories = [
        {'title': 'The Man and the Dog', 'likes':5, 'author':userData[0]},
        {'title': 'School Dance', 'likes':7, 'author':userData[1]},
        {'title': 'Garden of Goodness', 'likes':2, 'author':userData[2]},
        {'title': 'The Pirate Attack', 'likes':3, 'author':userData[3]},
        {'title': 'Billy the Snake', 'likes':11, 'author':userData[4]},
        {'title': '3 Old Men', 'likes':6, 'author':userData[5]}
    ]
    
    i=0 
    storyData = {}
    
    for story in stories:
        s = add_story(story['title'], story['likes'], story['author'])
        storyData[i] = s
        i+=1
       
    words = [
        {'story': storyData[0], 'userProfile': userData[0], 'content': 'There'},
        {'story': storyData[0], 'userProfile': userData[1], 'content': 'once'},
        {'story': storyData[0], 'userProfile': userData[0], 'content': 'was'},
        {'story': storyData[0], 'userProfile': userData[2], 'content': 'a'},
        {'story': storyData[0], 'userProfile': userData[1], 'content': 'cat'},
           
        {'story': storyData[1], 'userProfile': userData[1], 'content': 'At'},
        {'story': storyData[1], 'userProfile': userData[4], 'content': 'the'},
        {'story': storyData[1], 'userProfile': userData[0], 'content': 'dance'},
        {'story': storyData[1], 'userProfile': userData[4], 'content': 'we'},
        {'story': storyData[1], 'userProfile': userData[1], 'content': 'danced'},
            
        {'story': storyData[2], 'userProfile': userData[2], 'content': 'Garden'},
        {'story': storyData[2], 'userProfile': userData[5], 'content': 'Garden'},  

        {'story': storyData[3], 'userProfile': userData[3], 'content': 'Pirates'},
        {'story': storyData[3], 'userProfile': userData[0], 'content': 'ate'},   
        {'story': storyData[3], 'userProfile': userData[3], 'content': 'my'},
        {'story': storyData[3], 'userProfile': userData[0], 'content': 'cake'},  
        
        {'story': storyData[4], 'userProfile': userData[4], 'content': 'Billy'},
        {'story': storyData[4], 'userProfile': userData[0], 'content': 'was'},   
        {'story': storyData[4], 'userProfile': userData[5], 'content': 'looking'},
        {'story': storyData[4], 'userProfile': userData[1], 'content': 'for'},  
        {'story': storyData[4], 'userProfile': userData[4], 'content': 'his'},
        {'story': storyData[4], 'userProfile': userData[3], 'content': 'friends'},   
        {'story': storyData[4], 'userProfile': userData[2], 'content': 'but'},
        {'story': storyData[4], 'userProfile': userData[4], 'content': 'died'},  
        
        {'story': storyData[5], 'userProfile': userData[5], 'content': '3'},  
        {'story': storyData[5], 'userProfile': userData[0], 'content': 'blind'},
        {'story': storyData[5], 'userProfile': userData[4], 'content': 'men'},   
        {'story': storyData[5], 'userProfile': userData[5], 'content': 'wearing'},
        {'story': storyData[5], 'userProfile': userData[2], 'content': 'pink'},  
    ]
        

    for word in words:
        add_word(word['story'], word['userProfile'], word['content'])
    
def add_user(username,password):
    u = User.objects.get_or_create(username=username)[0]
    u.password = password
    u.save()
    return u
def add_userProfile(user):
    up = UserProfile.objects.get_or_create(user=user)[0]
    up.save()
    return up
def add_story(title,likes,author):
    s = Story.objects.get_or_create(title=title,author=author)[0]
    s.likes = likes
    s.save()
    return s
def add_word(story,userProfile,content):
    w = Word.objects.get_or_create(story=story,userProfile=userProfile,content=content)[0]
    w.story = story
    w.userProfile = userProfile
    w.content = content
    w.save()
    return w
        
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
