var button = document.getElementById('button')
var dbutton = document.getElementById('dbutton')
var input = document.getElementById('input')
var list = document.getElementById('list')

button.addEventListener('click', Addlist)
dbutton.addEventListener('click', Dellist)

function Addlist(){
    var makelist = document.createElement('li')
    makelist.innerHTML = input.value
    list.appendChild(makelist)
    input.value=' '
}

function Dellist() {
    input.value=''
}

function getKeywords() {
    
}