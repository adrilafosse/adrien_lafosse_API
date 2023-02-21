import requests
import json
import sqlite3


api_key = "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"
api_url = "https://api.openai.com/v1/engines/text-davinci-003/completions"

conn = sqlite3.connect('api/adrien.sqlite')
c = conn.cursor()

try:
    c.execute('''CREATE TABLE poems
                 (id INTEGER PRIMARY KEY, poem text)''')
except:
    pass

def generate_text(prompt):

    headers = {"Content-Type": "application/json",
               "Authorization": "Bearer " + api_key}
    data = {"prompt": prompt,
            "temperature": 0.5,
            "max_tokens": 1024,
            "n": 1}

    response = requests.post(api_url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        message = response.json()["choices"][0]["text"].strip()
    else:
        message = "Une erreur s'est produite : " + response.text

    return message

def save_poem(poem):
    c.execute("INSERT INTO poems (id,poem) VALUES (?,?)", (c.lastrowid,poem,))
    conn.commit()


chaine = input("Entrez un theme : ")
prompt = "haikus sur les {}".format(chaine)
poeme = generate_text(prompt)
print(poeme)
save_poem(poeme)

conn.close()
