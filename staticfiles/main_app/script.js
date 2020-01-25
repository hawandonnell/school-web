$(document).ready(() => {
    $('.sidebar').addClass('sidebar_hided')
    $('.nav_btn').click(() => {
        $('.sidebar').toggleClass('sidebar_hided');
    })
    $('.admin_icon').click(() => {
        window.location.replace('admin')
    })
    $('.search_icon').click(() => {
        $('.search__input').toggleClass('search__input_active')
    })
});