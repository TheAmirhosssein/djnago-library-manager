function generateSlugFeild() {
    var title = $('#titleField').val();
    var slug = $('#slugField').val()
    if (slug === ''){
        key = title.replace(/ /g, "-");
        $('#slugField').val(key);
    }
}

function SendMessage() {
    const messageText = $('#messageText').val();
    $.get('/dashboard/send-message-in-admin/', {
        message_text: messageText,
    }).then(res => {
        console.log(res);
        $('#message_area').html(res);
        // document.getElementById('messageText').scrollIntoView({behavior: "smooth"});
    });
}

function showSlug() {
    var element = document.getElementById("slugFieldDiv");
    element.classList.toggle("hidden");
}