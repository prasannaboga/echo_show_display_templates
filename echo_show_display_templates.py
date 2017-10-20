from __future__ import print_function
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
  # logger.info("=== event ===")
  # logger.info(json.dumps(event))
  
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
  logger.info(" ** intent_name ** " + intent_name)
  
  if intent_name == "DesignTemplate":
    return get_welcome_response()
  elif intent_name == "BodyTemplateOne":
    return body_template_one(intent, session)
  elif intent_name == "BodyTemplateTwo":
    return body_template_two(intent, session)
  elif intent_name == "BodyTemplateThree":
    return body_template_three(intent, session)
  elif intent_name == "BodyTemplateSix":
    return body_template_six(intent, session)
  elif intent_name == "ListTemplateOne":
    return list_template_one(intent, session)
  elif intent_name == "ListTemplateTwo":
    return list_template_two(intent, session)
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
  """ Why card response, hint is not coming """
  session_attributes = {}
  speech_response = {'text': 'Body Template One....'}
  card_response = {
    'type': 'Standard',
    'title': 'Body Template One Card',
    'text': 'Body Template One Card',
    'image': {
      'smallImageUrl': 'https://s3.amazonaws.com/the-shire/alexa/welcome_001.jpg',
      'largeImageUrl': 'https://s3.amazonaws.com/the-shire/alexa/welcome_001.jpg'
    }
  }
  directives = [
    {
      "type": "Display.RenderTemplate",
      "template": {
        "type": "BodyTemplate1",
        "token": "BT01",
        "backButton": "VISIBLE",
        "backgroundImage": {
          "contentDescription": "body_template_one",
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
            "text": '<font size="5">Body Template secondaryText</font>',
            "type": "RichText"
          },
          "tertiaryText": {
            "text": "<b>Body</b> <i>Template</i> <u>tertiaryText</u>",
            "type": "RichText"
          }
        }
      }
    }, {
      "type": "Hint",
      "hint": {
        "type": "PlainText",
        "text": "body template two.."
      }
    }
  ]
  return build_response(session_attributes, build_speechlet_response(speech_response, card_response, directives))


def body_template_two(intent, session):
  session_attributes = {}
  speech_response = {'text': 'Body Template Two....'}
  card_response = {
    'type': 'Standard',
    'title': 'Body Template Two Card',
    'text': 'Body Template Two Card',
    'image': {
      'smallImageUrl': 'https://s3.amazonaws.com/the-shire/alexa/welcome_001.jpg',
      'largeImageUrl': 'https://s3.amazonaws.com/the-shire/alexa/welcome_001.jpg'
    }
  }
  directives = [
    {
      "type": "Display.RenderTemplate",
      "template": {
        "type": "BodyTemplate2",
        "token": "BT02",
        "backButton": "VISIBLE",
        "backgroundImage": {
          "contentDescription": "body_template_two",
          "sources": [
            {
              "url": "https://s3.amazonaws.com/the-shire/alexa/body_template_two_1.jpg"
            },
            {
              "url": "https://s3.amazonaws.com/the-shire/alexa/body_template_two_2.jpg"
            }
          ]
        },
        "title": "Body Template Two",
        "image": {
          "contentDescription": "body_template_two",
          "sources": [
            {
              "url": "https://s3.amazonaws.com/the-shire/alexa/body_template_two_1.jpg"
            }
          ]
        },
        "textContent": {
          "primaryText": {
            "text": "Body Template primaryText",
            "type": "PlainText"
          },
          "secondaryText": {
            "text": "<font size='2'>Body Template secondaryText</font>",
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
        "text": "say body template three.."
      }
    }
  ]
  return build_response(session_attributes, build_speechlet_response(speech_response, card_response, directives))


def body_template_three(intent, session):
  session_attributes = {}
  speech_response = {'text': 'Body Template Three....'}
  card_response = {
    'type': 'Standard',
    'title': 'Body Template Three Card',
    'text': 'Body Template Three Card',
    'image': {
      'smallImageUrl': 'https://s3.amazonaws.com/the-shire/alexa/welcome_001.jpg',
      'largeImageUrl': 'https://s3.amazonaws.com/the-shire/alexa/welcome_001.jpg'
    }
  }
  directives = [
    {
      "type": "Display.RenderTemplate",
      "template": {
        "type": "BodyTemplate3",
        "token": "BT03",
        "backButton": "VISIBLE",
        "backgroundImage": {
          "contentDescription": "body_template_three",
          "sources": [
            {
              "url": "https://s3.amazonaws.com/the-shire/alexa/body_template_three.jpg"
            }
          ]
        },
        "title": "Body Template Three",
        "image": {
          "contentDescription": "body_template_three",
          "sources": [
            {
              "url": "https://s3.amazonaws.com/the-shire/alexa/body_template_three.jpg"
            }
          ]
        },
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
        "text": "say body template six.."
      }
    }
  ]
  return build_response(session_attributes, build_speechlet_response(speech_response, card_response, directives))


def body_template_six(intent, session):
  session_attributes = {}
  speech_response = {'text': 'Body Template Six....'}
  card_response = {
    'type': 'Standard',
    'title': 'Body Template Six Card',
    'text': 'Body Template Six Card',
    'image': {
      'smallImageUrl': 'https://s3.amazonaws.com/the-shire/alexa/welcome_001.jpg',
      'largeImageUrl': 'https://s3.amazonaws.com/the-shire/alexa/welcome_001.jpg'
    }
  }
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
        "text": "say body template one.."
      }
    }
  ]
  return build_response(session_attributes, build_speechlet_response(speech_response, card_response, directives))


