function randomChance(coin) {
  //Use for loop to determine if user wins with each coin//
    //if they win return the remaining quarters//
    //return 0 if coins=0 and no wins//
    var win = 1;
    var sum = prize + i;
    for(var i = coin; i >= 0; --i) {
      var prize = Math.floor((Math.random()*50)+51);
      if (i === 0) {
        console.log("cat");
        return 0;
      }
      if((Math.trunc(Math.random()*100)+1) === 1) {
        console.log("dog");
        return sum;
      }
  }
}
randomChance(80);
