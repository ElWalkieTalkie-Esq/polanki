#%%

import anki 
from anki.collection import Collection
from anki.notes import Note
from anki.decks import DeckId
from typing import List, Dict

path_to_collection = """/Users/walkietalkie/Library/Application Support/Anki2/User 1/collection.anki2"""

# Load the collection
col = Collection(path_to_collection)

# Get the notetype and deck
model = col.models.byName("Basic") 
deck_id = col.decks.id("Polish")

# %%
def search_for_duplicate(input_note: Dict[str, str], col: Collection) -> bool:
    """
    Search for a duplicate note in the Anki collection.

    Args:
        input_note (Dict[str, str]): Dictionary containing note fields (e.g., {'front': 'word', 'back': 'definition'})
        col (Collection): Anki collection object to search in

    Returns:
        bool: True if a duplicate note is found, False otherwise
    """
    for key, value in input_note.items():
        notes = col.find_notes(f'{key}:"{value}"')
        if len(notes) > 0:
            return True
    return False

# %%
test_import = [
    {'front':'tradycyjny', 'back':'traditional'},
    {'front': 'Mam na sobie', 'back': 'I am wearing (right now)'},
    {'front':'noszę', 'back':'I wear (habitually)'},
]

for input_item in test_import:
    if search_for_duplicate(input_item, col):
        print(f"Duplicate note found for {input_item}")
        continue
    note = col.new_note(model)
    note['Front'] = input_item['front']
    note['Back'] = input_item['back']   
    note.tags = ['test']
    col.add_note(note, DeckId(deck_id))
    print("Added new note")

col.close()
# %%
