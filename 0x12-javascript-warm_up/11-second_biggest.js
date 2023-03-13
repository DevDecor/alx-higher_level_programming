#!/usr/bin/node

if (process.argv.length < 4) console.log(0);
// clones the argv array
let nums = [...process.argv];
// removes the fist two default arguments
nums.splice(0, 2);

// converts all the arguments to integers
nums = nums.map(e => parseInt(e));
// find the maximum number
const max = Math.max(...nums);
// removes the maximum number
nums.splice(nums.indexOf(max), 1);

const arg = nums[0];
// prints the second maximum
if (arg) console.log(Math.max(...nums));
