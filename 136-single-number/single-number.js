/**
 * @param {number[]} nums
 * @return {number}
 */
    
 let nums = [2,2,3,3,4];
var singleNumber = function(nums){
    let result = 0 ;
    for (let i = 0 ; i < nums.length; i++){
        result = result ^ nums[i]
       
    }
     return result;
    if (result !== 0){
        console.log(result);
    }
}
singleNumber([2,2,3,3,4]);