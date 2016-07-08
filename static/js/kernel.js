var board =  document.getElementById("board")
var editorElm = document.getElementById('codeTextarea');
var codeEditor = CodeMirror.fromTextArea(editorElm, {
    mode: "text/x-python",
    lineNumbers: true,
    theme:'default',
    content:codeTextarea.text
});
codeEditor.setSize("auto","auto")
function saveCode(ruleid,callback){
    $.ajax({
        type:'POST',
        url:'/policy/rule/'+ruleid,
        data:{
            'code':codeEditor.getValue()
            },
        complete:function(){
            console.log("save successed")
            if(callback)
                callback()
        },
        dataType:"json",
        beforeSend: function(xhr, settings){
                //var csrftoken = getCookie('csrftoken');
                //xhr.setRequestHeader("X-CSRFToken", csrftoken);
      },
    } )

}
codeEditor.on("keyup",function(target,e){
    if (e.keyCode=="13"){//ente
        saveCode()
    }
})

function runRule(){
     uri =  'http://{host}/api/kernels'.replace("{host}",window.location.host)
     $.ajax({
        type:'POST',
        url:uri,
        data:JSON.stringify({
            name:'python2'
        }),
        complete:function(response){
            kernel_id = response.responseJSON.id
            initsocket(kernel_id)
        },
        dataType:'json'
     })
}
function uuid() {
    var s = [];
    var hexDigits = "0123456789abcdef";
    for (var i = 0; i < 36; i++) {
        s[i] = hexDigits.substr(Math.floor(Math.random() * 0x10), 1);
    }
    s[14] = "4"; // bits 12-15 of the time_hi_and_version field to 0010
    s[19] = hexDigits.substr((s[19] & 0x3) | 0x8, 1); // bits 6-7 of the clock_seq_hi_and_reserved to 01
    s[8] = s[13] = s[18] = s[23] = "-";

    var uuid = s.join("");
    return uuid;
}
function initsocket(kernelid){
    ws_url = 'ws://{host}/api/kernels/{kernel_id}/channels'.replace('{host}',window.location.host).replace("{kernel_id}",kernelid)
    ws = new WebSocket(ws_url)
    ws.onopen = function(e){
        console.log("connect on websocket")
        ws.send(JSON.stringify(
        {
            'header': {
                'username': '',
                'version': '5.0',
                'session': '',
                'msg_id': uuid(),
                'msg_type': 'execute_request'
            },
            'parent_header': {},
            'channel': 'shell',
            'content': {
                'code':codeEditor.getValue(),
                'silent': false,
                'store_history': false,
                'user_expressions' : {},
                'allow_stdin' : false
            },
            'metadata': {},
            'buffers': {}
        }))
    }
    ws.onclose = function(e){}
    ws.onmessage = function(e){
        msg = JSON.parse(e.data)
        switch(msg.msg_type){
            case "stream":
                console.log(msg.content.text)
                board.innerHTML = msg.content.text
                interruptKernel(kernel_id)
        }
    }
    ws.onerror = function(e){}
}
function interruptKernel(kernel_id){
    uri =  'http://{host}/api/kernels/shutdown/{kernel_id}'.replace("{host}",window.location.host).replace("{kernel_id}",kernel_id)
    $.ajax({
        type:'POST',
        url:uri,
        complete:function(response){
            console.log("interrupt kernel: "+kernel_id+" succcess")
        },
        dataType:'json'
    })
}