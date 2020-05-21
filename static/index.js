function resizeFirstTextContainer() {
    var height = $('.container-text').height();
    if($('.container-image').height() > $('.container-text').height()) {
        height = $('.container-image').height();
    }
    $('.main-text-container').height(height);
    var img_height = $('.container-image').height();
    console.log(img_height);
    var img_margin = height - img_height;
    console.log(img_margin);
    $('.container-image').css('margin-top', img_margin);
}

$(document).ready(resizeFirstTextContainer);
$(window).on('resize', resizeFirstTextContainer);