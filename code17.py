from dummyvocab import dummyData
# res = []
# for obj in dummyData:
#     word = obj['word']
#     meaning = obj['wordmeaning'][0]['meaning']
#     res.append(
#         {
#             "word":word,
#             "meaning":meaning
#         }
#     )
# print(res)
d=[{'word': 'Starving ', 'meaning': 'Too much hungry '}, {'word': 'Heroic ', 'meaning': 'Brave '}, {'word': 'Vanderlized ', 'meaning': 'Damage something '}, {'word': 'Tie a knot ', 'meaning': 'Getting married '}, {'word': 'Immaculate ', 'meaning': 'Spotless '}, {'word': 'Despise ', 'meaning': 'Hate'}, {'word': 'Leverage ', 'meaning': 'Ability to influence people'}, {'word': 'Deceive ', 'meaning': 'Betrey someone '}, {'word': 'Denounce ', 'meaning': 'Blame'}, {'word': 'Yeild ', 'meaning': 'To produce '}, {'word': 'Flick', 'meaning': 'A movie '}, {'word': 'Sue', 'meaning': 'Request '}, {'word': 'Rely', 'meaning': 'Having faith on someone '}, {'word': 'Yelling', 'meaning': 'Being angry '}, {'word': 'Imperceptible ', 'meaning': 'Unnoticeable '}]

import requests

url = "http://127.0.0.1:8000/addvocab"

payload = {
    "word": "endurance",
    "meaning": "Ability to continue"
}
# for payload in d:
response = requests.request("POST", url, json=payload)

print(response.text)