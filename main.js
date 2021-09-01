const rp = require("request-promise-native"),
    fs = require('fs'),
    QURAN_URL = 'https://api.quran.com/api/v4/verses/by_page/',
    QURAN_TOTAL_PAGES = 604;

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

let missingPages =[485]
//getPages()
function getPages() {

    let pagePromises = [];

    //for (let pageNo = 1; pageNo <= QURAN_TOTAL_PAGES; pageNo++) {
    missingPages.forEach(pageNo=> {
        
    
        options.url = QURAN_URL + pageNo


        let getPage = rp(null, options, (error, response, body) => {

            try {

                if (error) throw new Error(error);
                body = JSON.parse(body)
                fs.writeFileSync('./pages/' + pageNo, JSON.stringify(body, null, 2))

            } catch (err) {
                console.error(err)
            }
        });

        pagePromises.push(getPage);

    });

    Promise.all(pagePromises)
}

//verifyFiles()
function verifyFiles() {

    for (let i = 0; i < 605; i++) {
        const path = 'pages/'+i

        try {
            if (!fs.existsSync(path)) {
                console.log(i)
            }
        } catch (err) {
            console.error(err)
        }
    }

}

function iteratePages() { }
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