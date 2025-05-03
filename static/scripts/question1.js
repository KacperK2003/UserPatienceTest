window.onload = function () {
    const options = document.querySelectorAll('.loader-option');
    const confirmButton = document.querySelector('.confirm-button');
    let selectedChoice = null;

    options.forEach(option => {
        option.addEventListener('click', function () {
            options.forEach(opt => opt.classList.remove('selected'));
            this.classList.add('selected');
            selectedChoice = this.dataset.choice;
            confirmButton.disabled = false;
        });
    });

    confirmButton.addEventListener('click', function () {
        if (selectedChoice) {
            document.cookie = `question1_choice=${selectedChoice}; path=/; max-age=3600`;
            window.location.href = '/submit';
        }
    });
}
