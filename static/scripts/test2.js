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
    }, 1000);

    setTimeout(() => {
        measure();
        window.location.href = '/test3';
    }, 60000 * 3);
}

function measure() {
    const clickTime = new Date();
    const reactionTime = clickTime - startTime;
    document.cookie = `test2=${reactionTime}; path=/; max-age=3600`;
}

function onClick() {
    measure();
    window.location.href = '/test3';
}