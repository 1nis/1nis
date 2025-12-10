import datetime
import re

def update_readme():
    file_path = 'README.md'
    
    # 1. Lire le fichier actuel
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        print("❌ Erreur : Impossible de trouver le fichier README.md")
        return

    # 2. Préparer la date du jour
    now = datetime.datetime.now()
    date_str = now.strftime("%d/%m/%Y") # Format : 10/12/2025
    
    new_text_block = f"``📅 - Mise à jour automatique le : {date_str}``"

    # 3. CHERCHER ET REMPLACER
    pattern = r"``📅 - Mise à jour automatique le : .*?``"
    
    if not re.search(pattern, content):
        print("❌ ERREUR : Le script ne trouve pas la ligne de date dans le README.")
        print("Vérifie que ton README contient bien une ligne qui ressemble à :")
        print("``📅 - Mise à jour automatique le : XX/XX/XXXX``")
        return

    new_content = re.sub(pattern, new_text_block, content)

    # 4. Sauvegarder si changement
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"✅ Succès : Date mise à jour au {date_str}")
    else:
        print("ℹ️ La date était déjà à jour.")

if __name__ == "__main__":
    update_readme()
