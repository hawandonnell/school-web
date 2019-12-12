$(document).ready(() => {
    $('.nav_btn').click(() => {
        $('.sidebar').toggleClass('sidebar_hided');
    })
    $('.admin_icon').click(() => {
        window.location.replace('admin')
    })
});