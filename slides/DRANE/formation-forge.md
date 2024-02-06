---
marp: true
theme: teaching
paginate: true
size: 4:3
---

<!-- _class: titre-->
<style scoped>
img {position:absolute; top:40px; left:30px;z-index:-1; height:450px; width:360px; background:transparent!important}
h1 {margin-left:270px; padding-right:30px!important; line-height:1.15; text-align:right;}
</style>


# La Forge des <br>communs <br>numériques<br> éducatifs<!-- fit -->

![](https://forge.aeif.fr/framaka/visuel-forge/-/raw/main/brigit-et-komit/Brigit_et_Komit_transparent.png?ref_type=heads)

Cédric Eyssette - chargé de projet
DRANE site de Lyon



---
<!-- _class: i1t1 horizontal  -->
<style scoped>
p {font-size:1.3em; text-align:left!important;}
p:nth-of-type(1){width:400px; margin-left:20px!important; padding:0}
p:nth-of-type(2){margin-left:10px!important; width:410px}
</style>

![](https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Alexis_Kauffmann_-_Taipei_European_School_-_2017.jpg/800px-Alexis_Kauffmann_-_Taipei_European_School_-_2017.jpg)

Un projet initié en 2022 par **Alexis Kauffmann**, chef de projet logiciels et ressources éducatives libres à la _Direction du Numérique pour l'Éducation_ (DNE)


---
<!-- _class:  -->
<style scoped>
section {font-size:4.6em}
p {margin-top:0.4em; margin-left:50px}
h4 {margin-bottom:0.5em; text-align:center;margin-left:0; font-size:1.5em; margin-top:-30px!important}
</style>
#### Plan

**I -** Qu'est-ce qu'une forge ?
À quoi ça sert ?

**II -** Comment utiliser la forge ?

---
<!-- _class: -->
<style scoped>
h2 {background:rgba(0,0,0,0.9); color:white; padding:60px 130px;}
</style>
## I - Qu'est-ce <br>qu'une forge ?<br> À quoi ça sert ? <!-- fit -->

![bg](https://forge.aeif.fr/framaka/visuel-forge/-/raw/main/brigit-et-komit/Brigit_et_Komit_avec_fond_forge_sans_logo.png?ref_type=heads)


---
<!-- _class:  -->
Une forge ressemble à première vue à un **espace de  stockage en ligne** de fichiers que l'on peut synchroniser avec son propre ordinateur pour garantir la pérennité des données.

* Quelle est la différence avec NextCloud ?

---
<!-- _class: pp -->
<style scoped>
section {display:flex; flex-direction:column; align-items:center;}
p {margin:0;}
img {height:150px; background:transparent!important; float:left; margin-right:30px; margin-left:0px}
h3 {width:95%; background:rgba(0,0,0,0.1); padding-top:50px;  padding-bottom:50px; padding-right:40px}
</style>


### ![](https://forge.aeif.fr/framaka/visuel-forge/-/raw/main/avatars/avatar_Komit_face_cercle.png?ref_type=heads) A. Un outil conçu <br>initialement pour<br>les développeurs<!-- fit -->

<span data-marpit-fragment="1">… mais qu'on va pouvoir détourner pour en faire un outil pour tout le monde !</span>

---
<!-- _class:  -->
Une forge vise au départ à **héberger du code informatique**.

<span data-marpit-fragment="1">Elle n'est **pas faite pour héberger des fichiers lourds** (vidéo, audio, …)</span><span data-marpit-fragment="2"> : on y trouve surtout des fichiers au format texte.</span>

<span data-marpit-fragment="3">Une forge propose **un ensemble d'outils** pour répondre aux **besoins des développeurs**.</span>

<!-- Pas faite pour héberger des fichiers lourds :
exceptions possibles
Git LFS -->

---
<!-- _class: fmmm -->
<style scoped>
h4 {margin-bottom:0!important}
ul {margin-top:0;}
</style>

#### Pour développer un logiciel, on a besoin de :
1) pouvoir organiser et répartir les tâches à faire grâce à des outils de **gestion de projet**
2) pouvoir **éditer** facilement le code, conserver un **historique des modifications** et **revenir en arrière** en cas de problème
3) pouvoir lancer automatiquement des **scripts** qui vont tester / vérifier le code ou le compiler
4) s'il s'agit d'un logiciel en ligne, pouvoir facilement le **déployer sur le web**
5) pouvoir créer de la **documentation** facilement
6) pouvoir récupérer le **feedback des utilisateurs** (“_issues_”) et **collaborer** avec d'autres développeurs pour corriger les bugs et ajouter des fonctionnalités

---
La _Forge des Communs Numériques Éducatifs_ est une forge fondée sur un logiciel libre : Gitlab, qui propose tous ces outils.

<span data-marpit-fragment="1">La connexion se fait via le portail Apps Education</span><span data-marpit-fragment="2"> (possibilité de comptes externes).</span>

<span data-marpit-fragment="3">Les projets que l'on crée peuvent être publics ou privés.</span>

---
<!-- _class: fppp -->
Premier intérêt de la _Forge des Communs Numériques Éducatifs_ : on peut trouver sur la Forge des logiciels **libres**<span data-marpit-fragment="1"> faits **par des enseignants pour les enseignants**</span>

