import requests
import json

def emotion_detector(text_to_analyze):
    """
    Sends the provided text to the Watson NLP Emotion Detection API 
    and returns the raw string response from the server.
    """
    # Define the URL for the Watson NLP Emotion Predict service
    url = 'https://skills.network'
    
    # Set up the headers required by the Watson API
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Construct the input JSON payload
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Send the POST request to the Watson service
    response = requests.post(url, json=myobj, headers=headers)
    
    # Return the raw text response as required for Task 2
    return response.text
