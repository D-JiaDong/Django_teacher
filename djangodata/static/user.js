function checkUserName(){
    uName = document.regForm.userName.value
    //  $ == jQuery  JSON对象
    $.ajax({
            url:'/checkUserName/',
            type: 'POST',
            data: JSON.stringify({
                userName: uName
            }),
            dataType: 'json',
            success: function (data) {
                // data = JSON.parse(data)
                if(data.result == 1){
                    alert("用户名已经存在!")
                }
            }
        }
    )
}