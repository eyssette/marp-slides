---
marp: true
theme: teaching
paginate: true
size: 4:3
---

<!-- _class: titre -->

# Dialogues dans un slide
Quelques essais

---
<!-- _class:  -->
<style scoped>
.dialogue ul {
background-color:white;
list-style-type:none;
padding:initial;
}
.dialogue ul li:before{
	content:""!important;
}
.dialogue ul li {	
    background: #e5e5ea;
    margin-left: 24px;
    text-shadow: 1px 1px 0 #f3f3f4;
    border-radius: 20px 20px 20px 10px;
    -moz-border-radius: 20px 20px 20px 10px;
    -webkit-border-radius: 20px 20px 20px 10px;
    display: inline-block;
    padding: 12px 18px;
    max-width: 270px;
    min-height: 26px;
    min-width: 14px;
    font-size: 24px;
    line-height: 26px;
    position: relative;
    overflow-wrap: break-word;
    border-radius: 20px 20px 10px 20px;
    -moz-border-radius: 20px 20px 10px 20px;
    -webkit-border-radius: 20px 20px 10px 20px;
}

.dialogue ul ul li{
	color: #fff;
	text-shadow: 1px 1px 0 #1b96fc;
	background-color: #39a1f9;;
}

.dialogue ul li:before{
content: "";
  position: absolute;
  z-index: 0;
  bottom: 0;
  left: -7px;
  height: 20px;
  width: 20px;
  background: #eee;
  border-bottom-right-radius: 15px;
}

</style>

<div class="dialogue">

- Mais que penses-tu de cela ?
	- Je ne sais pas, et toi ?
	- Tu as 
</div>


---
<!-- _class: fpppppp -->
<style scoped>
.dialogue p {
	margin-top:1em;	
    margin-left: 24px;
    border-radius: 20px 20px 20px 20px;
    -moz-border-radius: 20px 20px 20px 20px;
    -webkit-border-radius: 20px 20px 20px 20px;
    padding: 20px 20px;
    max-width: 600px;
	display: table;
    line-height: 1em;
    position: relative;
    overflow-wrap: break-word;
    border-radius: 20px 20px 20px 20px;
    -moz-border-radius: 20px 20px 20px 20px;
    -webkit-border-radius: 20px 20px 20px 20px;
}

.dialogue p:nth-of-type(2n+1) {	
	background: #e5e5ea;
	text-shadow: 1px 1px 0 #f3f3f4;
	margin-left:100px;
	margin-right:auto;
}

.dialogue p:nth-of-type(2n) {	
	color: #fff;
	text-shadow: 1px 1px 0 #1b96fc;
	background-color: #39a1f9;
	margin-left: auto; 
	margin-right: 100px;
}

p:nth-of-type(2n+1):before{
content: "";
    position: absolute;
    z-index: 0;
    bottom: 0;
    left: -20px;
    height: 40px;
    width: 40px;
    background: #e5e5ea;
    border-bottom-right-radius: 30px;
}

p:nth-of-type(2n+1):after{
    content: "";
    position: absolute;
    z-index: 1;
    bottom: 0;
    left: -20px;
    width: 20px;
    height: 40px;
    background: white;
    border-bottom-right-radius: 30px;
}



p:nth-of-type(2n):before{
  content: "";
  position: absolute;
  z-index: 0;
  bottom: 0;
  right: -20px;
  height: 40px;
  width: 40px;
  background: #39a1f9;
  background-attachment: fixed;
  border-bottom-left-radius: 30px;
}

p:nth-of-type(2n):after{
  content: "";
  position: absolute;
  z-index: 1;
  bottom: 0;
  right: -21px;
  width: 21px;
  height: 41px;
  background: white;
  border-bottom-left-radius: 30px;
}


</style>

<div class="dialogue">

Mais que penses-tu de cela ?

Je ne sais pas, et toi ? Qu'en penses-tu ?

Rien, c'est fou !
</div>


---
<!-- _class: fpppppp -->
<style scoped>
.dialogue ul {
background-color:white;
list-style-type:none;
padding:initial;
margin-left:40px;
margin-right:40px;
}
.dialogue ul li:before{
	content:""!important;
	margin:0;
}

.dialogue ul li {
	margin-top:1em;	
    border-radius: 20px 20px 20px 20px;
    -moz-border-radius: 20px 20px 20px 20px;
    -webkit-border-radius: 20px 20px 20px 20px;
    padding: 20px 20px;
    max-width: 600px;
	display: table;
    line-height: 1em;
    position: relative;
    overflow-wrap: break-word;
    border-radius: 20px 20px 20px 20px;
    -moz-border-radius: 20px 20px 20px 20px;
    -webkit-border-radius: 20px 20px 20px 20px;
}

.dialogue ul li:nth-of-type(2n+1) {	
	background: #e5e5ea;
	text-shadow: 1px 1px 0 #f3f3f4;
	margin-left:80px;
	margin-right:auto;
}

.dialogue ul li:nth-of-type(2n) {	
	color: #fff;
	text-shadow: 1px 1px 0 #1b96fc;
	background-color: #39a1f9;
	margin-left: auto; 
	margin-right: 80px;
}

.dialogue ul li:nth-of-type(2n+1):before{
content: "";
    position: absolute;
    z-index: 0;
    bottom: 0;
    left: -20px;
    height: 40px;
    width: 40px;
    background: #e5e5ea;
    border-bottom-right-radius: 30px;
}

.dialogue ul li:nth-of-type(2n+1):after{
    content: "";
    position: absolute;
    z-index: 1;
    bottom: 0;
    left: -20px;
    width: 20px;
    height: 40px;
    background: white;
    border-bottom-right-radius: 30px;
}



.dialogue ul li:nth-of-type(2n):before{
  content: "";
  position: absolute;
  z-index: 0;
  bottom: 0;
  right: -20px;
  height: 40px;
  width: 40px;
  background: #39a1f9;
  background-attachment: fixed;
  border-bottom-left-radius: 30px;
}

.dialogue ul li:nth-of-type(2n):after{
  content: "";
  position: absolute;
  z-index: 1;
  bottom: 0;
  right: -21px;
  width: 21px;
  height: 41px;
  background: white;
  border-bottom-left-radius: 30px;
}


</style>

<div class="dialogue">

* Mais que penses-tu de cela ?
* Je ne sais pas, et toi ? Qu'en penses-tu ?
* Rien, c'est fou !
* C'est tellement incroyable !
</div>