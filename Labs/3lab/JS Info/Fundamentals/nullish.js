// 1
let user;

alert(user ?? "Anonymous"); // Anonymous (user not defined)

//2
let user = "John";

alert(user ?? "Anonymous"); // John (user defined)

//3
let firstName = null;
let lastName = null;
let nickName = "Supercoder";

// shows the first defined value:
alert(firstName ?? lastName ?? nickName ?? "Anonymous"); // Supercoder

//4
let firstName = null;
let lastName = null;
let nickName = "Supercoder";

// shows the first truthy value:
alert(firstName || lastName || nickName || "Anonymous"); // Supercoder


//5
let height = 0;

alert(height || 100); // 100
alert(height ?? 100); // 0

//6
let height = null;
let width = null;

// important: use parentheses
let area = (height ?? 100) * (width ?? 50);

alert(area); // 5000


//7
// without parentheses
let area = height ?? 100 * width ?? 50;

// ...works the same as this (probably not what we want):
let area = height ?? (100 * width) ?? 50;


//8
let x = (1 && 2) ?? 3; // Works

alert(x); // 2