---
marp: true
theme: teaching
paginate: true
size: 4:3
---

<!-- _class: titre -->

# ChatMD : <br>un chatbot <br>libre et gratuit <!-- fit -->

Cédric Eyssette (2023-2024)
https://eyssette.forge.aeif.fr/chatMD


---
<!-- _class:  -->
<style scoped>
	h3 {font-size:1.4em; margin-bottom:1em}
</style>

### Plan

I - Présentation générale de l'outil

II - Exemples d'usages

III - Options plus avancées et évolutions possibles



---
<!-- _class: partie -->
# I - Présentation <br>générale <br>de l'outil <!-- fit -->
Première partie


---
<!-- _class: f -->
<style scoped>
ol {padding-top:0}
</style>
### Point de départ

1) L'arrivée en masse des IA génératives redonne de l'intérêt aux chatbots
2) Un chatbot peut être un excellent moyen de trouver de l'information, de manière plus naturelle et interactive
3) Mais les IA génératives produisent des hallucinations, on n'est pas maître des réponses qu'elles produisent
4) Les solutions pour créer des chatbots plus contrôlés sont souvent payantes, avec des interfaces complexes et sans garantie de pérennité

---
<!-- _class: fpppppp -->
<style scoped>
p:last-of-type a {font-size:0.9em}
</style>

