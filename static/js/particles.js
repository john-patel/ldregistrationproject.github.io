
function verifyPassword() {
  var pw = document.getElementById("userPassword").value;
  // //check empty password field  
  var cpw = document.getElementById("userConfirmPassword").value;

  var emailInput = document.getElementById('userName');
  var emailValue = document.getElementById("userName").value;

  if (!emailValue.endsWith('.com')) {
    alert('Please enter a valid Gmail address.');
    emailInput.focus();
    return false;
  }

  if (pw != cpw) {
    document.getElementById("message").innerHTML = "**password is not matched..!";
    return false;
  }
  
}