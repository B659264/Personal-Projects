import random

# Word lists for different difficulty levels
easy_words = ["apple", "house", "chair", "table", "light", "water", "bread", "green", "brown", "music", "happy", "smile", "phone", "plant", "cloud", "shoe", "train", "river", "pizza", "sunny", "tiger", "mouse", "lemon", "grape", "stone", "paper", "pencil", "sleep", "beach", "grass", "heart", "party", "candy", "socks", "earth", "voice", "story", "smoke", "drink", "sugar", "dance", "money", "rainy", "horse", "zebra", "plate", "clock", "couch", "spoon", "fork", "knife", "shirt", "pants", "dress", "boots", "truck", "cabin", "field", "ocean", "berry", "panda", "koala", "eagle", "flame", "storm", "robot", "magic", "queen", "king", "honey", "bunny", "crown", "metal", "juice", "towel", "blanket", "puppy", "kitten", "pillow", "window", "summer", "winter", "autumn", "spring", "sand", "shell", "pearl", "maple", "cider", "cookie", "cactus", "motor", "pasta", "salad", "toast", "brush", "cable"]
medium_words = ["lantern", "orchard", "vortex", "harvest", "crimson", "miracle", "gallery", "fortune", "island", "voyage", "prairie", "crevice", "thicket", "bracket", "paradox", "venture", "mariner", "harmony", "tribute", "chalice", "compass", "emerald", "willow", "spiral", "sluice", "granite", "meadow", "canvas", "belfry", "quarry", "anthem", "portal", "cobalt", "copper", "silent", "symbol", "radius", "velvet", "plasma", "orphan", "glisten", "canyon", "spigot", "quiver", "shadow", "mantle", "rivet", "ingenious", "loyalty", "cascade", "charter", "frigid", "serene", "timber", "ramble", "strand", "scribe", "harbor", "chisel", "thread", "reckon", "bounty", "module", "purple", "ginger", "margin", "buffer", "prism", "marble", "faction", "socket", "aviary", "brazen", "fickle", "plunge", "nectar", "league", "timely", "banner", "carver", "cinder", "velcro", "summit", "quartz", "hollow", "frosty", "sprawl", "bishop", "voyager", "trifle", "beside", "tundra", "vermin", "throne", "lumber", "cipher", "mantis"]
hard_words = ["ephemeral", "conundrum", "labyrinth", "juxtapose", "quarantine", "zephyr", "quixotic", "xylophone", "parliament", "diaphanous", "chrysalis", "paradoxical", "juxtaposition", "mnemonic", "syzygy", "quagmire", "myriad", "zenith", "echelon", "ossuary", "quasar", "sanctuary", "threnody", "calamity", "bravado", "temerity", "insolent", "avarice", "anachronism", "coniferous", "pandemonium", "effervescent", "iridescent", "lugubrious", "magnanimous", "rhapsodic", "perspicuous", "carnivorous", "gregarious", "equanimity", "fastidious", "vicissitude", "audacious", "fortitude", "meticulous", "serendipity", "capricious", "stratagem", "voracious", "tenacious", "enigmatic", "salient", "clandestine", "belligerent", "precocious", "propitious", "tumultuous", "inexorable", "intrepid", "pernicious", "obfuscate", "obstinate", "mercurial", "atavistic", "indelible", "diatribe", "cognitive", "seditious", "inundate", "palimpsest", "apocryphal", "peripatetic", "acerbic", "deference", "behemoth", "baneful", "sycophant", "ineffable", "malediction", "recondite", "abstruse", "aegis", "heuristic", "zeitgeist", "quintessence", "maelstrom", "superfluous", "transient", "immutable", "ascetic", "exemplar", "parsimony", "umbrage", "idiosyncrasy", "susurrus", "proclivity", "antithesis", "raconteur", "magniloquent"]

game_run = True
wins = 0
losses = 0

def select_difficulty():
    while True:
        difficulty = input("\nWhat difficulty do you choose? easy, medium, or hard? ").lower()
        if difficulty in ["easy", "e"]:
            return easy_words
        elif difficulty in ["medium", "m"]:
            return medium_words
        elif difficulty in ["hard", "h"]:
            return hard_words
        else:
            print("That's not a valid difficulty!")

def give_hint(random_item, display, guessed_letters):
    hidden_indices = [i for i, letter in enumerate(display) if letter == "_"]
    if hidden_indices:
        chosen_index = random.choice(hidden_indices)
        revealed_letter = random_item[chosen_index]
        for position, letter in enumerate(random_item):
            if letter == revealed_letter:
                display[position] = letter
        if revealed_letter not in guessed_letters:
            guessed_letters.append(revealed_letter)
        print(f"\n💡 Hint: The letter '{revealed_letter}' has been revealed!")
    return display

# Main game loop
while game_run:
    print("\033[1mRemember, type 'hint' if you ever need help!\033[0m")
    hangman_words = select_difficulty()
    random_item = random.choice(hangman_words)
    
    display = ["_"] * len(random_item)
    print("\nThe word is", len(random_item), "letters long.")
    print(' '.join(display))
    
    guessed_letters = []
    strike = 0
    
    # Game loop for guessing
    while strike < 7 and "_" in display:
        guess = input("Guess a letter or the full word: ").lower()
        
        if guess == "hint":
            give_hint(random_item, display, guessed_letters)
        elif len(guess) == len(random_item) and guess.isalpha():
            if guess == random_item:
                print("\nWow! You guessed the right word!")
                display = list(random_item)
                break
            else:
                print("Sorry, that is not the right word.")
                strike += 1
                print("\033[1mStrike", strike,"/ 7\033[0m")
        elif len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("\nYou've already guessed that letter. Try again!")
            elif guess in random_item:
                print("Good guess!", guess, "is in the word.")
                for position, letter in enumerate(random_item):
                    if letter == guess:
                        display[position] = letter
                guessed_letters.append(guess)
            else:
                print("Sorry,", guess, "is not in the word.")
                strike += 1
                guessed_letters.append(guess)
                print("\033[1mStrike", strike,"/ 7\033[0m")
        else:
            print("\nPlease guess a valid single letter or a word of the correct length.")
            
        print("\n" + ' '.join(display))
        
   # gives a game over depending on whether the player lost or won
    if "_" not in display:
        print("\nCongratulations! You guessed the word:", random_item)
        wins += 1
    else:
        print("\nYou lost! The word was:", random_item)
        losses += 1
        
    print("\nYou won", wins, "times, and lost", losses, "times.\n")
    
    # asks if the user wants to play again at the end of a game
    while True:
        keep_running = input("Do you want to continue playing? Y/N: ").lower()
        if keep_running in ["n", "no"]:
            game_run = False
            break
        elif keep_running in ["y", "yes"]:
            break
        else:
            print("Invalid answer.. Please type Y or N.")