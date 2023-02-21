from flask import Flask, request
from rattrapage_adrien_lafosse import generate_text, save_poem
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('api/adrien.sqlite')
c = conn.cursor()

def create_haiku():
    data = request.json
    prompt = "haikus sur les {}".format(data['keyword'])
    poem = generate_text(prompt)
    save_poem(poem)
    return "Haiku créé avec succès!", 201

print("Voulez-vous voir la liste des haikus ?")
reponse = input("Entrez 'oui' ou 'non' : ")

if reponse.lower() == "oui":
    c.execute('SELECT * FROM poems')
    data = c.fetchall()
    for row in data:
        print(row)
else:
    print("D'accord, vous ne voulez pas voir la liste des fichiers.")

print("Voulez-vous voir un haiku particulier")
reponse2 = input("Entrez 'oui' ou 'non' : ")
nombre = int(input("Entrez un nombre : "))

if reponse2.lower() == "oui":
    c.execute('SELECT poem FROM poems where id = ?', (nombre,))
    data = c.fetchall()
    for row in data:
        print(row)

    print("Voulez-vous le supprimer")
    reponse3 = input("Entrez 'oui' ou 'non' : ")

    if reponse3.lower() == "oui":
        c.execute('DELETE FROM poems WHERE id = ?', (nombre,))  
        conn.commit()
        print(f"Le poème avec l'ID {nombre} a été supprimé.")

    else:
        print("D'accord, vous ne voulez pas supprimer le poeme")  
else:
    print("D'accord, vous ne voulez pas afficher un haiku particulier")