# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

# import json
# from pathlib import Path
# from typing import Any, Text, Dict, List


# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
# from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase


# class ActionCheckExistence(Action):
#     knowledge = Path("data/orderIDs.txt").read_text().split("\n")

#     def name(self) -> Text:
#         return "action_check_order_existence"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         print("jehrghe")
#         for blob in tracker.latest_message['entities']:
#             print(tracker.latest_message)
#             if blob['entity'] == 'orderIDs':
#                 name = blob['value']
#                 if name in self.knowledge:
#                     dispatcher.utter_message("exists in our db.")
#                 else:
#                     dispatcher.utter_message(
#                         text=f"Order ID : {name} doesnt exist in our db, are you sure it is correctly typed?")
#         return []


# class MyKnowledgeBaseAction(ActionQueryKnowledgeBase):
#     def __init__(self):
#         knowledge_base = InMemoryKnowledgeBase("data/orderStatusDb.json")
#         super().__init__(knowledge_base)



# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_check_order_existence"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("sdfsgd")
        dispatcher.utter_message(text="Hello World!sdretsrdytfg")

        return []
