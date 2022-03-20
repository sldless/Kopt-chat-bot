import requests, html
score = 0
while True:
    r = requests.get('https://opentdb.com/api.php?amount=1&difficulty=medium&type=boolean')
    data = r.json()
    data = data['results'][0]
    print(html.unescape(data['question']))
    answer = input('True or False: ')
    if answer.lower() == data['correct_answer'].lower():
        score += 1
        print('Correct!')
    else:
        if score != 0:
            score -= 1 
        print('Incorrect!')
    print('Score:', score)