#### <span data-marpit-fragment="2">Quelques exemples :</span>
1) [Emmanuel Zimmert : La Digitale](https://forge.aeif.fr/users/ladigitale/projects)
2) [Laurent Abbal](https://laurentabbal.forge.apps.education.fr/)
3) [Arnaud Champollion](https://achampollion.forge.aeif.fr/)
4) [Mes outils](https://eyssette.forge.aeif.fr/)
5) [Coopmaths : MathALÉA …](https://forge.aeif.fr/coopmaths/mathalea)

---
<!-- _class: pp -->
<style scoped>
section {display:flex; flex-direction:column; align-items:center;}
p {margin:0; }
img {height:150px; background:transparent!important; float:left; margin-right:30px; margin-left:0px}
h3 {width:95%; background:rgba(0,0,0,0.1); padding-top:50px;  padding-bottom:50px; padding-right:40px}
</style>


### ![](https://forge.aeif.fr/framaka/visuel-forge/-/raw/main/avatars/avatar_Komit_face_cercle.png?ref_type=heads) B. Un outil qu'on peut <br>détourner et qui peut <br>servir à tout le monde<!-- fit -->


---
<!-- _class:  -->
<style scoped>
h4 {position:absolute; top:70px; font-size:1.2em}
img {margin-top:3em}
p {font-size:0.6em; text-align:center; color:#333; margin-top:1em}
</style>


#### Trois détournements possibles

[![](https://raw.githubusercontent.com/eyssette/mindmap/main/detournements-possibles-de-la-forge-aper%C3%A7u.svg)](https://mymarkmap.netlify.app/#https://raw.githubusercontent.com/eyssette/mindmap/main/detournements-possibles-de-la-forge.md)

(cliquer sur l'image pour voir le détail)


---
<!-- _class:  -->
<style scoped>
h4 {margin-bottom:0; font-size:1.3em}
ol {text-align:left; font-size:1.12em}
</style>
#### Le principe

1) Utiliser le **Markdown** et respecter éventuellement une **syntaxe** particulière
3) Utiliser un **modèle** ou un **outil** sur la forge pour **transformer automatiquement** son texte en un site web, un diaporama …

<!-- Une entrée possible pour aller vers la forge : CodiMD -->
<!-- Single Source Publishing -->

---
<!-- _class:  -->
<style scoped>
h2 {background:rgba(0,0,0,0.9); color:white; padding:90px 130px;}
</style>
## II - Comment <br>utiliser la forge ? <!-- fit -->

![bg](https://forge.aeif.fr/framaka/visuel-forge/-/raw/main/brigit-et-komit/Brigit_et_Komit_avec_fond_forge_sans_logo.png?ref_type=heads)



---
<!-- _class: pp -->
<style scoped>
section {display:flex; flex-direction:column; align-items:center;}
p {margin:0; }
img {height:150px; background:transparent!important; float:left; margin-right:30px; margin-left:0px}
h3 {width:95%; background:rgba(0,0,0,0.1); padding-top:50px;  padding-bottom:50px; padding-right:40px}
</style>


### ![](https://forge.aeif.fr/framaka/visuel-forge/-/raw/main/avatars/avatar_Komit_face_cercle.png?ref_type=heads) A. Travailler en ligne<br>sur la forge <!-- fit -->


---
<!-- _class:  -->

1) Authentification via le portail Apps Education
2) Création d'un groupe
3) Création d'un nouveau projet, éventuellement à partir d'un [modèle](https://forge.apps.education.fr/modeles-projets)
4) Édition possible sur la forge directement
5) Configuration du déploiement de ce projet sur le web

<!-- pipeline, runner, job, gitlab-ci.yaml cd/ci-->

---
<!-- _class: pp -->
<style scoped>
section {display:flex; flex-direction:column; align-items:center;}
p {margin:0; }
img {height:150px; background:transparent!important; float:left; margin-right:30px; margin-left:0px}
h3 {width:95%; background:rgba(0,0,0,0.1); padding-top:50px;  padding-bottom:50px; padding-right:40px}
</style>


### ![](https://forge.aeif.fr/framaka/visuel-forge/-/raw/main/avatars/avatar_Komit_face_cercle.png?ref_type=heads) B. Travailler en local<br> avec _git_ <!-- fit -->


---
<!-- _class:  -->

Travailler en local, c'est travailler hors ligne, sur une copie de son projet.

#### Intérêt :
1) Édition plus rapide
2) Gestion plus facile de l'historique des modifications
2) Compilation plus rapide


---
<!-- _class:  -->
<style scoped>
section{font-size:3.45em}
ol {text-align:left}
</style>

On va avoir besoin de :
1) _Git_ : un logiciel qui permet de gérer l'historique des modifications et la synchronisation avec le projet en ligne
2) _VS Code_ ou un autre éditeur de code
3) _Logiciels pour la compilation_ : pandoc, jekyll, mdbook, mkdocs …

<span data-marpit-fragment="1">Tout peut se faire ensuite dans _VS Code_.</span>

---
<!-- _class: fppp -->
<style scoped>
h4 {margin-bottom:0}
</style>
#### Un peu de vocabulaire de la forge

1) _stage_ : ajouter des modications pour préparer un commit
2) _commit_ : validation de modifications
3) _push_ : pousser les commits sur le projet en ligne (“_remote_”)
4) _fetch_ et _pull_ : récupérer les commits du projet en ligne et les intégrer à sa copie locale
5) _merge_ : fusionner les modifications du projet en ligne et de la copie locale

---
<!-- _class: pp -->
<style scoped>
section {display:flex; flex-direction:column; align-items:center;}
p {margin:0; }
img {height:150px; background:transparent!important; float:left; margin-right:30px; margin-left:0px}
h3 {width:95%; background:rgba(0,0,0,0.1); padding-top:50px;  padding-bottom:50px; padding-right:40px}
</style>


### ![](https://forge.aeif.fr/framaka/visuel-forge/-/raw/main/avatars/avatar_Komit_face_cercle.png?ref_type=heads) B. Travailler à plusieurs :<br> les bonnes pratiques <!-- fit -->


---
<!-- _class:  -->
1) Bien documenter ce que l'on fait
2) Diviser le travail en branches
3) Faire des commits