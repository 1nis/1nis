import datetime

def update_readme():
    file_path = 'README.md'
    start_marker = ''
    end_marker = ''
    
    # 1. Obtenir la date
    now = datetime.datetime.now()
    date_str = now.strftime("%d/%m/%Y")
    new_line = f"📅 - **Mise à jour automatique le : {date_str}**\n"

    # 2. Lire le fichier
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 3. Trouver les index
    start_index = -1
    end_index = -1

    for i, line in enumerate(lines):
        if start_marker in line:
            start_index = i
        elif end_marker in line:
            end_index = i
            break # On arrête dès qu'on a trouvé la fin

    # 4. Vérifications de sécurité
    if start_index == -1 or end_index == -1:
        print("❌ Erreur : Balises introuvables. Le README n'a pas été modifié.")
        return
    
    if end_index <= start_index:
        print("❌ Erreur : L'ordre des balises est incorrect.")
        return

    # 5. Reconstruction du contenu (Chirurgical)
    # On garde tout AVANT le début + le début + la nouvelle ligne + la fin + tout APRÈS la fin
    new_content = lines[:start_index+1] + [new_line] + lines[end_index:]

    # 6. Écriture
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(new_content)
    
    print(f"✅ README mis à jour avec succès : {date_str}")

if __name__ == "__main__":
    update_readme()
