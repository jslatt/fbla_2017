$(document).ready(function () {
    $('.day').hover(function () {
        if($(this).length() != 1 ){
         $(this).append("test");
        }



    })
});