//客服显隐
function kefu() {
    $("#aFloatTools_Show").click(function () {
        $('#divFloatToolsView').animate({
            width: 'show',
            opacity: 'show'
        }, 100, function () {
            $('#divFloatToolsView').show();
        });
        $('#aFloatTools_Show').hide();
        $('#aFloatTools_Hide').show();
    });

    $("#aFloatTools_Hide").click(function () {
        $('#divFloatToolsView').animate({
            width: 'hide',
            opacity: 'hide'
        }, 100, function () {
            $('#divFloatToolsView').hide();
        });
        $('#aFloatTools_Show').show();
        $('#aFloatTools_Hide').hide();
    });
}
$(document).ready(function () {
    kefu();

    $("#Banner").owlCarousel({
        autoPlay: true,
        navigation: false,
        singleItem: true,
        stopOnHover: true,
        transitionStyle: 'fadeUp',
    });

    $("#MBanner").owlCarousel({
        autoPlay: true,
        navigation: false,
        singleItem: true,
        stopOnHover: true,
        transitionStyle: 'fadeUp',
    });

    $("#Product").owlCarousel({
        itemsCustom: [
            [0, 1],
            [450, 1],
            [600, 3],
            [700, 3],
            [1000, 3],
            [1200, 3],
            [1400, 3],
            [1600, 3]
        ],
        autoPlay: true,
        navigation: false,
        stopOnHover: true,
        transitionStyle: 'fadeUp',
    });

   

    $(".info-content").find("table").wrap("<div class='table-responsive'></div>");


    //手风琴导航
    $('.nav li a').click(function () {
        $(this).siblings().slideToggle();
        if ($(this).next().children('li').length == 0) {
            location.href = $(this).attr("href");
        }

        return false;
    })

    $('.dMtab ul').find('li').click(function () {
        $(this).addClass('select').siblings().removeClass('select');
        $('.bd > ul').hide();
        $('.bd > ul').eq($(this).index()).show();
    })

    $(".right-con .info").find("table").wrap("<div class='table-responsive'></div>");

    var OnlineH = $(".online").outerHeight();
    $(".online").css("margin-top", -OnlineH / 2);

    $(".online .left").click(function () {

        $(this).parent().parent().toggleClass("online-move");

    })

    // 企业图集
    jQuery(".picMarquee-left").slide({
        mainCell: ".bd ul",
        autoPlay: true,
        effect: "leftMarquee",
        vis: 2,
        interTime: 50,
        trigger: "click"
    });

    //获取window 的高度
    var $window = $(window),
        win_height_padded = $window.height();

    //给window绑定scroll事件
    $window.on('scroll', revealOnScroll);

    function revealOnScroll() {
        var scrolled = $window.scrollTop(),
            win_height_padded = $window.height();

        //显示动画
        $('.revealOnScroll:not(.animated)').each(function () {
            var $this = $(this),
                offsetTop = $this.offset().top;

            if (scrolled + win_height_padded > offsetTop) {
                if ($this.data('timeout')) {
                    window.setTimeout(function () {
                        $this.addClass('animated ' + $this.data('animation'));
                    }, parseInt($this.data('timeout'), 10));
                } else {
                    $this.addClass('animated ' + $this.data('animation'));
                }
            }
        });
        //二次隐藏显示
        $('.revealOnScroll.animated').each(function (index) {
            var $this = $(this),
                offsetTop = $this.offset().top;
            if (scrolled + win_height_padded < offsetTop) {
                $(this).removeClass('animated fadeInLeft fadeInRight');
            }
        });

    }
});

//返回顶部
function gotoTop(acceleration, stime) {
    acceleration = acceleration || 0.1;
    stime = stime || 10;
    var x1 = 0;
    var y1 = 0;
    var x2 = 0;
    var y2 = 0;
    var x3 = 0;
    var y3 = 0;
    if (document.documentElement) {
        x1 = document.documentElement.scrollLeft || 0;
        y1 = document.documentElement.scrollTop || 0;
    }
    if (document.body) {
        x2 = document.body.scrollLeft || 0;
        y2 = document.body.scrollTop || 0;
    }
    var x3 = window.scrollX || 0;
    var y3 = window.scrollY || 0;

    // 滚动条到页面顶部的水平距离
    var x = Math.max(x1, Math.max(x2, x3));
    // 滚动条到页面顶部的垂直距离
    var y = Math.max(y1, Math.max(y2, y3));

    // 滚动距离 = 目前距离 / 速度, 因为距离原来越小, 速度是大于 1 的数, 所以滚动距离会越来越小
    var speeding = 1 + acceleration;
    window.scrollTo(Math.floor(x / speeding), Math.floor(y / speeding));

    // 如果距离不为零, 继续调用函数
    if (x > 0 || y > 0) {
        var run = "gotoTop(" + acceleration + ", " + stime + ")";
        window.setTimeout(run, stime);
    }
}