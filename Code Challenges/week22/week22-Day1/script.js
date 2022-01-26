var Inp = document.getElementById("Inp");
var disp = document.getElementById("queueDisplay");

var queueArr = []

function enqueue(){
    var inpVal = Inp.value;
    console.log(inpVal);
    queueArr.push(inpVal);
    Inp.value = ""
    disp.innerHTML = "";
    showQueue()
    console.log(queueArr);
}

function dequeue(){
    queueArr.shift()
    disp.innerHTML = "";
    showQueue()
    console.log(queueArr);
}

function showQueue(){
    queueArr.forEach((item) => {
        let li = document.createElement("li");
        li.innerText = item;
        li.classList.add("arr-item")
        disp.appendChild(li);
    });
}

// class Queue {
//     constructor() {
//         this.items = [];
//     }
    
//     enqueue(element) {
//         return this.items.push(element);
//     }
    
//     dequeue() {
//         if(this.items.length > 0) {
//             return this.items.shift();
//         }
//     }
    

// }

// let queue = new Queue();
// queue.enqueue(1);
// queue.enqueue(2);
// queue.enqueue(4);
// queue.enqueue(8);
// console.log(queue.items);

// queue.dequeue();