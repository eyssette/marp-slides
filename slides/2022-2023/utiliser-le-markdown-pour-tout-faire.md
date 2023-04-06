---
marp: true
theme: teaching
paginate: true
size: 4:3
---

<!-- _class: titre -->
<style scoped>
span {font-size:0.7em}
</style>

# Utiliser <br>le Markdown<br>pour tout faire<!-- fit -->

Cédric Eyssette (2022-2023)
https://eyssette.github.io/

---
<!-- _class: partie -->
# I - <br>Pourquoi ? <!-- fit -->
Première partie


---
<!-- _class: souspartie -->
<style scoped>
p {margin:20px 60px; font-size:1.5em}
</style>

## A. Objectif principal

<span data-marpit-fragment="1">→ Travailler seulement avec des fichiers textes</span>

---
<!-- _class: etape fp -->
<style scoped>
h3 {padding-bottom:0.8em; font-size:1.2em}
</style>

### 1/ Un format léger
* **Édition** plus rapide
  * Pas besoin d'un logiciel lourd
  * Pas besoin d'un ordinateur hyper-performant 
  * Logiciels plus adaptés pour l'édition de textes
  * Focalisation sur le fond et pas sur la forme
* **Sauvegarde** plus économe et plus rapide
  * synchronisation facilitée
  * versionnage facilité
* **Recherche** plus rapide dans ses fichiers

<!-- 
VSCodium : évoquer (en parler plus tard)
git, forge pour synchronisation et versionnage
évoquer système de nommage des fichiers -->


---
<!-- _class: etape fpppppp -->
<style scoped>
h3 {padding-bottom:0.8em; font-size:1.2em}
</style>

### 2/ Un format ouvert

* On peut utiliser n'importe quelle **machine** et n'importe quel **logiciel** d'édition de texte
* On peut **collaborer** facilement sur un même fichier
* La **pérennité** du fichier est assurée


<!-- Pas prisonnier d'un logiciel qui doit être installé, on peut travailler de partout même avec un éditeur en ligne
(VS Code : édition en ligne possible) -->


---
<!-- _class: souspartie -->
<style scoped>
p {margin:0px 60px; font-size:1.2em}
</style>

## B. Le Markdown : un bon compromis

<span data-marpit-fragment="1">→ Une syntaxe qui reste simple</span>
<span data-marpit-fragment="2">→ Mais qui permet de créer<br>des documents complexes</span>


---
<!-- _class: etape fppp -->
<style scoped>
h3 {padding-bottom:0.8em; font-size:1.2em}
p {text-align:left;}
</style>
### 1/ Une syntaxe simple

- Titres : `# Titre 1` / `## Titre 2`
- Gras / italiques : `**gras**` / `_italiques_`
- Citations, code : `> citation` / ``` `code` ``` 
- Listes : `- texte` / `1. texte`
- Liens : `[texte](URL)`
- Images : `![description](URL)`


<!-- 
Balise code


Mettre ici comparaison entre markdown / html
entre markdown / latex

évoquer autres langages balisages

fichier lisible par un être humain / qui intègre des informations faciles à exploiter par une machine, un programme
-->

---
<!-- _class: etape fpppp -->
<style scoped>
h3 {padding-bottom:0.5em; font-size:1.2em}
</style>
### 2/ Une syntaxe qui permet de créer des documents complexes

- Possibilité d'intégrer du HTML, du $\LaTeX$
- Des extensions possibles du Markdown
- Possibilité d'avoir un en-tête en YAML
- Des outils pour transformer le markdown en un autre format
- Export HTML : intégration possible de styles CSS

<!-- 
Extensions du markdown :
notes de bas de page
tableaux
texte souligné / surligné / supprimé / exposant / indices

Ajouter ?
Des outils pour intégrer dans du markdown d'autres fichiers ?
fichier bibtex pour les 
-->

---
<!-- _class: partie -->
# II - <br>Comment ? <!-- fit -->
Deuxième partie