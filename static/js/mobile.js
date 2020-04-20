var mobile_toggler = document.querySelector('.mobile-container');
var mobile_nav = document.querySelector('.mobile-nav');
var decider =false;
var small_logo = document.querySelector('.altern-logo');
mobile_toggler.addEventListener('click',function(){
    if(decider==false){
        mobile_toggler.querySelector('.mobile-toggler').classList.add('exit');
        mobile_toggler.querySelector('.mobile-toggler').style.position = 'fixed';
        decider = true;
        mobile_nav.style.opacity = 1;
        mobile_nav.style.zIndex = 3;
        small_logo.style.position = 'fixed';

    }
    else{
        mobile_toggler.querySelector('.mobile-toggler').classList.remove('exit');
        mobile_toggler.querySelector('.mobile-toggler').style.position = 'absolute';

        decider = false;
        mobile_nav.style.opacity = 0;
        mobile_nav.style.zIndex = -3;
        small_logo.style.position = 'absolute';

    }
})