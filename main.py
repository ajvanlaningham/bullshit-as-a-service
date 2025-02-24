import random

def load_words(file_path):
    """Loads words or phrases from a file into a unique set to prevent duplicates."""
    try:
        with open(file_path, "r") as file:
            words = list(set(line.strip() for line in file.readlines() if line.strip()))  
            random.shuffle(words) 
            return words
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return []

def get_unique_word(word_list, used_words):
    """Gets a unique word from the list, ensuring it's not used yet. Resets if empty."""
    if not word_list:
        return "synergy"  # Fallback 

    available_words = set(word_list) - used_words  

    if not available_words:  
        used_words.clear()
        available_words = set(word_list)

    chosen_word = random.choice(list(available_words))
    used_words.add(chosen_word)
    return chosen_word

def generate_buzzphrase(nouns, verbs, adjectives, structures, used_words):
    """Generates a structured corporate-speak phrase using unique words."""
    if not structures:
        return "We need to leverage our scalable solutions to drive synergy."  # Fallback sentence
    
    structure = random.choice(structures)  # Pick a random sentence structure

    # Pick words uniquely using sets
    noun1 = get_unique_word(nouns, used_words["nouns"])
    noun2 = get_unique_word(nouns, used_words["nouns"])
    verb1 = get_unique_word(verbs, used_words["verbs"])
    verb2 = get_unique_word(verbs, used_words["verbs"])
    adjective1 = get_unique_word(adjectives, used_words["adjectives"])

    # Replace placeholders correctly
    return structure.format(
        noun1=noun1,
        noun2=noun2,
        verb1=verb1,
        verb2=verb2,
        adjective=adjective1
    )

def generate_speech():
    """Generates a full corporate speech."""
    nouns = load_words("data/buzzwords/nouns.txt")
    verbs = load_words("data/buzzwords/verbs.txt")
    adjectives = load_words("data/buzzwords/adjectives.txt")
    platitudes = load_words("data/buzzwords/platitudes.txt")
    structures = load_words("data/buzzwords/structures/sentence_structures.txt")

    if not (nouns and verbs and adjectives and platitudes and structures):
        print("Error: Missing data files. Please check your data folder.")
        return

    # Track used words to ensure uniqueness
    used_words = {"nouns": set(), "verbs": set(), "adjectives": set()}

    print("\n🔹 CEO-Inspired Speech 🔹\n")
    
    for _ in range(3):
        print(f"- {generate_buzzphrase(nouns, verbs, adjectives, structures, used_words)}")

    print(f"\n🚀 {random.choice(platitudes)} 🚀\n")

if __name__ == "__main__":
    generate_speech()