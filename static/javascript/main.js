let submitButton = document.querySelector('.submit-button');
let submitMessage = document.querySelector('h2');

const submitted = function(event) {
    submitMessage.textContent = 'Transaction Has Been Processed!';
}

submitButton.addEventListener('click', submitted);
