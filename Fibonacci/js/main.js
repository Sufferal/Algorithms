const inputElem   = document.querySelector("#fibo-num");
const startElem   = document.querySelector("#start-btn");
const computeElem = document.querySelector("#compute-flag");
const btnElems    = document.querySelectorAll(".algo");
const resultElem  = document.querySelector("#result-numbers");
const timeElem    = document.querySelector("#result-time");

// Clear input on refresh
window.addEventListener("load", () => (inputElem.value = ""));

computeElem.addEventListener("click", () =>
  computeElem.classList.toggle("active")
);

// When you click on an algorithm
btnElems.forEach((btn) => {
  btn.addEventListener("click", (e) => {
    // Remove active from all buttons
    btnElems.forEach((btn) => {
      btn.classList.remove("active");
    });
    // Add active to the current one
    e.target.classList.add("active");
  });
});

startElem.addEventListener("click", () => {
  timeElem.textContent = "Time: ";
  resultElem.textContent = "Result: ";
  const numValue = inputElem.value;
  if (numValue == "") return false;

  let start, end, timeTaken;
  const activeButton = document.querySelector(".algo-wrapper .btn.active");

  // Recursive 
  if (activeButton.classList.contains("algo-1")) {
    // Compute TILL that number
    if (computeElem.classList.contains("active")) {
      start = performance.now();
      for (let i = 0; i < numValue; i++) {
        resultElem.textContent += fiboRecursive(i) + ", ";
      }
      end = performance.now();
      timeTaken = end - start;
    }

    // Computer ONLY that number
    start = performance.now();
    resultElem.textContent += fiboRecursive(numValue);
    end = performance.now();
    timeTaken = end - start;

    timeElem.textContent += timeTaken + " milliseconds";
  }

  inputElem.value = "";
  inputElem.focus();
});
