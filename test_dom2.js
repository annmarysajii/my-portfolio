const fs = require('fs');
const jsdom = require("jsdom");
const { JSDOM } = jsdom;

const html = fs.readFileSync('project.html', 'utf8');

// Replace requestAnimationFrame to avoid jsdom errors
const newHtml = html.replace("<script src=\"scripts/motion.js\"></script>", "");

const dom = new JSDOM(newHtml, { runScripts: "dangerously", resources: "usable", url: "http://localhost/?id=gobunny" });

dom.window.onerror = function(message, source, lineno, colno, error) {
    console.error("PAGE ERROR:", message, error);
};

setTimeout(() => {
  const content = dom.window.document.getElementById('dynamic-gallery').innerHTML;
  console.log("Gallery length:", content.length);
  if(content.length < 10) {
      console.log("ERROR: Gallery is empty!");
  }
}, 1000);
