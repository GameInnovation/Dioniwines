//  $('h1').click(function(){
//    $(this).css('background-color', '#ff0000')
//  })



// var waypoints = $('#handler-first').waypoint(function (direction) {
//   notify(this.element.id + ' hit 25% from top of window')
// }, {
//   offset: '25%'
// })


// For The Sticky Navigation
$(document).ready(function () {

  $('.js--section-fatures').waypoint(function (direction) {

    if (direction == 'down') {
      $('nav').addClass('sticky');
    }

    else {
      $('nav').removeClass('sticky');
    }

  },

    { offset: '60px' })

  // Scroll on buttons

  $('.js--scroll-to-start').click(function () {
    $('html, body').animate({
      scrollTop: $('.js--section-fatures').offset().top
    }, 1000); //1000 miliseconts == 1 second
  })



  // Navigation scroll 

  $(function () {
    $('a[href*=#]:not([href=#])').click(function () {
      if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
        var target = $(this.hash);
        target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
        if (target.length) {
          $('html,body').animate({
            scrollTop: target.offset().top
          }, 1000);
          return false;
        }
      }
    });
  });

  // Animations on Scroll

  $('.js--wp-1').waypoint(function (direction) {
    $('.js--wp-1').addClass('animated fadeIn');
  }, { offset: '50%' });

  $('.js--wp-2').waypoint(function (direction) {
    $('.js--wp-2').addClass('animated fadeInUp');
  }, { offset: '50%' });

  $('.js--wp-3').waypoint(function (direction) {
    $('.js--wp-3').addClass('animated fadeIn');
  }, { offset: '50%' });

  $('.js--wp-4').waypoint(function (direction) {
    $('.js--wp-4').addClass('animated pulse');
  }, { offset: '50%' });




// Mobile Navigation
$('.js--nav-icon').click(function() 
  
    {
      // switch(true) {
      // case ($('.js--nav-icon').is(":visible")):
  if ($('.js--nav-icon').is(":visible") || $('.js--nav-icon').css('display') == 'block' || $('.js--nav-icon').css("visibility") == "visible") {
        
      var nav = $('.js--main-nav');
      nav.slideToggle(200);
      // row.removeClass('a .js--nav-icon');
      // row.addClass('a .js--nav-icon-2');
      // 'element' is hidden
      $('.js--nav-icon').hide();
      $('.js--nav-icon-2').show();
      
      $('.js--nav-icon').css('display') = 'none';
      $('.js--nav-icon').css("visibility") = "hidden";
        }
      }
 
    );


$('.js--nav-icon-2').click(function() {

      switch (true) {
        
        case ($('.js--nav-icon-2').is(":visible")):
          var nav = $('.js--main-nav');
          nav.slideToggle(200);
          // row.removeClass('a .js--nav-icon-2');
          // row.addClass('a .js--nav-icon');
          
          $('.js--nav-icon-2').hide();
          $('.js--nav-icon').show();
          // location.reload(true);

          $('.js--nav-icon-2').css('display') = 'none';
          
          
          
    }
  }
);

  var a_href = 'x_is_visible';
$(window).resize(function () 
  {
    // This will execute whenever the window is resized
  
  if ($(window).width() >= 1005) {
    if ($('.js--nav-icon-2').is(":visible")){
    // if (a_href == 'x_is_visible'){
      a_href = 'x_was_visible';
     $('.js--nav-icon-2').hide(1);

    if ($('.js--main-nav').is(":hidden")) {
     $('.js--main-nav').show(1);} 
    
    }

    if ($('.js--nav-icon').is(":visible")) {
      a_href = 'l_was_visible';
      $('.js--nav-icon').hide(1);

      if ($('.js--main-nav').is(":hidden")) {
        $('.js--main-nav').show(1);
      }
    }

  }
});

  $(window).resize(function () {
    // This will execute whenever the window is resized
    
    if ($(window).width() < 1005) {
      if (a_href == 'x_was_visible') {
        a_href = 'x_is_visible';
        $('.js--nav-icon-2').show(10);
        
      }
    }
  });

     
  $(window).resize(function () {
    // This will execute whenever the window is resized

    if ($(window).width() < 1005) {
      if (a_href == 'l_was_visible') {
        a_href = 'l_is_visible';
        $('.js--nav-icon').show(10);

        if ($('.js--main-nav').is(":visible")) {
          $('.js--main-nav').hide(1);
        }
        
      }
      }
  });
});
