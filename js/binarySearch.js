const binarySearch = (num, array) => {
  //  Pass in a num and an array to search through
  //  Find the middle value inside of the array and assign it to a variable
  //  Create an if statement to see if num == middle, if true return the index
  //  If num == middle is false, split the array in half and repeat the comparison
  //  Repeat this step if num == middle is false until true
  //  Return the index if found, return a -1 if not found
  count = 0;
  for(var i = 0; i < array.length; i++) {
    count += 1
  }
  let middle = Math.floor(count / 2);
  console.log(middle);

  let first_half = array.slice(middle);
  console.log(first_half);
};


module.exports = binarySearch

binarySearch(1, [1,2,3,4,5])

