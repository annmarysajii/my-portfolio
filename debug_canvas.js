const fs = require('fs');
const jsdom = require('jsdom');
const { JSDOM } = jsdom;
const html = fs.readFileSync('portfolio.html', 'utf8');

const dom = new JSDOM(html, { 
    runScripts: "dangerously", 
    pretendToBeVisual: true 
});

dom.window.onerror = function(msg, source, lineNo, columnNo, error) {
    console.error("JSDOM ERROR:", msg);
};

// Mock requestAnimationFrame to just run once
dom.window.requestAnimationFrame = (cb) => {
    try {
        cb();
    } catch (e) {
        console.error("RAF ERROR:", e);
    }
};

setTimeout(() => {
    // try to force bgFrame execution if it's there
    if (dom.window.bgFrame) {
        try {
            dom.window.currentCanvasTheme = "graphic-design";
            dom.window.bgFrame();
            console.log("bgFrame executed successfully for graphic design");
        } catch(e) {
            console.error("bgFrame crashed:", e);
        }
    } else {
        console.log("bgFrame not found globally");
    }
}, 500);
