function numbersOnly(arr) {
//   //use for loop to iterate through array//
//     //use typeof to determine if each arr[i] === "number"
//     //if(typeof arr[i] === "number")
//       //arrnew.push(arr[i])
  var newArray = [];
  for (var i = 0; i < arr.length; i++) {
    if (typeof arr[i] === "number") {
      newArray.push(arr[i]);

    }
  }
  console.log(newArray);
  return newArray;

}
numbersOnly([1, "apple", 4, "red", -2]);

function removeString(array) {
  var counter = 0; //need a variable to store the number of numbers in the array//
  for (var i = 0; i < array.length; i++) {
    if (typeof array[i] === "number") {  // if the typeof = "number" then we store that number in the array indice that corresponds with those that are numbers.//
      array[counter] = array[i];         // and we must increase counter by one each time so that the next "number" gets stored in the next indice in the array//
      counter++;
    }
  }
  array.length = counter;  // must truncate the origianl array to equal the number of numbers.
  console.log(array);
}
removeString([1, "apple", "red", 4, 2]);
