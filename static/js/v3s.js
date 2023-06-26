// Tab navigation

$("#video-url-tab-audio").click(()=>{
    document.getElementById("video-url-tab-video").classList.remove('active-video-url-tab-options');
    document.getElementById("video-url-tab-audio").classList.add('active-video-url-tab-options');

    document.getElementById("video-url-tab-container").style.display = "none";  
    document.getElementById("video-url-tab-audio-container").style.display = "block";
});

$("#video-url-tab-video").click(()=>{
    document.getElementById("video-url-tab-audio").classList.remove('active-video-url-tab-options');
    document.getElementById("video-url-tab-video").classList.add('active-video-url-tab-options');
    
    document.getElementById("video-url-tab-container").style.display = "block";  
    document.getElementById("video-url-tab-audio-container").style.display = "none";
});

$("#tab-options-vu").click(()=>{
    document.getElementById("tab-options-search").classList.remove('active-tab-options');
    document.getElementById("tab-options-playlist").classList.remove('active-tab-options');
    document.getElementById("tab-options-vu").classList.add("active-tab-options");

    document.getElementById('video-url-section').style.display="block";
    document.getElementById('searchby-section').style.display="none";
    document.getElementById('playlist-section').style.display="none";
})

$("#tab-options-search").click(()=>{
    document.getElementById("tab-options-search").classList.add('active-tab-options');
    document.getElementById("tab-options-playlist").classList.remove('active-tab-options');
    document.getElementById("tab-options-vu").classList.remove("active-tab-options");

    document.getElementById('video-url-section').style.display="none";
    document.getElementById('searchby-section').style.display="block";
    document.getElementById('playlist-section').style.display="none";
})

$("#tab-options-playlist").click(()=>{
    document.getElementById("tab-options-search").classList.remove('active-tab-options');
    document.getElementById("tab-options-playlist").classList.add('active-tab-options');
    document.getElementById("tab-options-vu").classList.remove("active-tab-options");

    document.getElementById('video-url-section').style.display="none";
    document.getElementById('searchby-section').style.display="none";
    document.getElementById('playlist-section').style.display="block";
})



let videoUrlSectionContainer = document.getElementById("video-url-section-container");



$("#video-url-btn").click(()=>searchVideoByUrl());


$("#search-video-btn").click(()=>searchVideoBtnClick())









function searchVideoByUrl(){
    if ($("#video-url").val().length === 0){
        Error(" *No video found", true, "error", "errorP",videoUrlSectionContainer);
 //video-url-section-container
        videoUrlSectionContainer.style.display = "none";
    }
    else {
        Error("", false);
        videoUrlSectionContainer.style.display = "block";
        new AjaxCalls().getBasicDetails($("#video-url").val())
    }
}

function searchVideoBtnClick(){
    let searchSectionContainer = document.getElementById("searchSection-container");

    if ($("#search-video-name").val().length === 0){
        //err, open, errorRoot="error", errorP = "errorP", sectionToHide=null
        Error(err=" *No video found", open=true, errorRoot="error-ss", errorP='errorP-ss');
        searchSectionContainer.style.display = "none";
    }
    else {
        Error("", false);
        searchSectionContainer.style.display = "block";

        new AjaxCalls().searchVideo($("#search-video-name").val())

        
    }
}


class removeSkeleton {

    removeImageSkeleton(id) {
        document.getElementById(id).classList.remove('img-skeleton');
    }

    removeCardSkeleton(id) {
        document.getElementById(id).classList.remove('card-skeleton');
    }

    removeTextSkeleton(id) {
        document.getElementById(id).classList.remove('text-skeleton');
    }
}


class searchSectionUpdate {
    constructor(data) {
        this.data = data;
    }

