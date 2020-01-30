$(document).ready(function(){
    $("a").hover(function(){
        $(this).addClass("newColor");
    }, function(){
        $(this).removeClass("newColor");
    });
});