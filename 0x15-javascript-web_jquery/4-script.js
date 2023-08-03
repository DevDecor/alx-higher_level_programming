$('DIV#toggle_header').bind('click', function (e) {
  const elem = $('header');
  if (elem.hasClass('green')) {
    elem.removeClass('green');
    elem.addClass('red');
  } else {
    elem.removeClass('red');
    elem.addClass('green');
  }
});
