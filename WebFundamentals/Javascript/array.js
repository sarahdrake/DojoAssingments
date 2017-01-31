var arr = ["James", "Jill", "Jane", "Jack"];
// function fancyArray(arr) {
//   // var arr = ["James", "Jill", "Jane", "Jack"];
//   for (var i = 0; i < arr.length; i++) {
//     arr[i] = i + '->' + arr[i];
//   }
//   console.log(arr);
//   return arr;
// }
// fancyArray(["James", "Jill", "Jane", "Jack"]);


function names(arr) {
  for (var i = 0; i < arr.length; i++) {
      console.log(i + " " + "->" + " " + arr[i]);
  }
}
names(["James", "Jill", "Jane", "Jack"]);
