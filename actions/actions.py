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

class FirstTimeFormFRA(FormAction):

    def name(self) -> Text:
        return "form_first_time_fra"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:

        if tracker.get_slot("first_time_fra") == True:
            return["first_time_fra","given_name_fra","location_fra"]
        else:
            return["first_time_fra"]

    def slot_mappings(self) -> Text:
        return {
        "first_time_fra": [
            self.from_intent(intent="affirm_fra", value=True),
            self.from_intent(intent="deny_fra", value=False)
            ],
        "given_name_fra": self.from_text(),
        "location_fra": self.from_text()
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        if tracker.get_slot("first_time_fra") == False:
            dispatcher.utter_message(template="utter_welcome_back_fra")
        else:
#            dispatcher.utter_message(template="utter_greet")
            dispatcher.utter_message(template="utter_greet_with_name_fra")
        return[]

class FirstTimeFormSWC(FormAction):

    def name(self) -> Text:
        return "form_first_time_swc"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:

        if tracker.get_slot("first_time_swc") == True:
            return["first_time_swc","given_name_swc","location_swc"]
        else:
            return["first_time_swc"]

    def slot_mappings(self) -> Text:
        return {
        "first_time_swc": [
            self.from_intent(intent="affirm_swc", value=True),
            self.from_intent(intent="deny_swc", value=False)
            ],
        "given_name_swc": self.from_text(),
        "location_swc": self.from_text()
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        if tracker.get_slot("first_time_swc") == False:
            dispatcher.utter_message(template="utter_welcome_back_swc")
        else:
#            dispatcher.utter_message(template="utter_greet")
            dispatcher.utter_message(template="utter_greet_with_name_swc")
        return[]

class FirstTimeFormLIN(FormAction):

    def name(self) -> Text:
        return "form_first_time_lin"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:

        if tracker.get_slot("first_time_lin") == True:
            return["first_time_lin","given_name_lin","location_lin"]
        else:
            return["first_time_lin"]

    def slot_mappings(self) -> Text:
        return {
        "first_time_lin": [
            self.from_intent(intent="affirm_lin", value=True),
            self.from_intent(intent="deny_lin", value=False)
            ],
        "given_name_lin": self.from_text(),
        "location_lin": self.from_text()
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        if tracker.get_slot("first_time_lin") == False:
            dispatcher.utter_message(template="utter_welcome_back_lin")
        else:
#            dispatcher.utter_message(template="utter_greet")
            dispatcher.utter_message(template="utter_greet_with_name_lin")
        return[]


class FeedbackFormFRA(FormAction):

    def name(self) -> Text:
        return "form_feedback_fra"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:

        # if the answer to "Did we do OK?" is no...
        if tracker.get_slot("feedback_fra") == False:
            return["feedback_fr", "feedback_reason_fr"]
        else:
            return["feedback_fra"]

    def slot_mappings(self) -> Text:
        return {
        "feedback_fra": [
            self.from_intent(intent="affirm_fra", value=True),
            self.from_intent(intent="deny_fra", value=False)
            ],
        "feedback_reason_fra": self.from_text()
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_message(template="utter_thanks_for_your_feedback_fra")
        return[]

class FeedbackFormSWC(FormAction):

    def name(self) -> Text:
        return "form_feedback_swc"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:

        # if the answer to "Did we do OK?" is no...
        if tracker.get_slot("feedback_swc") == False:
            return["feedback_swc", "feedback_reason_swc"]
        else:
            return["feedback_swc"]

    def slot_mappings(self) -> Text:
        return {
        "feedback_swc": [
            self.from_intent(intent="affirm_swc", value=True),
            self.from_intent(intent="deny_swc", value=False)
            ],
        "feedback_reason_swc": self.from_text()
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_message(template="utter_thanks_for_your_feedback_swc")
        return[]

class FeedbackFormLIN(FormAction):

    def name(self) -> Text:
        return "form_feedback_lin"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:

        # if the answer to "Did we do OK?" is no...
        if tracker.get_slot("feedback_lin") == False:
            return["feedback_lin", "feedback_reason_ln"]
        else:
            return["feedback_lin"]

    def slot_mappings(self) -> Text:
        return {
        "feedback_lin": [
            self.from_intent(intent="affirm_lin", value=True),
            self.from_intent(intent="deny_lin", value=False)
            ],
        "feedback_reason_lin": self.from_text()
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_message(template="utter_thanks_for_your_feedback_lin")
        return[]


class LanguageQuestionsFormFRA(FormAction):

    def name(self) -> Text:
        return "form_language_questions_fra"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:

        return["language_at_home_fra"]

    def slot_mappings(self) -> Text:
        return {
        "language_at_home_fra": self.from_text()
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_message(template="utter_get_back_on_topic_fra")
        return[]

class LanguageQuestionsFormSWC(FormAction):

    def name(self) -> Text:
        return "form_language_questions_swc"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:

        return["language_at_home_swc"]

    def slot_mappings(self) -> Text:
        return {
        "language_at_home_swc": self.from_text()
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_message(template="utter_get_back_on_topic_swc")
        return[]

class LanguageQuestionsFormLIN(FormAction):

    def name(self) -> Text:
        return "form_language_questions_lin"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:

        return["language_at_home_lin"]

    def slot_mappings(self) -> Text:
        return {
        "language_at_home_lin": self.from_text()
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_message(template="utter_get_back_on_topic_lin")
        return[]

class MythSourceFormFRA(FormAction):

    def name(self) -> Text:
        return "form_myth_source_fra"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:

        return["myth_source_fra"]

    def slot_mappings(self) -> Text:
        return {
        "myth_source_fra": self.from_text()
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_message(template="utter_thanks_for_your_feedback_fra")
        return[]

class MythSourceFormSWC(FormAction):

    def name(self) -> Text:
        return "form_myth_source_swc"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:

        return["myth_source_swc"]

    def slot_mappings(self) -> Text:
        return {
        "myth_source_swc": self.from_text()
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_message(template="utter_thanks_for_your_feedback_swc")
        return[]

class MythSourceFormLIN(FormAction):

    def name(self) -> Text:
        return "form_myth_source_lin"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:

        return["myth_source_lin"]

    def slot_mappings(self) -> Text:
        return {
        "myth_source_lin": self.from_text()
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_message(template="utter_thanks_for_your_feedback_lin")
        return[]


class ActionGetInfectionStatsFRA(Action):

    def name(self) -> Text:
        return "action_get_infection_stats_fra"

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

        if not new_deaths:
            new_deaths = 0
        if not new:
            new = 0

        dispatcher.utter_message(template="utter_get_infection_stats_fra",
                                 active = active,
                                 new = new,
                                 country = country,
                                 new_deaths = new_deaths,
                                 total_deaths = total_deaths
                                 )

        return []

class ActionGetInfectionStatsSWC(Action):

    def name(self) -> Text:
        return "action_get_infection_stats_swc"

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

        if not new_deaths:
            new_deaths = 0
        if not new:
            new = 0

        dispatcher.utter_message(template="utter_get_infection_stats_swc",
                                 active = active,
                                 new = new,
                                 country = country,
                                 new_deaths = new_deaths,
                                 total_deaths = total_deaths
                                 )
#        dispatcher.utter_message(text=f'There are {active} people infected in {country}, a change of {new} on yesterday.')

        return []

class ActionGetInfectionStatsLIN(Action):

    def name(self) -> Text:
        return "action_get_infection_stats_lin"

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

        if not new_deaths:
            new_deaths = 0
        if not new:
            new = 0

        dispatcher.utter_message(template="utter_get_infection_stats_lin",
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
