
function verifyPassword() {
    var emailInput = document.getElementById('userName');
    var emailValue = document.getElementById("userName").value;

    if (!emailValue.endsWith('.com')) {
        alert('Please enter a valid Gmail address.');
        emailInput.focus();
        return false;
    }
    // return true; // Allow form submission
}
