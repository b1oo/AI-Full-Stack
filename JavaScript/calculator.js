// Here is an example of a simple calculator implemented in JavaScript

const display = document.getElementById("display");

function updateDisplay(value) {
  display.value = value;
}

function clearDisplay() {
  display.value = "";
}

function handleOperator(operator) {
  const currentValue = display.value;
  const newValue = currentValue + operator;
  updateDisplay(newValue);
}

function calculate() {
  const currentValue = display.value;
  const calculatedValue = eval(currentValue);
  updateDisplay(calculatedValue);
}

const buttons = document.querySelectorAll("button");
buttons.forEach((button) => {
  button.addEventListener("click", (e) => {
    const value = e.target.dataset.value;
    if (!value) {
      return;
    }
    if (value === "clear") {
      clearDisplay();
    } else if (value === "=") {
      calculate();
    } else {
      handleOperator(value);
    }
  });
});
