function showReservationMenu(tableId) {
    $('#reservation-menu-' + tableId).removeAttr('hidden');
    $('#book-table-link-' + tableId).remove();
}

function confirmTableBooking(tableId) {

    var reservationMenuElement = $('#reservation-menu-' + tableId);

    date = $(reservationMenuElement).find('.dtDate').val();

    fromHour = $(reservationMenuElement).find('.slcFromHour').val();
    fromMinute = $(reservationMenuElement).find('.slcFromMinute').val()

    toHour = $(reservationMenuElement).find('.slcToHour').val();
    toMinute = $(reservationMenuElement).find('.slcToMinute').val();

    if(toHour < fromHour) {
        alert("Некоррестное время.");
    }

    if(toHour == fromHour && toMinute < fromMinute) {
        alert("Некоррестное время.");
    }

    /*
    if(toHour == fromHour && toMinute == fromMinute) {
        alert("Некоррестное время.");
    }
    */

    if(toHour == fromHour && Math.abs(toMinute - fromMinute) < 15) {
        alert("Резрвавация стола не может составлять менее 15 минут.");
    }

    reservationAvailable = false;
    $.post("/reserveTable?tableId=" + tableId + "&date=" + date + "&fromHour=" + fromHour + "&fromMinute=" + fromMinute + "&toHour=" + toHour + "&toMinute=" + toMinute, function (data) {
        alert(data);
    });
}