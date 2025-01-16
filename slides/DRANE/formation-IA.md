---
marp: true
theme: teaching
paginate: true
size: 4:3
---

<!-- _class: titre -->
<style scoped>
span {font-size:0.7em; display:block; margin-top:-10px}
</style>
# L'intelligence <br>artificielle :<br> <span>définitions et défis</span> <!-- fit -->

Cédric Eyssette - chargé de projet
DRANE site de Lyon



---
<!-- _class:  -->
<style scoped>
section {font-size:4em;}
</style>

### Plan

<span data-marpit-fragment="1">I - Quelques repères fondamentaux</span>

<span data-marpit-fragment="2">II - Côté profs</span>

<span data-marpit-fragment="3">III - Côté élèves</span>


---
<!-- _class: partie -->
# I - <br>Quelques repères <br>fondamentaux <!-- fit -->
Première partie


---
<!-- _class: souspartie -->
## A. <br>Une question philosophique :<br> la nature de l'intelligence <!-- fit -->


---
<!-- _class: i1t1 vertical -->

L'intelligence est-elle <br>le propre de l'être humain ?

![](https://www.musee-rodin.fr/sites/default/files/styles/scale_w1000_h500/public/2020-12/2017_05_23_penseur_jm016_1.jpg?itok=QxHLnDgd)

<!-- 
Question sur soi, sur sa propre pensée
remise en question

intelligence => Logos
Noûs
(matière / esprit ; ce qui nous rapproche de la divinité)

propre de l'être humain

raisonner (rapport à soi)
juger, décider (rapport au monde)
discuter (rapport aux autres)


-->

---
<!-- _class: i1t1 vertical-->
Le canard de Vaucanson (XVIII<sup>e</sup>)

![](https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/Ure%27s_rendering_of_Maillard%27s_automaton.jpg/800px-Ure%27s_rendering_of_Maillard%27s_automaton.jpg)


<!-- 
Question de la mécanisation de l'intelligence
 -->

---
<!-- _class: i2t0 -->

![](https://upload.wikimedia.org/wikipedia/commons/a/a3/Julien_Offray_de_La_Mettrie.jpg?uselang=fr)

![](https://www.edition-originale.com/media/h-3000-la-mettrie_lhomme-machine_1948_tirage-de-tete_0_24935.JPG)

<!-- automate spirituel
Homme-machine -->

---
<!-- _class: i1t1 vertical -->

L'automate joueur d'échecs (XVIII<sup>e</sup>)

![](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Racknitz_-_The_Turk_3.jpg/800px-Racknitz_-_The_Turk_3.jpg)

<!-- 
Le Turc mécanique ou l’automate joueur d'échecs est une célèbre mystification construite à la fin du xviiie siècle : il s’agissait d'un prétendu automate doté de la faculté de jouer aux échecs. I

Construit et dévoilé pour la première fois en 1770 par Johann Wolfgang von Kempelen, le mécanisme semblait capable de jouer contre un adversaire humain, ainsi que de résoudre le problème du cavalier, un casse-tête qui exige de déplacer un cavalier afin d'occuper une seule fois chaque case de l'échiquier
 -->


---
<!-- _class: i1t1 vertical -->
La machine de Turing

![](https://openclipart.org/image/800px/339637)

---
<!-- _class: i1t1 vertical -->
Le test de Turing

![](https://upload.wikimedia.org/wikipedia/commons/5/55/Turing_test_diagram.png)


---
<!-- _class: i1t1 vertical -->

Une expérience de pensée de Searle :<br> la chambre chinoise

[![](https://i.ibb.co/Njjxs77/chambre-Chinoise.png)](https://ladigitale.dev/digiview/#/v/65e952a4e0607)


---
<!-- _class: citationC fmmmmmmm-->
<style scoped>
figure {margin-right:-220px!important}
</style>

![bg left:20% ](https://web.static-rmg.be/if/c_fit,w_1200,h_1200/0d5ae89fcb900dc10d0d6a4fe76f6a07.jpg)

> « Même privée de compréhension, l’intelligence artificielle peut encore viser à reproduire la structure de l’intelligence humaine […] Non seulement elle le peut mais elle le doit — telle est du moins l’opinion de Simon et Newell et de bien d’autres chercheurs en IA de la première époque, pour qui, dans les termes de l’un d’eux, Roger Schank, « l’étude de l’intelligence artificielle n’est rien d’autre que l’étude de l’intelligence humaine ». […] Cette perspective est très tôt contestée par Minsky. Il veut affranchir l’IA de la contrainte de ce qu’il appelle l’équivalence forte — cet isomorphisme entre le chemin suivi par l’intelligence artificielle et l’intelligence humaine accomplissant la même tâche. Il estime qu’en l’état présent des sciences cognitives se jumeler avec elles ralentit l’IA dans sa progression. Elle a donc tout avantage à se limiter à une équivalence faible, qui se borne à imposer que l’intelligence artificielle aboutisse aux mêmes résultats que l’intelligence humaine attelée à la même tâche […] McCarthy est plus radical encore, et préconise d’oublier l’intelligence humaine et de ne s’occuper que de faire résoudre certains problèmes automatiquement par les ordinateurs. »
>> Daniel **Andler**, _Intelligence artificielle, intelligence humaine : la double énigme_

<!-- 
Intelligence :
capacité à résoudre des problèmes

IA étroite / IA générale
IA faible / IA forte

rapport au corps : cognition incarnée
-->



---
<!-- _class: souspartie -->
## B. Une question technique<br> et scientifique : l'IA, <br>comment ça fonctionne ?<!-- fit -->


---
<!-- _class: etape -->
### 1/ De l'IA symbolique <br>à l'IA connexioniste


---
<!-- _class:  -->
<style scoped>
p:nth-of-type(2) {margin-top:0.5em}
</style>

Premiers modèles d'IA : IA symbolique et déductive.
<span data-marpit-fragment="1">&rarr; les systèmes experts (exemple : l'ordinateur Watson conçu pour gagner au jeu Jeopardy)</span>

<span data-marpit-fragment="2">Changement de paradigme : l'IA devient statistique, inductive et connexioniste</span>
<span data-marpit-fragment="3">&rarr; AlphaGo puis AlphaGo Zero</span>

---
<!-- _class: etape -->
### 2/ IA / Machine learning / <br>Deep learning

---
<!-- _class: pp -->
<style scoped>
ol {list-style-type:none!important; margin-left:80px}
ol li {
  width: 700px;
  height: 700px;
  line-height: 120px;
  border-radius: 50%;
  font-size: 50px;
  color: white;
  font-weight: bold;
  text-align: center;
}
ol li {position:absolute; top:10px}
ol li:nth-of-type(1) {background-color: #020024}
ol li:nth-of-type(2) {background-color: #14145e; width:400px; height:400px; margin:150px; line-height: 150px; font-size:0.7em}
ol li:nth-of-type(3) {background-color: #8786c6; width:200px; height:200px; margin:250px; line-height: 210px; font-size:0.5em}
</style>

1) IA
2) Machine learning
3) Deep learning


---
<!-- _class: i1t1 vertical -->
<style scoped>
p {font-size:0.8em}
</style>

![](https://cdn.masto.host/scholarsocial/media_attachments/files/110/650/356/011/527/319/original/36d79dce16f1ac3c.png)

Cours de [Chloé-Agathe Azencott](https://cazencott.info/dotclear/public/lectures/2021-05-cours-Azencott.pdf)


---
<!-- _class: etape -->
### 3/ Les IA génératives


---
<!-- _class:  -->

1) Premier principe : les _embeddings_ ou vecteurs de mots
2) Deuxième principe : la prédiction de _tokens_
3) _Prompts_ / _RAG_ / _Fine-tuning_



<!-- 

IA générative
prédiction / vérité
prompt


IA symbolique / fonctionnalisme /représentationalisme
connexionisme ; réseaux de neurones




Deep Learning
empirisme pur
contredit à une exigence du rationalisme : exigence d'explicabilité

déduction / induction

prompt / RAG / fine-tuning

-->


---
<!-- _class: souspartie -->
## C. Des questions <br>éthiques, sociales,<br>juridiques et politiques <!-- fit -->


---
<!-- _class: i1t1 vertical -->
Lignes directrices éthiques sur l’utilisation de l’intelligence artificielle [:link:](https://drane.ac-lyon.fr/spip/Lignes-directrices-ethiques-utilisation-IA)

[![](https://i.ibb.co/SvH1Y99/lignes-directrices-IA-considerations-ethiques.png)](https://mymarkmap.netlify.app/#https://raw.githubusercontent.com/eyssette/mindmap/main/lignes-directrices-IA-considerations-ethiques.md)

---
<!-- _class:  -->

Une thèse très contestable : la neutralité de la technique.

<span data-marpit-fragment="1">Trois objections possibles :</span>

1) L'autonomie de la technique
2) Le déterminisme technique
3) La normativité de la technique

<!-- 



changements :
structure du travail

sexisme / racisme
droit d'auteur / normes écologiques
-->

---
<!-- _class: partie -->
# II - <br>Côté profs <br>[:link:](https://eyssette.forge.apps.education.fr/markpage/#https://github.com/eyssette/minisite-markpage/blob/main/concevoir-ressources-avec-IA.md)
<!-- fit -->
Deuxième partie

---
<!-- _class: i1t1 vertical -->
Trois gestes professionnels

![](https://raw.githubusercontent.com/eyssette/minisite-markpage/main/img/trois-gestes-professionnels.png)

---
<!-- _class: i1t1 vertical -->
Trois usages possibles

![](https://raw.githubusercontent.com/eyssette/minisite-markpage/main/img/trois-usages-IA.png)

---
<!-- _class: souspartie -->
## A. <br>Créer une ressource <!-- fit -->

---
<!-- _class: i1t1 vertical -->
[![](https://raw.githubusercontent.com/eyssette/minisite-markpage/main/img/creer-ressource-avec-IAG.png)](https://eyssette.forge.apps.education.fr/markpage/?sec=1&subsec=1#https://github.com/eyssette/minisite-markpage/blob/main/concevoir-ressources-avec-IA.md)


---
<!-- _class: souspartie -->
## B. <br>Adapter / changer le <br>format d'une ressource <!-- fit -->


---
<!-- _class: i1t1 vertical -->
[![](https://raw.githubusercontent.com/eyssette/minisite-markpage/main/img/adapter-changer-format-ressource-avec-IAG.png)](https://eyssette.forge.apps.education.fr/markpage/?sec=2&subsec=1#https://github.com/eyssette/minisite-markpage/blob/main/concevoir-ressources-avec-IA.md)

---
<!-- _class: souspartie -->
## C. <br>Évaluer / améliorer<br> une ressource <!-- fit -->


---
<!-- _class: i1t1 vertical -->
[![](https://raw.githubusercontent.com/eyssette/minisite-markpage/main/img/evaluer-ameliorer-ressource-avec-IA.png)](https://eyssette.forge.apps.education.fr/markpage/?sec=3&subsec=1#https://github.com/eyssette/minisite-markpage/blob/main/concevoir-ressources-avec-IA.md)


---
<!-- _class: partie -->
# III - <br>Côté élèves <!-- fit -->
Troisième partie

---
<!-- _class: souspartie -->
## A.  L'IA comme outil


---
<!-- _class:  -->
- Un outil d'aide pour apprendre et réviser
- Un tuteur personnel
- Les _learning analytics_

<span data-marpit-fragment="1">Exemples : [MIA Seconde](https://www.ac-paris.fr/mia-seconde-un-service-numerique-de-remediation-en-francais-et-en-mathematiques-131013)</span><span data-marpit-fragment="2">, PhiloGPT</span>

<span data-marpit-fragment="3">Un outil pour créer son propre chatbot (sans les hallucinations possibles d'une IA générative) : [ChatMD](https://eyssette.github.io/chatMD)</span>

<!-- 
PhiloGPT : vidéo
MIA seconde : Projet gouvernemental (Modules Interactifs Adaptatifs)
répétition espacée : Anki
-->

---
<!-- _class: souspartie -->
## B. L'IA comme objet de réflexion


---
<!-- _class:  -->
1) Approche EMI & EMC
2) Approche philosophique et littéraire


---
<!-- _class: fppppppp -->
### Pour approfondir

Un parcours de formation sur Magistère :

["Trajectoires IA" en AURA : accompagner l'intégration des IA en éducation](https://magistere.education.fr/ac-clermont/course/view.php?id=4683&section=1)

N'hésitez pas à me contacter pour toute question ou précision !