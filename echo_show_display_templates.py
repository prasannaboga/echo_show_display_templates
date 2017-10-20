from __future__ import print_function
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
  #logger.info("=== event ===")
  #logger.info(json.dumps(event))
  
  if event['session']['new']:
    print("event['session']['new']")
  if event['request']['type'] == "LaunchRequest":
    return on_launch(event['request'], event['session'])
  elif event['request']['type'] == "IntentRequest":
    on_intent_response = on_intent(event['request'], event['session'])
    logger.info(json.dumps(on_intent_response))
    return on_intent_response
  elif event['request']['type'] == "SessionEndedRequest":
    return on_session_ended(event['request'], event['session'])


def on_launch(launch_request, session):
  return get_welcome_response()


def on_intent(intent_request, session):
  intent = intent_request['intent']
  intent_name = intent_request['intent']['name']
  
  if intent_name == "DesignTemplate":
    return get_welcome_response()
  elif intent_name == "BodyTemplateOne":
    return body_template_one(intent, session)
  elif intent_name == "BodyTemplateTwo":
    return body_template_two(intent, session)
  elif intent_name == "AMAZON.HelpIntent":
    return get_welcome_response()
  else:
    raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
  print("on_session_ended")


def get_welcome_response():
  session_attributes = {}
  text_response = {'title': 'Echo Show Display Templates',
                   'text': 'Welcome Echo Show Display Templates....'}
  card_response = {
    'type': 'Standard',
    'title': 'Echo Show Display Templates',
    'text': 'Welcome Echo Show Display Templates....',
    'image': {
      'smallImageUrl': 'https://s3.amazonaws.com/the-shire/alexa/welcome_001.jpg',
      'largeImageUrl': 'https://s3.amazonaws.com/the-shire/alexa/welcome_001.jpg'
    }
  }
  return build_response(session_attributes, build_speechlet_response(text_response, card_response))


def body_template_one(intent, session):
  session_attributes = {}
  speech_response = {'text': 'Body Template One....'}
  directives = [
    {
      "type": "Display.RenderTemplate",
      "template": {
        "type": "BodyTemplate1",
        "token": "string",
        "backButton": "VISIBLE",
        "backgroundImage": {
          "contentDescription": "string",
          "sources": [
            {
              "url": "https://s3.amazonaws.com/the-shire/alexa/body_template_one.jpg"
            }
          ]
        },
        "title": "Body Template One",
        "textContent": {
          "primaryText": {
            "text": "Body Template primaryText",
            "type": "PlainText"
          },
          "secondaryText": {
            "text": "<font size='4'>Body Template secondaryText</font>",
            "type": "RichText"
          },
          "tertiaryText": {
            "text": "Body Template tertiaryText",
            "type": "PlainText"
          }
        }
      }
    }
  ]
  return build_response(session_attributes, build_speechlet_response(speech_response, {}, directives))


def body_template_two(intent, session):
  session_attributes = {}
  speech_response = {'text': 'Body Template Two....'}
  directives = [
    {
      "type": "Display.RenderTemplate",
      "template": {
        "type": "BodyTemplate1",
        "token": "string",
        "backButton": "VISIBLE",
        "backgroundImage": {
          "contentDescription": "string",
          "sources": [
            {
              "url": "https://s3.amazonaws.com/the-shire/alexa/body_template_one.jpg"
            }
          ]
        },
        "title": "Body Template Two",
        "textContent": {
          "primaryText": {
            "text": "Body Template primaryText",
            "type": "PlainText"
          },
          "secondaryText": {
            "text": "<font size='4'>Body Template secondaryText</font>",
            "type": "RichText"
          },
          "tertiaryText": {
            "text": "Body Template tertiaryText",
            "type": "PlainText"
          }
        }
      }
    },
    {
      "type": "Hint",
      "hint": {
        "type": "PlainText",
        "text": "Alexa, say body template three.."
      }
    }
  ]
  return build_response(session_attributes, build_speechlet_response(speech_response, {}, directives))

