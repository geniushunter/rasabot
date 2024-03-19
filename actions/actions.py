from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionTechnologyprovided(Action):
    def name(self) -> Text:
        return "action_technology_provided"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        print(entities)
        for e in entities:
            if e['entity'] == 'tech_topic':
                name = e["value"]
                name = name.lower()

                if name in ['ml', 'machine learning']:
                    message = "Machine learning (ML) is branch of artificial intelligence (AI) that enables computers to 'self-learn' from data."
                    Link = "https://en.wikipedia.org/wiki/Machine_learning"
                    dispatcher.utter_message(text=message)
                    dispatcher.utter_template("utter_info", tracker, link=Link)
                    return []

                if name in ['ai', 'artificial intelligence']:
                    message = "Artificial intelligence (AI) is the ability of a computer or a robot controlled by a computer to do tasks."
                    Link = "https://en.wikipedia.org/wiki/Artificial_intelligence"
                    dispatcher.utter_message(text=message)
                    dispatcher.utter_template("utter_info", tracker, link=Link)
                    return []

                if name in ['dl', 'deep learning']:
                    message = "Deep learning is a method in artificial intelligence (AI) that teaches computers to process data in a way."
                    Link = "https://en.wikipedia.org/wiki/Deep_learning"
                    dispatcher.utter_message(text=message)
                    dispatcher.utter_template("utter_info", tracker, link=Link)
                    return []

        return []
