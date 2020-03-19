// Foundation JavaScript
// Documentation can be found at: http://foundation.zurb.com/docs
$(document).foundation({
  equalizer : {
    // Specify if Equalizer should make elements equal height once they become stacked.
    equalize_on_stack: true
  }
});



// Change Date on Bottom of footer automagically
  var currentYear = (new Date).getFullYear();
  $(document).ready(function() {
  $("#year").text( (new Date).getFullYear() );
  })

// Course show/hide javascript

if ($("a.syllabus-toggle")[0])  
{
    $('.syllabus').hide();
    
    $('a.syllabus-toggle').click(function() {
    
        if ($(this).text()=='show description') {   
            $(this).text('hide description');
        } else {
            $(this).text('show description');
        }
            
        $(this).next().slideToggle(500);
        
        return false;
    
    });

};

// Staff Contacts "Search" and 'Filter by "x"'' javascript


    $("#filter").keyup(function () {
        
        //alert('woah');
        
        var filter = $(this).val();
        
        /*
        $("div.staff-contact").each(function () {
            if (filter == '') {
                $(this).removeAttr("style");
            } else {
                $(this).attr("style","display:none");
            }
        });
        */
        
        $("div.staff-contact").each(function () {
            if ($(this).text().search(new RegExp(filter, "i")) < 0) {
                $(this).attr("style","display:none");
                $(this).next("hr").attr("style","display:none");
            } else {
                $(this).removeAttr("style");
                $(this).next("hr").removeAttr("style");
            }
        });
        
        
      //  $("#filter-count").text(count);
      
    });




// Slider Settings - http://kenwheeler.github.io/slick/
if ($(".slider-hp")[0])
{
    $(".slider-hp").slick({
        autoplay: true,
        autoplaySpeed: 8000, // Rotation Speed
        speed: 300, // Transition Speed
        fade: true,
        responsive: [{
            breakpoint: 1024,
            settings: {
                arrows:false
            }
        }, {
            breakpoint: 642,
            settings: {
                arrows:false
            }
        }, {
            breakpoint: 400,
            settings: {
                arrows:false
            } 
        },

        ],
    })

    // Animate headers in slider
        .on('beforeChange', function (event, slick, currentSlide, nextSlide) {
        // console.log('before change');
        $("div.slider-text-container > h2#text-animate-" + currentSlide).css("opacity", "0.001");
        $("div.slider-text-container > h3#text-animate-" + currentSlide).css("opacity", "0.001");
    })

        .on('afterChange', function (event, slick, currentSlide, nextSlide) {
        // console.log('after change');
        $("div.slider-text-container > h2#text-animate-" + currentSlide).css("opacity", "1");
        $("div.slider-text-container > h3#text-animate-" + currentSlide).css("opacity", "1");
    });

    $(document).ready(function () {
        // console.log('on ready');
        $("div.slider-text-container > h2#text-animate-" + currentSlide).css("opacity", "1");
        $("div.slider-text-container > h3#text-animate-" + currentSlide).css("opacity", "1");
    });

    var currentSlide = $('.slider-hp').slick('slickCurrentSlide');
};

// jQuery-lazyload-any - https://github.com/emn178/jquery-lazyload-any

    // Homepage Video - Uncomments code when player scrolls into view
if ($(".lazyload-jw-video")[0])
{
    $('.lazyload-jw-video').lazyload();
}
// Foundation JavaScript
// Documentation can be found at: http://foundation.zurb.com/docs
$(document).foundation();

// Reloads the foundation script so the mega menu partial can swap out
if( document.getElementById('scoped-content') != null )
{
    $("#scoped-content").on("replace", function() {
    $(document).foundation();
    });
};

            // $(".off-canvas-submenu").hide();
                $(".off-canvas-submenu-call").click(function(e) {
                    e.preventDefault();

                     // var icon = $(this).parent().next(".off-canvas-submenu").is(':visible') ? '.fa-chevron-circle-up' : '.fa-chevron-circle-down';
                     // $(this).parent().next(".off-canvas-submenu").slideToggle('fast');
                     // $(this).find("i").toggleClass('fa-rotate-90');
                     $(this).parent().toggleClass('closed open');
                     $(this).siblings("ul.off-canvas-submenu").slideToggle('fast');
                });

                $(".active").parents('.off-canvas-submenu').show(); 
                // $(".active").parent().siblings(".off-canvas-submenu-call").find("i").toggleClass('fa-rotate-90');
                // $(".active").parent().siblings(".off-canvas-submenu-call").parent().toggleClass('tester-to-go');

// Profile anchor fix conflicting with right show/hide nav

jQuery( document ).ready(function( $ ) {

$('.profile-content a[href^="#"]').not('a[href="#"]').on('click', function(event) {
var anchor_href = $(this).attr('href');
anchor_href = anchor_href.slice(1);
var target = $('a[name^="' + anchor_href + '"]');
    if( anchor_href.length ) {
        event.preventDefault();
        $('html, body').animate({
            scrollTop: target.offset().top
        }, 500);
    }
}); // end .profile-content

}); // end jQuery( document ).ready



