const book = document.getElementById("book");
const buisness = document.getElementById("buisness");
const buisnessS = document.getElementById("buisnessShow");
const bookS = document.getElementById("bookShow");




function bookShow (){
    buisnessS.style.display = "none";
    bookS.style.display = "initial";
}

function buisnessShow (){
    buisnessS.style.display = "initial";
    bookS.style.display = "none";
}


book.addEventListener('click', bookShow);
buisness.addEventListener('click', buisnessShow);