const stopwatch = document.querySelector("#stopwatch");
const timerDisplay = document.querySelector("#timer");

let startTime;
let updatedTime;
let difference;
let tInterval;
let running = false;

function startTimer(){
  if(!running){
    startTime = new Date().getTime();
    tInterval = setInterval(getShowTime, 1);
    running = true;
  }else{
    clearInterval(tInterval);
    running = false;
  }
}

function resetTimer(){
  clearInterval(tInterval);
  running = false;
  // reset the timer display
  timerDisplay.innerHTML = "00:00:00.000";
}

function getShowTime(){
  updatedTime = new Date().getTime();
  if (startTime){
    difference = updatedTime - startTime;
  }
  // calculate (and subtract) whole days
  let days = Math.floor(difference / (1000 * 60 * 60 * 24));
  difference -= days * (1000 * 60 * 60 * 24);
  
  // calculate (and subtract) whole hours
  let hours = Math.floor(difference / (1000 * 60 * 60));
  difference -= hours * (1000 * 60 * 60);
  
  // calculate (and subtract) whole minutes
  let mins = Math.floor(difference / (1000 * 60));
  difference -= mins * (1000 * 60);
  
  // calculate (and subtract) whole seconds
  let secs = Math.floor(difference / 1000);
  difference -= secs * 1000;
  
  // display the stopwatch
  timerDisplay.innerHTML = 
    (days > 0 ? days + " days " : "") + 
    (hours < 10 ? "0" + hours : hours) + ":" + 
    (mins < 10 ? "0" + mins : mins) + ":" + 
    (secs < 10 ? "0" + secs : secs) + "." + 
    (difference < 100 ? 
      (difference < 10 ? "00" + difference : "0" + difference) :
      difference
    );
}
