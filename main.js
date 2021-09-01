const stringify = require("csv-stringify");

const rp = require("request-promise-native"),
    fs = require('fs'),
    _ = require('lodash'),
    {convertArrayToCSV} = require('convert-array-to-csv'),
    QURAN_URL = 'https://api.quran.com/api/v4/verses/by_page/',
    QURAN_TOTAL_PAGES = 604,
    AUDIO_BASE_URL = "https://audio.qurancdn.com/",
    CSV_HEADER = ["'Page Number'", "'Arabic Word'", "'English Word'", "'URL to Arabic Audio'", "'Verse'"],
    JSON_PATH = "pages/json/",
    CSV_PATH = "pages/csv/"

let options = {
    method: 'GET',
    url: QURAN_URL,
    qs:
    {
        per_page: '1000',
        page: '1',
        word_fields: 'text_uthmani',
        words: 'true',
        fields: 'text_uthmani',
        language: 'en'
    },
    body: '{}'
};

let missingPages = [485]
//getPages()
function getPages() {

    let pagePromises = [];

    for (let pageNo = 1; pageNo <= QURAN_TOTAL_PAGES; pageNo++) {
        //missingPages.forEach(pageNo=> {


        options.url = QURAN_URL + pageNo


        let getPage = rp(null, options, (error, response, body) => {

            try {

                if (error) throw new Error(error);
                body = JSON.parse(body)
                fs.writeFileSync(JSON_PATH + pageNo, JSON.stringify(body, null, 2))

            } catch (err) {
                console.error(err)
            }
        });

        pagePromises.push(getPage);

    }
    //);

    Promise.all(pagePromises)
}

//verifyFiles()
function verifyFiles() {

    for (let i = 0; i < 605; i++) {
        const path = JSON_PATH + i

        try {
            if (!fs.existsSync(path)) {
                console.log(i)
            }
        } catch (err) {
            console.error(err)
        }
    }

}

iteratePages()
async function iteratePages() {
    let pages = [],  pagePromises=[];
    pages = await fs.promises.readdir(JSON_PATH, (err, files) => { return files })

    let flag = false
    pages.forEach(async function (page) {
        let csv = []
        //Trigger to stop after 1 file
        if (page == "100") flag =true;  if(flag) return function(){}; 

       // let promise = new Promise ( (resolve, reject)=>{
            let rawdata = fs.readFileSync(JSON_PATH + page);
            let pageJson = JSON.parse(rawdata);
            _.each(pageJson.verses, (verse) => {
                _.each(verse.words, (word) => {
                    word.audio_url && csv.push(
                        ["'"+page+"'", "'"+word.text_uthmani+"'", "'"+word.translation.text+"'",
                        "'"+AUDIO_BASE_URL + word.audio_url+"'","'"+ verse.text_uthmani+"'"]);
                })
            })
            let data = convertArrayToCSV(csv, { header: CSV_HEADER, separator: ',' })
            await fs.promises.writeSync(CSV_PATH + page + ".csv", data)//.then(()=>{resolve(page)})

        //})
        
        //pagePromises.push(promise)
    });


    // Promise.all(pagePromises).then(result => {
    //     console.log("Promises Done");
    // })


}
/*
Iterate through the pages and make json files

take a json file and change to csv
    add header to csv //use createRow(default) and add to wordArray
    initialize base url for audio and array
    get page from file name
    iterate through verses
        iterate through  words
            if FIRST
                wordArray =+ ["Page Number", "Arabic Word", "English Word", "URL to Arabic Audio","Verse"] //move to top

            wordArray =+  [nameofFile,word.text_uthmani, word.translation.text, audioBaseUrl + word.audio_url, verse];
    write wordArray to new file 'page_##.csv'

**please verify that the csv file works

*/