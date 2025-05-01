document.addEventListener('DOMContentLoaded', function () {
    const banner = document.getElementById('cookie-banner');

    if (!banner) return;

    if (document.cookie.includes('cookiesAccepted=true')) {
        banner.style.display = 'none';
    }

    const button = banner.querySelector('button');
    if (button) {
        button.addEventListener('click', function () {
            banner.style.display = 'none';

            const d = new Date();
            d.setTime(d.getTime() + (365 * 24 * 60 * 60 * 1000));
            document.cookie = "cookiesAccepted=true; expires=" + d.toUTCString() + "; path=/";
        });
    }
});
