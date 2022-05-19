$(document).ready(function() {
    loadNewQuote();
    
    $('button').click(function(){
      loadNewQuote();
    });
  });
  
  var loadNewQuote = function() {
    var newQuote = quoteMachine.getQuote(quotes);
    $('blockquote').text(newQuote[1]);  // Quote
    $('.quote p').text("-" + newQuote[0]);  // Author
    $('footer #current').text(newQuote[2]); // Index
    $('footer #total').text(newQuote[3]) // Total
  };
  
  var quotes = [
    {"Unknown": "It isn't courage if you're not afraid."},
    {"William Shakespeare": "There's divinity that shapes our ends, rough-hew them how we will."},
    {"John Lennon": "Life is what happens to you while you're busy making other plans"},
    {"Albert Einstein": "I want to know God's thoughts. The rest are just details."},
    {"Rory Gilmore": "Buy me coffee and call me Ace."},
    {"Unknown": "Don't tell God how big your storm is.  Tell the storm how big your God is!"},
    {"Ernest Hemingway": "A man may be destroyed but not defeated."},
    {"William Shakespeare": "The fault, dear Brutus, is not in our stars but in ourselves that we are underlings."},
    {"Mark Twain": "Golf is a nice walk spoiled by a small ball."},
    {"Eleanor Roosevelt": "You deserve what you tolerate."},
    {"Abby Jones": "I like orange hair, and I cannot lie."},
    {"Buddy the Elf": "I just like to smile.  Smiling's my favorite."},
    {"Dave Barry": "No one cares if you can't dance well.  Just get up and dance!"},
    {"C&C Music Factory":"Everybody dance now."},
    {"Krista Stuck": "He who goes to bed with itchy bottom wakes with stinky fingers."},
    {"Kid President": "Be somebody that makes everybody feel like a somebody."},
    {"Smokey the Bear": "Only you can prevent forest fires."},
    {"Monty Python and the Holy Grail": "I fart in your general direction. Your mother was a hamster and your father smelled of elderberries!"},
    {"Sue Sevener": "Bite Me!"},
    {"Jill Freeman": "Not my monkey, not my circus!"},
    {"Abby Jones": "You can't pray to yourself.  You can pray to God quietly, but you can't pray to yourself."},
    {"from Step Brothers": "You ate white dog poop?!"},
    {"from Ruth Destache": "Every accomplishment starts with the decision to try."},
    {"from Ruth Destache": "There isn't enough room in your mind for both worry and faith.  You must decide which one will live there."},
    {"from Laela Jones Williams": "If at first you don't succeed, do NOT try skydiving!"},
    {"from a student via Janelle Barclay Nielsen": "Life's going to throw some things at you that aren't worth catching."},
    {"jhinze": "During your journey through life, if you come to a fork in the road...take it."},
    {"Shonna Dorsey": "Be good and kind to each other; you never know what others are going through."},
    {"Shonna Dorsey": "The better you take care of yourself, the more you can do for others."},
  ];
  
  var quoteMachine = {
    getRandom: function(numVals) {
      return Math.floor(Math.random() * numVals);
    },
    
    getAuthor: function(quote) {
      return Object.keys(quote);
    },
    
    getQuote: function(quotes) {
      var selectedIndex = this.getRandom(quotes.length);
      var quote = quotes[selectedIndex];
      var author = this.getAuthor(quote);
      return [author, quote[author], selectedIndex + 1, quotes.length];
    }
  };$(document).ready(function() {
    loadNewQuote();
    
    $('button').click(function(){
      loadNewQuote();
    });
  });
  
  var loadNewQuote = function() {
    var newQuote = quoteMachine.getQuote(quotes);
    $('blockquote').text(newQuote[1]);  // Quote
    $('.quote p').text("-" + newQuote[0]);  // Author
    $('footer #current').text(newQuote[2]); // Index
    $('footer #total').text(newQuote[3]) // Total
  };
  
  var quotes = [
    {"Unknown": "It isn't courage if you're not afraid."},
    {"William Shakespeare": "There's divinity that shapes our ends, rough-hew them how we will."},
    {"John Lennon": "Life is what happens to you while you're busy making other plans"},
    {"Albert Einstein": "I want to know God's thoughts. The rest are just details."},
    {"Rory Gilmore": "Buy me coffee and call me Ace."},
    {"Unknown": "Don't tell God how big your storm is.  Tell the storm how big your God is!"},
    {"Ernest Hemingway": "A man may be destroyed but not defeated."},
    {"William Shakespeare": "The fault, dear Brutus, is not in our stars but in ourselves that we are underlings."},
    {"Mark Twain": "Golf is a nice walk spoiled by a small ball."},
    {"Eleanor Roosevelt": "You deserve what you tolerate."},
    {"Abby Jones": "I like orange hair, and I cannot lie."},
    {"Buddy the Elf": "I just like to smile.  Smiling's my favorite."},
    {"Dave Barry": "No one cares if you can't dance well.  Just get up and dance!"},
    {"C&C Music Factory":"Everybody dance now."},
    {"Krista Stuck": "He who goes to bed with itchy bottom wakes with stinky fingers."},
    {"Kid President": "Be somebody that makes everybody feel like a somebody."},
    {"Smokey the Bear": "Only you can prevent forest fires."},
    {"Monty Python and the Holy Grail": "I fart in your general direction. Your mother was a hamster and your father smelled of elderberries!"},
    {"Sue Sevener": "Bite Me!"},
    {"Jill Freeman": "Not my monkey, not my circus!"},
    {"Abby Jones": "You can't pray to yourself.  You can pray to God quietly, but you can't pray to yourself."},
    {"from Step Brothers": "You ate white dog poop?!"},
    {"from Ruth Destache": "Every accomplishment starts with the decision to try."},
    {"from Ruth Destache": "There isn't enough room in your mind for both worry and faith.  You must decide which one will live there."},
    {"from Laela Jones Williams": "If at first you don't succeed, do NOT try skydiving!"},
    {"from a student via Janelle Barclay Nielsen": "Life's going to throw some things at you that aren't worth catching."},
    {"jhinze": "During your journey through life, if you come to a fork in the road...take it."},
    {"Shonna Dorsey": "Be good and kind to each other; you never know what others are going through."},
    {"Shonna Dorsey": "The better you take care of yourself, the more you can do for others."},
  ];
  
  var quoteMachine = {
    getRandom: function(numVals) {
      return Math.floor(Math.random() * numVals);
    },
    
    getAuthor: function(quote) {
      return Object.keys(quote);
    },
    
    getQuote: function(quotes) {
      var selectedIndex = this.getRandom(quotes.length);
      var quote = quotes[selectedIndex];
      var author = this.getAuthor(quote);
      return [author, quote[author], selectedIndex + 1, quotes.length];
    }
  };