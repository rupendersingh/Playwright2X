const prompt = require('prompt-sync')();
let expected = prompt("Enter the Expected Result = ");
let actual = prompt("Enter the Actual Result = ");

console.log("Expected = " + expected);
console.log("Actual = " + actual);

if (expected === actual) {
    console.log(" ✅ Test Passed");
}
else
    console.log(" ❌ Test Failed");