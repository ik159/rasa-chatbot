# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

import json
from pathlib import Path
from typing import Any, Text, Dict, List ,Optional


from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher ,Action
from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase
from rasa_sdk import Tracker
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.events import AllSlotsReset, SlotSet
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.types import DomainDict

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


<<<<<<< HEAD



# show projects
class ValidateRegisterForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_appointment_form"
    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        return []

    def validate_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate slot value."""
        required_slots = ["name" , "appointment_date" , "description"]
        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                return [SlotSet("requested_slot" , slot_name)]
 
        return [SlotSet("requested_slot" , None)]
       # if not slot_value:
       #  return {"name": None}
       # else: 
        # return {"name": slot_value}	
class ActionSubmitProject(Action):
    def name(self) -> Text:
        return "actions_submit_appoint"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
	
        user_name = tracker.get_slot("name")
        appointment_date = tracker.get_slot("appointment_date")
        description = tracker.get_slot("description")
        print("name  is  : ",user_name) 
        print("date is  is  : ",appointment_date) 
        
		
        dispatcher.utter_message(template="utter_details_thanks")
        return[]

# This is a simple example for a custom action which utters "Hello World!"


# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_check_order_existence"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         print("sdfsgd")
#         dispatcher.utter_message(text="Hello World!sdretsrdytfg")

#         return []
=======
>>>>>>> f79ed5d20ec08d062f5f8acf963ccd0d14c6828a
