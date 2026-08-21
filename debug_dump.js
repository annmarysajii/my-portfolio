const fs = require('fs');
const html = fs.readFileSync('project.html', 'utf8');

const scripts = html.match(/<script>(.*?)<\/script>/gs);
if (scripts) {
    let code = scripts[0].replace(/<\/?script>/g, '');
    fs.writeFileSync('debug_script.js', code);
}
