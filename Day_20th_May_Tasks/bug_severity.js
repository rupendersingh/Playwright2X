const prompt = require('prompt-sync')();
let score = Number(prompt("Enter the Impact score = "));
console.log("Input = " + score);
//let statusMsg = null;
switch (true) {
    case (score >= 9 && score <= 10):
        statusMsg = "Critical (block release)";
        break;
    case (score >= 7 && score <= 8):
        statusMsg = "High";
        break;

    case (score >= 4 && score <= 6):
        statusMsg = "Medium";
        break;

    case (score >= 1 && score <= 3):
        statusMsg = "Low";
        break;

    default:
        statusMsg = "Invalid Score";
}

console.log("Output: " + statusMsg);