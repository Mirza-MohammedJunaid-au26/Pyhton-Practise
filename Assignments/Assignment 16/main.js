var user_box = document.getElementById("user-box");
var comp_box = document.getElementById("computer-box");
var user_img = document.createElement("img");
var comp_img = document.createElement("img");
var result = document.getElementById("result");

function rock(){
    user_box.append(user_img);
    user_img.classList.add("img");
    user_img.src = "./img/rock.png"
    inp = "rock"
    Computer(inp)
}

function paper(){
    user_box.append(user_img);
    user_img.classList.add("img");
    user_img.src = "./img/paper.png"
    inp = "paper"
    Computer(inp)
}

function scissor(){
    user_box.append(user_img);
    user_img.classList.add("img");
    user_img.src = "./img/scissor.png"
    inp = "scissor"
    Computer(inp)
}

function Computer(UserInp){

    var num = Math.floor((Math.random() * 3) + 1);
    
    if(num == 1){
        comp_box.append(comp_img);
        comp_img.classList.add("img");
        comp_img.src = "./img/rockk.png"
    }
    else if(num == 2){
        comp_box.append(comp_img);
        comp_img.classList.add("img");
        comp_img.src = "./img/paper.png"
    }
    else if(num == 3){
        comp_box.append(comp_img);
        comp_img.classList.add("img");
        comp_img.src = "./img/scissorr.png"
    }

    if(num == 1 && UserInp == "rock"){
        result.innerText = "!!! DRAW !!!"
    }
    else if(num == 1 && UserInp == "paper"){
        result.innerText = "!!! You Win !!!"
    }
    else if(num == 1 && UserInp == "scissor"){
        result.innerText = "!!! You Lose !!!"
    }
    else if(num == 2 && UserInp == "rock"){
        result.innerText = "!!! You Lose !!!"
    }
    else if(num == 2 && UserInp == "paper"){
        result.innerText = "!!! Draw !!!"
    }
    else if(num == 2 && UserInp == "scissor"){
        result.innerText = "!!! You Win !!!"
    }
    else if(num == 3 && UserInp == "rock"){
        result.innerText = "!!! You Win !!!"
    }
    else if(num == 3 && UserInp == "paper"){
        result.innerText = "!!! You Lose !!!"
    }
    else if(num == 3 && UserInp == "scissor"){
        result.innerText = "!!! Draw !!!"
    }


}   