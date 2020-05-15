function resizeMenu() {
    $('.menu-row').each(function() {
        var cards_count = $(this).children('.menu-card').length;
        var card_width = $(window).width() * 0.85 / cards_count;
        $(this).children('.menu-card').width(card_width);
    });
};

$(document).ready(resizeMenu);
$(window).on('resize', resizeMenu);

$(document).ready(function() {
    $($('.menu-row')[0]).css('margin-top', '25px');
    $($('.menu-row')[$('.menu-row').length - 1]).css('margin-bottom', '25px');
    /*
    $('.menu-row').each(function() {
        for (var i = 1; i < $(this).children('.menu-card').length - 1; i++) {
            $($(this).children('.menu-card')[i]).css('margin-right', '25px').css('margin-left', '25px');
        }
    });
    */
    $('.menu-row').each(function() {
        $(this).children('.menu-card').css('margin-right', '12px').css('margin-left', '12px');
    });
});

for (var i = 1; i < $('.menu-row').length - 1; i++) {
    $($('.menu-row')[i]).css('margin-top', '25px').css('margin-bottom', '25px');
}
