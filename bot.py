#name: hangmanbot username: hangtheman_bot


import sys
from time import sleep
from hangman import *
from flask import Flask, request, jsonify
import requests

app=Flask(__name__)
token='your token goes here'
def sendMessage (chat_id, message):
    requests.post (url='https://api.telegram.org/bot'+token'/sendMessage', data={'chat_id':chat_id, 'text': message})
    return ''
    

@app.route ('/'+token, methods=['POST'])
def main ():
    data=request.get_json()
    current_letter=data['message']['text']
    chat_id=str(data['message']['chat']['id'])
    global word, letters, tries, status, over
    if (current_letter.lower()=='hi'):
        sendMessage(chat_id, "Hey there! \nSend 'Hi' to restart or 'Bye' to end the game anytime")
        (word, letters, tries,status)=new_game()
        over=False
        if not status:
            over=True
            sendMessage(chat_id, "Something went wrong")
        else:
            sendMessage(chat_id, display(word, letters, tries))
    elif (current_letter.lower()=='bye'):
        sendMessage(chat_id, "BYE!")
        over=True;
    elif not over:
        if (current_letter.isalnum () and len (current_letter)==1):
            (msg,letters, tries)=legal (word, letters, current_letter, tries)
            sendMessage (chat_id, msg)
            sendMessage(chat_id, display(word, letters, tries))
            if isLost(word,letters, tries):
                msg="Game lost :(\nThe movie is\n"+ "".join(word)+"\nSend 'Hi' to restart or 'Bye' to end the game anytime"
                sendMessage(chat_id, msg)
                over=True
            if  isWon(word,letters,tries):
                sendMessage(chat_id, "Game won!\nSend 'Hi' to restart or 'Bye' to end the game")
                over=True
        else:
            sendMessage(chat_id, "Single numbers and letters only!")
    return ''


if __name__=='__main__':
    app.run(host='0.0.0.0', port='8443', debug=True)
    