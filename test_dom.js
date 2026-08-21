const fs = require('fs');
const jsdom = require("jsdom");
const { JSDOM } = jsdom;

const html = fs.readFileSync('project.html', 'utf8');
const dom = new JSDOM(html, { runScripts: "dangerously", resources: "usable" });

// Mock location
Object.defineProperty(dom.window, 'location', {
  value: { search: '?id=gobunny', protocol: 'file:', hostname: 'localhost' }
});

setTimeout(() => {
  const content = dom.window.document.getElementById('dynamic-gallery').innerHTML;
  console.log("Gallery length:", content.length);
  if(content.length < 100) {
      console.log("ERROR: Gallery is empty!");
  } else {
      console.log("Success! Gallery is populated.");
  }
}, 500);
