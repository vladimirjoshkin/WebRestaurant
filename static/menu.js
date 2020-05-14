function resizeMenu() {
    $('.menu-row').each(function() {
        var cards_count = $(this).children('.menu-card').length;
        var card_width = $(window).width() * 0.85 / cards_count;
        $(this).children('.menu-card').width(card_width);
    });
};

$(document).ready(resizeMenu);
$(window).on('resize', resizeMenu);
