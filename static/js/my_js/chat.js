    var socket = io.connect('http://' + document.domain + ':' + location.port);

    function Mybtn() {
        var user_id = document.getElementById('user_id').innerText;
        var msg = $("#textarea").val();
        socket.emit('send_message',{data:msg,'send_id':user_id})
    }

    function myfunc(username) {
         socket.emit('newLogin',username,function (e) {
             window.location.href = '/'
         });
     }


     function logoutfunc(user_id) {
         socket.emit('newLogout',user_id,function (e) {
             window.location.href = '/login/'
         });
     }

     socket.on('newLogout_return',function (username) {
         var li = document.getElementsByClassName(username);
         for(var i =0;i<li.length;i++){
             li[i].remove();
         }
     })

    socket.on('newLogin_return',function (username) {
        $(".chat03_content ul").append("<li id='"+username+"'>\n" +
            "                                    <label class=\"online\">\n" +
            "                                    </label>\n" +
            "                                    <a href=\"javascript:;\">\n" +
            "                                        <img src=\"static/img/head/origin.jpg\"></a><a href=\"javascript:;\" class=\"chat03_name\">"+username+"</a>\n" +
            "                                </li>")
    });

//消息回复
     socket.on('recive_msg', function (res) {
         var g = res['msg']
          function h() {
				-1 != g.indexOf("*#emo_") && (g = g.replace("*#", "<img src='static/img/").replace("#*", ".gif'/>"), h())
			}
			h();
               var msgBox = $('.chat01_content');
               msgBox.append("<div class=\"message clearfix\"><div class=\"wrap-text\">" +
             "<h5 class=\"clearfix\">"+res['username']+"</h5><div>"+g+"</div></div><div class=\"wrap-ri\">" +
             "<div clsss=\"clearfix\"><span>"+res['create_time']+"</span>" +
             "</div></div><div style=\"clear:both;\"></div></div>");
            $(".chat01_content").scrollTop(msgBox[0].scrollHeight+220)
    });
