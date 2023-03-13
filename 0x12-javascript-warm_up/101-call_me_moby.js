module.exports.callMeMoby = function (x, call) {
  if (x < 0) return;
  for (let i = 0; i < x; i++) call();
};
