const fs = require('fs');
const html = fs.readFileSync('portfolio.html', 'utf8');

const scripts = html.match(/<script>(.*?)<\/script>/gs);
if (scripts) {
    scripts.forEach((script, idx) => {
        let code = script.replace(/<\/?script>/g, '');
        try {
            // Check syntax by creating a Function
            new Function(code);
            console.log(`Script ${idx} syntax OK`);
        } catch (e) {
            console.error(`Script ${idx} SYNTAX ERROR: ${e.message}`);
        }
    });
}
