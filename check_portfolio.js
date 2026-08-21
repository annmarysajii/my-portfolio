const fs = require("fs");
const html = fs.readFileSync("portfolio.html", "utf-8");
const scripts = html.match(/<script>([\s\S]*?)<\/script>/g);
if (scripts) {
  scripts.forEach((scriptTag, i) => {
    const code = scriptTag.replace(/<\/?script>/g, "");
    try {
      new Function(code);
      console.log(`Portfolio Script ${i} syntax OK`);
    } catch (e) {
      console.error(`Portfolio Script ${i} SYNTAX ERROR: ${e.message}`);
    }
  });
}
