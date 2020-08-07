function writeblog(blogId, state, opr){
    blogTitle = document.blogForm.blogTitle.value
    blogContent =  blogEditor.getData()
    blogTips = document.blogForm.blogTips.value
    blogClassId = document.blogForm.blogClassId.value
    //  $ == jQuery  JSON对象
    $.ajax({
            url:'/bloglist/',
            type: 'POST',
            data: JSON.stringify({
                blogTitle: blogTitle,
                blogId: blogId,
                blogContent: blogContent,
                blogTips: blogTips,
                blogClassId: blogClassId,
                blogState: state,
                opr: opr,
            }),
            dataType: 'json',
            success: function (data) {
                // data = JSON.parse(data)
                if(opr == 'goAdd'){
                    bcObj = $('#blogClassId')
                    blogClassList = data.params.blogClassList
                    text = ""
                    bcObj.empty()
                    for(i=0; i<blogClassList.length; i ++){
                        text += '<option value="' + blogClassList[i].classid + '">' + blogClassList[i].classname + '</option>'
                    }
                    bcObj.append(text)
                }else if(opr == 'add'){
                    if(data.result == 1){
                        alert('发布成功')
                    }else{
                        alert('发布失败')
                    }
                }


           }
        }
    )
}

$(document).ready(
    function(){
        writeblog(0, 0, 'goAdd')
    }
)