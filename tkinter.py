# -*- coding: utf-8 -*-


import tkinter as tk
from tkinter import simpledialog, messagebox
import random

verbs = {
    'first': ['sind', 'haben', 'gehen', 'machen', 'kommen', 'sehen', 'finden', 'nehmen', 'sprechen', 'lesen', 'essen', 'trinken', 'fahren', 'schreiben', 'stehen', 'sitzen', 'liegen', 'laufen', 'arbeiten', 'spielen', 'lernen', 'fühlen', 'kennen', 'denken', 'sagen'],
    'ich': ['bin', 'habe', 'gehe', 'mache', 'komme', 'sehe', 'finde', 'nehme', 'spreche', 'lese', 'esse', 'trinke', 'fahre', 'schreibe', 'stehe', 'sitze', 'liege', 'laufe', 'arbeite', 'spiele', 'lerne', 'fühle', 'kenne', 'denke', 'sage'],
    'du': ['bist', 'hast', 'gehst', 'machst', 'kommst', 'siehst', 'findest', 'nimmst', 'sprichst', 'liest', 'isst', 'trinkst', 'fährst', 'schreibst', 'stehst', 'sitzt', 'liegst', 'läufst', 'arbeitest', 'spielst', 'lernst', 'fühlst', 'kennst', 'denkst', 'sagst'],
    'er/sie/es': ['ist', 'hat', 'geht', 'macht', 'kommt', 'sieht', 'findet', 'nimmt', 'spricht', 'liest', 'isst', 'trinkt', 'fährt', 'schreibt', 'steht', 'sitzt', 'liegt', 'läuft', 'arbeitet', 'spielt', 'lernt', 'fühlt', 'kennt', 'denkt', 'sagt'],
    'wir': ['sind', 'haben', 'gehen', 'machen', 'kommen', 'sehen', 'finden', 'nehmen', 'sprechen', 'lesen', 'essen', 'trinken', 'fahren', 'schreiben', 'stehen', 'sitzen', 'liegen', 'laufen', 'arbeiten', 'spielen', 'lernen', 'fühlen', 'kennen', 'denken', 'sagen'],
    'ihr': ['seid', 'habt', 'geht', 'macht', 'kommt', 'seht', 'findet', 'nehmt', 'sprecht', 'lest', 'esst', 'trinkt', 'fahrt', 'schreibt', 'steht', 'sitzt', 'liegt', 'lauft', 'arbeitet', 'spielt', 'lernt', 'fühlt', 'kennt', 'denkt', 'sagt'],
    'sie/Sie': ['sind', 'haben', 'gehen', 'machen', 'kommen', 'sehen', 'finden', 'nehmen', 'sprechen', 'lesen', 'essen', 'trinken', 'fahren', 'schreiben', 'stehen', 'sitzen', 'liegen', 'laufen', 'arbeiten', 'spielen', 'lernen', 'fühlen', 'kennen', 'denken', 'sagen']
}

