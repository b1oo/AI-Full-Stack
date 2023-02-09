// Here's an example of a simple clock implemented in JavaScript using the setInterval function to update the time every second

const clockDisplay = document.getElementById("clock");

function updateClock() {
  const date = new Date();
  const time = date.toLocaleTimeString();
  clockDisplay.innerHTML = time;
}

setInterval(updateClock, 1000);

// <div id="clock"></div> // html code to show