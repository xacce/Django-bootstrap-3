var django = {
    "jQuery": jQuery
};


$(function () {
//    $('.vDateField').each(function () {
//        var field = $(this)
//        var html = $('<div class="row"><div class="col-lg-3"><input name="" class="ZebraDateField form-control" type="text" id="%s_join" size="8"></div>' +
//            '<div class="col-lg-2"><input name="" class="vTimeField form-control" type="text" id="%s_join" size="8"></div></div>')
//        html.insertAfter(field)
//        var datefield = html.find('.ZebraDateField')
//        var timefield = html.find('.vTimeField')
//
//        field.parents('form').on('submit', function () {
//            var val = field.val()
//            var time = $('#' + field.prop('id') + '_join').val()
//            field.attr('value', datefield.val() + ' ' + timefield.val())
//            return true
//        })
//    })

    djbo_reinit_for($('body'))

    // search
    $('#runsearch').on('click', function () {
        var input = $('#searchbar')
        $('#search_form').detach()
        var form = $('<form id="search_form"></form>')
        form.appendTo($('body'))
        input.clone(true).prop('id', '').appendTo(form)
        form.submit()
    })
//    $(".collapse").collapse()
//    $('.panel-collapse .panel-heading').on('click', function () {
//        $(this).next('.panel-body').show('fast')
//    })
})

function djbo_reinit_for(object) {

    object.find('.vIntegerField').mask('999999999999')
    object.find('.vDecimalField')
        .each(function () {
            var e = $(this)
            e.mask('0{1,' + e.attr('data-digits') + '}.0{1,' + e.attr('data-decimal-places') + '}')
        })

    var for_date = object.find('.ZebraDateField,.vDateField,.datetime_input input[name="datetime_0"]')
    var for_time = object.find('.vTimeField,.datetime_input input[name="datetime_1"]')
    if (for_date.length) for_date.Zebra_DatePicker({'format': 'Y-m-d'});
    if (for_time.length) for_time.timeEntry({show24Hours: true, spinnerImage: ''})
}