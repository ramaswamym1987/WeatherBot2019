from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import warnings

from rasa.core.agent import Agent
from rasa.core.interpreter import RasaNLUInterpreter
from rasa.core.channels.console import CmdlineInput
from rasa.utils.endpoints import EndpointConfig
import asyncio
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='./log/botchat_log.txt')

import rasa
from rasa.core.run import serve_application
def run_weather_bot(serve_forever=True):
    interpreter = RasaNLUInterpreter('./models/nlu/current')
    action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
    agent = Agent.load('./models/dialogue', interpreter = interpreter, action_endpoint=action_endpoint)
    if serve_forever:
        agent.handle_channels([CmdlineInput()])
    return agent

'''
from rasa.core.interpreter import NaturalLanguageInterpreter

def run(dbug=False):
    if dbug:
        init_debug_logging()
    interpreter = NaturalLanguageInterpreter.create("./models/nlu/current")
    action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
    agent = Agent.load("models/dialog", interpreter=interpreter,action_endpoint=action_endpoint)
    rasa.core.run.serve_application(agent,channel='cmdline')
'''

if __name__ == '__main__':
    warnings.filterwarnings(action='ignore', category=DeprecationWarning)
    run_weather_bot()
