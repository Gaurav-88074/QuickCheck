const fetch = require("node-fetch");
const foptions = {
    method: "GET",
    headers: {
        'Accept': 'application/json',
        'Content-type': 'application/json'
    },
};
fetch("https://vocabapi2022-production.up.railway.app/allword", foptions)
    .then(response => response.json())
    .then(async (data) => {
        data.forEach(async (obj) => {
            const b = {
                word: obj.word,
                meaning: obj.wordmeaning[0].meaning
            }
            const options = {
                method: 'POST', body: JSON.stringify(b), headers: {
                    'Accept': 'application/json',
                    'Content-type': 'application/json'
                },
            };
            // console.log(options)
            await fetch('https://vocabapi2023-production.up.railway.app/addvocab', options)
                .then(response => response.json())
                .then(response => console.log(response))
                .catch(err => console.error(err));

        })
    })
//   const options = {method: 'POST', body: '{"word":"vanderlized","meaning":"destroy something"}'};

//   fetch('http://127.0.0.1:8000/addvocab', options)
//     .then(response => response.json())
//     .then(response => console.log(response))
//     .catch(err => console.error(err));