    update() {
        let ssCards = document.getElementById("search-section-cards");

        ssCards.innerHTML = "";


        this.data.forEach(d=>{
            let ssCard = document.createElement("div"); 
            ssCard.className = "search-section-card";

            let ssCardLeft = document.createElement("div");
            ssCardLeft.className = "search-section-card-left";

            let ssCardLeftImgCont = document.createElement("div");
            ssCardLeftImgCont.className = "search-section-card-left-img";
            ssCardLeftImgCont.innerHTML = `<img src='${d.thumbnail_url}' alt='${d.title}' />`;

            ssCardLeft.appendChild(ssCardLeftImgCont);

            ssCard.appendChild(ssCardLeft);

            let ssCardRight = document.createElement("div");
            ssCardRight.className = "search-section-card-right";

            let ssCardRightContent = document.createElement("div");
            ssCardRightContent.className = "search-section-card-right-content";

            let ssCardRightContentTitleP = document.createElement("p");
            ssCardRightContentTitleP.className = "ss-card-right-content-title";
            ssCardRightContentTitleP.innerHTML = d.title;

            let ssCardRightContentContainer = document.createElement("div");
            ssCardRightContentContainer.className = "ss-card-right-content-container";

            ssCardRightContentContainer.innerHTML = `<span id="ss-card-duration">${d['video-duration']}</span>
                                        <p id='ss-card-download-btn-${d.id}' videoUrl='${d.video_url}'>Download</p>`;


            ssCardRightContent.appendChild(ssCardRightContentTitleP);
            ssCardRightContent.appendChild(ssCardRightContentContainer);

            ssCardRight.appendChild(ssCardRightContent);

            ssCard.appendChild(ssCardRight);

            ssCards.append(ssCard);


            $("#ss-card-download-btn-"+d.id).click(()=>{
                console.log(d.video_url);

                document.getElementById("tab-options-search").classList.remove('active-tab-options');
                document.getElementById("tab-options-playlist").classList.remove('active-tab-options');
                document.getElementById("tab-options-vu").classList.add("active-tab-options");

                document.getElementById('video-url-section').style.display="block";
                document.getElementById('searchby-section').style.display="none";
                document.getElementById('playlist-section').style.display="none";
            

                $("#video-url").val(d.video_url);

                let videoUrlSectionContainer = document.getElementById("video-url-section-container");

                if ($("#video-url").val().length === 0){
                    Error(" *Invalid Url", true);
                    videoUrlSectionContainer.style.display = "none";
                }
                else {
                    Error("", false);
                    videoUrlSectionContainer.style.display = "block";

                    new AjaxCalls().getBasicDetails($("#video-url").val());

                    new AjaxCalls().getStreamedData($("#video-url").val());

                }
            })



        })

    }

}


class updateBasicDetails {
    constructor(data) {
        try{
            this.title = data.title.title;
            this.thumbnail_url = data.thumbnail_url.thumbnail_url;
            this.duration = data.duration;
        }
        catch(e) {
            this.audio_data = data.audio_itag;
            this.video_data = data.video_itag;
        }
        this.removeSkeleton = new removeSkeleton();
    }
    
    updateBasicDetails() {
        this.removeSkeleton.removeTextSkeleton("video-title-id");
        document.getElementById('video-title').innerHTML = this.title;
        document.getElementById('video-duration').innerHTML =  `Duration: <span>${this.duration}</span>`;

        this.removeSkeleton.removeImageSkeleton("video-url-section-image");
        document.getElementById('video-url-section-image').innerHTML = `<img src='${this.thumbnail_url}' alt='${this.title}' />`
    }

    createAudioVideoCards(rootTag, data, cardClass, type) {

        let cardItems = document.createElement('div');
        cardItems.classList.add(cardClass);
        cardItems.setAttribute('itag', data['itag']);

        cardItems.id="card-"+type+data['itag'];

        let typeP = document.createElement("p");
        let resP = document.createElement("p");
        let icon = document.createElement("span");

        typeP.innerHTML = (type === "video") ? data['mime_type'] : (data['mime_type'] === 'mp4') ? "mp3" : data['mime_type'];
        resP.innerHTML = (type === 'video') ? data['res'] : data['abr'] ;
        
        if (type==='video') {
            if (data['as_audio'] === true) {
                icon.className = "video-url-card-items-volume-up";
                icon.innerHTML = `<i class='fa fa-volume-high'> </i>`;
            }
            else {
                icon.className = "video-url-card-items-volume-mute";
                icon.innerHTML = `<i class='fa fa-volume-mute'> </i>`;
            }
        }
        else {
            icon.className = "video-url-card-items-volume-up";
            icon.innerHTML = `<i class='fa fa-volume-high'> </i>`;
        }

        cardItems.appendChild(typeP);
        cardItems.appendChild(resP);
        cardItems.appendChild(icon);

        rootTag.appendChild(cardItems); 

        $("#card-"+type+data['itag']).click(function () { 
            //console.log(data['itag'])
            new AjaxCalls().downlaodByItag(data['itag'], $("#video-url").val())
        });  
    }

