function blogClass(pageSize, currentPage, classId, opr){
    cName = document.classForm.className.value
    uName =  document.classForm.cName.value
    aName = document.classForm.aName.value
    if(opr == 'submitUpdate' || opr == 'add'){
        currentPage = document.classForm.currentPage.value
        classId = document.classForm.cId.value
    }
    //  $ == jQuery  JSON对象
    $.ajax({
            url:'/classlist/',
            type: 'POST',
            data: JSON.stringify({
                className: cName,
                pageSize: pageSize,
                currentPage: currentPage,
                classId: classId,
                opr: opr,
                uName: uName,
                aName: aName
            }),
            dataType: 'json',
            success: function (data) {
                // data = JSON.parse(data)
                if(opr == 'update'){
                    $('#modal-update').modal()
                    uClass = data.uClass
                    params = data.params
                    document.classForm.cName.value = uClass.classname
                    document.classForm.cId.value =  uClass.classid
                    document.classForm.currentPage.value = params.currentPage

                    cArray = document.classForm.cState
                    for(i=0;i < cArray.length; i++){
                        if(data.uClass.classstate == i+1){
                            cArray[i].checked = 'checked'
                        }
                    }

                }else{
                    bodyObj = $('#bodyData')
                    params = data.params
                    text = ""
                    bodyObj.empty()
                    for(i=0; i<data.data.length;i++){
                        text += "<tr><td></td><td>" + data.data[i].classid + "</td><td>"
                            + data.data[i].classname + "</td>" + "<td></td>" +
                            "<td>" +
                            " <a href=\"javascript:blogClass(" + params.pageSize + ',' + params.currentPage + ' , ' +data.data[i].classid + ",\'update\')\">修改</a>"  +
                            " <a href=\"javascript:blogClass(" + params.pageSize + ',' + params.currentPage + ' , ' +data.data[i].classid + ",\'delClass\')\">删除</a>"  +
                            "</td>" +
                            "</tr>"
                    }
                    bodyObj.append(text)

                    // 实现分页显示
                    footObj = $('#pageData')
                    footObj.empty()
                    pageText = ' <tr align="right">' +
                           '                <td colspan="6">' +
                           '                   总共有'+params.counts+'条 总共有'+ params.totalPage +'页' +
                           '                   当前第' + params.currentPage + '页' +
                           '                    <a href="javascript:blogClass(' + params.pageSize + ',' + 1 + ' , ' +params.totalPage + ',\'search\')" >首页</a>' +
                           '                    <a href="javascript:blogClass(' + params.pageSize + ',' + (params.currentPage <= 1 ? 1:params.currentPage - 1) + ' , ' +params.totalPage + ',\'search\')" >上一页</a>' +
                           '                    <a href="javascript:blogClass(' + params.pageSize + ',' + (params.currentPage >= params.totalPage ? params.totalPage:params.currentPage + 1) + ' , ' +params.totalPage + ',\'search\')" >下一页</a>' +
                           '                    <a href="javascript:blogClass(' + params.pageSize + ',' + params.totalPage + ' , ' +params.totalPage + ',\'search\')">尾页</a>' +
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
                if(opr == 'submitUpdate' || opr == 'add'){
                    $('#modal-update').modal('hide')
                    $('#modal-add').modal('hide')
                }

           }
        }
    )
}
$(document).ready(
    function(){
        blogClass(10, 1, 0, 'search')
    }
)