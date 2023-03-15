#!/usr/bin/node
const dict = require('./101-data').dict;

const totalist = Object.entries(dict);
const vals = Object.values(dict).map(e => e.toString());
const valsUniq = [...new Set(vals)];
const newDict = {};
valsUniq.sort().forEach(e => {
  newDict[e] = [];
});
totalist.map(e => e.map(f => f.toString())).forEach(e => {
  newDict[e[1]].push(e[0]);
  newDict[e[1]].sort();
});
console.log(newDict);
