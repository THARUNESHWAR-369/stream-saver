$("#audio-download-btn").click(()=>{
    $("#video-download-btn").removeClass('btn-active');
    $("#audio-download-btn").addClass('btn-active');

    $(".audio-download-container").css('display', 'block');
    $(".video-download-container").css('display', 'none');
});

$("#video-download-btn").click(()=>{
    $("#audio-download-btn").removeClass('btn-active');
    $("#video-download-btn").addClass('btn-active');
    
    $(".video-download-container").css('display', 'block');
    $(".audio-download-container").css('display', 'none');
});

function showLoader() {
    $("#loader").css('display', 'block');
}

function hideLoader() {
    $("#loader").css('display', 'none');
}

function footerAnim(anim) {
    if (anim) {
        $(".footer").css('bottom', null);
        document.querySelector('.footer').style.bottom = null;
        $('.footer').css('margin-top', '2rem')
    }
    else {
        $(".footer").css('bottom', '0px');
        $('.footer').css('margin-top', '0rem')
    }
}

function updateVideoData(video_data) {
    let video_download_options_container = document.getElementById('video-download-options-container');
    
    for(var vd in video_data) {

        let a = document.createElement('a');
        a.id = 'textId';
        a.target = '_blank';
        a.href= video_data[vd][0];

        let span = document.createElement('span');
        
        let span_p = document.createElement('p');
        span_p.id = 'quality';
        span_p.innerHTML = video_data[vd][2]+"P";

        let span_p_icon = document.createElement('p');
        if (video_data[vd][5] != null) {
            span_p_icon.id = "volume-icon-mute";
            span_p_icon.innerHTML = `<i class="fa fa-volume-mute" aria-hidden="true"></i>`;
        }
        else {
            span_p_icon.id = "volume-icon";
            span_p_icon.innerHTML = `<i class="fa fa-volume-up" aria-hidden="true"></i>`;
        }
        let span_p_type = document.createElement('p');
        span_p_type.id="option-type";
        span_p_type.innerHTML = video_data[vd][1];

        a.appendChild(span_p)
        a.appendChild(span_p_icon)
        a.appendChild(span_p_type)
        span.appendChild(a)
        

        video_download_options_container.appendChild(span)
    }
}

function updateAduioData(audio_data) {
    let audio_download_options_container = document.getElementById('audio-download-options-container');
    
    for(var vd in audio_data) {
        let a = document.createElement('a');
        a.id = 'textId';
        a.target = '_blank';
        a.href= audio_data[vd][0];

        let span = document.createElement('span');
        
        let span_p = document.createElement('p');
        span_p.id = 'quality';
        span_p.innerHTML = audio_data[vd][2]+"P";

        let span_p_icon = document.createElement('p');
        span_p_icon.id = "volume-icon";
        span_p_icon.innerHTML = `<i class="fa fa-volume-up" aria-hidden="true"></i>`;
        
        let span_p_type = document.createElement('p');
        span_p_type.id="option-type";
        span_p_type.innerHTML = audio_data[vd][3];

        a.appendChild(span_p)
        a.appendChild(span_p_icon)
        a.appendChild(span_p_type)
        span.appendChild(a)

        audio_download_options_container.appendChild(span)
    }
}

function updateDownloadsOptions(download_data) {
    updateVideoData(download_data['video_download_data']);
    updateAduioData(download_data['audio_download_data']);
}

function updateData(v_meataData) {

    // updated Thumbnail 
    $("#thumb").attr('src', v_meataData['meta']['thumb']);
    $("#thumb").click(()=>{
        let a = document.createElement('a');
        a.href = v_meataData['meta']['source'];
        a.target = "_blank";
        a.click();
    })

    // update description
    $("p#video-name").html(v_meataData['meta']['title']);
    $("p#video-duration").html(v_meataData['meta']['duration']);
}

$("#searchMovie").click(()=>{
    showLoader()
    $.ajax({
        type: "POST",
        url: "/",
        data: { "video_url": $("#video_url").val() }, 
        success: function(data) {
            console.log("Request successful, response received:", data);

            if (data['status']) {
                $(".error").css('display', 'none');
                $("p#error-p").html("");
                footerAnim(true);

                // display content
                $(".content").css('display', 'block');

                updateData(data);
                document.getElementById('video-download-options-container').innerHTML = "";
                document.getElementById('audio-download-options-container').innerHTML = "";
                updateDownloadsOptions(data)
                hideLoader()
            }
            else {
                $(".content").css('display', 'none');
                $(".error").css('display', 'block');
                $("p#error-p").html(data['error']);
                footerAnim(false);
                hideLoader()
            }

        },
        error: function(xhr, status, error) {
            console.error("Error:", error);
        }
    });

})

footerAnim(false)