window.onload = function() {
    const nextButton = document.querySelector('.next-button');
    nextButton.addEventListener('click', onClick);
}

function onClick() {
    window.location.href = 'http://localhost:8000/test1';
}