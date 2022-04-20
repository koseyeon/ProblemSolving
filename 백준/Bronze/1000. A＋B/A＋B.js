"use strict";
const fs = require("fs");
const input = fs.readFileSync(0, "utf8").split("\n");
const [a, b] = input[0].split(" ");
console.log(Number(a) + Number(b));