words_data = {
    'der': {
        'Teppich': {'turkish_meaning': 'halı'},
        'Wein': {'turkish_meaning': 'şarap'},
        'Hund': {'turkish_meaning': 'köpek'},
        'Tisch': {'turkish_meaning': 'masa'},
        'Stuhl': {'turkish_meaning': 'sandalye'},
        'Mann': {'turkish_meaning': 'adam'},
        'Himmel': {'turkish_meaning': 'gökyüzü'},
        'Mond': {'turkish_meaning': 'ay'},
        'Wald': {'turkish_meaning': 'orman'},
        'Berg': {'turkish_meaning': 'dağ'},
        'Fluss': {'turkish_meaning': 'nehir'},
        'See': {'turkish_meaning': 'göl'},
        'Haus': {'turkish_meaning': 'ev'},
        'Fenster': {'turkish_meaning': 'pencere'},
        'Tür': {'turkish_meaning': 'kapı'},
        'Baum': {'turkish_meaning': 'ağaç'},
        'Stift': {'turkish_meaning': 'kalem'},
        'Zug': {'turkish_meaning': 'tren'},
        'Garten': {'turkish_meaning': 'bahçe'},
        'Vogel': {'turkish_meaning': 'kuş'},
        'Freund': {'turkish_meaning': 'arkadaş'},
        'Lehrer': {'turkish_meaning': 'öğretmen'},
        'Schuh': {'turkish_meaning': 'ayakkabı'},
        'Brief': {'turkish_meaning': 'mektup'},
        'Schlüssel': {'turkish_meaning': 'anahtar'},
        'Kopf': {'turkish_meaning': 'baş'},
        'Computer': {'turkish_meaning': 'bilgisayar'},
        'Bruder': {'turkish_meaning': 'erkek kardeş'},
        'Schrank': {'turkish_meaning': 'dolap'},
        'Fernsehen': {'turkish_meaning': 'televizyon'},
        'Kühlschrank': {'turkish_meaning': 'buzdolabı'}
    },
    'die': {
        'Dusche': {'turkish_meaning': 'duş'},
        'Brüder': {'turkish_meaning': 'erkek kardeşler'},
        'Apfel': {'turkish_meaning': 'elma'},
        'Frau': {'turkish_meaning': 'kadın'},
        'Katze': {'turkish_meaning': 'kedi'},
        'Blume': {'turkish_meaning': 'çiçek'},
        'Ente': {'turkish_meaning': 'ördek'},
        'Schule': {'turkish_meaning': 'okul'},
        'Sofas': {'turkish_meaning': 'koltuklar'},
        'Universität': {'turkish_meaning': 'üniversite'},
        'Stadt': {'turkish_meaning': 'şehir'},
        'Land': {'turkish_meaning': 'ülke'},
        'Sprache': {'turkish_meaning': 'dil'},
        'Musik': {'turkish_meaning': 'müzik'},
        'Blatt': {'turkish_meaning': 'yaprak'},
        'Straße': {'turkish_meaning': 'cadde'},
        'Zeitung': {'turkish_meaning': 'gazete'},
        'Zeitschrift': {'turkish_meaning': 'dergi'},
        'Tasche': {'turkish_meaning': 'çanta'},
        'Uhr': {'turkish_meaning': 'saat'},
        'Karte': {'turkish_meaning': 'harita'},
        'Maus': {'turkish_meaning': 'fare'},
        'Nacht': {'turkish_meaning': 'gece'},
        'Idee': {'turkish_meaning': 'fikir'},
        'Woche': {'turkish_meaning': 'hafta'},
        'Sonne': {'turkish_meaning': 'güneş'},
        'Arbeit': {'turkish_meaning': 'iş'},
        'Kuchen': {'turkish_meaning': 'kek'},
        'Stunde': {'turkish_meaning': 'saat'}
    },
    'das': {
        'Sofa': {'turkish_meaning': 'koltuk'},
        'Dunkel': {'turkish_meaning': 'karanlık'},
        'Regal': {'turkish_meaning': 'raf'},
        'Rot': {'turkish_meaning': 'kırmızı'},
        'Weiss': {'turkish_meaning': 'beyeaz'},
        'Buch': {'turkish_meaning': 'kitap'},
        'Haus': {'turkish_meaning': 'ev'},
        'Kind': {'turkish_meaning': 'çocuk'},
        'Auto': {'turkish_meaning': 'araba'},
        'Geld': {'turkish_meaning': 'para'},
        'Telefon': {'turkish_meaning': 'telefon'},
        'Fahrrad': {'turkish_meaning': 'bisiklet'},
        'Boot': {'turkish_meaning': 'tekne'},
        'Uhr': {'turkish_meaning': 'saat'},
        'Radio': {'turkish_meaning': 'radyo'},
        'Computer': {'turkish_meaning': 'bilgisayar'},
        'Hemd': {'turkish_meaning': 'gömlek'},
        'Mantel': {'turkish_meaning': 'palto'},
        'Kleid': {'turkish_meaning': 'elbise'},
        'Spiel': {'turkish_meaning': 'oyun'},
        'Bild': {'turkish_meaning': 'resim'},
        'Licht': {'turkish_meaning': 'ışık'},
        'Leben': {'turkish_meaning': 'hayat'},
        'Bett': {'turkish_meaning': 'yatak'},
        'Zimmer': {'turkish_meaning': 'oda'},
        'Gesicht': {'turkish_meaning': 'yüz'},
        'Wort': {'turkish_meaning': 'kelime'},
        'Beispiel': {'turkish_meaning': 'örnek'},
        'Problem': {'turkish_meaning': 'problem'},
        'Thema': {'turkish_meaning': 'tema'},
        'Ende': {'turkish_meaning': 'son'},
        'Bier': {'turkish_meaning': 'bira'},
        'Jahr': {'turkish_meaning': 'yıl'},
        'Name': {'turkish_meaning': 'isim'},
        'Foto': {'turkish_meaning': 'fotoğraf'},
        'Zimmer': {'turkish_meaning': 'oda'},
        'Frühstück': {'turkish_meaning': 'kahvaltı'}
    }
}



