var bs = require("./binarySearch");

console.log(bs.binarySearch(1, [1,2,3,4,5]) === 0);
console.log(bs.binarySearch(2, [1,2,3,4,5]) === 1);
console.log(bs.binarySearch(3, [1,2,3,4,5]) === 2);
console.log(bs.binarySearch(4, [1,2,3,4,5]) === 3);
console.log(bs.binarySearch(5, [1,2,3,4,5]) === 4);

console.log(bs.binarySearch(7, [1,5,7,2,3,8,4,9]) === 5);
