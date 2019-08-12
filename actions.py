import logging
import requests
import json
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from rasa_sdk.events import Restarted

logger = logging.getLogger(__name__)
logging.basicConfig(filename='./log/actions_log.txt')

class ActionRestart(Action):
    def name(self):
        return "action_restart"
    def run(self, dispatcher, tracker, domain):
        return [Restarted()]

'''
class ActionWeather(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_weather"
    def run(self, dispatcher, tracker, domain):
        # what your action should do
        location = tracker.get_slot('location')
        dispatcher.utter_message('Hi')  # send the message back to the user
        return []
'''

class ActionWeather(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_weather"
    def run(self, dispatcher, tracker, domain):
        from apixu.client import ApixuClient
        api_key = 'd47a4f7a5bc84662ac0113212193107'
        client = ApixuClient(api_key)
        loc = tracker.get_slot('location')
        current = client.current(q=loc)
        #country = current['location']['country']
        city = current['location']['name']
        condition = current['current']['condition']['text']
        temperature_c = current['current']['temp_c']
        humidity = current['current']['humidity']
        wind_mph = current['current']['wind_mph']
        response = """It is currently {} in {} at the moment. The temperature is {} degrees, the humidity is {}% and the wind speed is {} mph.""".format(condition, city, temperature_c, humidity, wind_mph)
        dispatcher.utter_message(response)
        return [SlotSet('location',loc)]

        '''
        print(tracker.get_slot('location'))
        dispatcher.utter_message('test weather ')
        return []'''
