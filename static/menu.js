function resizeMenu() {
    $('.menu-row').each(function() {
        var cards_count = $(this).children('.menu-card').length;
        var card_width = ($(window).width() * 0.70 - 25 * cards_count) / cards_count;
        $(this).children('.menu-card').width(card_width);
    });
};

$(document).ready(resizeMenu);
$(window).on('resize', resizeMenu);

$(document).ready(function() {
    $('.menu-row').each(function() {
        $(this).css('margin-top', '25px').css('margin-bottom', '25px');
        $(this).children('.menu-card').css('margin-right', '12px').css('margin-left', '12px');
    });

    $($('.menu-row')[0]).css('margin-top', '25px').css('margin-bottom', '25px');
    $($('.menu-row')[$('.menu-row').length - 1]).css('margin-top', '25px').css('margin-bottom', '25px');
});

var added_products = [];

function addToCard(productId) {
    if (!added_products.includes(productId)) {
        added_products.push(productId);
    }
    document.cookie = "added_products=" + added_products;
}

/*
for (var i = 1; i < $('.menu-row').length - 1; i++) {
    $($('.menu-row')[i]).css('margin-top', '25px').css('margin-bottom', '25px');
}
*/
