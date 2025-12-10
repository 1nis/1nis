import datetime

# 1. Obtenir la date actuelle
now = datetime.datetime.now()
date_str = now.strftime("%d/%m/%Y") # Format: JJ/MM/AAAA
new_content = f"📅 - **Mise à jour automatique le : {date_str}** <br>"

# 2. Lire le fichier README
file_path = 'README.md'
with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 3. Remplacer le contenu entre les balises
start_marker = ''
end_marker = ''
new_lines = []
in_zone = False
found_zone = False

for line in lines:
    if start_marker in line:
        new_lines.append(line) # Garder la balise de début
        new_lines.append(new_content + "\n") # Ajouter la nouvelle date
        in_zone = True
        found_zone = True
    elif end_marker in line:
        new_lines.append(line) # Garder la balise de fin
        in_zone = False
    elif not in_zone:
        new_lines.append(line)

if not found_zone:
    print("Erreur : Balises non trouvées dans le README.")
else:
    # 4. Écrire les modifications
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)
    print(f"README mis à jour avec la date : {date_str}")
