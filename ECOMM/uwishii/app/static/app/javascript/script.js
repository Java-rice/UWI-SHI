
const nav = document.querySelector('.navbar');


/**if(bar){
    bar.addEventListener('click',()=>{
        nav.classList.add('active');
    })
}

if(close){
    close.addEventListener('click',()=>{
        nav.classList.remove('active');
    })
}*/

document.querySelector('#menu-btn').onclick =()=>{
    nav.classList.toggle('active');
}