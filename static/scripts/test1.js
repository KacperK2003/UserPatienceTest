window.onload = function() {
    onLoad();
}

var startTime = null;

function onLoad() {
    startTime = new Date();

    const nextButton = document.querySelector('.next-button');

    nextButton.style.pointerEvents = 'none';
    nextButton.style.opacity = '0.5';

    setTimeout(() => {
        nextButton.style.pointerEvents = 'auto';
        nextButton.style.opacity = '1';
        nextButton.addEventListener('click', onClick);
    }, 60000);

    setTimeout(() => {
        //window.location.href = 
    }, 60000 * 3);
}

function onClick() {
    console.log(startTime);
}