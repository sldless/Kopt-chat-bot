import requests
while True:
    user = input('> ')
    if user == '':
        user = 'e'
    if user == 'exit':
        break
    else:
        chat = requests.get(
            f'https://api.popcat.xyz/chatbot?msg={user}')
        try:
            print(f"Kopt: {chat.json()['response']}")
        except:
            print("Kopt: ?")
            