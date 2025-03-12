import os
import keyring
from mistralai import Mistral
import openai
from polanki.enums import Level
from polanki.llm_prompts import sentence_gen_v1, sentence_validation_v1

def generate_example_sentence(level: Level, 
                              phrase: str,
                              model: str = "mistral-large-latest",
                              prompt: str = sentence_gen_v1 ) -> str:

    client = Mistral(api_key=keyring.get_password("polanki", "mistral"))

    chat_response = client.chat.complete(
        model=model,
        messages = [
            {
                "role": "system",
                "content": prompt,
        },
        {
            "role": "user",
            "content": f"My level is {level.value}",
        },
        {
            "role": "user",
            "content": phrase,
        }
    ], 
    temperature=0.2,
    )
    return chat_response.choices[0].message.content


def validate_polish_sentence(sentence: str,
                            model: str = "gpt-4o-mini",
                            prompt: str = sentence_validation_v1 ) -> str:
    """
    
    """

    client = openai.Client(api_key=keyring.get_password("polanki", "openai"))

    chat_response = client.chat.completions.create(
        model=model,
        response_format={"type": "json_object"},
        messages = [
            {
                "role": "system",
                "content": prompt,
        },
        {
            "role": "user",
            "content": sentence,
        }
    ], 
    temperature=0,
    )
    return chat_response

