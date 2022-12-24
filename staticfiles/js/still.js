function changeNavBg(){
    var nav = document.getElementById('nav-bar');
    var scrollContent = document.getElementById('scrollspyHeading2');
    let value = scrollContent.offsetTop-100;
    var scrollValue = window.scrollY;
    if (scrollValue >= value){
        nav.classList.add('nav-color');
    }
    else{
        nav.classList.remove('nav-color');
    }
}

window.addEventListener('scroll', changeNavBg);