var bs = require("./binarySearch");
var test_array = [1,2,3,4,5];
var super_big_array = [1,5,7,2,3,8,4,9];

console.log(bs.binarySearch(1, test_array) === 0);
console.log(bs.binarySearch(2, test_array) === 1);
console.log(bs.binarySearch(3, test_array) === 2);
console.log(bs.binarySearch(4, test_array) === 3);
console.log(bs.binarySearch(5, test_array) === 4);

console.log(bs.binarySearch(7, super_big_array) === 5);
