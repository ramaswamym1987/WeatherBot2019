from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import warnings

from rasa.nlu.training_data import load_data
from rasa.nlu import config
from rasa.nlu.model import Trainer

from rasa.core import utils
from rasa.core.agent import Agent
from rasa.core.policies.keras_policy import KerasPolicy
from rasa.core.policies.memoization import MemoizationPolicy

import asyncio
from rasa.core import config as policy_config

import logging
logger = logging.getLogger(__name__)
logging.basicConfig(filename='./log/dlog.txt')

def train_nlu():
    training_data = load_data('./data/nlu.md')
    trainer = Trainer(config.load("config.yml"))
    trainer.train(training_data)
    model_directory = trainer.persist('./models/nlu/', fixed_model_name="current")
    return model_directory

def train_dialogue(domain_file="domain.yml",model_path="./models/dialogue",training_data_file="./data/stories.md"):
    #agent = Agent(domain_file, policies=[MemoizationPolicy(max_history=3), KerasPolicy()])
    #training_data = agent.load_data(training_data_file)
    #agent.train(training_data,epochs=400,batch_size=100,validation_split=0.2)
    #agent.persist(model_path)

    policies = policy_config.load("./policies.yml")
    agent = Agent(domain_file, policies=policies)
    loop = asyncio.get_event_loop()
    dataa = loop.run_until_complete(agent.load_data(training_data_file))
    agent.train(dataa)
    agent.persist(model_path)

    return agent

if __name__ == '__main__':
    warnings.filterwarnings(action='ignore', category=DeprecationWarning)
    train_nlu()
    train_dialogue()
