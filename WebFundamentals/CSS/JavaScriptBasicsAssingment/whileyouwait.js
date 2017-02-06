var daysUntilMyBirthday = 60;

for (var daysUntilMyBirthday = 60; daysUntilMyBirthday > -1; daysUntilMyBirthday--) {
  if (daysUntilMyBirthday > 30 && daysUntilMyBirthday <= 60) {
    console.log(daysUntilMyBirthday, "more days until my bithday. Such a long time... :(");
  }
  if (daysUntilMyBirthday <= 30 && daysUntilMyBirthday > 5) {
    console.log(daysUntilMyBirthday, "days until my birthday!!!!!");
  }
  if (daysUntilMyBirthday <= 5 && daysUntilMyBirthday > 0) {
    console.log(daysUntilMyBirthday, "DAYS UNTIL MY BIRTHDAY OMG YAS!");
  }
  if (daysUntilMyBirthday == 0) {
    console.log("It's my birthday!");
  }
}
