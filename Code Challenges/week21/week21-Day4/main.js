var inp1 = document.getElementById("Input-1");
var inp2 = document.getElementById("Input-2");
var ansSec = document.getElementById("ans-section");

function sum(){
    let inp1_val = + inp1.value; 
    let inp2_val = + inp2.value;
    let ans = inp1_val+inp2_val
    let ans_head = document.createElement("h1");
    ans_head.innerText = "Addition is : " + ans;
    ansSec.append(ans_head);
}