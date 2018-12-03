import json
from PIL import Image, ImageDraw, ImageFont
from random import random
from alexa_response import get_welcome_response
from game_play import start_game

dimention = 340

def lambda_handler(event, context):
	# print event
	if event["session"]["new"]:
		on_session_started(event["session"])
	if event["request"]["type"] == "LaunchRequest":
		return on_launch(event["request"], event["session"])
	elif event["request"]["type"] == "IntentRequest":
		return on_intent(event["request"], event["session"])
	elif event["request"]["type"] == "SessionEndedRequest":
		return on_session_ended(event["request"], event["session"])

def on_session_started(session):
	print "Starting new session."

def on_launch(launch_request, session):
	return get_welcome_response(session)

def on_intent(IntentRequest, session):
	intent = intent_request["intent"]
	intent_name = intent_request["intent"]["name"]

	if intent_name == "AMAZON.FallbackIntent":
		return get_Fallback_instructions(intent_request, session)
	elif intent_name == "AMAZON.CancelIntent":
		return get_Cancel_instructions(intent_request, session)
	elif intent_name == "AMAZON.HelpIntent":
		return get_Help_instructions(intent_request, session)
	elif intent_name == "AMAZON.StopIntent":
		return get_Stop_instructions(intent_request, session)
	elif intent_name == "AMAZON.NavigateHomeIntent":
		return get_NavigateHome_instructions(intent_request, session)
	elif intent_name == "directionIntent":
		return get_Direction_instructions(intent_request, session)
	elif intent_name == "newgameIntent":
		return get_NewGame_instructions(intent_request, session)
	elif intent_name == "myhighscoreIntent":
		return get_HighScore_instructions(intent_request, session)
	elif intent_name == "overallhighscoreIntent":
		return get_OverallHighScore_instructions(intent_request, session)
	elif intent_name == "reverseIntent":
		return get_Reverse_instructions(intent_request, session)
	elif intent_name == "AMAZON.MoreIntent":
		return get_More_instructions(intent_request, session)
	elif intent_name == "AMAZON.NavigateSettingsIntent":
		return get_NavigateSettings_instructions(intent_request, session)
	elif intent_name == "AMAZON.NextIntent":
		return get_Next_instructions(intent_request, session)
	elif intent_name == "AMAZON.PageUpIntent":
		return get_PageUp_instructions(intent_request, session)
	elif intent_name == "AMAZON.PageDownIntent":
		return get_PageDown_instructions(intent_request, session)
	elif intent_name == "AMAZON.PreviousIntent":
		return get_Previous_instructions(intent_request, session)
	elif intent_name == "AMAZON.ScrollRightIntent":
		return get_ScrollRight_instructions(intent_request, session)
	elif intent_name == "AMAZON.ScrollDownIntent":
		return get_ScrollDown_instructions(intent_request, session)
	elif intent_name == "AMAZON.ScrollLeftIntent":
		return get_ScrollLeft_instructions(intent_request, session)
	elif intent_name == "AMAZON.ScrollUpIntent":
		return get_ScrollUp_instructions(intent_request, session)

def get_NewGame_instructions(intent_request, session):
	game_id = intent_request["slots"]["game_type"]["resolutions"]["resolutionsPerAuthority"][0]["values"][0]["value"]["id"]
	if game_id=="1":
		a = 1
	elif game_id=="2":
		a = 1
	elif game_id in ["3","4","5"]:
		temp = int(game_id)
		mat = start_game(temp)
		return get_newgame_response(temp, mat, session)


