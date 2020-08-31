$('.form_datetime').datetimepicker({
    //language:  'fr',
    weekStart: 1,
    todayBtn: 1,
    autoclose: 1,
    todayHighlight: 1,
    startView: 2,
    forceParse: 0,
    showMeridian: 1
});
$('.form_date').datetimepicker({
    language: 'fr',
    weekStart: 1,
    todayBtn: 1,
    autoclose: 1,
    todayHighlight: 1,
    startView: 2,
    minView: 2,
    forceParse: 0
});
$('.form_time').datetimepicker({
    language: 'fr',
    weekStart: 1,
    todayBtn: 1,
    autoclose: 1,
    todayHighlight: 1,
    startView: 1,
    minView: 0,
    maxView: 1,
    forceParse: 0
});
laydate.render({
    elem: '#birthday' //指定元素
});
laydate.render({
    elem: '#birthdayTime'
    , type: 'time'
});
laydate.render({
    elem: '#birthdaycustom' //指定元素
});
laydate.render({
    elem: '#birthdaycustomTime'
    , type: 'time'
});
laydate.render({
    elem: '#birthdayanalyseTime'
    , type: 'time'
});
laydate.render({
    elem: '#birthdayanalyse' //指定元素
});


function resolve_bazi(data) {
    bazi_result = eval("(" + data + ")");
    wuxingscore = bazi_result['wuxingscore']
    tonglei = bazi_result['tongle']
    rigan_wx = bazi_result['rigan']
    is_weak = bazi_result['isweak'] ? 1 : 0
    minTong = bazi_result['minTong']
    minYi = bazi_result['minYi']
    bazi = bazi_result['shengchenbazi']
    yileilist = bazi_result['yileilist']

    var shengchenHtml = "";
    shengchenHtml += '五行强度：<br/>'
    shengchenHtml += '金：' + wuxingscore[0] + '<br/>'
    shengchenHtml += '木：' + wuxingscore[1] + '<br/>'
    shengchenHtml += '水：' + wuxingscore[2] + '<br/>'
    shengchenHtml += '火：' + wuxingscore[3] + '<br/>'
    shengchenHtml += '土：' + wuxingscore[4] + '<br/>'
    shengchenHtml += '八字：' + bazi + '<br/>'
    if (is_weak) {
        shengchenHtml += '日干为' + rigan_wx + ',八字偏弱<br/>'
        shengchenHtml += '喜用神：' + tonglei + ',' + rigan_wx + '<br/>'
    } else {
        shengchenHtml += '日干为' + rigan_wx + ',八字偏旺<br/>'
        shengchenHtml += '喜用神：' + yileilist[0] + ',' + yileilist[1] + ',' + yileilist[2] + ',' + '<br/>'
    }
    $('#shengchen').html(shengchenHtml);
}

function resolve_wuge(data, xing, mingzi) {
    var wugeHtml = "";
    wuge_result = eval("(" + data + ")");
    wuxing = wuge_result['wuxing'];
    xingbh = wuge_result['xingbh'];
    mingbh = wuge_result['mingbh'];
    tian = wuge_result['tian'];
    ren = wuge_result['ren'];
    di = wuge_result['di'];
    zong = wuge_result['zong'];
    sancaiScore = wuge_result['sancaiScore'];
    wuge = wuge_result['wuge'];
    wugeHtml += '姓名五行：<br/>';
    if (xing.length == 2) {
        wugeHtml += xing[0] + '：' + wuxing[0] + '<br/>';
        wugeHtml += xing[1] + '：' + wuxing[1] + '<br/>';
    } else
        wugeHtml += xing[0] + '：' + wuxing[0] + '<br/>'
    if (mingzi.length == 2) {
        wugeHtml += mingzi[0] + '：' + wuxing[xing.length] + '<br/>'
        wugeHtml += mingzi[1] + '：' + wuxing[xing.length + 1] + '<br/>'
    } else
        wugeHtml += mingzi[0] + '：' + wuxing[xing.length] + '<br/>'
    wugeHtml += '姓名笔画（康熙字典）：<br/>'
    wugeHtml += xing[0] + '：' + xingbh + '  (复姓取第一个字)<br/>'
    if (mingzi.length == 2) {
        wugeHtml += mingzi[0] + '：' + mingbh[0] + '<br/>'
        wugeHtml += mingzi[1] + '：' + mingbh[1] + '<br/>'
    } else
        wugeHtml += mingzi[0] + '：' + mingbh[0] + '<br/>'

    wugeHtml += '天格：' + tian + '<br/>'
    wugeHtml += '地格：' + di + '<br/>'
    wugeHtml += '人格：' + ren + '<br/>'
    wugeHtml += '总格：' + zong + '<br/>'
    wugeHtml += '三才分数：' + sancaiScore + '<br/>'
    wugecp = ''
    if (wuge > 2)
        wugecp = '大吉'
    else if (wuge == 2)
        wugecp = '吉'
    else if (wuge == 1)
        wugecp = '佳'
    else if (wuge == 0)
        wugecp = '良'
    wugeHtml += '五格测评：' + wugecp + '  <br/>'

    $('#wugeresult').html(wugeHtml);
}

