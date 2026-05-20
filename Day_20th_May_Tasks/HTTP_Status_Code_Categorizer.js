const prompt = require('prompt-sync')();
let statusCode = Number(prompt("Enter the Status Code = "));
console.log("Input = " + statusCode);
//console.log(typeof (statusCode));

let statusMsg = null;
switch (true) {
    case (statusCode >= 200 && statusCode <= 299):
        statusMsg = "Success";
        break;
    case (statusCode >= 300 && statusCode <= 399):
        statusMsg = "Redirection";
        break;

    case (statusCode >= 400 && statusCode <= 499):
        statusMsg = "Client Error";
        break;

    case (statusCode >= 500 && statusCode <= 599):
        statusMsg = "Server Error";
        break;

    default:
        statusMsg = "Invalid";
}

console.log("Output: " + statusMsg);