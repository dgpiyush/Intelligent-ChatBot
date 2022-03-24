var text_box = '<div class="card-panel right" style="width: 75%; position: relative">' +
        '<div style="position: absolute; top: 0; left:3px; font-weight: bolder" class="title">{sender}</div>' +
        '{message}' +
        '</div>';

function scrolltoend() {
    $('#board').stop().animate({
        scrollTop: $('#board')[0].scrollHeight
    }, 800);
}

function send(sender, receiver, message) {
    $.post('/api/messages/', '{"sender": "'+ sender +'", "receiver": "'+ receiver +'","message": "'+ message +'" }', function (data) {
        console.log(data);
        var box = text_box.replace('{sender}', "You");
        box = box.replace('{message}', message);
        $('#board').append(box);
        scrolltoend();
        
    })
}

function send1(receiver, message) {
    $.post('/api/messages1/', '{"sender": "'+ 22 +'", "receiver": "'+ receiver +'","message": "'+ message +'" }', function (data) {
        console.log(data);
        var box = text_box.replace('{sender}', "You");
        box = box.replace('{message}', message);
        console.log(message);
        $('#board').append(box);
        scrolltoend();
    })
}

function sendfu(sender, message) {
    $.post('/ask', '{"sender": "'+ sender +'", "receiver": "'+ 22 +'","message": "'+ message +'" }', function (data) {
        console.log(data);
        var box = text_box.replace('{sender}', "You");
        box = box.replace('{message}', message);
        console.log(message);
        $('#messageText').val('');

        // $('#board').append(box);
        // scrolltoend();
        
    })
}

function receive() {
    $.get('/api/messages/'+ sender_id + '/' + receiver_id, function (data) {
        console.log(data);
        if (data.length !== 0)
        {
            for(var i=0;i<data.length;i++) {
                console.log(data[i]);
                var box = text_box.replace('{sender}', data[i].sender);
                box = box.replace('{message}', data[i].message);
                box = box.replace('right', 'left blue lighten-5');
                $('#board').append(box);
                scrolltoend();
            }
        }
    })
}


function receive1() {
    $.get('/api/messages1/'+ sender_id + '/' + receiver_id, function (data) {
        console.log(data);
        if (data.length !== 0)
        {
            for(var i=0;i<data.length;i++) {
                console.log(data[i]);
                var box = text_box.replace('{sender}', 'User-'+data[i].sender);
                box = box.replace('{message}', data[i].message);
                box = box.replace('right', 'left blue lighten-5');
                $('#board').append(box);
                scrolltoend();
            }
        }
    })
}

function receive2() {
    $.get('/api/messages1/'+ sender_id + '/' + receiver_id, function (data) {
        console.log(data);
        if (data.length !== 0)
        {
            const chatPanel = document.getElementById("chatPanel");

            for(var i=0;i<data.length;i++) {
                console.log(data[i]);
                $(".media-list").append('<li class="media"><div class="media-body"><div class="media"><div style = "color : white" class="media-body">' + data[i].message + '<hr/></div></div></div></li>');
                $(".fixed-panel").stop().animate({ scrollTop: $(".fixed-panel")[0].scrollHeight}, 1000);
                var ans= data[i].message;
                // msg.text = ans;
                console.log("htis is fdflsdjfljsd "+(data[i].message));
               
                // speechSynthesis.speak(msg);
            }
        }
    })
}
