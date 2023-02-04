const btnElems = document.querySelectorAll(".algo");

const toggleClass = (e) => {
  e.target.classList.toggle("active");
};

const clearBtns = () => {
  btnElems.forEach((btn) => {
    btn.classList.remove("active");
  });
};

btnElems.forEach((btn) => {
  btn.addEventListener("click", (e) => {
    clearBtns();
    toggleClass(e);
  });
});
