
$("document").ready(function(){
  $(".close").on("click", function(){
    //closing
    $(".pop").addClass( "hidden" );
  });

  $("article").on("click", function(){
    $(".pop").addClass("hidden")
    var elmid ="#pop-" + $(this).attr('id');
    var targeted = $(elmid);
    targeted.removeClass("hidden")
    $('html, body').animate({
      scrollTop: targeted.offset().top
    }, 800);
  });

    $(".rightround").on("click", function(){
//closing

  $(".daytwo").removeClass("hiddendisplay")
  $(".dayone").addClass("hiddendisplay")
  $(".leftround").removeClass("activebtn");
  $(this).addClass( "activebtn" );



  });


    $(".leftround").on("click", function(){

//closing
  $(".dayone").removeClass("hiddendisplay")
  $(".daytwo").addClass("hiddendisplay")
  $(".rightround").removeClass("activebtn");
  $(this).addClass( "activebtn" );



  });

})
