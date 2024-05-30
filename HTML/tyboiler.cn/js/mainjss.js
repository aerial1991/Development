
//标示当前菜单背景
function ChangeBg2() {
    var f = false;
    var pathname = window.location.pathname;
    var ObjLi = $(".nav_column  li ");
    var ObjA;

    for (var i = 0; i < ObjLi.length; i++) {
        ObjA = "/" + $(ObjLi[i]).children().children("a").attr("href");

        if (pathname == ObjA) {
            f = true;
            ObjLi[i].className = "hover";
        } else {
            ObjLi[i].className = '';
        }

    }
    if (!f) {
        ChangeBg2();
    }
}
//标示当前菜单背景
function ChangeBg55() {
    var f = false;
    var pathname = window.location.pathname;
    var ObjLi = $(".nav_column  li ");
    var ObjA;

    for (var i = 0; i < ObjLi.length; i++) {
        ObjA = "/" + $(ObjLi[i]).children().children("a").attr("href");

        if (pathname == ObjA) {
            f = true;
            ObjLi[i].className = "hover";
        } else {
            ObjLi[i].className = '';
        }

    }
    //    if (!f) {
    //        ChangeBg2();
    //    }
}
//标示当前菜单背景
function ChangeBg2() {
    var nav = document.getElementById("navNum");
    if (nav == null) {
        return;
    }
    var ObjLi = $(".nav_column  li ");
    var ObjA;
    for (var i = 0; i < ObjLi.length; i++) {
        ObjA = $(ObjLi[i]).children().children("a").attr("title");
        if (nav.value == null || nav.value == "") {
            ObjLi[0].className = "hover";

        }

        if (nav.value == i || nav.value == ObjA) {
            ObjLi[i].className = "hover";
        } else {
            ObjLi[i].className = '';
        }
    }
}
var codeTo = true;
$(document).ready(function () {
    var sjvar = document.getElementById('sjurl');
    if (sjvar)
        sjvar.href = murl;
    //  ChangeBg();
    altImg();
    kefu();
    // jQuery(".indexBanner").slide({ mainCell: ".bdPic li", effect: "left", prevCell: ".prev", nextCell: ".next", autoPlay: true }); //首页banner滚动
    jQuery(".photo_list").slide({ mainCell: ".photo_box ul", autoPage: true, effect: "left", autoPlay: true, vis: 5, prevCell: ".carousel_right", nextCell: ".carousel_left", trigger: "click" }); //首页企业图集滚动
    jQuery(".about_photo").slide({ mainCell: ".about_pt ul", autoPage: true, effect: "left", autoPlay: true, vis: 3, prevCell: ".about_btn_right", nextCell: ".about_btn_left", trigger: "click" }); //首页公司介绍滚动
    jQuery(".box30_1").slide({ titCell: ".dMtab li", mainCell: ".bd", delayTime: 500, titOnClassName: "select" }); // 供应详细页 切换

    //联系我们 表单验证
    if ($.formValidator) {
        $.formValidator.initConfig({ formID: "formMessage", debug: false, submitOnce: true,
            onError: function (msg, obj, errorlist) {
                alert(msg);
            },
            submitAfterAjaxPrompt: '有数据正在异步验证，请稍等...'
        });
        $("#tTitle").formValidator({ onShow: "请输入联系人", onFocus: "必填项，请输入联系人", onCorrect: "谢谢您的合作" }).inputValidator({ min: 1, empty: { leftEmpty: false, rightEmpty: false, emptyError: "两边不能有空符号" }, onError: "不能为空,请确认" });
        $("#tTel").formValidator({ empty: true, onShow: "请输入你的手机或电话，可以为空哦", onFocus: "格式例如：0577-88888888或11位手机号码", onCorrect: "谢谢你的合作", onEmpty: "你真的不想留手机或电话了吗？" }).regexValidator({ regExp: ["tel", "mobile"], dataType: "enum", onError: "你输入的手机或电话格式不正确" });
        $("#tEmail").formValidator({ onShow: "请输入邮箱", onFocus: "邮箱6-100个字符,输入正确了才能离开焦点", onCorrect: "恭喜你,你输对了", defaultValue: "" }).inputValidator({ min: 6, max: 100, onError: "你输入的邮箱长度非法,请确认" }).regexValidator({ regExp: "^([\\w-.]+)@(([[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.)|(([\\w-]+.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(]?)$", onError: "你输入的邮箱格式不正确" });
        $("#verificationCode0").formValidator({ empty: false, onShow: "请输入4位验证码", onFocus: "请输入4位验证码", onCorrect: "格式正确" }).regexValidator({ regExp: "^\\d{4}$", onError: "请输入4位数字" });
        $("#verificationCode0").click(function () {
            if (codeTo) {
                f_refreshtype();
            }

        });
    }

});
//首页友情链接
function showFriendLink(varthis) {
    var hd = $(".box15_1").get(0).style.height;
    if (hd == "40px" || hd == "") {
        $(".box15_1").get(0).style.height = "auto";
        $(".links_title").get(0).style.height = $(".box15_1").eq(0).height() + "px";
        $(varthis).attr("style", "background:url(/mfile/568/images/links_btn_on_03.png) no-repeat left top");
    } else {
        $(".box15_1").get(0).style.height = "40px";
        $(".links_title").get(0).style.height = "40px";
        $(varthis).attr("style", "background:url(/mfile/568/images/links_btn_03.png) no-repeat left top");
    }

}
//图片弹窗
function altImg() {
    $(".box32_1 .thickbox").click(function () {
        var g = this.src || false;
        var htmls = '<img  src=\"' + g + '\" alt="layer">';
        $.layer({
            type: 1,   //0-4的选择,
            title: false,
            border: [0],
            closeBtn: [0, true],
            offset: ['', '50%'],
            border: [10, 0.3, '#000'],
            shadeClose: true,
            area: ['auto', 'auto'],
            page: {
                html: htmls
            }
        });
    });
}
//f581 首页 提交表单
function ajaxPost581() {

    if ($("#tFkContent").val() == "" || $("#tTitle").val() == "" || $("#tTel").val() == "" || $("#tAddress").val() == "" || $("#verificationCode0").val() == "") {
        alert("请填写完整信息");
        return false;
    } else {

        var formdata = $("#formMessage input,textarea").fieldSerialize();
        $.ajax({
            type: "post",
            url: "services.aspx?op=sub&mf=581",
            data: { datas: formdata },
            success: function (data) {

                var returnObj = eval("(" + data + ")");
                //        	                    if (returnObj.state == "1") {
                //        	                        clearInput();
                //        	                    }
                alert(returnObj.message);
                clearInput();
                //document.getElementById("img1").style.display = "none";


            }, error: function () {
                debugger;
            }

        });

    }
}
function f_refreshtype() {
    var Image1 = document.getElementById("IMGCheckCode");
    if (Image1 != null) {
        Image1.style.display = "inline";
        Image1.src = "services.aspx?op=getcodeimg&mf=581" + "&r=" + Math.random();
        codeTo = false;
    }
}
function clearInput() {
    $('#formMessage').clearForm();
    $("#tFkContent").val("");
}
//f703 联系我们 提交表单
function ajaxPost406() {

    if ($("#tFkContent").val() == "" || $("#tTitle").val() == "" || $("#tTel").val() == "" || $("#tEmail").val() == "" || $("#verificationCode0").val() == "") {
        alert("请填写完整信息");
        return false;
    } else {

        var formdata = $("#formMessage input,textarea").fieldSerialize();
        $.ajax({
            type: "post",
            url: "services.aspx?op=sub&mf=406",
            data: { datas: formdata },
            success: function (data) {

                var returnObj = eval("(" + data + ")");
                if (returnObj.state == "1") {
                    clearInput();
                }
                alert(returnObj.message);
                //document.getElementById("img1").style.display = "none";


            }, error: function () {
                debugger;
            }

        });

    }
}
//客服显隐
function kefu() {
    $("#aFloatTools_Show").click(function () {
        $('#divFloatToolsView').animate({ width: 'show', opacity: 'show' }, 100, function () { $('#divFloatToolsView').show(); });
        $('#aFloatTools_Show').hide();
        $('#aFloatTools_Hide').show();
    });

    $("#aFloatTools_Hide").click(function () {
        $('#divFloatToolsView').animate({ width: 'hide', opacity: 'hide' }, 100, function () { $('#divFloatToolsView').hide(); });
        $('#aFloatTools_Show').show();
        $('#aFloatTools_Hide').hide();
    });
}
//等比缩放
function AutoResizeImage(maxWidth, maxHeight, objImg) {
    var img = new Image();
    img.src = objImg.src;
    var hRatio;
    var wRatio;
    var Ratio = 1;
    var w = img.width;
    var h = img.height;
    wRatio = maxWidth / w;
    hRatio = maxHeight / h;
    if (maxWidth == 0 && maxHeight == 0) {
        Ratio = 1;
    } else if (maxWidth == 0) { //
        if (hRatio < 1)
            Ratio = hRatio;
    } else if (maxHeight == 0) {
        if (wRatio < 1)
            Ratio = wRatio;
    } else if (wRatio < 1 || hRatio < 1) {
        Ratio = (wRatio <= hRatio ? wRatio : hRatio);
    }
    if (Ratio < 1) {
        w = w * Ratio;
        h = h * Ratio;
    }
    objImg.height = h;
    objImg.width = w;
}

