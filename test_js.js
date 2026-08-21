const fs = require('fs');
const vm = require('vm');
['index.html', 'portfolio.html', 'project.html', 'game.html'].forEach(file => {
    const content = fs.readFileSync(file, 'utf8');
    const scripts = content.match(/<script>([\s\S]*?)<\/script>/g);
    if (!scripts) return;
    scripts.forEach((s, i) => {
        const code = s.replace(/<\/?script>/g, '');
        try {
            new vm.Script(code);
            console.log(`[OK] ${file} script ${i}`);
        } catch (e) {
            console.error(`[ERROR] ${file} script ${i}: ${e.message}`);
        }
    });
});
