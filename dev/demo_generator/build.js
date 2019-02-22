const scraper = require('website-scraper');
var fs = require('fs-extra');

const siteURL = process.argv[2];
const destinationDirectory = process.argv[3];

fs.removeSync(destinationDirectory);

const options = {
  urls: [siteURL],
  directory: destinationDirectory,
  recursive: true,
  urlFilter: function(url){
    return url.indexOf(siteURL) === 0;
  },
};

scraper(options).then((result) => {});
