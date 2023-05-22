// let v = [1,3,4]
// for (const key in v) {
//     console.log(key);
// }
var inorderTraversal = function(array) {
    let res = []
    function dfs(arr){
        if (Array.isArray(arr)===false){
            res.push(arr);
            return
        }
        for (const index in arr){
            dfs(arr[index])
        }
    }
    dfs(array)
    
    console.log(res)
    // return res
    let i = 0
    return {
        next : function(){
            let ii = i;
            i+=1;
            return {
                value : res[ii]
            }
        },
        done:function() {
            return i===res.length;
        }
    }
    // let i = 0
    
};

const gen = inorderTraversal([[[6]],[1,3],[]]);
console.log(gen.next().value); // 1
console.log(gen.next().value); // 1
console.log(gen.next().value); // 1
