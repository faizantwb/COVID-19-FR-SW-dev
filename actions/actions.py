# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction
from typing import Dict, Text, Any, List, Union

import json
import requests

class FirstTimeFormFR(FormAction):

    def name(self) -> Text:
        return "form_first_time_fr"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:

        if tracker.get_slot("first_time_fr") == True:
            return["first_time_fr","given_name_fr","location_fr"]
        else:
            return["first_time_fr"]

    def slot_mappings(self) -> Text:
        return {
        "first_time_fr": [
            self.from_intent(intent="affirm_fr", value=True),
            self.from_intent(intent="deny_fr", value=False)
            ],
        "given_name_fr": self.from_text(),
        "location_fr": self.from_text()
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        if tracker.get_slot("first_time_fr") == False:
            dispatcher.utter_message(template="utter_welcome_back_fr")
        else:
#            dispatcher.utter_message(template="utter_greet")
            dispatcher.utter_message(template="utter_greet_with_name_fr")
        return[]

class FirstTimeFormSW(FormAction):

    def name(self) -> Text:
        return "form_first_time_sw"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:

        if tracker.get_slot("first_time_sw") == True:
            return["first_time_sw","given_name_sw","location_sw"]
        else:
            return["first_time_sw"]

    def slot_mappings(self) -> Text:
        return {
        "first_time_sw": [
            self.from_intent(intent="affirm_sw", value=True),
            self.from_intent(intent="deny_sw", value=False)
            ],
        "given_name_sw": self.from_text(),
        "location_sw": self.from_text()
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        if tracker.get_slot("first_time_sw") == False:
            dispatcher.utter_message(template="utter_welcome_back_sw")
        else:
#            dispatcher.utter_message(template="utter_greet")
            dispatcher.utter_message(template="utter_greet_with_name_sw")
        return[]

class FeedbackFormFR(FormAction):

    def name(self) -> Text:
        return "form_feedback_fr"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:

        # if the answer to "Did we do OK?" is no...
        if tracker.get_slot("feedback_fr") == False:
            return["feedback_fr", "feedback_reason_fr"]
        else:
            return["feedback_fr"]

    def slot_mappings(self) -> Text:
        return {
        "feedback_fr": [
            self.from_intent(intent="affirm_fr", value=True),
            self.from_intent(intent="deny_fr", value=False)
            ],
        "feedback_reason_fr": self.from_text()
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_message(template="utter_thanks_for_your_feedback_fr")
        return[]

class FeedbackFormSW(FormAction):

    def name(self) -> Text:
        return "form_feedback_sw"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:

        # if the answer to "Did we do OK?" is no...
        if tracker.get_slot("feedback_sw") == False:
            return["feedback_sw", "feedback_reason_sw"]
        else:
            return["feedback_sw"]

    def slot_mappings(self) -> Text:
        return {
        "feedback_sw": [
            self.from_intent(intent="affirm_sw", value=True),
            self.from_intent(intent="deny_sw", value=False)
            ],
        "feedback_reason_sw": self.from_text()
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_message(template="utter_thanks_for_your_feedback_sw")
        return[]

class LanguageQuestionsFormFR(FormAction):

    def name(self) -> Text:
        return "form_language_questions_fr"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:

        return["language_at_home_fr"]

    def slot_mappings(self) -> Text:
        return {
        "language_at_home_fr": self.from_text()
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_message(template="utter_get_back_on_topic_fr")
        return[]

class LanguageQuestionsFormSW(FormAction):

    def name(self) -> Text:
        return "form_language_questions_sw"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:

        return["language_at_home_sw"]

    def slot_mappings(self) -> Text:
        return {
        "language_at_home_sw": self.from_text()
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_message(template="utter_get_back_on_topic_sw")
        return[]


class MythSourceFormFR(FormAction):

    def name(self) -> Text:
        return "form_myth_source_fr"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:

        return["myth_source_fr"]

    def slot_mappings(self) -> Text:
        return {
        "myth_source_fr": self.from_text()
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_message(template="utter_thanks_for_your_feedback_fr")
        return[]

class MythSourceFormSW(FormAction):

    def name(self) -> Text:
        return "form_myth_source_sw"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:

        return["myth_source_sw"]

    def slot_mappings(self) -> Text:
        return {
        "myth_source_sw": self.from_text()
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_message(template="utter_thanks_for_your_feedback_sw")
        return[]

class ActionGetInfectionStatsFR(Action):

    def name(self) -> Text:
        return "action_get_infection_stats_fr"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # this is where to paste the call to API
        country = "DRC"
        url = "https://covid-193.p.rapidapi.com/statistics"
        headers = { 'x-rapidapi-host': "covid-193.p.rapidapi.com", 'x-rapidapi-key': "c41cd0c62dmshb99d2fb0a63207dp1775a0jsna4f33aea1040"}
        query_string = {"country":country}

        # get the response
        response = requests.request("GET", url, headers=headers, params=query_string)
        response_JSON = response.json()

        #get the bits of the response we want
        active = response_JSON['response'][0]['cases']['active']
        new = response_JSON['response'][0]['cases']['new']
        new_deaths = response_JSON['response'][0]['deaths']['new']
        total_deaths = response_JSON['response'][0]['deaths']['total']

        dispatcher.utter_message(template="utter_get_infection_stats_fr",
                                 active = active,
                                 new = new,
                                 country = country,
                                 new_deaths = new_deaths,
                                 total_deaths = total_deaths
                                 )

        return []

class ActionGetInfectionStatsSW(Action):

    def name(self) -> Text:
        return "action_get_infection_stats_sw"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # this is where to paste the call to API
        country = "DRC"
        url = "https://covid-193.p.rapidapi.com/statistics"
        headers = { 'x-rapidapi-host': "covid-193.p.rapidapi.com", 'x-rapidapi-key': "c41cd0c62dmshb99d2fb0a63207dp1775a0jsna4f33aea1040"}
        query_string = {"country":country}

        # get the response
        response = requests.request("GET", url, headers=headers, params=query_string)
        response_JSON = response.json()

        #get the bits of the response we want
        active = response_JSON['response'][0]['cases']['active']
        new = response_JSON['response'][0]['cases']['new']
        new_deaths = response_JSON['response'][0]['deaths']['new']
        total_deaths = response_JSON['response'][0]['deaths']['total']

        dispatcher.utter_message(template="utter_get_infection_stats_sw",
                                 active = active,
                                 new = new,
                                 country = country,
                                 new_deaths = new_deaths,
                                 total_deaths = total_deaths
                                 )
#        dispatcher.utter_message(text=f'There are {active} people infected in {country}, a change of {new} on yesterday.')

        return []

class ActionGetPandemicVideo(Action):

    def name(self) -> Text:
        return "action_link_to_pandemic_video"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        country = "DRC"

        # dispatcher.utter_message(attachment={
        #     "type": "video",
        #     "payload": {
        #         "title": "Watch Below Video",
        #         "src": "https://www.youtube.com/watch?v=nMelwUuGqpA"
        #     }
        # })

        return []
