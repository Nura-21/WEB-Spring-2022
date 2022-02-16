// // 1
// let message;

// message = 'Hello'; // store the string 'Hello' in the variable named message

// //2
// let message;
// message = 'Hello!';

// alert(message);

//3
// let message = 'Hello!'; // define the variable and assign the value

// alert(message); // Hello!

// ! You can not declare multiple times with same name, it gives error in console.

// 4
// let user = 'John', age = 25, message = 'Hello';
// alert(user);
// alert(age);
// alert(message);

// 5
// let user = 'John',
//   age = 25,
//   message = 'Hello';
// alert(user);
// alert(age);
// alert(message);

// 6
// 'var' keyword is almost the same as 'let', but it's like 'old-school way'

//7
// let message;

// message = 'Hello!';

// message = 'World!'; // value changed

// alert(message);

// 8
let hello = 'Hello world!';

let message;

// copy 'Hello world' from hello into message
message = hello;

// now two variables hold the same data
alert(hello); // Hello world!
alert(message); // Hello world!

// 9
let $ = 1; // declared a variable with the name "$"
let _ = 2; // and now a variable with the name "_"

alert($ + _); // 3

// 10
// note: no "use strict" in this example

// num = 5; // the variable "num" is created if it didn't exist

// alert(num); // 5

// "use strict";

// num = 5; // error: num is not defined


// 11
const myBirthday = '18.04.1982';
// for constant variables

// 12
// const myBirthday = '18.04.1982';

// myBirthday = '01.01.2001'; // error, can't reassign the constant!

// 13
const COLOR_RED = "#F00";
const COLOR_GREEN = "#0F0";
const COLOR_BLUE = "#00F";
const COLOR_ORANGE = "#FF7F00";

// ...when we need to pick a color
let color = COLOR_ORANGE;
alert(color); // #FF7F00
