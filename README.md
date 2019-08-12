# Weather Bot_2019

This chat bot let us know the weather.

# Rasa Installation
[https://rasa.com/docs/rasa/user-guide/installation/#installation](https://rasa.com/docs/rasa/user-guide/installation/#installation)

# Requirements

    pip install -r requirements.txt

# Steps:
1. Create a directory "weatherbot"
2. Inside the "weatherbot" directory create two sub-directories namely
    A. data
    B. models
3. Inside the "data" directory, create two files namely
    A. nlu.md     ---> holds the various intents to be used and its relevant content/data
    B. stories.md ---> holds the various story content/data formats how the chatbot behavies

    For "nlu.md" creation, initially create the nlu in "nlu.json" format as below and can be converted into "nlu.md" format using the command
    " rasa data convert nlu --data nlu.json --out nlu.md --format md "

                    {
                      "rasa_nlu_data":
                      {
                        "common_examples": [
                          {
                            "text": "Hello",
                            "intent": "greet",
                            "entities": []
                          },
                          {
                            "text": "goodbye",
                            "intent": "goodbye",
                            "entities": []
                          },
                          {
                            "text": "What's the weather in Berlin at the moment?",
                            "intent": "inform",
                            "entities": [
                              {
                                "start": 22,
                                "end": 28,
                                "value": "Berlin",
                                "entity": "location"
                              }
                            ]
                          }
                      }
                    }


    For "stories.md" creation, initially create the nlu in "stories.md" format as below
    
                  ##story_no
                  * intent_1
                      - action_A
                  * intent_2
                      - action_B
                      - action_C
                  * intent_3
                      - action_D

                  <---Sample Example--->
                    ## story_001
                    * greet
                       - utter_greet
                    * inform
                       - utter_ask_location
                    * inform{"location": "London"}
                       - slot{"location": "London"}
                       - action_weather
                    * goodbye
                       - utter_goodbye
                       - action_restart
                    ## story_002
                    * greet
                       - utter_greet
                    * inform{"location": "Paris"}
                       - slot{"location": "Paris"}
                       - action_weather
                    * goodbye
                       - utter_goodbye
                       - action_restart

4. Train the nlu model and dialogue managenment model via trainer.py

5. After successful training, start the action server using the command ' python -m rasa_sdk.endpoint --actions actions ' in a seperate terminal.

6. Then run the weather bot, using the command ' python botchat.py ' 
 `Bot loaded. Type a message and press enter (use '/stop' to exit): `
`Your input ->  Hi   `                                                                                                                                                                                        
`Hello! How can I help?`
`Your input ->  Whats the weather?`                                                                                                                                                                           
`In what location?`
`Your input ->  In Chennai  `                                                                                                                                                                                 
`It is currently Partly cloudy in Chennai at the moment. The temperature is 38.0 degrees, the humidity is 45% and the wind speed is 11.9 mph.`
`Your input ->  bye    `                                                                                                                                                                                      
`Bye bye :(`
`Your input -> `
