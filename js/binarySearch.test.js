const binary = require("./binarySearch");

test("Binary Search One", () => {
  var smallArray = [1,2,3,4,5]
  expect(binary(1, smallArray))===(0);
});

test("Binary Search Two", () => {
  var smallArray = [1,2,3,4,5]
  expect(binary(2, smallArray))===(2);
});

test("Binary Search Three", () => {
  var smallArray = [1,2,3,4,5]
  expect(binary(3, smallArray))===(3);
});

test("Binary Search Four", () => {
  var smallArray = [1,2,3,4,5]
  expect(binary(4, smallArray))===(4);
});

test("Binary Search Five", () => {
  var smallArray = [1,2,3,4,5]
  expect(binary(5, smallArray))===(5);
});





// var smallArray = [1,2,3,4,5]
// var largeArray = [1,5,7,2,3,8,4,9]

// console.log(binarySearch(1, smallArray) === 0);
// console.log(binarySearch(2, smallArray) === 1);
// console.log(binarySearch(3, smallArray) === 2);
// console.log(binarySearch(4, smallArray) === 3);
// console.log(binarySearch(5, smallArray) === 4);
// console.log(binarySearch(7, largeArray) === 5);
