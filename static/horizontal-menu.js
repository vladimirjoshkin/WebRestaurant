function resizeHorizontalMenu() {
    var bm_li_count = $('.bottom-menu-list li').length;
    var bm_li_new_width = $(window).width() / bm_li_count * 0.70;
    $('.bottom-menu-list').children('li').each(function() {
        $(this).width(bm_li_new_width);
    });
};

$(document).ready(resizeHorizontalMenu);
$(window).on('resize', resizeHorizontalMenu)