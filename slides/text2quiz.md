---
marp: true
theme: teaching
paginate: true
size: 4:3
---
<style>
  .cross {
    position: relative;
    display: inline-block;
  }
  .cross::before {
    border-bottom: 8px solid #9e0e0e;
    -webkit-transform: skewY(-40deg);
    transform: skewY(-40deg);
}
  .cross::after {
    border-bottom: 8px solid #9e0e0e;
    -webkit-transform: skewY(40deg);
    transform: skewY(40deg);
}
.cross::before, .cross::after {
    content: '';
    width: 100%;
    position: absolute;
    right: 0;
    top: 42%;
}
</style>


<!-- _class: titre -->
<style scoped>
/* h1 {margin-top:-2.6em!important}
ol {width:800px!important; position:absolute; top:270px; text-align:center; list-style-type:none; font-weight:600; margin:0} */
h1 {margin-top:-0.6em!important}
ol {list-style-type:none; font-weight:600; font-size:1.7em; text-align:left}
ol li {position:absolute; width:400px}
ol li:nth-of-type(1) {top:50px; left:220px;}
ol li img {height:100px}
ol li:nth-of-type(2) {top:30px; left:600px}
ol li:nth-of-type(3) {top:320px; left:200px}
ol li:nth-of-type(4) {top:350px; left:500px}
</style>
# Text2quiz <!-- fit -->
Cédric Eyssette
cedric.eyssette@ac-lyon.fr

<!-- 1) Un outil libre et gratuit en ligne
2) Sans création de compte, sans données personnelles enregistrées -->

1) ![](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Git_icon.svg/194px-Git_icon.svg.png)
2) <span class="cross">💰</span>  <!-- gratuit -->
3) <span class="cross">👤</span> <!-- pas de compte -->
4) <span class="cross">🍪</span> <!-- Pas de cookie -->

---
<!-- _class:  -->
<style scoped>
p{margin-bottom:0.5em}
.details {margin-left:1em; display:inline-block;}
.details span {font-size:0.72em}
</style>

**13 types de questions**<br><span data-marpit-fragment="1" class="details">Vrai&#8239;/&#8239;faux, QCM, Texte à trous, Flashcard, Remise en ordre, Étiquettes à positionner ...</span>

<span data-marpit-fragment="2">**Plusieurs modes de partage**</span><br><span data-marpit-fragment="3" class="details">Entre collègues</span><span data-marpit-fragment="4" class="details">Pour les élèves <span>(autoévaluation ou évaluation)</span></span>

<span data-marpit-fragment="5">**Des usages plus avancés**<br><span class="details">Latex, Markdown, HTML</span></span>

---
<!-- _class: -->
<style>
strong{color: rgba(14, 23, 107,92%);
    font-weight:600;}
pre {margin:30px 60px!important; font-size:0.72em}
</style>

**Le principe** : un simple fichier texte avec une syntaxe simple à apprendre.

<pre data-marpit-fragment="1">
VF || Énoncé || V
Trous || Texte avec des {{V:trous|trou}}
Flashcard || Recto || Verso
</pre>

<span data-marpit-fragment="2">On peut mettre ce fichier texte sur une forge.</span>

<span data-marpit-fragment="3">Text2quiz transforme automatiquement le texte en un quiz : [exemple](https://text2quiz.vercel.app/?v=1.0#VF%20%7C%7C%20%C3%89nonc%C3%A9%20%7C%7C%20V%0ATrous%20%7C%7C%20Texte%20avec%20des%20%7B%7BV:trous%7Ctrou%7D%7D%0AFlashcard%20%7C%7C%20Recto%20%7C%7C%20Verso).</span>