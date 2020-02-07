
// Creates yellow hue over links in the navbar
$(document).ready(function(){
    $("a").hover(function(){
        $(this).addClass("newColor");
    }, function(){
        $(this).removeClass("newColor");
    });
});
