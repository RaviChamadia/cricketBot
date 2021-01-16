import botCommands
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
@app.route('/',methods=['POST','GET'])

def cricketBot():
    incoming_msg=request.values.get('Body')
    messageList=incoming_msg.split(" ")
    response=MessagingResponse()
    if len(messageList)>1:
        response.message(botCommands.commands(messageList[0],messageList[1]))
        return str(response)
    else:
        response.message(botCommands.commands(messageList[0]))
        return str(response)


if __name__=="__main__":
    app.run()
