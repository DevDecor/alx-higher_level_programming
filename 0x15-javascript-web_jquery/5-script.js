$('DIV#add_item').bind('click', function (e) {
  const elem = $('UL.my_list');
  elem.append('<li>Item</li>');
});
