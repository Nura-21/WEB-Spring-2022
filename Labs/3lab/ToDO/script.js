let list = document.querySelector('.list');
let input = document.querySelector('.box');

function remove(){
    this.parentNode.remove();
}

function addTask(){
    if(input.value != ""){
        let div = document.createElement("div");
        div.className="task";

        let task = document.createElement("div");
        task.className = "new";

        let check = document.createElement("input");
        check.type = "checkbox";
        check.className = "checkbox";

        let p = document.createElement("p");
        p.innerHTML = input.value;

        let image = document.createElement("img");
        image.className = "delete-img";
        image.src = "delete.png";
        
        task.appendChild(check);
        task.appendChild(p);
        div.appendChild(task);
        div.appendChild(image);
        list.appendChild(div);

        image.addEventListener('click', remove);
        input.value = "";
    }else{
        alert("Please write a name of task.")
    }
}

