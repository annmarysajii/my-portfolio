const fs = require('fs');
let html = fs.readFileSync('project.html', 'utf-8');

// Extract the script tag
let scriptContent = html.match(/<script>([\s\S]*?)<\/script>/)[1];

// Make a fake browser environment
const jsEnv = `
const window = { location: { search: '?id=gobunny', protocol: 'http:', hostname: 'localhost' } };
const document = {
    getElementById: (id) => ({
        innerHTML: '',
        style: {}
    }),
    querySelector: () => ({ style: {} }),
    documentElement: { style: { setProperty: () => {} } },
    body: { classList: { remove: () => {} } }
};
const URLSearchParams = class {
    constructor(search) { this.search = search; }
    get(param) { return 'gobunny'; }
};
let PORTFOLIO_DATA = {
    "gobunny": [
      "assets/portfolio-data/GoBunny_brand/BRANDCOLOR_GOBUNNY.svg",
      "assets/portfolio-data/GoBunny_brand/GO BUNNY.png"
    ]
};
window.PORTFOLIO_DATA = PORTFOLIO_DATA;

${scriptContent.replace('window.addEventListener', '//')}
loadProject();
`;

try {
    new Function(jsEnv)();
    console.log("No runtime errors!");
} catch(e) {
    console.log("Runtime error:", e);
}
