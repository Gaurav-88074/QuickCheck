function sleep(ms) {
    return new Promise((resolve,reject)=>{
        setTimeout(resolve, ms);
    })
    // return new Promise(resolve => setTimeout(resolve, ms));
}
async function demo() {
    for (let i = 0; i < 5; i++) {
        console.log(`Waiting ${i} seconds...`);
        await sleep(2000);
    }
    console.log('Done');
}

demo();