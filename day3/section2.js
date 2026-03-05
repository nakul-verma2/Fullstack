const add = function(num1, num2) {
    let result = num1 + num2;
    console.log(result);
};

let input1 = Number(prompt("Enter first number:"));
let input2 = Number(prompt("Enter second number:"));

add(input1, input2);

function square(num) {
    console.log(num * num);
}

const square2 = (num) => {
    console.log(num * num);
};

let userinput = Number(prompt("Enter a number to square:"));
square(userinput);
square2(userinput);


const check = (num) => {
    if (num % 2 === 0) {
        console.log("Even");
    } else {
        console.log("Odd");
    }
};

check(10);

function celsiusToFahrenheit(celsius) {
    let fahrenheit = (celsius * 9/5) + 32;
    console.log(fahrenheit);
}

function fahrenheitToCelsius(fahrenheit) {
    let celsius = (fahrenheit - 32) * 5/9;
    console.log(celsius);
}

celsiusToFahrenheit(30);
fahrenheitToCelsius(86);

const multiply = (a, b) => {
    return a * b;
};

console.log(multiply(5, 4));