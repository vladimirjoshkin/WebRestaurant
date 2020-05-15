$(document).ready(function() {
    $('.event-card').each(function() {
        if($(this).height() < $(this).children('img').height()) {
            $(this).height($(this).children('img').height());
        }
    });
    $($('.event-card')[$('.events-body').children('.event-card').length - 1]).css('border-bottom', '');
});

function repositionCards() {
    $('.event-card').each(function() {
        $(this).width($(window).width() * 0.85);
        var c_margin = $(window).width() * (1 - 0.85) / 2;
        $('.events-body').css('margin-left', c_margin).css('margin-right', c_margin);
    });
}

$(document).ready(repositionCards);
$(document).on('resize', repositionCards);