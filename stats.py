#stats.py

def get_num_words(text):
    return len(text.split())

def get_num_characters(text):
    lowered_text = text.lower()
    text_counter = {
        'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0,
        'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0,
        'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0,
        'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0
    }
    for char in lowered_text:
        if char in text_counter:
            text_counter[char] += 1
    return text_counter

def sort_characters(dictionary):
    dictionary_list = []
    
    # Step 1: Loop through each character in the dictionary
    for char in dictionary:
        # Step 2: Create a new dictionary for this character
        new_dict = {"char": char, "num": dictionary[char]}
        # Step 3: Add it to the list
        dictionary_list.append(new_dict)
    
    # Step 4: Sort the list (you'll need a helper function here)
    dictionary_list.sort(reverse=True, key=sort_on)
    
    return dictionary_list
    
def sort_on(item):
    return item["num"]