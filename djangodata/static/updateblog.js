function updateblog(blogId, state, opr){
    blogTitle = document.blogForm.blogTitle.value
    blogContent =  blogEditor.getData()
    blogTips = document.blogForm.blogTips.value
    blogClassId = document.blogForm.blogClassId.value
    blogId = document.blogForm.blogId.value

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
                if(opr == 'update'){
                    $('#modal-update').modal()
                    uBlog = data.uBlog
                    params = data.params
                    document.blogForm.blogTitle.value = uBlog.blogtitle
                    document.blogForm.blogId.value =  uBlog.blogid
                    document.blogForm.blogContent.value = uBlog.blogcontent
                    document.blogForm.blogTips.value =  uBlog.blogtips

                    classid = uBlog.classid
                    bcObj = $('#blogClassId')
                    blogClassList = data.params.blogClassList
                    text = ""
                    bcObj.empty()
                    for(i=0; i<blogClassList.length; i ++){
                        if(classid == blogClassList[i].classid){
                             text += '<option selected="selected" value="' + blogClassList[i].classid + '">' + blogClassList[i].classname + '</option>'
                        }else{
                             text += '<option value="' + blogClassList[i].classid + '">' + blogClassList[i].classname + '</option>'
                        }

                    }
                    bcObj.append(text)

                }else if(opr == 'submitUpdate'){
                    if(data.result == 1){
                        alert('修改成功')
                    }else{
                        alert('修改失败')
                    }
                }


           }
        }
    )
}
$(document).ready(
    function(){
        updateblog(0, 0, 'update')
    }
)