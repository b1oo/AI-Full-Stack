// Here's an example of how you can use JavaScript to retrieve a random quote from the favqs.com API and display it on the page

const quoteDisplay = document.getElementById("quote");

async function getQuote() {
  const response = await fetch("https://favqs.com/api/qotd");
  const quote = await response.json();
  quoteDisplay.innerHTML = quote.quote.body;
}

getQuote();


// <blockquote id="quote"></blockquote>


