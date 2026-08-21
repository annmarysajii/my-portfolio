const fs = require('fs');
const code = fs.readFileSync('scripts/motion.js', 'utf8');
try {
    new Function(code);
    console.log("motion.js syntax OK");
} catch(e) {
    console.error("motion.js error", e);
}
