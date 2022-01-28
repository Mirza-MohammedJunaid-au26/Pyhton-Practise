var inp = document.getElementById("Inp");
var ans = document.getElementById("ansSection");
function getVal(){
    var val = inp.value;

    for(let i=0;i<val.length;i++){

        if(val.includes("#")){   

            let idx = val.indexOf("#");
            console.log("idx : "+idx);
            let valAt = val[idx];
            let prevIdx = val[idx-1]
            let newVar = prevIdx+valAt
            val = val.replace(newVar,"")
            console.log(val);
        }
        else{
            break;
        }
    }

    ans.innerHTML = val;
}

