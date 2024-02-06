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
<!-- _class: -->
<style scoped>
h2 {background:rgba(0,0,0,0.9); color:white; padding:60px 130px;}
</style>
## I - Qu'est-ce <br>qu'une forge ?<br> À quoi ça sert ? <!-- fit -->

![bg](https://forge.aeif.fr/framaka/visuel-forge/-/raw/main/brigit-et-komit/Brigit_et_Komit_avec_fond_forge_sans_logo.png?ref_type=heads)


---
<!-- _class:  -->
Une forge ressemble à première vue à un **espace de  stockage en ligne** de fichiers que l'on peut synchroniser avec son propre ordinateur pour garantir la pérennité des données

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
<!-- _class: fmm -->

Pour développer un logiciel, on a besoin de :
1) pouvoir organiser et répartir les tâches à faire grâce à des outils de **gestion de projet**
2) pouvoir **éditer** facilement le code, conserver un **historique des modifications** et pouvoir revenir en arrière en cas de problème
3) pouvoir lancer automatiquement des **scripts** qui vont tester / vérifier le code ou le compiler
4) s'il s'agit d'un logiciel en ligne, pouvoir facilement le **déployer sur le web**
5) pouvoir créer de la **documentation** facilement
6) pouvoir récupérer le **feedback des utilisateurs** et **collaborer** avec d'autres développeurs pour corriger les bugs et ajouter des fonctionnalités


---
<!-- _class: fpppppp -->
&rArr; Un premier intérêt de la _Forge des Communs Numériques Éducatifs_ :  <span data-marpit-fragment="1">des logiciels éducatifs faits par des enseignants pour les enseignants</span>

#### <span data-marpit-fragment="2">Quelques exemples :</span>
1) [Emmanuel Zimmert : La Digitale](https://forge.aeif.fr/users/ladigitale/projects)
2) [Laurent Abbal](https://laurentabbal.forge.apps.education.fr/)
3) [Arnaud Champollion](https://achampollion.forge.aeif.fr/)
4) [Mes outils](https://eyssette.forge.aeif.fr/)

---
<!-- _class: pp -->
<style scoped>
section {display:flex; flex-direction:column; align-items:center;}
p {margin:0; }
img {height:150px; background:transparent!important; float:left; margin-right:30px; margin-left:0px}
h3 {width:95%; background:rgba(0,0,0,0.1); padding-top:50px;  padding-bottom:50px; padding-right:40px}
</style>


### ![](https://forge.aeif.fr/framaka/visuel-forge/-/raw/main/avatars/avatar_Komit_face_cercle.png?ref_type=heads) B. Un outil plus large :<br>des détournements<br> possibles !<!-- fit -->

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
<!-- _class: pp -->
<style scoped>
section {display:flex; flex-direction:column; align-items:center;}
p {margin:0; }
img {height:150px; background:transparent!important; float:left; margin-right:30px; margin-left:0px}
h3 {width:95%; background:rgba(0,0,0,0.1); padding-top:50px;  padding-bottom:50px; padding-right:40px}
</style>


### ![](https://forge.aeif.fr/framaka/visuel-forge/-/raw/main/avatars/avatar_Komit_face_cercle.png?ref_type=heads) B. Travailler en local<br> avec _git_ <!-- fit -->


---
<!-- _class: pp -->
<style scoped>
section {display:flex; flex-direction:column; align-items:center;}
p {margin:0; }
img {height:150px; background:transparent!important; float:left; margin-right:30px; margin-left:0px}
h3 {width:95%; background:rgba(0,0,0,0.1); padding-top:50px;  padding-bottom:50px; padding-right:40px}
</style>


### ![](https://forge.aeif.fr/framaka/visuel-forge/-/raw/main/avatars/avatar_Komit_face_cercle.png?ref_type=heads) B. Travailler à plusieurs<br> avec les branches <!-- fit -->