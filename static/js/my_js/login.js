$(function () {
    $("#submitBtn").click(function (event) {
        event.preventDefault();
         var username = $("input[name='username']").val();
         var password = $("input[name='password']").val();
         if(!username ||!password)
         {
          $("#login_form").removeClass('shake_effect');
          setTimeout(function()
          {
           $("#login_form").addClass('shake_effect')
          },1);
              var danger = $(".alert-danger")
              danger.text("请输入完整登陆信息~");
              danger.css('display','block');
              return;
          }

            zlajax.post({
            'url':'/login/',
            'data':{
                'username':username,
                'password':password
            },
            'success':function (result) {
                if(result['code']==200){
                     myfunc(username)
                }else{
                     var danger = $(".alert-danger");
                      danger.text(result['message']);
                      danger.css('display','block');
                }
            }
        });
    });
    $("#create").click(function (event) {
        event.preventDefault();
        var username = $("input[name='r_user_name']").val();
        var password = $("input[name='r_password']").val();
        if(!username ||!password)
         {
          $("#login_form").removeClass('shake_effect');
          setTimeout(function()
          {
           $("#login_form").addClass('shake_effect')
          },1);
              var danger = $(".alert-danger")
              danger.text("请输入完整注册信息~");
              danger.css('display','block');
              return;
          }
         zlajax.post({
            'url':'/regist/',
            'data':{
                'username':username,
                'password':password
            },
            'success':function (result) {
                if(result['code']==200){
                         var danger = $(".alert-danger");
                        danger.css('display','none');
                        var success = $(".alert-success");
                        success.text('注册成功,即将正在进入登陆页面~');
                        success.css('display','block');
                        setTimeout(function () {
                          window.location.href = '/login/'
                        },2000)
                }else{
                      var danger = $(".alert-danger");
                      danger.text(result['message']);
                      danger.css('display','block');
                }
            }
        });

    })
    $("#close_btn").click(function (event) {
        var user_id = $(this).attr('data-user-id');
        console.log(user_id);
        zlajax.post({
            'url':'/logout/',
            'data':{'user_id':user_id},
            'success':function (result) {
                if(result['code']==200){
                    logoutfunc(user_id);
                }else{
                    window.location.href = '/login/'
                }
            }
        })
    })
})
