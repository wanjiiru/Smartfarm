$(document).ready(function(){
    // Collapse Navbar when the scroll is triggered
    var navbarCollapse = function () {
        if ($("#navMain").offset().top > 100) {
            $("#navMain").addClass("navbar-shrink");
        } else {
            $("#navMain").removeClass("navbar-shrink");
        }
    };
    // Collapse the nav bar if page is not at the top
    navbarCollapse();
    // Collapse the navbar when there is scroll activity
    $(window).scroll(navbarCollapse);

    $('.close-nav').click(function(){
        document.getElementById("sideNav").style.width = "0";
    })

    $('.open-nav').click(function(){
        document.getElementById('sideNav').style.width = "290px";
    })

})
