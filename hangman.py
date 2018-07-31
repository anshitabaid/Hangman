from random import randint
from bs4 import BeautifulSoup
import requests
def getMovies ():
    url="https://www.imdb.com/search/title?groups=top_250&sort=user_rating"
    response=requests.get (url);
    html_soup=BeautifulSoup (response.text, 'html.parser')
    movie_containers =html_soup.find_all ('div', class_='lister-item mode-advanced')
    words=[]
    l=0
    for movie in movie_containers:
        words.append ( movie.find ('h3',class_='lister-item-header').find ('a').get_text ())
        l+=1
    for i in range (l):
        words[i]=[c.upper() for c in words [i] ]
    return (words)


def new_game():
    words=getMovies ()
    word=words[randint(0,len(words)-1)]
    tries=7
    letters=[]
    status=True
    return (word, letters, tries,status)

def display(word, letters, tries):
    toprint =""
    for c in word:
        if (c in letters) or (c.isalpha()==False):
            #print(c, end=' ')
            toprint=toprint +c+" "
        else:
            toprint=toprint + "_ "
            #print  ('_', end=' ')
    toprint=toprint +"\nTries " + str(tries) + "\nLetters used: "+ str(letters)+"\n"
    return (toprint)

def legal(word, letters, current_letter, tries):
    msg=""
    if current_letter in letters:
        msg="Letter already entered"
    else:
        if current_letter in word:
        #print("\nCharacter found")
            msg="\nCharacter found\n"
        
        else:
        #print ("\nCharacter not found")
            msg="\nCharacter not found\n"
            tries-=1
    
        letters.append(current_letter)
    return (msg,letters, tries)

def isLost (word, letters, tries):
    flag=True
    for c in word:
        if (c not in letters):
            flag=False
            break
    if (flag==False and tries==0):
        return True
    else:
        return False

def isWon (word, letters, tries):
    flag=True
    for x in word:
        if x.isalnum() and x not in letters:
            flag=False
            break
    if (flag==True and tries>=0):
        return True
    else:
        return False
