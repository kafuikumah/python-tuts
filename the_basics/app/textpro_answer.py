# We start by creating a Sentence Maker that capitalizes sentences. With this, we shall use the capitalize() method
def sentence_maker(phrase):
    interrogatives = ("how", "what", "which", "who", "why", "when", "whom", "whose")
    capitalized = phrase.capitalize()

    # Now, we want to be able to write a logic that can tell which sentence is a question or not. With this, we will assume that
    # All sentences starts with interrogative words like, "How", "What", "Which", "Who", "Why" "When" "Whom" and "Whose"
    # With the use of the startswith() method inbuilt in python, we can be able to tell what the starting word is and apply
    # A check to test if the starting word is an interrogative or not.
    

    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)
    

## A sentence with an interrogative now appends a question mark at the end and also capitalizes it.
## If the sentence does not have an interrogative, a fullstop is appended and still capitalized. Awesome


## WRITING A LOGIC TO RECEIVE THE PROMPTS
results = []
while True:
    user_input = input('Say something: ')

    if user_input == "\end":
        break
    else:
        results.append(sentence_maker(user_input))

    
print(results)

# Format the sentence properly. we do not want the sentences in a list form
print(" ".join(results))