def list_template_one(intent, session):
  session_attributes = {}
  speech_response = {'text': 'List Template One....'}
  card_response = {
    'type': 'Standard',
    'title': 'List Template One Card',
    'text': 'List Template One Card',
    'image': {
      'smallImageUrl': 'https://s3.amazonaws.com/the-shire/alexa/welcome_001.jpg',
      'largeImageUrl': 'https://s3.amazonaws.com/the-shire/alexa/welcome_001.jpg'
    }
  }
  
  list_items = []
  for i in range(1, 6):
    _i = str(i)
    item = {
      "token": "LI0"+_i,
      "image": {
        "contentDescription": "LI0"+_i,
        "sources": [
          {
            "url": "https://s3.amazonaws.com/the-shire/alexa/00{}.jpg".format(_i)
          }
        ]
      },
      "textContent": {
        "primaryText": {
          "text": "PrimaryText 0"+_i,
          "type": "PlainText"
        },
        "secondaryText": {
          "text": "SecondaryText 0"+_i,
          "type": "PlainText"
        },
        "tertiaryText": {
          "text": "TertiaryText 0"+_i,
          "type": "PlainText"
        }
      }
    }
    list_items.append(item)
  
  directives = [
    {
      "type": "Display.RenderTemplate",
      "template": {
        "type": "ListTemplate1",
        "token": "LT01",
        "backButton": "VISIBLE",
        "backgroundImage": {
          "contentDescription": "list_template_one",
          "sources": [
            {
              "url": "https://s3.amazonaws.com/the-shire/alexa/list_template_one.jpg"
            }
          ]
        },
        "title": "List Template One",
        "listItems": list_items
      }
    },
    {
      "type": "Hint",
      "hint": {
        "type": "PlainText",
        "text": "say list template two.."
      }
    }
  ]
  return build_response(session_attributes, build_speechlet_response(speech_response, card_response, directives))


def list_template_two(intent, session):
  session_attributes = {}
  speech_response = {'text': 'List Template Two....'}
  card_response = {
    'type': 'Standard',
    'title': 'List Template Two Card',
    'text': 'List Template Two Card',
    'image': {
      'smallImageUrl': 'https://s3.amazonaws.com/the-shire/alexa/welcome_001.jpg',
      'largeImageUrl': 'https://s3.amazonaws.com/the-shire/alexa/welcome_001.jpg'
    }
  }
  
  list_items = []
  for i in range(1, 6):
    _i = str(i)
    item = {
      "token": "LI20" + _i,
      "image": {
        "contentDescription": "LI20" + _i,
        "sources": [
          {
            "url": "https://s3.amazonaws.com/the-shire/alexa/00{}.jpg".format(_i)
          }
        ]
      },
      "textContent": {
        "primaryText": {
          "text": "PrimaryText 0" + _i,
          "type": "PlainText"
        },
        "secondaryText": {
          "text": "SecondaryText 0" + _i,
          "type": "PlainText"
        },
        "tertiaryText": {
          "text": "TertiaryText 0" + _i,
          "type": "PlainText"
        }
      }
    }
    list_items.append(item)
  
  directives = [
    {
      "type": "Display.RenderTemplate",
      "template": {
        "type": "ListTemplate2",
        "token": "LT02",
        "backButton": "VISIBLE",
        "backgroundImage": {
          "contentDescription": "list_template_two",
          "sources": [
            {
              "url": "https://s3.amazonaws.com/the-shire/alexa/list_template_two.jpg"
            }
          ]
        },
        "title": "List Template Two",
        "listItems": list_items
      }
    },
    {
      "type": "Hint",
      "hint": {
        "type": "PlainText",
        "text": "say list template one.."
      }
    }
  ]
  return build_response(session_attributes, build_speechlet_response(speech_response, card_response, directives))


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
