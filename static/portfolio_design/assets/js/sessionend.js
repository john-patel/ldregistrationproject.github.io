const sessionDuration = 30; // 15 seconds
let remainingTime = sessionDuration;

// Function to update the remaining time on the HTML page
function updateRemainingTime() {
    document.getElementById("timer").textContent = remainingTime;
    remainingTime--;

    if (remainingTime >= 0) {
        setTimeout(updateRemainingTime, 1000);
    } else {
        // Session end code
        document.getElementById("message").textContent = "Session ended. Redirecting...";
        setTimeout(() => {
            // Redirect to a different page after session ends
            window.location.href = "errorPage/";
        }, 1000);
    }
}
// Start the countdown
setTimeout(updateRemainingTime, 1000);