if __name__ == "__main__":
	event = {
			"version": "1.0",
			"session": {
				"new": true,
				"sessionId": "amzn1.echo-api.session.8a4e4c19-8be3-47e2-b359-fc4c2cd00c99",
				"application": {
					"applicationId": "amzn1.ask.skill.1750447a-7d94-4a41-a561-d7f9c046db8f"
				},
				"user": {
					"userId": "amzn1.ask.account.AETW55NUAB6D2NLWYMHR2SZ3L3JB4EKHC74YGWRGFX5WGRIWQAEKUH7NSQAU4DEBP36ETAEUZQ54EFDTXPSLJGO2T6AFVMVLIADHIDMUS5IE6LFGGHKWOCLWCDOJS7OWDDPEOLK645R4235MGMIKLBKWT3NHTXTTAHZ6WRJKJ3RUIZQT6FWLZCEIGQ362MYRFYKXXB5RHAV5YHY"
				}
			},
			"context": {
				"Display": {},
				"System": {
					"application": {
						"applicationId": "amzn1.ask.skill.1750447a-7d94-4a41-a561-d7f9c046db8f"
					},
					"user": {
						"userId": "amzn1.ask.account.AETW55NUAB6D2NLWYMHR2SZ3L3JB4EKHC74YGWRGFX5WGRIWQAEKUH7NSQAU4DEBP36ETAEUZQ54EFDTXPSLJGO2T6AFVMVLIADHIDMUS5IE6LFGGHKWOCLWCDOJS7OWDDPEOLK645R4235MGMIKLBKWT3NHTXTTAHZ6WRJKJ3RUIZQT6FWLZCEIGQ362MYRFYKXXB5RHAV5YHY"
					},
					"device": {
						"deviceId": "amzn1.ask.device.AH77HIGY6SOQOOUHTOCZAB3BNVTQ6OMLWCTTY3C5FGTB22J4QOC4RVYXLP4RRJNVF5AFI2FDRLD5YMP55N2PT4ESKWHAOUFOTUSSXTDBN32A6GU5S2KPIVEVPRQVBGCUDZQMLNZVFXCVZQCAAGFYLJ3Q6RTQ",
						"supportedInterfaces": {
							"Display": {
								"templateVersion": "1.0",
								"markupVersion": "1.0"
							},
							"Alexa.Presentation.APL": {
								"runtime": {
									"maxVersion": "1.0"
								}
							}
						}
					},
					"apiEndpoint": "https://api.eu.amazonalexa.com",
					"apiAccessToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IjEifQ.eyJhdWQiOiJodHRwczovL2FwaS5hbWF6b25hbGV4YS5jb20iLCJpc3MiOiJBbGV4YVNraWxsS2l0Iiwic3ViIjoiYW16bjEuYXNrLnNraWxsLjE3NTA0NDdhLTdkOTQtNGE0MS1hNTYxLWQ3ZjljMDQ2ZGI4ZiIsImV4cCI6MTU0MzczOTIwMCwiaWF0IjoxNTQzNzM1NjAwLCJuYmYiOjE1NDM3MzU2MDAsInByaXZhdGVDbGFpbXMiOnsiY29uc2VudFRva2VuIjpudWxsLCJkZXZpY2VJZCI6ImFtem4xLmFzay5kZXZpY2UuQUg3N0hJR1k2U09RT09VSFRPQ1pBQjNCTlZUUTZPTUxXQ1RUWTNDNUZHVEIyMko0UU9DNFJWWVhMUDRSUkpOVkY1QUZJMkZEUkxENVlNUDU1TjJQVDRFU0tXSEFPVUZPVFVTU1hUREJOMzJBNkdVNVMyS1BJVkVWUFJRVkJHQ1VEWlFNTE5aVkZYQ1ZaUUNBQUdGWUxKM1E2UlRRIiwidXNlcklkIjoiYW16bjEuYXNrLmFjY291bnQuQUVUVzU1TlVBQjZEMk5MV1lNSFIyU1ozTDNKQjRFS0hDNzRZR1dSR0ZYNVdHUklXUUFFS1VIN05TUUFVNERFQlAzNkVUQUVVWlE1NEVGRFRYUFNMSkdPMlQ2QUZWTVZMSUFESElETVVTNUlFNkxGR0dIS1dPQ0xXQ0RPSlM3T1dERFBFT0xLNjQ1UjQyMzVNR01JS0xCS1dUM05IVFhUVEFIWjZXUkpLSjNSVUlaUVQ2RldMWkNFSUdRMzYyTVlSRllLWFhCNVJIQVY1WUhZIn19.HaSVcKu1_H2yzJooXucDfHItXjwi9jXZxp61_yHHCOuNtB_SKCwkAfzR5S5CKGQ2i8-eQmr2IMSnxiDILChRn5_ZfNX0incZCmIKxxVHGC0BvnwirbUPT6X89vK5mXLdM7wU23To2mgELhcA6b9uP8JkXbINqKl89LOVe5kRsx7_eX8bslAliUyYHEztEtcXDHrJr4hQSzJO1hqolO4IhaS10DBD8C2aCHtQoDnqOpg0LYJkV8orAn24h0gjTtH8XYZ6_c1VzLIN5rofbP2nl_cSKnLf0htVfeKlBoGE9pn5j3oxZ-X0iwOBai6WsYRuHmEBA8hUVS7gNqxMQGxzWQ"
				},
				"Viewport": {
					"experiences": [
						{
							"arcMinuteWidth": 246,
							"arcMinuteHeight": 144,
							"canRotate": False,
							"canResize": False
						}
					],
					"shape": "RECTANGLE",
					"pixelWidth": 1024,
					"pixelHeight": 600,
					"dpi": 160,
					"currentPixelWidth": 1024,
					"currentPixelHeight": 600,
					"touch": [
						"SINGLE"
					]
				}
			},
			"request": {
				"type": "IntentRequest",
				"requestId": "amzn1.echo-api.request.f41091b8-e5d0-4bfd-a0cd-3c934894bd2d",
				"timestamp": "2018-12-02T07:26:40Z",
				"locale": "en-IN",
				"intent": {
					"name": "newgameIntent",
					"confirmationStatus": "NONE",
					"slots": {
						"game_type": {
							"name": "game_type",
							"value": "3 cross 3",
							"resolutions": {
								"resolutionsPerAuthority": [
									{
										"authority": "amzn1.er-authority.echo-sdk.amzn1.ask.skill.1750447a-7d94-4a41-a561-d7f9c046db8f.game_type",
										"status": {
											"code": "ER_SUCCESS_MATCH"
										},
										"values": [
											{
												"value": {
													"name": "three cross three",
													"id": "3"
												}
											}
										]
									}
								]
							},
							"confirmationStatus": "NONE",
							"source": "USER"
						}
					}
				}
			}
		}
	print lambda_handler(event,{})
