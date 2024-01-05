import re
import sys
import pyperclip
# Sur linux, installer xclip et xsel pour pouvoir conserver le contenu de pyperclip.copy dans le clipboard après la fermeture du script

def remove_yaml_header(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Recherche de l'en-tête YAML
    yaml_header_regex = r'^---\n.*?\n---\n+'
    content = re.sub(yaml_header_regex, '', content, flags=re.DOTALL)
    
    return content

def remove_part_titles(content):
    # Suppression des références aux titres de parties
    part_titles = ['Première partie', 'Deuxième partie', 'Troisième partie']
    for title in part_titles:
        content = re.sub(r'^' + re.escape(title) + r'$', '', content, flags=re.MULTILINE)
    
    return content

def remove_html_comments(content):
    # Suppression des commentaires HTML
    comment_regex = r'<!--.*?-->'
    content = re.sub(comment_regex, '', content, flags=re.DOTALL)
    
    return content

def remove_style_tags(content):
    # Suppression des balises <style> et <style scoped> ainsi que leur contenu
    style_regex = r'<style(?:\sscoped)?>(?:.|\n)*?</style>(\n+)?'
    content = re.sub(style_regex, '', content, flags=re.IGNORECASE)
    
    return content

def remove_fragment_attributes(content):
    # Suppression des occurrences de data-marpit-fragment="X"
    fragment_regex = r'data-marpit-fragment(="\d+")?'
    content = re.sub(fragment_regex, '', content)
    
    return content


def remove_separators(content):
    # Suppression des marqueurs de séparation "---"
    separator_regex = r'^---\n'
    content = re.sub(separator_regex, '', content, flags=re.MULTILINE)
    
    return content

def replace_br_tags(content):
    # Remplacement des balises <br> ou <br/> par un espace
    br_regex = r'<br\s?/?>'
    content = re.sub(br_regex, ' ', content, flags=re.IGNORECASE)
    
    return content

def replace_spaces(content):
    # Remplacement des doubles (et +) espaces par un espace simple
    content = re.sub(r'  +', ' ', content)
    # Remplacement des triples (et +) retours à la ligne par un double retours à la ligne
    content = re.sub(r'\n\n\n+', '\n\n', content)
    # Suppression des retours à la ligne au début du fichier
    content = re.sub(r'^\n+', '', content)
    
    return content

def process_file(file_path):
    # Suppression de l'en-tête YAML
    content = remove_yaml_header(file_path)

    # Suppression des références aux titres de parties
    content = remove_part_titles(content)

    # Suppression des commentaires HTML
    content = remove_html_comments(content)
    
    # Suppression des balises <style> et <style scoped>
    content = remove_style_tags(content)

    # Suppression des occurrences de data-marpit-fragment="X"
    content = remove_fragment_attributes(content)

    # Suppression des marqueurs de séparation
    content = remove_separators(content)
    
    # Remplacement des balises <br> ou <br/> par un espace
    content = replace_br_tags(content)
    
    # Remplacement des espaces inutiles
    content = replace_spaces(content)
    
    return content

# Vérification des arguments en ligne de commande
if len(sys.argv) != 2:
    print("Usage: python md-raw.py <input_file>")
    sys.exit(1)

input_file = sys.argv[1]

# Traitement du fichier Markdown
content = process_file(input_file)

# Création du fichier RAW

output_file = input_file.rsplit('.', 1)[0] + '-RAW.md'

pyperclip.copy(content.rstrip())