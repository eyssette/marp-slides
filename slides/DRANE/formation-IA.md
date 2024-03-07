---
marp: true
theme: teaching
paginate: true
size: 4:3
---

<!-- _class: titre -->

# L'Intelligence artificielle : définitions et défis

Cédric Eyssette - chargé de projet
DRANE site de Lyon



---
<!-- _class:  -->
<style scoped>
section {font-size:6em;}
* {text-align:center}
</style>

### Plan

I - Quelques repères<br> fondamentaux

<span data-marpit-fragment="1">II - Côté profs</span>

<span data-marpit-fragment="2">III - Côté élèves</span>


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
### 1/ De l'IA symbolique et déductive à l'IA statistique, inductive <br>et connexioniste

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

1) Premier principe : les embeddings ou vecteurs de mots
2) Deuxième principe : la prédiction de tokens
3) Prompts / RAG / Fine-tuning



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

![](https://eyssette.forge.aeif.fr/mindmap/lignes-directrices-IA-considerations-ethiques.svg)

---
<!-- _class:  -->

Une thèse très contestable : la neutralité de la technique

1) L'autonomie de la technique
2) Le déterminisme technique
3) La normativité de la technique : <span data-marpit-fragment="1">l'IA hérite de certaines normes</span> <span data-marpit-fragment="2">, elle ne respecte pas certaines normes</span><span data-marpit-fragment="3">, elle introduit de nouvelles normes</span>

<!-- 



changements :
structure du travail

sexisme / racisme
droit d'auteur / normes écologiques


-->

<!--

Adaptée de Anna Jobin, Marcello Ienca et Effy Vatena, « The Global Landscape of AI Ethics Guidelines », Nature Machine Intelligence, vol. 1, 2019, p. 389-399.

La transparence, qui correspond à la première moitié du cinquième principe général dont il vient d’être question : un SAI auquel une personne recourt ou est soumise doit être transparent pour cette personne — elle doit être en état de comprendre ses mécanismes fondamentaux, les motivations, intérêts et engagements des organismes qui l’ont conçu, diffusé, ou déployé, et les raisons de ses décisions particulières et le cas échéant avoir le droit et les moyens concrets de les contester.
La justice et l’équité : d’une part les bénéfices de l’intelligence artificielle doivent être répartis de manière équitable ; en particulier, l’intelligence artificielle doit éviter les biais et toute forme de discrimination, délibérée ou involontaire ; elle doit être accessible à tous ; d’autre part l’intelligence artificielle doit servir à remédier aux inégalités et injustices existantes ; elle doit contribuer à resserrer la solidarité entre personnes et communautés.
L’innocuité (non-malfaisance) : l’intelligence artificielle ne doit mettre en péril d’aucune façon les personnes, leurs biens, leurs droits ; elle doit s’entourer de toutes les précautions possibles pour éviter d’infliger des dommages matériels ou moraux aux personnes et aux collectivités (par exemple de favoriser la prolifération de nouvelles et d’informations mensongères ou d’encourager l’hostilité à l’égard de certains groupes ; ou encore d’engager une course aux armements en matière militaire et de cybersécurité, etc.).
La responsabilité : tout déploiement d’un SAI doit engager la responsabilité pleine et entière des personnes et organismes impliqués dans la conception, la diffusion et le déploiement du système, en particulier en cas de mauvais fonctionnement ou de conséquence adverse imprévue.
La protection de la vie privée (privacy), tout particulièrement la maîtrise des données personnelles, le droit de savoir qui en détient certaines et ce qui en est fait et celui de les retirer de toute banque de données hormis celles autorisées par la loi.
Le progrès (bienfaisance) : l’intelligence artificielle ne doit être employée que lorsqu’elle apporte une amélioration aux conditions d’existence des personnes et des collectivités.
L’autonomie et la dignité : chacun doit être libre de recourir ou non à un SAI, de lui déléguer certaines décisions et de reprendre à tout moment cette délégation ; l’intelligence artificielle doit contribuer à protéger la liberté et les droits des personnes et à étendre leurs capabilités, les moyens d’agir dont ils disposent concrètement ; elle ne doit en aucune façon, directement ou indirectement, porter atteinte à leur dignité ; elle doit respecter leurs valeurs particulières, sachant que certaines ne sont pas universellement partagées — en d’autres termes, elle se doit d’inclure une diversité de cultures et de systèmes normatifs, formalisés ou non.
Le respect des obligations générales vis-à-vis des populations et de l’environnement : le développement de l’intelligence artificielle (par opposition à son déploiement) ne doit pas avoir de conséquences délétères pour certaines catégories de personnes (employés, prestataires, mais aussi résidents des communes sièges d’entreprises d’IA) ni pour la planète, notamment en matière de consommation énergétique.

-->

---
<!-- _class: partie -->
# II - <br>Côté profs <br>[:link:](https://eyssette.forge.aeif.fr/markpage/#https://github.com/eyssette/minisite-markpage/blob/main/concevoir-ressources-avec-IA.md)
<!-- fit -->
Deuxième partie

---


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
![](https://raw.githubusercontent.com/eyssette/minisite-markpage/main/img/creer-ressource-avec-IAG.png)


---
<!-- _class: souspartie -->
## B. <br>Adapter / changer le <br>format d'une ressource <!-- fit -->


---
<!-- _class: i1t1 vertical -->
![](https://raw.githubusercontent.com/eyssette/minisite-markpage/main/img/adapter-changer-format-ressource-avec-IAG.png)

---
<!-- _class: souspartie -->
## C. <br>Évaluer / améliorer<br> une ressource <!-- fit -->


---
<!-- _class: i1t1 vertical -->
![](https://raw.githubusercontent.com/eyssette/minisite-markpage/main/img/evaluer-ameliorer-ressource-avec-IA.png)


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

<!-- 
PhiloGPT : vidéo
MIA seconde : Projet gouvernemental (Modules Interactifs Adaptatifs)
Chatbot

répétition espacée : Anki
-->

---
<!-- _class: souspartie -->
## B. L'IA comme objet de réflexion


---
<!-- _class:  -->
1) Approche EMI & EMC
2) Approche philosophique et littéraire
