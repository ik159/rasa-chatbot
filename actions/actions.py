# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

import json
from pathlib import Path
from typing import Any, Text, Dict, List


from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase


class ActionCheckExistence(Action):
    knowledge = Path("data/orderIDs.txt").read_text().split("\n")

    def name(self) -> Text:
        return "action_check_order_existence"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("jehrghe")
        for blob in tracker.latest_message['entities']:
            print(tracker.latest_message)
            if blob['entity'] == 'orderIDs':
                name = blob['value']
                if name in self.knowledge:
                    f = open('data/orderStatusDb.json')
                    data = json.load(f)
                    for i in data['orders']:
                       # print(i)
                        #print(name)
                        if str(i['id']) == name :
                            entity_nameCustomer=i['name']
                            print(entity_nameCustomer)
                            entity_orderDate=i['date']
                            entity_status=i['status'] 
                            entity_deliverydate = i['deliverydate']   
                    f.close()
                    print("hellll")
                    dispatcher.utter_message(response="utter_order_details",nameCustomer=entity_nameCustomer,orderDate=entity_orderDate,status=entity_status ,deliverydate =entity_deliverydate)
                else:
                    dispatcher.utter_message(
                        text=f"Order ID : {name} doesnt exist in our db, are you sure it is correctly typed?")
        return []


class MyKnowledgeBaseAction(ActionQueryKnowledgeBase):
    def __init__(self):
        knowledge_base = InMemoryKnowledgeBase("data/orderStatusDb.json")
        super().__init__(knowledge_base)


