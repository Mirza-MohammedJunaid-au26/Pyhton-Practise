var colorBox = document.getElementById("color-box");

function generateRandomColor() {
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}

function storeColor(){

    var colorArr = []

    for(var i = 0;i<5;i++){
        var randomColor=generateRandomColor();
        colorArr.push(randomColor);
    }
    return colorArr
}
  
function giveColor(){

    colorBox.innerHTML = " "

    var ColorArr=storeColor();

    ColorArr.forEach((item) => {
        let div = document.createElement("div");
        let p = document.createElement("p");
        div.classList.add("box")
        div.style.background = item;
        p.classList.add("color-name")
        p.innerText = item;
        colorBox.appendChild(div);
        div.appendChild(p);
    });


}