[ChatMD](https://eyssette.forge.apps.education.fr/chatMD/) est un logiciel libre et gratuit qui permet de créer en ligne un chatbot simplement et sans création de comptes, ni pour le créateur ni pour l'utilisateur.

<span data-marpit-fragment="1">ChatMD ne récolte pas de cookies non plus et il est donc totalement compatible RGPD.</span>

<span data-marpit-fragment="2"> Il est disponible sur la Forge des communs numériques éducatifs :
https://eyssette.forge.apps.education.fr/chatMD/</span>


---
<!-- _class: fppppppp -->

[ChatMD](https://eyssette.forge.apps.education.fr/chatMD/) ne repose pas sur de l'intelligence artificielle générative.

Le but est d'avoir un meilleur contrôle sur le chatbot et d'éviter les hallucinations propres aux IA génératives.

<span data-marpit-fragment="1">Il faut donc définir soi-même les réponses possibles du chatbot et anticiper ainsi les interactions possibles avec l'utilisateur.</span>

---
<!-- _class: fppppppp -->

La configuration du chatbot se fait à partir d'un simple fichier en Markdown avec une syntaxe particulière, facile à apprendre.

<span data-marpit-fragment="1">On peut utiliser [CodiMD](https://codimd.apps.education.fr/) sur le portail Apps Education, ce qui permet de travailler de manière collaborative sur un chatbot ou même de donner l'accès à des élèves pour qu'ils créent un chatbot.</span>


---
<!-- _class:  -->
<style scoped>
pre {margin-left:60px; margin-right:60px; padding-bottom: 1px}
</style>

### Le principe 

```markdown
## Titre de ma réponse
- déclencheur 1
- déclencheur 2

Contenu de la réponse : on peut
utiliser toute la syntaxe Markdown,
intégrer des images, des vidéo,
des iframes …

1. [Proposition 1](Titre Proposition 1)
2. [Proposition 2](Titre Proposition 2)

```

---
<!-- _class:  -->
ChatMD calcule la réponse la plus appropriée en prenant en compte les déclencheurs, le titre de la réponse et éventuellement le contenu de la réponse.

<span data-marpit-fragment="1">C'est un calcul de similarité qui permet de prendre en compte : les fautes d'orthographe, les termes proches mais pas identiques.</span>

---
<!-- _class: partie -->
# II - Exemples <br>d'usages <!-- fit -->
Deuxième partie

---
<!-- _class: souspartie -->
## A. Pour les élèves <br>(voire : par les élèves) <!-- fit -->

---
<!-- _class: f -->

Guide méthodologique pour la rédaction d'un devoir : [méthode pour la dissertation en philosophie](https://eyssette.forge.aeif.fr/chatMD/#https://eyssette.forge.aeif.fr/chatbot/dissertation-philosophie.md)  …


<span data-marpit-fragment="1">Guide pratique pour l'utilisation d'une technique expérimentale : un [microscope](https://eyssette.forge.aeif.fr/chatMD/#https://codimd.apps.education.fr/xGNHIJSeTVCk6FHas-_71g), une [perceuse à colonne](https://eyssette.forge.aeif.fr/chatMD/#https://codimd.apps.education.fr/j2c6hkpCRuua0almpXIMdA?both) …</span>

<span data-marpit-fragment="2">Soutien pour la révision d'un cours, ou activité préalable de découverte avant un cours : [révision des définitions en philosophie](https://eyssette.forge.aeif.fr/chatMD/#https://github.com/eyssette/chatbot/blob/main/vocabulaire-philosophie.md), [découverte des sons produits par les chauve-souris](https://eyssette.forge.aeif.fr/chatMD/#https://codimd.apps.education.fr/vzZtsGoxReGEYMAdecZlCg)</span>

<span data-marpit-fragment="3">Réponse à des questions fréquentes d'élèves ou de parents : [sur l'orientation ou les formations disponibles](https://eyssette.forge.aeif.fr/chatMD/#https://codimd.apps.education.fr/FEW7JMjbSXur_C5IxLuFEg), [sur le passage au collège](https://eyssette.forge.aeif.fr/chatMD/#https://codimd.apps.education.fr/MRGzdbetRru3VbpeRePIJQ) …</span>


---
<!-- _class:  -->

Discussion avec un personnage historique : [la reine Marie-Antoinette](https://eyssette.forge.aeif.fr/chatMD/#https://codimd.apps.education.fr/s/YyWmE5XYd), [Lucie Aubrac](https://eyssette.forge.aeif.fr/chatMD/#https://codimd.apps.education.fr/s/TGg7nwolB), [Bartholomew Roberts](https://eyssette.forge.aeif.fr/chatMD/#https://codimd.apps.education.fr/Rw3tzAaoQSis7vo3pthirQ)

<span data-marpit-fragment="1">Histoire dont vous êtes le héros : [en DNL Anglais/Philosophie](https://eyssette.github.io/chatMD/#https://codimd.apps.education.fr/wWukuOEaT8CjOqpYP3p1tA)  …</span>


<!-- 
https://eyssette.forge.aeif.fr/chatMD/#https://codimd.apps.education.fr/PsdbCN3FQtWY0QX-g6b2_A
 -->

---
<!-- _class: souspartie -->
## B. Pour des collègues <br>(formation, accès à <br>des informations …) <!-- fit -->


---
<!-- _class:  -->

Tutoriel pour l'utilisation d'un outil informatique : [utilisation de la Forge](https://eyssette.forge.aeif.fr/chatMD/#https://github.com/eyssette/chatbot/blob/main/utiliser-la-forge.md), [mise en place d'ELEA](https://drane.ac-lyon.fr/spip/ELEA-la-plateforme-Moodle-de-l)

<span data-marpit-fragment="1">Guide pratique pour pouvoir répondre à un problème, accès plus facile et interactif à des informations : [redirection vers la bonne plateforme d'assistance](https://drane-lyon.forge.aeif.fr/chatMD/#https://codimd.apps.education.fr/KgiRUrr8Ttq9-CxZGmxmmg), [gestion des fiches Google]()</span>



---
<!-- _class:  -->

### Faire son Chatbot

[Un modèle](https://codimd.apps.education.fr/mBGbHStJSVOSrlGfGb981A?both)

Des tutoriels : [sur le site de ChatMD](https://eyssette.forge.aeif.fr/chatMD), [sur le site de l'académie d'Aix-Marseilles](https://www.pedagogie.ac-aix-marseille.fr/jcms/c_11196334/fr/decouvrir-chatmd), [sur des sites de collègues](https://itsenglishoclock.com/2024/03/19/creer-et-utiliser-des-chatbots-en-classe-de-langue/#ChatMD_Creer_son_propre_robot_libre_open_source)

---
<!-- _class: partie -->
# III - Options <br>plus avancées et <br>évolution de l'outil <!-- fit -->
III

---
<!-- _class: fpppppp -->

### Apparence du chatbot

1) On peut supprimer le clavier si on veut guider l'utilisateur avec des options.
2) On peut configurer l'apparence de son chatbot : choix de l'avatar, styles personnalisés (CSS).

<span data-marpit-fragment="1">**En préparation** : choix de différents thèmes possibles.</span>



---
<!-- _class: fp -->

### Réponses du chatbot

1) On peut intégrer les mathématiques.
2) Le chatbot peut détecter automatiquement les insultes.
3) On peut mettre plusieurs réponses possibles et laisser chatMD faire un choix aléatoire parmi ces réponses.
4) On peut changer les messages par défaut si le chatbot n'a pas trouvé de réponse appropriée.

<span data-marpit-fragment="1">**En préparation** : intégration possible de ChatMD avec une IA générative.</span>

---
<!-- _class: fppp -->

### Syntaxe du chatbot

1) On peut changer la syntaxe des titres de réponse pour mieux organiser son document.
2) On peut utiliser des variables pour éviter les répétitions.

<span data-marpit-fragment="1">**En préparation** : exécution de fonctions plus complexes pour calculer la réponse appropriée, par exemple en prenant en compte une réponse précédente.</span>


---
<!-- _class: fpppp -->

### Hébergement du chatbot

1) On peut utiliser la version en ligne sur la Forge.
2) On peut aussi créer son propre chatMD sur la Forge : on peut alors définir des liens raccourcis

<span data-marpit-fragment="1">**En préparation** : des options de sécurisation</span><span data-marpit-fragment="2">, une version serveur …</span>

<!-- 
Sécurisation : pour n'accepter que des chatbots précis
Version serveur : base de données + importantes (rapidité) / avoir un retour des utilisateurs sur les réponses reçues
-->

---
<!-- _class:  -->
<style scoped>
a {display:block; margin-top:0.4em}
</style>

ChatMD est un logiciel destiné à s'adapter aux besoins des collègues.

<span data-marpit-fragment="1">Il ne faut pas hésiter à faire des demandes ou des remarques pour faire évoluer le logiciel : cedric.eyssette@ac-lyon.fr</span>
