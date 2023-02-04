const inputElem = document.querySelector("#fibo-num");
const startElem = document.querySelector("#start-btn");
const btnElems = document.querySelectorAll(".algo");

// Clear input on refresh
window.addEventListener("load", () => inputElem.value = "");

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
  startTimer();
});
