const { exec } = require('child_process');
exec('node -e "const fs = require(\'fs\'); const html = fs.readFileSync(\'portfolio.html\', \'utf-8\');"', (err, stdout, stderr) => {
    if (err) console.error(err);
    console.log(stdout);
});
