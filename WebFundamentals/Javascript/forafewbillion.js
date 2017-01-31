
var reward = 0.01;

for (var days = 1; days < 31; days++) {
  if (days >= 2) {
    reward = reward * 2;
  }
}
console.log("The reward after 30 days is", reward, "dollars");
