$(document).ready(function() {

 $('.querC').click(function(){
    var start = $('.start').val();
    var limit = $('.limit').val();
    $('.imgitem').fadeOut('fast');
    for (i = start; i < limit; i++) {
      $('.spawn').append('<table><tr><td><img src="https://www2.wrdc.wa-k12.net/pictures/bainbrs/0' + i + '.JPG" width="100px" height="150px"/></td></tr><tr><td>' + i + '</td></tr></table>');
    }
  })
});