    updateStreamsData() {
        try {
            this.removeSkeleton.removeCardSkeleton("video-url-tab-cards");
        }
        catch (e) {}

        let videoStreamTag = document.getElementById("video-url-tab-cards");
        try {
            videoStreamTag.innerHTML = "";
            this.video_data.forEach(vd => {
                //console.log(vd)
                this.createAudioVideoCards(videoStreamTag, vd, "video-url-card-items", "video")
            });
        }
        catch (e) {
            videoStreamTag.innerHTML = `
                <div class='error' id='video-url-tab-cards-error'>
                    <p class='errorP' id='video-url-tab-cards-errorP'>No data found</p>
                </div>
            `;
            Error(" *No data found", true, 'video-url-tab-cards-error', 'video-url-tab-cards-errorP', null);
        }

        try {this.removeSkeleton.removeCardSkeleton("audio-url-tab-cards");}
        catch (e) {}

        let audioStreamTag = document.getElementById("audio-url-tab-cards");

        try {
            audioStreamTag.innerHTML = "";
            this.audio_data.forEach(ad => {
            //console.log(ad)
                this.createAudioVideoCards(audioStreamTag, ad, "video-url-card-items", "audio")
            });
        }
        catch (e) {
            audioStreamTag.innerHTML = `
                <div class='error' id='audio-url-tab-cards-error'>
                    <p class='errorP' id='audio-url-tab-cards-errorP'>No data found</p>
                </div>
            `;
            Error(" *No data found", true, 'audio-url-tab-cards-error', 'audio-url-tab-cards-errorP', null);
        }        

    }

}


class AjaxCalls {
    downlaodByItag(itag, video_url){
        $.ajax({
            type: "POST",
            url: "/downloadByItag",
            data: JSON.stringify({
                "video-url": video_url,
                "itag": itag
            }),
            contentType: "application/json",
            dataType: 'json',
            success: function (response) {
                //console.log(response)
                let a = document.createElement("a");    
                a.href = response['url'];
                a.target = "_blank";
                a.click();
            }
        });
    }

    getBasicDetails(video_url){
        $.ajax({
            type: "POST",
            url: "/getBasicDetails",
            data: JSON.stringify({
                "video-url": video_url
            }),
            contentType: "application/json",
            dataType: 'json',
            success: function (response) {
                console.log(response)
                if (response['status']) {
                    new updateBasicDetails(response).updateBasicDetails();
                    new AjaxCalls().getStreamedData($("#video-url").val())
                }
                else {
                    //err, open, errorRoot="error", errorP = "errorP"
                    Error(" *Invalid Url", true, "error", "errorP" ,videoUrlSectionContainer);
                }
            }
        });
    }

    getStreamedData(video_url){
        $.ajax({
            type: "POST",
            url: "/getStreamsData",
            data: JSON.stringify({
                "video-url": video_url
            }),
            contentType: "application/json",
            dataType: 'json',
            success: function (response) {
                console.log(response)
                if (response['status']) {
                    new updateBasicDetails(response).updateStreamsData();
                }
                else {
                    
                    document.getElementById("video-url-tab-cards").innerHTML = `
                        <div class='error' id='video-url-tab-container-error'>
                            <p class='errorP' id='video-url-tab-container-errorP'>${response['error']}</p>
                        </div>
                    `;
                    document.getElementById("audio-url-tab-cards").innerHTML = `
                        <div class='error' id='video-url-tab-audio-container-error'>
                            <p class='errorP' id='video-url-tab-audio-container-errorP'>${response['error']}</p>
                        </div>
                    `;

                    Error(response['error'], true, 'video-url-tab-container-error', 'video-url-tab-container-errorP');
                    Error(response['error'], true, 'video-url-tab-audio-container-error', 'video-url-tab-audio-container-errorP');
                }
            }
        });
    }

    searchVideo(video_name){
        $.ajax({
            type: "POST",
            url: "/searchVideo",
            data: JSON.stringify({
                "search-video-name": video_name
            }),
            contentType: "application/json",
            dataType: 'json',
            success: function (response) {
                console.log(response)
                if (response['status']) {
                    new searchSectionUpdate(response['search_data']).update();
                }
                else {
                    Error(" *Invalid Url", true);
                }
            }
        });
    }
}

function Error(err=" *Not found", open=false, errorRoot="error", errorP = "errorP", sectionToHide=null) {
    if (open) {
        (sectionToHide != null) ? videoUrlSectionContainer.style.display = "none" : null;
        document.getElementById(errorRoot).style.display = "block";
        document.getElementById(errorP).innerHTML = err;
    }
    else {
        document.getElementById(errorRoot).style.display="none";
    }
}