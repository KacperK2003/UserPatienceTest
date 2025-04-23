window.onload = function() {
    onLoad();
}

var startTime = new Date();

function onLoad() {
    const nextButton = document.querySelector('.next-button');

    nextButton.style.pointerEvents = 'none';
    nextButton.style.opacity = '0.5';

    setTimeout(() => {
        nextButton.style.pointerEvents = 'auto';
        nextButton.style.opacity = '1';
        nextButton.addEventListener('click', onClick);
    }, 60000);

    setTimeout(() => {
        measure();
        window.location.href = 'http://localhost:8000/summary';
    }, 60000 * 3);
}

function measure() {
    const clickTime = new Date();
    const reactionTime = clickTime - startTime;
    document.cookie = `test3=${reactionTime}; path=/; max-age=3600`;
}

function onClick() {
    measure();
    window.location.href = 'http://localhost:8000/summary';
}