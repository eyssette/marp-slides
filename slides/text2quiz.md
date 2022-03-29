---
marp: true
theme: teaching
paginate: true
size: 4:3
---

<!-- _class: titre -->
<style scoped>
h1 {margin-top:-2.6em!important}
ol {width:750px!important; position:absolute; top:270px; text-align:center; list-style-type:none}
</style>
# Text2quiz <!-- fit -->
Cédric Eyssette
cedric.eyssette@ac-lyon.fr

1) Un outil libre et gratuit en ligne
2) Sans création de compte, sans données personnelles enregistrées

---
<!-- _class:  -->

* 13 types de questions
  * Vrai/faux, QCM, Texte à trous, Flashcard, Remise en ordre, Etiquettes à positionner ...
* Plusieurs modes de partage : entre collègues, pour les élèves (autoévaluation ou évaluation)
* Possibilité d'utiliser du Latex, du markdown, du HTML

---
<!-- _class:  -->
<style scoped>
pre {margin:30px 60px!important}
</style>

Le principe : un simple fichier texte avec une syntaxe simple à apprendre.

<div data-marpit-fragment="1">

```
VF || Énoncé || V
Trous || Texte avec des {{V:trous|trou}}
Flashcard || Recto || Verso
```

</div>

On peut mettre ce fichier texte sur une forge : text2quiz peut alors [transformer automatiquement ce texte en un quiz](https://text2quiz.vercel.app/?v=1.0#VF%20%7C%7C%20%C3%89nonc%C3%A9%20%7C%7C%20V%0ATrous%20%7C%7C%20Texte%20avec%20des%20%7B%7BV:trous%7Ctrou%7D%7D%0AFlashcard%20%7C%7C%20Recto%20%7C%7C%20Verso).


