document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.caption-number');
    elems.forEach(function (el) {
        if (el && el.textContent) {
            el.textContent = el.textContent.replace(/(\d)\.(?=\d)/g, '$1-');
        }
    });
});
