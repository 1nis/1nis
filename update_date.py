import datetime
import re

# 1. Obtenir la date actuelle
now = datetime.datetime.now()
date_str = now.strftime("%d/%m/%Y")
new_content = f"📅 - **Mise à jour automatique le : {date_str}** <br>"

# 2. Lire le fichier README
file_path = 'README.md'
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# 3. Remplacer le contenu avec une Regex (Plus sûr)
# Cela cherche tout ce qui est entre les balises et le remplace
pattern = r"()(.*?)()"
replacement = f"\\1\n{new_content}\n\\3"

# Le flag DOTALL permet au point (.) de matcher aussi les retours à la ligne
new_content_full = re.sub(pattern, replacement, content, flags=re.DOTALL)

# 4. Écrire les modifications seulement si ça a changé
if new_content_full != content:
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content_full)
    print(f"✅ README mis à jour avec la date : {date_str}")
else:
    print("ℹ️ La date était déjà à jour, pas de changement.")
