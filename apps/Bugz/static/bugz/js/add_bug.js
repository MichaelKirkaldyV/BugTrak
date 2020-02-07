$(document).ready(function(){
    $(".nav").hover(function(){
        $(this).addClass("newColor");
    }, function(){
        $(this).removeClass("newColor");
    });

    $(".op").hover(function(){
        $(this).addClass("highlight");
    }, function(){
        $(this).removeClass("highlight");
    });

    $(".admin-option").hide();
    $(".admin-option2").hide();

    $(".admin-link").click(function(event){
        event.preventDefault();
        $(".admin-option").toggle();
    });

    $(".admin-link2").click(function(event){
        event.preventDefault();
        $(".admin-option2").toggle();
    });
});