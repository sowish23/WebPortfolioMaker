function add_div(){
    var div = document.createElement('div');
    div.className = 'projects-list';
    div.innerHTML = document.getElementById('projects-list').innerHTML;
    document.getElementById('projects-box').appendChild(div);
}



function remove_div(obj){
    document.getElementById('field').removeChild(obj.parentNode);
}