#Textpro Coding challenge
while True:
    prompt = input('Say something: ')

    message = f"{prompt}. {prompt}? {prompt}!"
    if prompt == '\end':
        print(message)
        break
    else:
        continue