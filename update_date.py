import datetime
import re

def update_readme():
    file_path = 'README.md'
    
    # 1. Lire le contenu actuel
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        print("❌ Erreur : Le fichier README.md est introuvable.")
        return

    # 2. Préparer la nouvelle date
    now = datetime.datetime.now()
    date_str = now.strftime("%d/%m/%Y")
    # Note : On garde les balises dans le remplacement pour ne pas les perdre
    new_content_block = f"\n📅 - **Mise à jour automatique le : {date_str}** <br>\n"

    # 3. Utiliser une Regex pour trouver et remplacer UNIQUEMENT le bloc ciblé
    # Le pattern cherche : (Début) n'importe quoi au milieu (Fin)
    pattern = r".*?"
    
    # re.DOTALL permet au point (.) de matcher aussi les sauts de ligne
    new_full_content = re.sub(pattern, new_content_block, content, flags=re.DOTALL)

    # 4. Vérifier si on a fait un changement
    if new_full_content == content:
        print("ℹ️ La date est déjà à jour. Aucun changement nécessaire.")
    else:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_full_content)
        print(f"✅ Succès : Date mise à jour au {date_str}")

if __name__ == "__main__":
    update_readme()
