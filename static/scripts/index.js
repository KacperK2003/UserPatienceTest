window.onload = function() {
    const nextButton = document.querySelector('.next-button');
    nextButton.addEventListener('click', onClick);
}

function onClick() {
    window.location.href = '/test1';
}