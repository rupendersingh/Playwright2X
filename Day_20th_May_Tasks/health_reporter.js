const prompt = require('prompt-sync')();
let percent = Number(prompt("Enter the percentage of Test Case Passed = "));
console.log("Input = " + percent);
//let statusMsg = null;
switch (true) {
    case (percent === 100):
        statusMsg = "Green Build";
        break;
    case (percent >= 90 && percent <= 99):
        statusMsg = "Stable (investigate failures)";
        break;

    case (percent >= 70 && percent <= 89):
        statusMsg = "Unstable";
        break;

    case (percent < 70):
        statusMsg = "Broken Build (block deployment)";
        break;

    default:
        statusMsg = "Invalid percent";
}

console.log("Output: " + statusMsg);