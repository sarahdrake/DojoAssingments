//use for loop to loop through each indice in the array//
//use console log function to print first-name and last_name

// var students = [
//    {first_name:  'Michael', last_name : 'Jordan'},
//    {first_name : 'John', last_name : 'Rosales'},
//    {first_name : 'Mark', last_name : 'Guillen'},
//    {first_name : 'KB', last_name : 'Tonel'}
// ]
// names (students)
// function  names (arr) {
//   for (var i = 0; i < arr.length; i++) {
//     console.log(students[i].first_name," ", students[i].last_name);
//   }
// }

// var students = [
//    {first_name:  'Michael', last_name : 'Jordan'},
//    {first_name : 'John', last_name : 'Rosales'},
//    {first_name : 'Mark', last_name : 'Guillen'},
//    {first_name : 'KB', last_name : 'Tonel'}
// ]
// names (students)
// function  names (arr) {
//   for (var i = 0; i < arr.length; i++) {
//     console.log((i + 1) + "  " + "-" + "  " + students[i].first_name + " " + students[i].last_name + " " + "-" + " " + (students[i].first_name.length + students[i].last_name.length));
//   }
// }

var users = {
 'students': [
     {first_name:  'Michael', last_name : 'Jordan'},
     {first_name : 'John', last_name : 'Rosales'},
     {first_name : 'Mark', last_name : 'Guillen'},
     {first_name : 'KB', last_name : 'Tonel'}
  ],
 'instructors': [
     {first_name : 'Michael', last_name : 'Choi'},
     {first_name : 'Martin', last_name : 'Puryear'}
  ]
 }
 function names(arr) {
   console.log("Students");
   for (var i = 0; i < users.students.length; i++) {

     console.log((i + 1) + "  " + "-" + "  " + users.students[i].first_name + " " + users.students[i].last_name + " " + "-" + " " + (users.students[i].first_name.length + users.students[i].last_name.length));
  }
  console.log("Instructors");
  for (var i = 0; i < users.instructors.length; i++){
    console.log((i + 1) + "  " + "-" + "  " + users.instructors[i].first_name + " " + users.instructors[i].last_name + " " + "-" + " " + (users.instructors[i].first_name.length + users.instructors[i].last_name.length));
  }
}
names (users);
