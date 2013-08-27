$(function () {
    //var tmpl = $('.xapload_tmpl')
    $('.xapload_add_input').on('change', function () {
        var e = $(this)
        var input = e[0]
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function (event) {
                var tmpl = e.parents('.xapload_gallery').find('.xapload_tmpl').clone()
                tmpl.removeClass('xapload_tmpl').addClass('xapload_wrapper')
                tmpl.find('.xapload_image').attr('src', event.target.result)
                tmpl.insertBefore(e.parents('.xapload_wrapper')).show()
                var url = e.parents('.xapload_gallery').data('upload_url')

                var formData = new FormData(e.parents('.xapload_add_form form')[0]);

                $.ajax({
                    url: url,
                    type: 'POST',
                    xhr: function () {  // custom xhr
                        myXhr = $.ajaxSettings.xhr();
                        if (myXhr.upload) {
                            myXhr.upload.addEventListener('progress', progressHandlingFunction, false);
                        }
                        return myXhr;
                    },
                    success: function (result) {
                        tmpl.data('delete_url', result['delete_url'])
                        tmpl
                            .fadeOut(400, function () {
                                tmpl.find('.xapload_image').attr('src', '/crop/140/140/' + result['path'])
                            })
                            .fadeIn(400);
                    },
                    data: formData,
                    cache: false,
                    contentType: false,
                    processData: false
                });

                function progressHandlingFunction(e) {
                    if (e.lengthComputable) {
                        var bar = tmpl.find('.xapload_progress')
                        var prs = e.loaded / e.total * 100
                        bar.find('.xapload_progress_text').text((Math.round(prs)) + '%')
                        bar.css('width', prs + '%')
                        if (prs == 100) {
                            // bar.hide()

                        }
                    }
                }
            }
            reader.readAsDataURL(input.files[0]);
        }


    })
    $('.xapload_gallery').on('click', '.xapload_remove', function () {
        var e = $(this).parents('.xapload_wrapper')
        $.getJSON(e.data('delete_url'), function (result) {
            e.fadeOut('fast', function () {
                $(this).detach()
            })

        })
    })
})