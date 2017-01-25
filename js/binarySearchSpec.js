var bs = require("./binarySearch"),
  test_array = ['A','B','C','D','E'];

console.log(bs.binarySearch("A", test_array) === 0);
console.log(bs.binarySearch("B", test_array) === 1);
console.log(bs.binarySearch("C", test_array) === 2);
console.log(bs.binarySearch("D", test_array) === 3);
console.log(bs.binarySearch("E", test_array) === 4);
