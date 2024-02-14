import os
import boto3
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def createSession(session):
    #create Session object in DDB
    ddb_table_name = os.environ.get('DYNAMODB_PERSISTENCE_TABLE_NAME')
    logger.info(ddb_table_name)
    dynamodb = boto3.client('dynamodb')
    key = dynamodb.put_item(
        TableName=ddb_table_name,
        Item={
            'id': {
                'S': session
                },
            'name': {
                'S': ''
                },
            'lives' : {
                'N': '3'
                },
            'q1': {
                'BOOL': False
                },
            'q2': {
                'BOOL': False
                },
            'q3': {
                'BOOL': False
                },
            'q4': {
                'BOOL': False
                },
            'q5': {
                'BOOL': False
                }
            }
    )
    #sessionInfo = key['Item']
    logger.info(key)
    #logger.info(sessionInfo)
    return key

def getSessionInfo(session):
    #Pull Session Info from DDB
    ddb_table_name = os.environ.get('DYNAMODB_PERSISTENCE_TABLE_NAME')
    logger.info(ddb_table_name)
    dynamodb = boto3.client('dynamodb')
    key = dynamodb.get_item(
        TableName=ddb_table_name,
        Key={
            'id': {
                'S': session
                }
            }
    )
    sessionInfo = key['Item']
    logger.info(key)
    logger.info(sessionInfo)
    return sessionInfo


def updateName(session, name):
    ddb_table_name = os.environ.get('DYNAMODB_PERSISTENCE_TABLE_NAME')
    logger.info(ddb_table_name)
    dynamodb = boto3.client('dynamodb')
    key = dynamodb.update_item(
        TableName=ddb_table_name,
        Key={
            'id': {
                'S': session
                }
            },
        AttributeUpdates={
            'name': {
                'Value': {
                    'S': name
                    }
                }
            }
    )
    #sessionInfo = key['Item']
    logger.info(key)
    #logger.info(sessionInfo)
    return key

def updateQuestion(session, question):
    ddb_table_name = os.environ.get('DYNAMODB_PERSISTENCE_TABLE_NAME')
    logger.info(ddb_table_name)
    dynamodb = boto3.client('dynamodb')
    key = dynamodb.update_item(
        TableName=ddb_table_name,
        Key={
            'id': {
                'S': session
                }
            },
        AttributeUpdates={
            question : {
                'Value': {
                    'BOOL': True
                    }
                }
            }
    )
    #sessionInfo = key['Item']
    logger.info(key)
    #logger.info(sessionInfo)
    return key

def loseLife(session):
    sessionInfo = getSessionInfo(session)
    lives = sessionInfo['lives']['N']
    lives = int(lives) - 1
    
    ddb_table_name = os.environ.get('DYNAMODB_PERSISTENCE_TABLE_NAME')
    logger.info(ddb_table_name)
    dynamodb = boto3.client('dynamodb')
    key = dynamodb.update_item(
        TableName=ddb_table_name,
        Key={
            'id': {
                'S': session
                }
            },
        AttributeUpdates={
            'lives' : {
                'Value': {
                    'N': str(lives)
                    }
                }
            }
    )
    #sessionInfo = key['Item']
    logger.info(key)
    #logger.info(sessionInfo)
    if lives==0:
        return "Game Over"
    else:
        return lives
    