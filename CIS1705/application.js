function select_semester(id) {
    $('.semester-details').hide();
    $('.semester-tab.current').removeClass('current');
    $(id).show();
    $(id + '-tab').addClass('current');
}

function click_handler(ev) {
    ev.preventDefault();
    var link = $(this);
    select_semester(link.attr('href'));
}

$(document).ready(function() {
    select_semester('#semester1');
    $('a.semester-tab').on('click', click_handler);
});
