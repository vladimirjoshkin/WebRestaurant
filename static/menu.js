function resizeMenu() {
    $('.menu-row').each(function() {
        var cards_count = $(this).children('.menu-card').length;
        var card_width = ($(window).width() * 0.70 - 25 * cards_count) / cards_count;
        $(this).children('.menu-card').width(card_width);
        /*
        var max_height = 0;
        var cards_heights = [];
        var row_elements = $(this).children('.menu-card');
        for(i = 0; i < row_elements.length; i++) {
            cards_heights[i] = $(row_elements[i]).height();
        }
        console.log(row_elements);
        console.log(cards_heights);
        max_height = Math.max.apply(null, cards_heights);
        $(this).children('.menu-card').height(max_height);
        */
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
    $('#menu-card-bottom-area-' + productId).css('background-color', 'green')
    $('#link-add-to-card-' + productId).text('Добавлено');
}

/*
for (var i = 1; i < $('.menu-row').length - 1; i++) {
    $($('.menu-row')[i]).css('margin-top', '25px').css('margin-bottom', '25px');
}
*/
