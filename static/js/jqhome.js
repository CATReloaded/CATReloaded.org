
$("document").ready(function(){
  $(".close").on("click", function(){
    //closing
    $(".pop").addClass( "hidden" );
  });

  $("article").on("click", function(){
    //opening
    $(".pop").removeClass("hidden")
    $('html, body').animate({
      scrollTop: $(".pop").offset().top
    }, 800);
  });

  $(".rightround").on("click", function(){
//closing

  $(".daytwo").removeClass("hidden")
  $(".dayone").addClass("hidden")
  $(".leftround").removeClass("activebtn");
  $(this).addClass( "activebtn" );



  });


    $(".leftround").on("click", function(){

//closing
  $(".dayone").removeClass("hidden")
  $(".daytwo").addClass("hidden")
  $(".rightround").removeClass("activebtn");
  $(this).addClass( "activebtn" );



  });

})
