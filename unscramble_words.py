import nltk
from nltk.corpus import wordnet

def unscramble_word(word):
    # Get a set of valid English words from the NLTK corpus
    permutations = set(nltk.corpus.words.words())
    
    # Find words in the permutations set that have the same letters as the given word
    unscrambled_words = [w for w in permutations if sorted(w) == sorted(word)]
    
    return unscrambled_words

def get_word_meaning(word):
    synsets = wordnet.synsets(word)
    if synsets:
        # Get the definitions of all synsets for the word
        meanings = [syn.definition() for syn in synsets]
        return meanings
    return ["Meaning not found."]

def main():
    try:
        while True:
            # Prompt the user to input multiple jumbled words separated by commas
            user_input = input("\nEnter single or comma-separated jumbled words (or type 'q' to quit): ").lower()
            
            if user_input == "q":
                print("Program terminated.")
                break
            
            # Split the user input into individual words
            jumbled_words = user_input.split(",")
            
            for jumbled_word in jumbled_words:
                jumbled_word = jumbled_word.strip()  # Remove any extra spaces
                unscrambled_words = unscramble_word(jumbled_word)
                
                if unscrambled_words:
                    print("\nPossible unscrambled words for", jumbled_word + ":")
                    for i, unscrambled_word in enumerate(unscrambled_words, start=1):
                        meanings = get_word_meaning(unscrambled_word)
                        print(f"{i}. Unscrambled word: {unscrambled_word}")
                        for j, meaning in enumerate(meanings, start=1):
                            print(f"   {j}. Meaning: {meaning}")
                else:
                    print("No valid unscrambled word found for", jumbled_word)
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
