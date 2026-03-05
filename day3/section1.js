let text = "JavaScript";
console.log(text.length);

function checkNumber(value) {
    if (typeof value === "number") {
        return true;
    } else {
        return false;
    }
}

console.log(checkNumber(25));
console.log(checkNumber("25"));

let str = "123";
let num = Number(str);
console.log(num);

let a = 10;
let b = 20;

if (a > b) {
    console.log("Greater");
} else if (a < b) {
    console.log("Smaller");
} else {
    console.log("Equal");
}

let fName = "Rahul";
let lName = "Sharma";
let fullName = fName + " " + lName;

console.log(fullName);
