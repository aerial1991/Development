window.TabCat = function (newInfoLi, dtCon, spanA, fn) {
    newInfoLi = $(newInfoLi);
    dtCon = $(dtCon);
    dtCon.addClass("tabCat");
    if (spanA) {
        spanA = $(spanA);
    }
    fn = fn || function (index, ob, dtCon, spanA) {
        ob.addClass('cur').siblings().removeClass('cur');
        dtCon.eq(index).show().siblings(".tabCat").hide();
        if (spanA) {
            $(spanA).attr('href', ob.attr("href") || ob.find("a").attr('href'));
        }
    }
    newInfoLi.mouseenter(function (event) {
        var ob = $(this);
        var index = newInfoLi.index(ob);
        fn(index, ob, dtCon, spanA);
    }).eq(0).mouseenter();
    newInfoLi.filter(':last').parent().addClass('nobor');
}