// 
var form = document.querySelector('.submit-form');
function appear(){
    formY = form.getBoundingClientRect().top;
    appear_Y = window.innerHeight / 1.3;
    if(formY < appear_Y){
        form.classList.add('appear');
    }
}
window.addEventListener('scroll',appear);


var message_exit = document.querySelector('.message-exit');
var message = document.querySelector('.messages');

message_exit.addEventListener('click',function(){
    message.style.display="none";
})