def body_template_three(intent, session):
  session_attributes = {}
  speech_response = {'text': 'Body Template Two....'}
  directives = [
    {
      "type": "Display.RenderTemplate",
      "template": {
        "type": "BodyTemplate1",
        "token": "string",
        "backButton": "VISIBLE",
        "backgroundImage": {
          "contentDescription": "string",
          "sources": [
            {
              "url": "https://s3.amazonaws.com/the-shire/alexa/body_template_one.jpg"
            }
          ]
        },
        "title": "Body Template Two",
        "textContent": {
          "primaryText": {
            "text": "Body Template primaryText",
            "type": "PlainText"
          },
          "secondaryText": {
            "text": "<font size='4'>Body Template secondaryText</font>",
            "type": "RichText"
          },
          "tertiaryText": {
            "text": "Body Template tertiaryText",
            "type": "PlainText"
          }
        }
      }
    },
    {
      "type": "Hint",
      "hint": {
        "type": "PlainText",
        "text": "Alexa, say body template three.."
      }
    }
  ]
  return build_response(session_attributes, build_speechlet_response(speech_response, {}, directives))

def body_template_six(intent, session):
  session_attributes = {}
  speech_response = {'text': 'Body Template Six....'}
  directives = [
    {
      "type": "Display.RenderTemplate",
      "template": {
        "type": "BodyTemplate6",
        "token": "Template6",
        "backButton": "VISIBLE",
        "backgroundImage": {
          "contentDescription": "string",
          "sources": [
            {
              "url": "https://s3.amazonaws.com/the-shire/alexa/body_template_six.jpg"
            }
          ]
        },
        "title": "Body Template Six",
        "textContent": {
          "primaryText": {
            "text": "Body Template primaryText",
            "type": "PlainText"
          },
          "secondaryText": {
            "text": "Body Template secondaryText",
            "type": "PlainText"
          },
          "tertiaryText": {
            "text": "Body Template tertiaryText",
            "type": "PlainText"
          }
        }
      }
    },
    {
      "type": "Hint",
      "hint": {
        "type": "PlainText",
        "text": "Alexa, say body template one.."
      }
    }
  ]
  return build_response(session_attributes, build_speechlet_response(speech_response, {}, directives))


def list_template_one(intent, session):
  session_attributes = {}
  speech_response = {'text': 'Body Template Two....'}
  directives = [
    {
      "type": "Display.RenderTemplate",
      "template": {
        "type": "BodyTemplate1",
        "token": "string",
        "backButton": "VISIBLE",
        "backgroundImage": {
          "contentDescription": "string",
          "sources": [
            {
              "url": "https://s3.amazonaws.com/the-shire/alexa/body_template_one.jpg"
            }
          ]
        },
        "title": "Body Template Two",
        "textContent": {
          "primaryText": {
            "text": "Body Template primaryText",
            "type": "PlainText"
          },
          "secondaryText": {
            "text": "<font size='4'>Body Template secondaryText</font>",
            "type": "RichText"
          },
          "tertiaryText": {
            "text": "Body Template tertiaryText",
            "type": "PlainText"
          }
        }
      }
    },
    {
      "type": "Hint",
      "hint": {
        "type": "PlainText",
        "text": "Alexa, say body template three.."
      }
    }
  ]
  return build_response(session_attributes, build_speechlet_response(speech_response, {}, directives))

def list_template_two(intent, session):
  session_attributes = {}
  speech_response = {'text': 'Body Template Two....'}
  directives = [
    {
      "type": "Display.RenderTemplate",
      "template": {
        "type": "BodyTemplate1",
        "token": "string",
        "backButton": "VISIBLE",
        "backgroundImage": {
          "contentDescription": "string",
          "sources": [
            {
              "url": "https://s3.amazonaws.com/the-shire/alexa/body_template_one.jpg"
            }
          ]
        },
        "title": "Body Template Two",
        "textContent": {
          "primaryText": {
            "text": "Body Template primaryText",
            "type": "PlainText"
          },
          "secondaryText": {
            "text": "<font size='4'>Body Template secondaryText</font>",
            "type": "RichText"
          },
          "tertiaryText": {
            "text": "Body Template tertiaryText",
            "type": "PlainText"
          }
        }
      }
    },
    {
      "type": "Hint",
      "hint": {
        "type": "PlainText",
        "text": "Alexa, say body template three.."
      }
    }
  ]
  return build_response(session_attributes, build_speechlet_response(speech_response, {}, directives))


def build_speechlet_response(speech_response, card_response={}, directives=[], reprompt_text=None,
                             should_end_session=False):
  return {
    'outputSpeech': {
      'type': 'PlainText',
      'text': speech_response['text']
    },
    'card': card_response,
    'directives': directives,
    'reprompt': {
      'outputSpeech': {
        'type': 'PlainText',
        'text': reprompt_text
      }
    },
    'shouldEndSession': should_end_session
  }


def build_response(session_attributes, speechlet_response):
  return {
    'version': '1.0',
    'sessionAttributes': session_attributes,
    'response': speechlet_response
  }
