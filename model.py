from dotenv import find_dotenv, load_dotenv
from transformers import pipeline
from langchain import PromptTemplate, LLMChain, OpenAI
import os
import requests

load_dotenv(find_dotenv())
HUGGINGFACE_API_TOKEN = os.getenv("HUGGING_FACE_API")

# imgtotext

def imagetotext(url):
    image_to_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-large")
    text = image_to_text(url)[0]["generated_text"]
    print(text)
    return text

#llm

def generate_story(scenario):

    template = """You are a story teller, based on the scenario
    you need to generate a small story which is no more than 50
    words

    Context: {scenario}
    Story:
    """

    prompt = PromptTemplate(template=template, input_variables=["scenario"])
    story_llm = LLMChain(
        llm=OpenAI(model_name="gpt-3.5-turbo", temperature=1),
        prompt=prompt,
        verbose=True
    )
    story = story_llm.predict(scenario=scenario)
    print(story)
    return story

# caption = imagetotext("sample1.jpg")
# story = generate_story(caption)

#def text2speech(message):
#     API_URL = "https://api-inference.huggingface.co/models/espnet/kan-bayashi_ljspeech_vits"
#     headers = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}
#     payloads = {
#         "inputs": message
#     }
#     response = requests.post(API_URL, headers=headers, json=payloads)
#     with open('audio.flac', 'wb') as file:
#         file.write(response.content)