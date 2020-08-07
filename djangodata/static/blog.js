function blog(pageSize, currentPage, blogId, opr){
    cName = document.classForm.blogTitle.value
    state = 0
    if(opr == 'publish'){
        state = 1
    }else if(opr == 'cancel'){
        state = 4
    }
    //  $ == jQuery  JSON对象
    $.ajax({
            url:'/bloglist/',
            type: 'POST',
            data: JSON.stringify({
                blogTitle: cName,
                pageSize: pageSize,
                currentPage: currentPage,
                blogState: state,
                blogId: blogId,
                opr: opr,
            }),
            dataType: 'json',
            success: function (data) {
                // data = JSON.parse(data)
                if(opr == 'update'){

                }else{
                    bodyObj = $('#bodyData')
                    params = data.params
                    text = ""
                    bodyObj.empty()
                    for(i=0; i<data.data.length;i++){
                        text += "<tr><td>" + data.data[i].blogid + "</td>" +
                            "<td>" + data.data[i].blogtitle + "</td>" +
                            "<td>" + data.data[i].blogsummary + "</td>" +
                            "<td>" + data.data[i].blogtips + "</td>" +
                            "<td>" + data.data[i].classid__classname + "</td>" +
                             "<td>" + data.data[i].userid__username + "</td>"
                        if(data.data[i].blogstate == 1){
                             text += "<td>已发布</td>"
                        }else if(data.data[i].blogstate == 2){
                             text += "<td>审核中</td>"
                        }else if(data.data[i].blogstate == 3){
                             text += "<td>草稿</td>"
                        }else if(data.data[i].blogstate == 4){
                             text += "<td>已撤销</td>"
                        }

                        text += "<td>" +
                            "<button type='button'  class='btn-primary btn-sm' onclick=\"javascript:document.location.href='/goupdateblog/?blogId=" + data.data[i].blogid +"&opr=update\';\">修改</button>"  +
                            "<button  type='button'  class='btn-info btn-sm' onclick=\"blog(" + params.pageSize + ',' + params.currentPage + ' , ' +data.data[i].blogid + ",'publish')\">发布</button>"  +
                            "<button  type='button'  class='btn-danger btn-sm' onclick=\"blog(" + params.pageSize + ',' + params.currentPage + ' , ' +data.data[i].blogid + ",'cancel')\">撤销</button>"  +
                            "</td>" +
                            "</tr>"
                    }
                    bodyObj.append(text)

                    // 实现分页显示
                    footObj = $('#pageData')
                    footObj.empty()
                    pageText = ' <tr align="right">' +
                           '                <td colspan="8">' +
                           '                   总共有'+params.counts+'条 总共有'+ params.totalPage +'页' +
                           '                   当前第' + params.currentPage + '页' +
                           '                    <a href="javascript:blog(' + params.pageSize + ',' + 1 + ' , ' +params.totalPage + ',\'search\')" >首页</a>' +
                           '                    <a href="javascript:blog(' + params.pageSize + ',' + (params.currentPage <= 1 ? 1:params.currentPage - 1) + ' , ' +params.totalPage + ',\'search\')" >上一页</a>' +
                           '                    <a href="javascript:blog(' + params.pageSize + ',' + (params.currentPage >= params.totalPage ? params.totalPage:params.currentPage + 1) + ' , ' +params.totalPage + ',\'search\')" >下一页</a>' +
                           '                    <a href="javascript:blog(' + params.pageSize + ',' + params.totalPage + ' , ' +params.totalPage + ',\'search\')">尾页</a>' +
                           '                    <select name="pageSize">' +
                           '                        <option value="10" >10</option>' +
                           '                        <option value="20" >20</option>' +
                           '                        <option value="50" >50</option>' +
                           '                        <option value="100">100</option>' +
                           '                    </select>' +
                           '                </td>' +
                           '            </tr>'
                    footObj.append(pageText) // DOM  innerHTML
                    document.classForm.currentPage.value = params.currentPage
                }
           }
        }
    )
}
$(document).ready(
    function(){
        blog(10, 1, 0, 'search')
    }
)