# Your words_data dictionary here

def practice_articles():
   while True:
     article = random.choice(list(words_data.keys()))
     german_word, word_data = random.choice(list(words_data[article].items()))
     turkish_meaning = word_data['turkish_meaning']

     user_input = simpledialog.askstring("Article Practice", f"Please enter the correct article for '{german_word}':")
     if user_input is None:
        messagebox.showinfo("Info", "Practice cancelled.")
        break

     if user_input.lower() == article:
         messagebox.showinfo("Result", f"Correct! '{german_word}' means '{turkish_meaning}' in Turkish.")
     elif user_input == "2":
           practice_translation()
     elif user_input == "3": 
            practice_verbs()
     else:
         messagebox.showerror("Result", f"Wrong! The correct article for '{german_word}' is '{article}'. '{german_word}' means '{turkish_meaning}' in Turkish.")


def practice_translation():
    while True:
        article_tr = random.choice(list(words_data.keys()))
        german_word_tr, word_data = random.choice(list(words_data[article_tr].items()))
        turkish_meaning = word_data['turkish_meaning']
        user_input = simpledialog.askstring("Please enter the correct translation for '{}': ".format(german_word_tr)).strip().lower()


        if user_input == turkish_meaning:
           print("Korrect!")
        elif user_input == "1":
           practice_articles()
        elif user_input == "3":
           practice_verbs()
        elif user_input == 'quit':
           print('Take care!')
           break
        else:
           print("\033[91mFalsch! The correct translation for '{}' means '{}' in Turkish.\033[0m".format(german_word_tr, turkish_meaning))
       

def practice_verbs():
    while True:

        chosen_verb = random.choice(verbs['first'])
        position_of_random = verbs['first'].index(chosen_verb) 
        chosen_item = random.choice(list(verbs.keys()))
        chosen_item_value = verbs[chosen_item]
        list_chosen_item_value = list(chosen_item_value)
        position_of_random_item = list_chosen_item_value[position_of_random]

        user_input_verbs = simpledialog.askstring("Verb Conjiguation", f"Please enter Correct form of the '{chosen_verb}' for '{chosen_item}': ")

        if user_input_verbs == position_of_random_item:
           messagebox.showinfo("Result", f"Korrect")
        elif user_input_verbs == "2":
           practice_translation()
        elif user_input_verbs == "1":
           practice_articles()
        else:
           messagebox.showerror("Result", f"Falch! Correct form for the Verb is '{position_of_random_item}' for '{chosen_item}'")

def practice_translation():
    while True:
        article_tr = random.choice(list(words_data.keys()))
        german_word_tr, word_data = random.choice(list(words_data[article_tr].items()))
        turkish_meaning = word_data['turkish_meaning']
        user_input = input("Please enter the correct translation for '{}': ".format(german_word_tr)).strip().lower()
        
        if user_input == turkish_meaning:
           print("Korrect!")
        elif user_input == "1":
           practice_articles()
        elif user_input == "3":
           practice_verbs()
        elif user_input == 'quit':
           print('Take care!')
           break
        else:
           print("\033[91mFalsch! The correct translation for '{}' means '{}' in Turkish.\033[0m".format(german_word_tr, turkish_meaning))
       
    
root = tk.Tk()
root.title("German Practice App")


def ok_action():
    ok_button = tk.Button(root, text="OK", command=ok_action)
    ok_button.pack()

 
def cancel_action():
    cancel_button = tk.Button(root, text="Cancel", command=root.destroy)
    cancel_button.pack()


root = tk.Tk()
root.title("German Practice")

article_button = tk.Button(root, text="Article Practice", command=practice_articles)
verb_button = tk.Button(root, text="Verb Conjiguation", command=practice_verbs, )
translation_button = tk.Button(root, text="German to Turkish Translation", command=practice_translation)


article_button.pack(pady=20)
verb_button.pack(pady=20)
translation_button.pack(pady=20)

# Running the application
root.mainloop()
