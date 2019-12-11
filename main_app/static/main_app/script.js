$(document).ready(() => {
    $('.nav_btn').click(() => {
        $('.sidebar').toggleClass('sidebar_hided');
    })
    $('.owl-carousel').owlCarousel({
        loop:true,
        items:1
    })
});