import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json.json"))

def search(word) -> str:
        """
        search( ) -> a function to return the definition of a word.\n
        Args:
            word -> Word inputted to get definition
        """
        word = word.lower()
        if word in data:
            return data[word]
        elif word.title() in data:
            return data[word.title()]
        elif word.upper() in data:
            return data[word.upper()]
        elif len(get_close_matches(word, data.keys(), cutoff = 0.8)) > 0:
            close_match = get_close_matches(word, data.keys(), cutoff = 0.8)[0]
            # print("Did you mean %s instead" %  (get_close_matches(word, data.keys(), cutoff = 0.8))[0])
            print(f"Did you mean {close_match} instead?")
            try:
                alt = int(input("\n1. Yes\n2. NO\n-> "))
                if alt == 1:
                    return data[close_match]
                elif alt == 2:
                    return f"{word} could not be found. Please doublecheck it."
                else:
                    return "Invalid entry"
            except ValueError:
                return "Error! enter either 1 or 2."
        else:
           return f"Oops! could not find '{word}'"
            

search_word = (input("Enter word to search: "))

output = search(search_word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)