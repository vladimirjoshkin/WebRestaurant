function positionFooterMainCenter() {
    var margin = ($('.footer-main').parent().width() - $('.footer-main').width()) / 2;
    $('.footer-main').css('margin-left', margin).css('margin-right', margin);

    var margin = ($('.container-copyright').parent().width() - $('.container-copyright').width()) / 2;
    $('.container-copyright').css('margin-left', margin).css('margin-right', margin);
}

$(document).ready(positionFooterMainCenter)
$(window).on('resize', positionFooterMainCenter)
