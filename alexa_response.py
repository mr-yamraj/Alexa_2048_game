from dynamodb_data import get_item, put_item
from game_play_template_650x280 import game_play_template_1
from game_play_template_1020x150 import game_play_template_2
from start_app_window import start_app_window_template

def get_useid(session):
    userid = session["user"]["userId"]
    account_key = userid.split('.')[3]
    return account_key

def user_in_database(userid):
    response = get_item(userid, ["gameplayed", "gamesaved"])
    try:
        gameplayed = response["Item"]["gameplayed"]["N"]
    except:
        gameplayed = None
    if gameplayed == None:
        gameplayed = 0
        response1 = put_item(userid)
        outputSpeech_text = "<speak>" + "Welcome to two zero four eight game. Looks like it is your first time. Lets break all the records" + "</speak>"
        repromt_outputSpeech_text = "<speak>" + "Just say start four cross four" + "</speak>"
    elif gameplayed == 0:
        outputSpeech_text = "<speak>" + "Welcome back to two zero four eight game. Looks like you havent played yet. Just say start four cross four" + "</speak>"
        repromt_outputSpeech_text = "<speak>" + "It is an easy game you just have to say direction to move the blocks and increase your score. To start say start four cross four" + "</speak>"
    else:
        try:
            gamesaved = response["gamesaved"]["BOOL"]
            if gamesaved == True:
                outputSpeech_text = "<speak>" + "Welcome back buddy. You have a saved game. Do you want to resume playing that?" + "</speak>"
                repromt_outputSpeech_text = "<speak>" + "Just say start saved game or start a new game" + "</speak>"
            else:
                outputSpeech_text = "<speak>" + "Welcome back buddy. Which high score you want to beat" + "</speak>"
                repromt_outputSpeech_text = "<speak>" + "Just say start four cross four" + "</speak>"
        except:
            gamesaved = False
            outputSpeech_text = "<speak>" + "Welcome back buddy. Which high score you want to beat" + "</speak>"
            repromt_outputSpeech_text = "<speak>" + "Just say start four cross four" + "</speak>"
    return outputSpeech_text, repromt_outputSpeech_text, gameplayed, gamesaved

def get_welcome_response(session):
    userid = get_useid(session)
    outputSpeech_text, repromt_outputSpeech_text, gameplayed, gamesaved = user_in_database(userid)
    response = get_response(outputSpeech_text=outputSpeech_text, repromt_outputSpeech_text=repromt_outputSpeech_text, template=start_app_window_template, session=session)
    sessionAttributes = get_session_attributes(userid=userid)
    return give_response(response=response, sessionAttributes=sessionAttributes)

def game_type(temp):
    #move the blocks to increase your score
    outputSpeech_text = "<speak> Starting new "
    if temp == 3:
        outputSpeech_text += "three cross three "
    elif temp in [2, 4]:
        outputSpeech_text += "four cross four "
    elif temp == 5:
        outputSpeech_text += "five cross five "
    outputSpeech_text += "stratigically move the blocks to increase your score </speak>"
    repromt_outputSpeech_text = "<speak> Say Up Down Left Right to move the blocks </speak>"
    return outputSpeech_text, repromt_outputSpeech_text

def get_newgame_response(temp, mat, session):
    userid = get_useid(session)
    url_image = make_image(mat, userid)
    outputSpeech_text, repromt_outputSpeech_text = game_type(temp)
    game_play_template_1["dataSources"]["bodyTemplate3Data"]["image"]["sources"][0]["url"] = url_image
    game_play_template_1["dataSources"]["bodyTemplate3Data"]["image"]["sources"][1]["url"] = url_image
    response = get_response(outputSpeech_text=outputSpeech_text, repromt_outputSpeech_text=repromt_outputSpeech_text, template=game_play_template_1, session=session)
    sessionAttributes = get_session_attributes(userid=userid)
    return give_response(response=response, sessionAttributes=sessionAttributes)


def get_session_attributes(current_mat = [[0,0,0],[0,0,0],[0,0,0]], prev_session_attributes = {}, userid = ""):
    sessionAttributes = {}
    sessionAttributes["current_mat"] = current_mat
    sessionAttributes["userid"] = userid
    return sessionAttributes

def get_outputSpeech(outputSpeech_type, outputSpeech_text):
    outputSpeech = {}
    outputSpeech["type"] = outputSpeech_type
    outputSpeech["text"] = outputSpeech_text
    return outputSpeech

def get_card(card_type, card_title, card_content, card_text):
    card = {}
    card["type"] = card_type
    card["title"] = card_title
    card["content"] = card_content
    card["text"] = card_text
    return card

def get_repromt(repromt_outputSpeech_type, repromt_outputSpeech_text):
    reprompt = {}
    reprompt["outputSpeech"] = get_outputSpeech(repromt_outputSpeech_type, repromt_outputSpeech_text)
    return reprompt

response = {
        'version': '1.0',
        'sessionAttributes': {},
        'response': {
            "directives": [
                {
                    "type": "Alexa.Presentation.APL.RenderDocument",
                    "datasources": start_app_window_template["dataSources"],
                    "document": start_app_window_template["document"]
                }
            ],
            "outputSpeech": {
                "type": "SSML",
                "ssml": '''<speak>'''+"speech_response"+''' </speak>'''
            },
            "reprompt": {
                "outputSpeech": {
                    "type": "SSML",
                    "ssml": "<speak>how can i help you ?</speak>"
                }
            },
            "shouldEndSession": True,
            "card": {
                "type": "Standard",
                "title": "content.simpleCardTitle",
                "content": "content.simpleCardContent"
            }
        }
    }

def get_directives(template, current_mat):
    directives = {}
    directives["type"] = "Alexa.Presentation.APL.RenderDocument"
    directives["datasources"] = template["dataSources"]
    directives["document"] = template["document"]
    return [directives]


def get_response(outputSpeech_text, session, outputSpeech_type = "PlainText", card_type = "SSML", card_title = "", card_content = "", card_text = "", repromt_outputSpeech_type = "SSML", repromt_outputSpeech_text = "", shouldEndSession = True, current_mat = [[0,0,0],[0,0,0],[0,0,0]], template = "list"):
    response = {}
    response["outputSpeech"] = get_outputSpeech(outputSpeech_type, outputSpeech_text)
    if card_title != "":
        response["card"] = get_card(card_type, card_title, card_content, card_text)
    if repromt_outputSpeech_text != "":
        response["reprompt"] = get_repromt(repromt_outputSpeech_type, repromt_outputSpeech_text)
    response["shouldEndSession"] = shouldEndSession
    response["directives"] = get_directives(template, current_mat, session)
    return response

def give_response(response, session_attributes = {}):
    lambda_response = {}
    lambda_response["version"] = "string"
    if session_attributes != {}:
        lambda_response["sessionAttributes"] = session_attributes
    lambda_response["response"] = response
    return lambda_response