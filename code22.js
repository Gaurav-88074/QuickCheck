arr = new Array()
arr.push(13)
arr.push(14)
arr.push(15)
arr.push(16)
//value ,index
function update(value,index,array){
    array[index]=value*10;
}
console.log(arr);
arr.forEach(update)
console.log(arr);
//lol