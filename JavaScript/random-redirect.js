// Here's an example of a simple random redirector implemented in JavaScript

const links = [
    "https://www.google.com",
    "https://www.facebook.com",
    "https://www.youtube.com",
    "https://www.twitter.com",
    "https://www.instagram.com",
  ];
  
  function redirect() {
    const randomIndex = Math.floor(Math.random() * links.length);
    const link = links[randomIndex];
    window.location.href = link;
  }
  

