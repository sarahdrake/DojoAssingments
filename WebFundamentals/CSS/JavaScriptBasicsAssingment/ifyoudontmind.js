
var hour = 5;
var minute = 55;
var period = "PM";

if (period == "AM")
{
  if (minute < 30)
  {
    console.log("It's just after", hour, "in the morning");
  }
  else
  {
    console.log("It's almost", hour + 1, "in the morning");
  }
}
else if (period == "PM")
{
    if (minute < 30)
    {
      console.log("It's just after", hour, "in the evening");
    }
    else
    {
      console.log("It's almost", hour + 1, "in the evening");
    }
}
