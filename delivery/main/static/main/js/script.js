var increaseButtons = document.querySelectorAll('.increase');
var decreaseButtons = document.querySelectorAll('.decrease');

increaseButtons.forEach(function(button) {
    button.addEventListener('click', function() {
        var number = button.parentElement.querySelector('.number');
        var num = Number(number.textContent);
        num = num + 1;
        number.textContent = num;

        var link = document.querySelector('#add-to-cart-' + button.parentElement.parentElement.parentElement.parentElement.id);
        link.href = link.href.split('?')[0] + '?quantity=' + parseInt(num);
    });
});

decreaseButtons.forEach(function(button) {
    button.addEventListener('click', function() {
        var number = button.parentElement.querySelector('.number');
        var num = Number(number.textContent);
        if (num > 1) {
            num = num - 1;
            number.textContent = num;

            var link = document.querySelector('#add-to-cart-' + button.parentElement.parentElement.parentElement.parentElement.id);
            link.href = link.href.split('?')[0] + '?quantity=' + parseInt(num);
        }
    });
});

var quantityInputs = document.querySelectorAll('.number');

quantityInputs.forEach(function(input) {
    input.addEventListener('input', function() {
        var number = input.innerText;
        var link = document.querySelector('#add-to-cart-' + input.parentElement.parentElement.parentElement.parentElement.id);
        link.href = link.href.split('?')[0] + '?quantity=' + number;
    });
});

