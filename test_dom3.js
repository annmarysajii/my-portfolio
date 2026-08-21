const fs = require('fs');
const jsdom = require("jsdom");
const { JSDOM } = jsdom;

const html = fs.readFileSync('project.html', 'utf8');
const datajs = fs.readFileSync('scripts/data.js', 'utf8');

// Replace requestAnimationFrame to avoid jsdom errors
let newHtml = html.replace("<script src=\"scripts/motion.js\"></script>", "");
// Inject data.js directly
newHtml = newHtml.replace("<script src=\"scripts/data.js\"></script>", "<script>" + datajs + "</script>");

const dom = new JSDOM(newHtml, { runScripts: "dangerously", resources: "usable", url: "http://localhost/?id=gobunny" });

dom.window.onerror = function(message, source, lineno, colno, error) {
    console.error("PAGE ERROR:", message, error);
};

setTimeout(() => {
  const content = dom.window.document.getElementById('dynamic-gallery').innerHTML;
  console.log("Gallery length:", content.length);
  if(content.length < 10) {
      console.log("ERROR: Gallery is empty!");
  } else {
      console.log("SUCCESS! HTML:\n" + content.substring(0, 300) + "...");
  }
}, 1000);
