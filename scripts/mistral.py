#%%
import os
import keyring
from mistralai import Mistral
from polanki.enums import Level
from polanki.llm import generate_example_sentence, validate_polish_sentence



word = "kot"

for user_level_str in Level.__members__.keys():
    print(user_level_str, "  Generating example sentence")
    user_level = Level(user_level_str)
    example_sentence = generate_example_sentence(user_level, word)
    print("------")
    print(example_sentence)
    print('------')
    print("Validating sentence")
    validation = validate_polish_sentence(example_sentence)

    print(validation.choices[0].message.content)
    print("------", 5*"\n")

# %%
