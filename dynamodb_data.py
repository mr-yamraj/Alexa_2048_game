import boto3

dynamodb = boto3.client('dynamodb')
table_name = '2048_game_data'

def make_key(userid):
	key = {}
	temp = {}
	temp['S'] = account_key
	key['userid'] = temp
	return key

def make_projection_expression(items):
	temp_string = ""
	for i in range(len(items)):
		temp_string += items[i]
		if (i != len(items) - 1):
			temp_string += ', '
	return temp_string

def get_item(userid, items):
	response = dynamodb.get_item(
		TableName=table_name,
		Key = make_key(userid),
		ProjectionExpression=make_projection_expression(items),
	)
	return response

def put_item(userid):
	response = dynamodb.put_item(
		TableName=table_name,
		Item = {
			'userid':{
				"S" : account_key
			},
			'gameplayed':{
				'N':'0'
			}
		}
	)
	return response

def update_item(userid, sessionAttributes):
	response = dynamodb.update_item(
		TableName=table_name,
		Key = make_key(userid),
		AttributeUpdates = mkae_AttributeUpdates(sessionAttributes)
		)
	return response