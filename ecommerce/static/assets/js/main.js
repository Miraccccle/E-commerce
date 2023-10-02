(function ($) {
    "use strict";
    
    // Dropdown on click
    $(document).ready(function () {
    function toggleNavbarMethod() {
        if ($(window).width() > 992) {
            $('.navbar .nav-item.dropdown').on('mouseover', function () {
                $(this).addClass('show');
            }).on('mouseout', function () {
                $(this).removeClass('show');
            });

            // Prevent closing sub-dropdowns when clicking inside
            $('.navbar .dropdown-menu').on('mouseover', function () {
                $(this).parent().addClass('show');
            }).on('mouseout', function () {
                $(this).parent().removeClass('show');
            });
        } else {
            $('.navbar .nav-item.dropdown').removeClass('show');
        }
    }
    toggleNavbarMethod();
    $('.navbar .dropdown-menu:last').on('click', function(event) {
    event.stopPropagation();
});


    $(window).resize(toggleNavbarMethod);
});





    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


    // Vendor carousel
    $('.vendor-carousel').owlCarousel({
        loop: true,
        margin: 29,
        nav: false,
        autoplay: true,
        smartSpeed: 1000,
        responsive: {
            0:{
                items:2
            },
            576:{
                items:3
            },
            768:{
                items:4
            },
            992:{
                items:5
            },
            1200:{
                items:6
            }
        }
    });


    // Related carousel
    $('.related-carousel').owlCarousel({
        loop: true,
        margin: 29,
        nav: false,
        autoplay: true,
        smartSpeed: 1000,
        responsive: {
            0:{
                items:1
            },
            576:{
                items:2
            },
            768:{
                items:3
            },
            992:{
                items:4
            }
        }
    });


    // Product Quantity
    $('.quantity button').on('click', function () {
        var button = $(this);
        var oldValue = button.parent().parent().find('input').val();
        if (button.hasClass('btn-plus')) {
            var newVal = parseFloat(oldValue) + 1;
        } else {
            if (oldValue > 0) {
                var newVal = parseFloat(oldValue) - 1;
            } else {
                newVal = 0;
            }
        }
        button.parent().parent().find('input').val(newVal);
    });
    
})(jQuery);

