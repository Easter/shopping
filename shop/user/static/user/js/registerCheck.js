





 $(function() {  
     
    $(".errorClass").each(function() {  
        showError($(this)); 
      
}



function checkUsername()
{
    //判断用户名的长度
    var id = document.getElementById("usernamesignup");
    var username=id.value;    
    if(username.length > 10 || username.length < 3)
    {
      document.getElementById(id.name).innerHTML = "输入的用户名需要在3 ～ 10之间";
      return false;
    } 
    else
    return true;
}




 




 $.ajax({  
        url:"项目名称/UserServlet",
        data:{method:"ajaxValidateLoginname", usernamesignup:value}, 
        type:"POST",  
        dataType:"json",  
        async:false, 
        cache:false,  
        success:function(result) {  
            if(!result) {  
                $("#" + id + "Error").text("用户名已被注册！");  
                showError($("#" + id + "Error"));  
                return false;  
            }  
        }  
    });  
    return true;  
}  














 

function checkPassword()
{
    var password = document.getElementById("passwordsignup").value;    
    return true;
}
function checkPassword2()
{
     var id=document.getElementById("passwordsignup");
     var id2=document.getElementById("passwordsignup_confirm");
     var password = id.value;    
     var password2 = id2.value;
     if(password!=password2)
     {
        document.getElementById(err_id2).innerHTML="密码不一致";
        return false;
     }
     return true;    
}









function confirm(){ 
  var tel=$username.val(); 
  var pwd=$password.val(); 
 
     $.ajax({ 
       url:config.baseServerUrl + 'http://mtest.lihs.me/test/api/user/login',//相对应的esb接口地址
       type:'post',  
       data:{mobile:tel,password:pwd}, 
       success:function(data){ 
         if(data.success){ 
           var customerId = data.attr.usernameInfo.id;  
           sessionStorage.username = username; 
           window.location.href='https://www.baidu.com'; 
         else{ 
           if(tel != data.tel){ 
             alert(data.message); 
             $tel.val(""); 
             $pwd.val(""); 
             return false; 
            } 
            if(pwd != data.pwd){ 
             alert(data.message); 
             $pwd.val(""); 
             return false; 
            } 
         } 
       } 
    }) 
  } 
}




/*function jumpTo(p, url) { 
   var customerId=sessionStorage.username; 
   if (customerId == undefined) { 
     p.attr("href", "http://mtest.lihs.me/test/api/user/login"); 
<span style="white-space:pre">  </span>}

 else { 
      p.attr("href", url); 
    } 
} 
 function infoJumpTo() { 
   var $info = $("#info"); 
   jumpTo($info, "http://localhost/page/AmountAscension/amountAscension.html"); 
} 
 function starJumpTo() { 
   var $star = $("#star"); 
   jumpTo($star, "http://localhost/page/MyAccount/myAccount.html"); 
 }

*/
 
function login(){ 
var userName=document.getElementById("username").value; 
var pwd=document.getElementById("passwordsignup").value; 
var repwd=document.getElementById("passwordsignup_confirm").value; 
var matchResult=true; 
if(userName==""||pwd==""||repwd==""||address==""){ 
alert("请确认是否有空缺项！"); 
matchResult=false; 
}else if(userName.length<6||userName.length>20){ 
alert("用户名长度应在6到20个字符之间！"); 
matchResult=false; 
}else if(pwd != repwd){ 
alert("两次输入的密码不相同！"); 
matchResult=false; 
}else if(pwd.length<6||pwd.length>20||repwd.length<6||repwd.length>20){ 
alert("密码或重复密码长度应在6到20个字符之间！"); 
matchResult=false; 
}else if(pwd!=repwd){ 
alert("密码和重复密码不同，请重新输入！"); 
matchResult=false; 
}else if(userName.length<6||userName.length>20){ 
alert("用户名长度应在6到20个字符之间！"); 
matchResult=false; 
} 

if(matchResult==true){ 
var mailreg = /^\w+@\w+(\.\w+)+$/; 
if(!address.match(mailreg)){ 
alert("邮箱格式不正确"); 
matchResult=false; 
} 
} 

 

return matchResult; 
} 