function query() {
    console.log("query")
    xing = document.getElementById("xing").value
    if (xing == null || xing == undefined || xing == '') {
        alert("姓氏不能为空")
		return;
    }
    sex = $("input[name='optradio']:checked").val();
    date = document.getElementById("birthday").value
    if (date == null || date == undefined || date == '') {
        alert("日期不能为空")
		return;
    }
    time = document.getElementById("birthdayTime").value
    if (time == null || time == undefined || time == '') {
        alert("时间不能为空")
		return;
    }
    console.log(time)
    doublename = $('#doublename  option:selected').val()
    zhidingziradio = $("input[name='zhidingziradio']:checked").val();
    firstname = ''
    secname = ''
    if (zhidingziradio == 1) {
        firstname = document.getElementById("zhidingzi").value
    } else {
        secname = document.getElementById("zhidingzi").value
    }


    $.post("/analyse_bazi",
        {
            'date': date, 'time': time,
        },
        function (data, status) {
            resolve_bazi(data)

            $.post("/query",
                {
                    'tonglei': tonglei,
                    'rigan_wx': rigan_wx,
                    'is_weak': is_weak,
                    'minTong': minTong,
                    'minYi': minYi,
                    'wuxingscore': wuxingscore.join(),
                    'xing': xing,
                    'sex': sex,
                    'doublename': doublename,
                    'firstname': firstname,
                    'secname': secname
                },
                function (data, status) {

                    var itemHtml = "";
                    listName = eval("(" + data + ")");
                    for (var i = 0, len = listName.length; i < len; i++) {
                        itemHtml += '<a href="#result" onclick="analyse(xing,this)" style="padding-left: 20px;padding-top: 10px;display:inline-block">' + xing + listName[i] + '</a>';
                    }
                    $('#result').html(itemHtml);
                });
        });
}


function querycustom() {
    xing = document.getElementById("xingcustom").value
    sex = $("input[name='optradiocustom']:checked").val();
    doublename = $('#doublenamecustom  option:selected').val()
    firstWx = $('#firstwuxing  option:selected').val()
    secondWx = $('#secondwuxing  option:selected').val()

    $.post("/querycustom",
        {
            'xing': xing, 'sex': sex, 'firstWx': firstWx, 'secondWx': secondWx, 'doublename': doublename
        },
        function (data, status) {
            var itemHtml = "";
            listName = eval("(" + data + ")");
            for (var i = 0, len = listName.length; i < len; i++) {
                itemHtml += '<a href="#result" onclick="analyse(xing,this)" style="padding-left: 20px;padding-top: 10px;display:inline-block">' + xing + listName[i] + '</a>';
            }
            $('#result').html(itemHtml);
        });
}

function analyse(xing, obj) {
    mingzi = ""
    quanming = obj.innerHTML
    if (xing.length == 2)
        mingzi = quanming.substring(2)
    else
        mingzi = quanming.substring(1)
    $('#mingzi').val(mingzi)
    $('#xingshi').val(xing)
    $.post("/analyse_mingzi",
        {
            'xing': xing, 'ming': mingzi
        },
        function (data, status) {
            resolve_wuge(data, xing, mingzi);
        });
}

function analyzemingzi() {
    xing = $("#xingshi").val()
    if (xing == null || xing == undefined || xing == '') {
        alert("姓氏不能为空")
		return;
    }
    ming = $("#mingzi").val()
    date = document.getElementById("birthdayanalyse").value
    if (date == null || date == undefined || date == '') {
        alert("日期不能为空")
		return;
    }
    time = document.getElementById("birthdayanalyseTime").value
    if (time == null || time == undefined || time == '') {
        alert("时间不能为空")
		return;
    }
    $.post("/analyse_mingzi",
        {
            'xing': xing, 'ming': ming
        },
        function (data, status) {
            resolve_wuge(data, xing, ming);
        }
    );
    $.post("/analyse_bazi",
        {
            'date': date, 'time': time,
        },
        function (data, status) {
            resolve_bazi(data)
        }
    );
}