$(function () {
    djbo_youtubefield_init_for(false, $('body'))
    $(document).bind('djbo_update_for', djbo_youtubefield_init_for)

})

function djbo_youtubefield_init_for(event, object) {
    object.find('.youtube_field').each(function () {
        var e = $(this)
        var wrapper = e.parents('.youtube_field_wrapper')
        e.change(function () {
            var video_id = youtube_parser(e.val())
            if (video_id == undefined) {
                wrapper.find('.youtube_field_iframe').hide()
            }
            else {
                var iframe = wrapper.find('.youtube_field_iframe').attr('src', 'http://www.youtube.com/embed/' + video_id).data('original-url', e.val())
                iframe.load(function () {
                    $(this).show('fast')
                })
            }
        })


    })

}
function youtube_parser(url) {
    var regExp = /^.*((youtu.be\/)|(v\/)|(\/u\/\w\/)|(embed\/)|(watch\?))\??v?=?([^#\&\?]*).*/;
    var match = url.match(regExp);
    if (match && match[7].length == 11) {
        return match[7];
    } else {
        return undefined
    }
}