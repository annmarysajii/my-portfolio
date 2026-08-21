const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf-8');
const styles = html.match(/<style>([\s\S]*?)<\/style>/g);
if (styles) {
    styles.forEach(s => console.log(s.substring(0, 150) + "...\n"));
}
