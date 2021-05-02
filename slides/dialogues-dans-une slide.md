---
marp: true
theme: teaching
paginate: true
size: 4:3
---

<!-- _class: titre -->

# Dialogues dans un slide
Quelques essais

<style>
section.dialogue ul {
background-color:white;
list-style-type:none;
padding:initial;
margin-left:40px;
margin-right:40px;
overflow-Y:scroll;
margin-top:20px;
max-height:700px;
padding-bottom:50px;
}
section.dialogue ul li:before{
	content:""!important;
	margin:0;
}

section.dialogue ul li {
	margin-top:1em;
    border-radius: 20px 20px 20px 20px;
    -moz-border-radius: 20px 20px 20px 20px;
    -webkit-border-radius: 20px 20px 20px 20px;
    padding: 20px 20px;
    max-width: 600px;
	display: table;
    line-height: 1.25em;
    position: relative;
    overflow-wrap: break-word;
    border-radius: 20px 20px 20px 20px;
    -moz-border-radius: 20px 20px 20px 20px;
    -webkit-border-radius: 20px 20px 20px 20px;
}

section.dialogue ul li:nth-of-type(2n+1) {	
	background: #e5e5ea;
	text-shadow: 1px 1px 0 #f3f3f4;
	margin-left:80px;
	margin-right:auto;
}

section.dialogue ul li:nth-of-type(2n) {	
	color: #fff;
	text-shadow: 1px 1px 0 #1b96fc;
	background-color: #39a1f9;
	margin-left: auto; 
	margin-right: 80px;
}

section.dialogue ul li:nth-of-type(2n+1):before{
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

section.dialogue ul li:nth-of-type(2n+1):after{
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

section.dialogue ul li:nth-of-type(2n):before{
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

section.dialogue ul li:nth-of-type(2n):after{
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

---
<!-- _class: fmm dialogue pp -->

* Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc id vehicula dolor. 
* Lorem ipsum dolor sit amet.
* Lorem ipsum dolor sit amet
* Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc id vehicula dolor. 
* Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc id vehicula dolor. 
* Lorem ipsum dolor sit amet.
* Lorem ipsum dolor sit amet
* Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc id vehicula dolor. 
