function resizeHorizontalMenu() {
    var bm_li_count = $('.bottom-menu-list li').length;
    var bm_li_new_width = $('header').width() / bm_li_count * 0.70 - $('.logo-img').width();
    $('.bottom-menu-list').children('li').each(function() {
        $(this).width(bm_li_new_width);
    });

    var margin = ($('header').width() - $('.top-menu').width()) / 2;
    $('.top-menu').css('margin-left', margin).css('margin-right', margin);
};


$(document).ready(resizeHorizontalMenu);
$(window).on('resize', resizeHorizontalMenu)

/*
function resizeHeader() {
    $('header').width($(window).width());
}

$(document).ready(resizeHeader);
$(window).on('resize', resizeHeader)
*/