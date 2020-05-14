function resizeMenu() {
    $('.menu-row').each(function() {
        var cards_count = $(this).length;
        var card_width = $(window).width * 0.85 / cards_count;
        $(this).width(cards_width);
    });
};

$(document).ready(resizeMenu);
$(window).on('resize', resizeMenu)