// Install puppeteer-core if this host does not provide it. Set CHROME_PATH and NODE_PATH.
const puppeteer = require('puppeteer-core');
const {pathToFileURL} = require('node:url');
(async()=>{
 const [html,pdf]=process.argv.slice(2);if(!html||!pdf)throw Error('Usage: export_pdf.cjs input.html output.pdf');
 const browser=await puppeteer.launch({executablePath:process.env.CHROME_PATH||'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:true,args:['--no-sandbox']});
 try{const page=await browser.newPage();await page.goto(pathToFileURL(html).href,{waitUntil:'load'});await page.evaluate(()=>document.fonts.ready);const fit=await page.evaluate(()=>Array.from(document.querySelectorAll('.page')).map((e,i)=>({page:i+1,height:e.clientHeight,scroll:e.scrollHeight,footer:e.querySelector('footer').getBoundingClientRect().top,previous:e.querySelector('footer').previousElementSibling.getBoundingClientRect().bottom,images:Array.from(e.querySelectorAll('img')).every(x=>x.complete&&x.naturalWidth>0)})));console.log(JSON.stringify(fit));if(fit.some(x=>x.scroll>x.height+1||x.previous>x.footer||!x.images))throw Error('Page fit or image check failed');await page.pdf({path:pdf,preferCSSPageSize:true,printBackground:true,displayHeaderFooter:false});}finally{await browser.close()}
})().catch(e=>{console.error(e);process.exit(1)});
