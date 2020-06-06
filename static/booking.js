function showReservationMenu(tableId) {
    $('#reservation-menu-' + tableId).removeAttr('hidden');
    $('#book-table-link-' + tableId).remove();
}

function confirmTableBooking(tableId) {

    date = $('#dtDate').val();

    fromHour = $('#slcFromHour').val();
    fromMinute = $('#slcFromMinute').val();

    toHour = $('#slcToHour').val();
    toMinute = $('#slcToMinute').val();

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