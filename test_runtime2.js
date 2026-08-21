const fs = require('fs');
let html = fs.readFileSync('project.html', 'utf-8');

// Extract the script tag
let scriptContent = html.match(/<script>([\s\S]*?)<\/script>/)[1];

// Make a fake browser environment
const jsEnv = `
const window = { innerWidth: 1024, location: { search: '?id=gobunny', protocol: 'http:', hostname: 'localhost' } };
const document = {
    getElementById: (id) => {
        let el = {
            innerHTML: '',
            style: {},
            classList: { add: ()=>{}, remove: ()=>{} },
            setAttribute: ()=>{}
        };
        if (id === 'dynamic-gallery') global.gal = el;
        return el;
    },
    querySelector: () => ({ style: {}, classList: {add:()=>{}, remove:()=>{}}, setAttribute: ()=>{} }),
    documentElement: { style: { setProperty: () => {} } },
    body: { classList: { remove: () => {}, add: () => {} } },
    createElement: () => ({})
};
const URLSearchParams = class {
    constructor(search) { this.search = search; }
    get(param) { return 'gobunny'; }
};
const setInterval = () => 1;
const clearInterval = () => {};
const lucide = { createIcons: () => {} };

let PORTFOLIO_DATA = {
    "gobunny": [
      "assets/portfolio-data/GoBunny_brand/BRANDCOLOR_GOBUNNY.svg",
      "assets/portfolio-data/GoBunny_brand/GO BUNNY.png"
    ]
};
window.PORTFOLIO_DATA = PORTFOLIO_DATA;

${scriptContent.replace(/window\.addEventListener/g, '//')}
loadProject();
console.log("Gallery Inner HTML Length:", global.gal ? global.gal.innerHTML.length : 0);
if(global.gal) console.log(global.gal.innerHTML.substring(0, 300));
`;

try {
    new Function('global', jsEnv)(global);
    console.log("No runtime errors!");
} catch(e) {
    console.log("Runtime error:", e);
}
