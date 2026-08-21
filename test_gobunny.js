const data = {
    'gobunny': [
        "assets/portfolio-data/GoBunny_brand/3.png",
        "assets/portfolio-data/GoBunny_brand/4.png",
        "assets/portfolio-data/GoBunny_brand/ART DIRECTION PORTFOLIO (1).png",
        "assets/portfolio-data/GoBunny_brand/ART DIRECTION PORTFOLIO.png",
        "assets/portfolio-data/GoBunny_brand/Copy of ART DIRECTION PORTFOLIO (3).png",
        "assets/portfolio-data/GoBunny_brand/GO BUNNY.png",
        "assets/portfolio-data/GoBunny_brand/It is time for some strawberries.png",
        "assets/portfolio-data/GoBunny_brand/Your paragraph text (30).png",
        "assets/portfolio-data/GoBunny_brand/Your paragraph text (33).png",
        "assets/portfolio-data/GoBunny_brand/Your paragraph text (35).png",
        "assets/portfolio-data/GoBunny_brand/Your paragraph text (36).png",
        "assets/portfolio-data/GoBunny_brand/Your paragraph text (37).png"
    ]
};

const id = 'gobunny';
const media = data[id];
const styleBlock = "";
function renderMedia(f) { return `<media>${f}</media>`; }

let htmlStr = styleBlock;
const findFile = (keyword) => media.find(f => f.toLowerCase().includes(keyword.toLowerCase()));
const findFiles = (keyword) => media.filter(f => f.toLowerCase().includes(keyword.toLowerCase()));
const notFound = (list) => media.filter(f => !list.includes(f));

const logoPrimary = findFile('GO BUNNY');
const logoSecondary = findFiles('Your paragraph text').filter(f => f.includes('35') || f.includes('36') || f.includes('33')); 
const pack1 = findFile('3.png');
const pack2 = findFile('4.png');
const apps = findFiles('ART DIRECTION PORTFOLIO').concat(findFiles('Your paragraph text (37)')).concat(findFiles('Your paragraph text (30)'));
const inContext = findFiles('It is time for some strawberries');

const otherConcept = notFound([logoPrimary, ...logoSecondary, pack1, pack2, ...apps, ...inContext].filter(Boolean));
console.log("No errors.");
