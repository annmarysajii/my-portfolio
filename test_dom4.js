const fs = require('fs');
const jsdom = require("jsdom");
const { JSDOM } = jsdom;
const html = fs.readFileSync('project.html', 'utf8');
const dom = new JSDOM(html.replace("<script src=\"scripts/motion.js\"></script>", ""), { runScripts: "dangerously", url: "http://localhost/?id=gobunny" });
setTimeout(() => {
  console.log("MAIN HTML:", dom.window.document.getElementById('main').innerHTML);
}, 1000);
