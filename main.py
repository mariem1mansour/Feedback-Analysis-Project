# Installer les bibliothèques nécessaires
# !pip install goose3
# !pip install textblob
# !pip install mysql-connector-python

# Importation des modules
from textblob import TextBlob
from goose3 import Goose
import mysql.connector
import tkinter as tk
from tkinter import messagebox

# Fonction pour analyser l'URL et stocker dans MySQL
def analyze_url():
    url = url_entry.get()  # Récupérer l'URL depuis le champ d'entrée
    if not url:
        messagebox.showerror("Erreur", "Veuillez entrer une URL valide.")
        return
    
    # Extraction de l'article
    g = Goose()
    article = g.extract(url=url)
    content = article.cleaned_text

    if not content:
        messagebox.showerror("Erreur", "Impossible d'extraire le texte de l'URL.")
        return

    # Analyse de sentiment
    text_blob = TextBlob(content)
    sentiment = text_blob.sentiment.polarity

    # Afficher les résultats dans le champ de sortie
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, f"Texte extrait :\n{content}\n\n")
    result_text.insert(tk.END, f"Sentiment : {'Positif' if sentiment > 0 else 'Négatif' if sentiment < 0 else 'Neutre'} ({sentiment})")

    # Stocker dans MySQL
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="feedback_analysis"
        )
        cursor = connection.cursor()
        insert_query = """
        INSERT INTO feedback (url, content, sentiment) 
        VALUES (%s, %s, %s)
        """
        cursor.execute(insert_query, (url, content, sentiment))
        connection.commit()
        cursor.close()
        connection.close()
        messagebox.showinfo("Succès", "Les résultats ont été enregistrés dans la base de données.")
    except mysql.connector.Error as err:
        messagebox.showerror("Erreur", f"Erreur lors de la connexion à MySQL : {err}")

# Configuration de l'interface graphique
root = tk.Tk()
root.title("Analyse des Feedbacks")

# Champ pour entrer l'URL
url_label = tk.Label(root, text="Entrez l'URL de la page produit :", font=("Arial", 12))
url_label.pack(pady=5)
url_entry = tk.Entry(root, width=50, font=("Arial", 12))
url_entry.pack(pady=5)

# Bouton pour lancer l'analyse
analyze_button = tk.Button(root, text="Analyser", font=("Arial", 12), command=analyze_url)
analyze_button.pack(pady=10)

# Zone de texte pour afficher les résultats
result_label = tk.Label(root, text="Résultats :", font=("Arial", 12))
result_label.pack(pady=5)
result_text = tk.Text(root, width=60, height=15, font=("Arial", 10))
result_text.pack(pady=5)

# Lancement de la fenêtre
root.mainloop()
