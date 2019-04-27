#utf-8

# Create your models here.
import ctypes
import time
import random
import BaziAlgorithm
import CalendarChina


wx_dict = {}
bh_dict = {}
bh_wg_dict = {1:1,3:1,5:1,6:1,7:1,8:1,11:1,13:1,15:1,16:1,17:1,18:1,21:1,23:1,24:1,25:1,29:1,31:1,32:1,33:1,35:1,37:1,39:1,41:1,45:1,47:1,48:1,52:1,55:1,57:1,61:1,63:1,65:1,67:1,68:1,81:1,
              2:0,4:0,9:0,10:0,12:0,14:0,19:0,20:0,22:0,26:0,27:0,28:0,30:0,36:0,34:0,38:0,40:0,42:0,43:0,44:0,46:0,49:0,50:0,51:0,53:0,54:0,56:0,58:0,59:0,60:0,62:0,64:0,66:0,69:0,70:0,71:0,72:0,73:0,74:0,75:0,76:0,77:0,78:0,79:0,80:0}
mand_arr = []
womand_arr = []
man_arr = []
woman_arr = []

WuXingTable = ['金', '木', '水', '火', '土' ]
wxZiIndexDic = {'金':0, '木':1, '水':2, '火':3, '土':4 }
wxIndexDic={'j':0,'m':1,'s':2,'h':3,'t':4}

TianGan_WuXingProp = [1, 1, 3, 3, 4,4, 0, 0, 2, 2]
DiZhi_WuXingProp = [2, 4, 1, 1, 4,3, 3, 4, 0, 0, 4, 2]
GenerationSourceTable = [4, 2, 0, 1,3]
TianGan = '甲乙丙丁戊己庚辛壬癸'
DiZhi = '子丑寅卯辰巳午未申酉戌亥'
tian=0
sancai_score={'mmm':10,'mmh':10,'mmt':10,'mmj':5,'mms':7,
              'mhm':10,'mhh':8,'mht':10,'mhj':5,'mhs':4,
              'mtm':4,'mth':8,'mtt':9,'mtj':7,'mts':4,
              'mjm':4,'mjh':4,'mjt':5,'mjj':4,'mjs':4,
              'msm':10,'msh':5,'mst':5,'msj':10,'mss':10,
              'hmm':10,'hmh':10,'hmt':10,'hmj':5,'hms':8,
              'hhm':10,'hhh':8,'hht':10,'hhj':4,'hhs':4,
              'htm':7,'hth':10,'htt':10,'htj':10,'hts':7,
              'hjm':4,'hjh':4,'hjt':6,'hjj':4,'hjs':4,
              'hsm':5,'hsh':4,'hst':4,'hsj':4,'hss':4,
              'tmm':8,'tmh':8,'tmt':5,'tmj':4,'tms':5,
              'thm':10,'thh':10,'tht':10,'thj':7,'ths':4,
              'ttm':8,'tth':10,'ttt':10,'ttj':10,'tts':5,
              'tjm':5,'tjh':5,'tjt':10,'tjj':10,'tjs':10,
              'tsm':5,'tsh':4,'tst':4,'tsj':6,'tss':4,
              'jmm':5,'jmh':5,'jmt':5,'jmj':4,'jms':5,
              'jhm':5,'jhh':6,'jht':6,'jhj':4,'jhs':4,
              'jtm':8,'jth':10,'jtt':10,'jtj':10,'jts':7,
              'jjm':4,'jjh':4,'jjt':10,'jjj':8,'jjs':8,
              'jsm':10,'jsh':5,'jst':9,'jsj':10,'jss':8,
              'smm':10,'smh':10,'smt':10,'smj':5,'sms':10,
              'shm':8,'shh':4,'sht':5,'shj':4,'shs':4,
              'stm':4,'sth':8,'stt':8,'stj':8,'sts':4,
              'sjm':5,'sjh':5,'sjt':10,'sjj':8,'sjs':10,
              'ssm':10,'ssh':4,'sst':4,'ssj':10,'sss':8}

def ComputeGanIndex(gan):
     for i in range(0,10):
        if(TianGan[i] == gan):
            break;
     if i >= 10:
         return -1;
     return i;

def ComputeZhiIndex( zhi):
     for i in range(0,12):
        if(DiZhi[i] == zhi):
            break;
     if i >= 12:
         return -1;
     return i;

def init_data():
    data_lines_j = open('data/j.txt',encoding='utf-8').readlines()
    data_lines_m = open('data/m.txt',encoding='utf-8').readlines()
    data_lines_s = open('data/s.txt',encoding='utf-8').readlines()
    data_lines_h = open('data/h.txt',encoding='utf-8').readlines()
    data_lines_t = open('data/t.txt',encoding='utf-8').readlines()
    for line in data_lines_j:  # 去掉头部无用信息
        l = line.strip().split(':')
        if len(l)==2:
            for word in l[1]:
                wx_dict[word]='j'
                bh_dict[word]=int(l[0])
    for line in data_lines_m:  # 去掉头部无用信息
        l = line.strip().split(':')
        if len(l)==2:
            for word in l[1]:
                wx_dict[word]='m'
                bh_dict[word]=int(l[0])
    for line in data_lines_s:  # 去掉头部无用信息
        l = line.strip().split(':')
        if len(l)==2:
            for word in l[1]:
                wx_dict[word]='s'
                bh_dict[word]=int(l[0])
    for line in data_lines_h:  # 去掉头部无用信息
        l = line.strip().split(':')
        if len(l)==2:
            for word in l[1]:
                wx_dict[word]='h'
                bh_dict[word]=int(l[0])
    for line in data_lines_t:  # 去掉头部无用信息
        l = line.strip().split(':')
        if len(l)==2:
            for word in l[1]:
                wx_dict[word]='t'
                bh_dict[word]=int(l[0])

    data_lines_all = open('data/bh.txt',encoding='utf-8').readlines()
    for line in data_lines_all:  # 去掉头部无用信息
        l = line.strip().split(':')
        if len(l)==2:
            for word in l[1]:
                bh_dict[word]=int(l[0])

    man=open('data/man.txt',encoding='utf-8').read()
    woman=open('data/woman.txt',encoding='utf-8').read()
    for word in man:
        man_arr.append(word)

    for word in woman:
        woman_arr.append(word)


    dman=open('data/mand.txt',encoding='utf-8').readlines()
    dwoman=open('data/womand.txt',encoding='utf-8').readlines()

    for line in dman:
        line = line.strip()
        if len(line)==2:
            mand_arr.append(line)

    for line in dwoman:
        line = line.strip()
        if len(line)==2:
            womand_arr.append(line)

def get_sizhu_from_date(year,month,day,hour,minute):
    dll = ctypes.windll.LoadLibrary('valuatedll.dll')
    sizhu_result = dll.GetSiZhuFromDate(year, month, day, hour, minute)
    return sizhu_result

def get_bazi_from_date(year,month,day,hour,minute):
    analyse_result = {}
    wuxingscore = [0.0,0.0,0.0,0.0,0.0]
    shengchenbazi = ""
    rigan = ""
    isweak = True
    minTong = ""
    minYi = ""
    yileilist = []
    analyse_result['wuxingscore']= wuxingscore
    analyse_result['shengchenbazi']= shengchenbazi
    analyse_result['rigan']= rigan
    analyse_result['isweak']= isweak
    analyse_result['minTong']= minTong
    analyse_result['minYi']= minYi
    analyse_result['yileilist']= yileilist
    bazi = CalendarChina.GetSiZhu(year,month,day,hour,minute)
    test_result = BaziAlgorithm.EvalBaziScore(bazi)
    strtemp=test_result.split(',')
    wx_score_lei = []
    wx_score_lei_temp = []
    for i in range(0,5):
        wx_score_lei.append(float(strtemp[i]))
        analyse_result['wuxingscore'][i]= float(strtemp[i])
        wx_score_lei_temp.append(float(strtemp[i]))
    analyse_result['shengchenbazi'] = bazi


    rigan_wx=TianGan_WuXingProp[ComputeGanIndex(bazi[4])]
    tonglei=GenerationSourceTable[rigan_wx]
    analyse_result['rigan'] = WuXingTable[rigan_wx]
    tonglei_score=wx_score_lei[rigan_wx]+wx_score_lei[tonglei]
    analyse_result['tongle']=WuXingTable[tonglei]
    analyse_result['yileilist'].clear()
    for indexwuxing in range(5):
        if indexwuxing!=rigan_wx and indexwuxing!=tonglei:
            analyse_result['yileilist'].append(WuXingTable[indexwuxing])
    yilei_score=wx_score_lei[0]+wx_score_lei[1]+wx_score_lei[2]+wx_score_lei[3]+wx_score_lei[4]-tonglei_score
    is_weak=True
    if tonglei_score>yilei_score:
        is_weak=False
    minTongScore = min(wx_score_lei[tonglei],wx_score_lei[rigan_wx])
    tempRi = wx_score_lei_temp[rigan_wx]
    analyse_result['rigan'] = WuXingTable[rigan_wx]
    analyse_result['isweak'] = is_weak
    tempTong = wx_score_lei_temp[tonglei]
    wx_score_lei_temp.remove(tempRi)
    wx_score_lei_temp.remove(tempTong)
    minYiScore = min(wx_score_lei_temp)
    for indexwuxing in range(5):
        if minTongScore == wx_score_lei[indexwuxing]:
            analyse_result['minTong'] = WuXingTable[indexwuxing]
        if minYiScore == wx_score_lei[indexwuxing]:
            analyse_result['minYi'] = WuXingTable[indexwuxing]
    return analyse_result


# score =[0,0,0,0,0]
# for j in range(0,8):
#    if j%2==0:
#        wx_index = TianGan_WuXingProp[ComputeGanIndex(bazi[j])]
#    else:
#        wx_index = DiZhi_WuXingProp[ComputeZhiIndex(bazi[j])]
#    score[wx_index]=score[wx_index]+1
def choose_name_from_baze(tonglei,rigan_wx,is_weak,minTong,minYi,wuxingscore,type,first='',sec=''):
    mustWx = []
    goodWx = []
    for i in range(0,5):
        if float(wuxingscore[i])<1:
            goodWx.append(i)
    if is_weak=='1':
        mustWx.append(wxZiIndexDic[minTong])
    else:
        mustWx.append(wxZiIndexDic[minYi])
    if len(goodWx)<1:
        if is_weak=='1':
            goodWx.append(wxZiIndexDic[minYi])
        else:
            goodWx.append(wxZiIndexDic[minTong])
    goodWx.extend(mustWx)
    goodWx = list(set(goodWx))

    good_ret = []
    total_arr = []
    if type==1:
        total_arr = mand_arr
    elif type == 2:
        total_arr = womand_arr
    elif type == 3 or type == 5 or type == 7:
        total_arr = man_arr
    elif type == 4 or type == 6 or type == 8:
        total_arr = woman_arr
    if type==1 or type == 2:
        for name in total_arr:
            wxName = wx_dict.get(name[0])
            if wxName != None:
                wxIndexFirst = wxIndexDic.get(wxName)
            else:
                continue
            wxName = wx_dict.get(name[1])
            if wxName != None:
                wxIndexSecond = wxIndexDic.get(wxName)
            else:
                continue
            if len(goodWx)>1:
                if wxIndexFirst != wxIndexSecond:
                    if wxIndexFirst in goodWx and wxIndexSecond in goodWx:
                        good_ret.append(name)
            elif len(goodWx)==1:
                if wxIndexFirst == wxIndexSecond and wxIndexFirst == goodWx[0]:
                    good_ret.append(name)
    elif type == 3 or type == 4:
        for name in total_arr:
            wxName = wx_dict.get(name[0])
            if wxName != None:
                wxIndexFirst = wxIndexDic.get(wxName)
            else:
                continue
            if len(goodWx)>1 or len(goodWx)==1:
                if wxIndexFirst in goodWx:
                    good_ret.append(name)
    elif type==5 or type == 6:
        for name in total_arr:
            wxName = wx_dict.get(name[0])
            if wxName != None:
                wxIndexFirst = wxIndexDic.get(wxName)
            else:
                continue
            if len(goodWx)>1 or len(goodWx)==1:
                if wxIndexFirst in goodWx:
                    good_ret.append(name+sec)
    elif type==7 or type == 8:
        for name in total_arr:
            wxName = wx_dict.get(name[0])
            if wxName != None:
                wxIndexFirst = wxIndexDic.get(wxName)
            else:
                continue
            if len(goodWx)>1 or len(goodWx)==1:
                if wxIndexFirst in goodWx:
                    good_ret.append(first+name)
    if len(good_ret)>500:
        return random.sample(good_ret, 500)
    else:
        return good_ret

def choose_from_wuxing(firstWuxing,secondWuxing,type):
    good_rusult = []
    total_arr = []
    if type == 1:
        total_arr = mand_arr
    elif type == 2:
        total_arr = womand_arr
    elif type == 3:
        total_arr = man_arr
    elif type == 4:
        total_arr = woman_arr
    for name in total_arr:
        if type == 3 or type == 4:
            wxNameFirst = wx_dict.get(name[0])
            if wxNameFirst != None:
                wxIndexFirst = wxIndexDic.get(wxNameFirst)
            else:
                continue
            if wxZiIndexDic[firstWuxing]==wxIndexFirst:
                good_rusult.append(name)
        else:
            wxNameFirst = wx_dict.get(name[0])
            if wxNameFirst != None:
                wxIndexFirst = wxIndexDic.get(wxNameFirst)
            else:
                continue
            wxNameSecond = wx_dict.get(name[1])
            if wxNameSecond != None:
                wxIndexSecond = wxIndexDic.get(wxNameSecond)
            else:
                continue
            if wxZiIndexDic[firstWuxing]==wxIndexFirst and wxZiIndexDic[secondWuxing]==wxIndexSecond and name[0] != name[1]:
                good_rusult.append(name)
    if len(good_rusult)>500:
        return random.sample(good_rusult, 500)
    else:
        return good_rusult


def analyse_mingzi(xing,ming):
    mingzi = xing+ming
    lenMingzi = len(mingzi)
    lenMing = len(ming)
    wuxing = []
    xingbh = bh_dict.get(xing[0], 0)
    mingbh = []
    for i in range(lenMingzi):
        if wx_dict.__contains__(mingzi[i]):
            if wx_dict[mingzi[i]] == 'j':
                wuxing.append('金')
            elif wx_dict[mingzi[i]] == 'm':
                wuxing.append('木')
            elif wx_dict[mingzi[i]] == 's':
                wuxing.append('水')
            elif wx_dict[mingzi[i]] == 'h':
                wuxing.append('火')
            elif wx_dict[mingzi[i]] == 't':
                wuxing.append('土')
        else:
            wuxing.append('无')

    for i in range(lenMing):
        mingbh.append(bh_dict.get(ming[i], 0))
    tian = bh_dict.get(xing[0], 10) + 1
    ren = bh_dict.get(xing[0], 10) + bh_dict.get(ming[0], 10)
    if (len(ming) == 2):
        di = bh_dict.get(ming[0], 10) + bh_dict.get(ming[1], 10)
        zong = bh_dict.get(ming[0], 10) + bh_dict.get(ming[1], 10) + bh_dict.get(xing[0], 10)
    else:
        di = bh_dict.get(ming[0], 10) + 1
        zong = bh_dict.get(ming[0], 10) + bh_dict.get(xing[0], 10)
    sancai = ''
    if tian % 10 == 1 or tian % 10 == 2:
        sancai = sancai + 'm'
    elif tian % 10 == 3 or tian % 10 == 4:
        sancai = sancai + 'h'
    elif tian % 10 == 5 or tian % 10 == 6:
        sancai = sancai + 't'
    elif tian % 10 == 7 or tian % 10 == 8:
        sancai = sancai + 'j'
    elif tian % 10 == 9 or tian % 10 == 0:
        sancai = sancai + 's'

    if ren % 10 == 1 or ren % 10 == 2:
        sancai = sancai + 'm'
    elif ren % 10 == 3 or ren % 10 == 4:
        sancai = sancai + 'h'
    elif ren % 10 == 5 or ren % 10 == 6:
        sancai = sancai + 't'
    elif ren % 10 == 7 or ren % 10 == 8:
        sancai = sancai + 'j'
    elif ren % 10 == 9 or ren % 10 == 0:
        sancai = sancai + 's'

    if di % 10 == 1 or di % 10 == 2:
        sancai = sancai + 'm'
    elif di % 10 == 3 or di % 10 == 4:
        sancai = sancai + 'h'
    elif di % 10 == 5 or di % 10 == 6:
        sancai = sancai + 't'
    elif di % 10 == 7 or di % 10 == 8:
        sancai = sancai + 'j'
    elif di % 10 == 9 or di % 10 == 0:
        sancai = sancai + 's'
    sancaiScore = sancai_score.get(sancai, 10)
    wugedi = bh_wg_dict.get(di)
    wugetian = bh_wg_dict.get(tian)
    wugeren = bh_wg_dict.get(ren)
    wugezong = bh_wg_dict.get(zong)
    result = {}
    result["wuxing"]=wuxing
    result["xingbh"]=xingbh
    result["mingbh"]=mingbh
    result["tian"]=tian #笔画
    result["ren"]=ren
    result["di"]=di
    result["zong"]=zong
    result["sancaiScore"]=sancaiScore
    result["wuge"]=wugedi+wugetian+wugezong+wugeren
    return result

def cuputer_score(xing,good_500):
    di_500={}
    ren_500={}
    zong_500={}
    sancai_500 = []
    wuge_150=[]
    if  len(xing)==1:
        tian = bh_dict.get(xing[0],10)+1
        for name in good_500:
            ren_500[name]=bh_dict.get(xing[0],10)+bh_dict.get(name[0],10)
            if(len(name)==2):
                di_500[name]=bh_dict.get(name[0],10)+bh_dict.get(name[1],10)
                zong_500[name]=bh_dict.get(name[0],10)+bh_dict.get(name[1],10)+bh_dict.get(xing[0],10)
            else:
                di_500[name]=bh_dict.get(name[0],10)+1
                zong_500[name]=bh_dict.get(name[0],10)+bh_dict.get(xing[0],10)
            sancai=''
            if tian%10==1 or tian%10==2:
                sancai=sancai+'m'
            elif tian%10==3 or tian%10==4:
                sancai=sancai+'h'
            elif tian%10==5 or tian%10==6:
                sancai=sancai+'t'
            elif tian%10==7 or tian%10==8:
                sancai=sancai+'j'
            elif tian%10==9 or tian%10==0:
                sancai=sancai+'s'

            if ren_500[name]%10==1 or ren_500[name]%10==2:
                sancai=sancai+'m'
            elif ren_500[name]%10==3 or ren_500[name]%10==4:
                sancai=sancai+'h'
            elif ren_500[name]%10==5 or ren_500[name]%10==6:
                sancai=sancai+'t'
            elif ren_500[name]%10==7 or ren_500[name]%10==8:
                sancai=sancai+'j'
            elif ren_500[name]%10==9 or ren_500[name]%10==0:
                sancai=sancai+'s'

            if di_500[name]%10==1 or di_500[name]%10==2:
                sancai=sancai+'m'
            elif di_500[name]%10==3 or di_500[name]%10==4:
                sancai=sancai+'h'
            elif di_500[name]%10==5 or di_500[name]%10==6:
                sancai=sancai+'t'
            elif di_500[name]%10==7 or di_500[name]%10==8:
                sancai=sancai+'j'
            elif di_500[name]%10==9 or di_500[name]%10==0:
                sancai=sancai+'s'
            tup_sancai_score = (name,sancai_score.get(sancai,10))
            sancai_500.append(tup_sancai_score)
    else:
        tian = bh_dict.get(xing[0],10)+bh_dict.get(xing[1],10)
        for name in good_500:
            ren_500[name]=bh_dict.get(xing[1],10)+bh_dict.get(name[0],10)
            if(len(name)==2):
                di_500[name]=bh_dict.get(name[0],10)+bh_dict.get(name[1],10)
                zong_500[name]=bh_dict.get(name[0],10)+bh_dict.get(name[1],10)+bh_dict.get(xing[0],10)+bh_dict.get(xing[1],10)
            else:
                di_500[name]=bh_dict.get(name[0],10)+1
                zong_500[name]=bh_dict.get(name[0],10)+bh_dict.get(xing[0],10)+bh_dict.get(xing[1],10)
            sancai=''
            if tian%10==1 or tian%10==2:
                sancai=sancai+'m'
            elif tian%10==3 or tian%10==4:
                sancai=sancai+'h'
            elif tian%10==5 or tian%10==6:
                sancai=sancai+'t'
            elif tian%10==7 or tian%10==8:
                sancai=sancai+'j'
            elif tian%10==9 or tian%10==0:
                sancai=sancai+'s'

            if ren_500[name]%10==1 or ren_500[name]%10==2:
                sancai=sancai+'m'
            elif ren_500[name]%10==3 or ren_500[name]%10==4:
                sancai=sancai+'h'
            elif ren_500[name]%10==5 or ren_500[name]%10==6:
                sancai=sancai+'t'
            elif ren_500[name]%10==7 or ren_500[name]%10==8:
                sancai=sancai+'j'
            elif ren_500[name]%10==9 or ren_500[name]%10==0:
                sancai=sancai+'s'

            if di_500[name]%10==1 or di_500[name]%10==2:
                sancai=sancai+'m'
            elif di_500[name]%10==3 or di_500[name]%10==4:
                sancai=sancai+'h'
            elif di_500[name]%10==5 or di_500[name]%10==6:
                sancai=sancai+'t'
            elif di_500[name]%10==7 or di_500[name]%10==8:
                sancai=sancai+'j'
            elif di_500[name]%10==9 or di_500[name]%10==0:
                sancai=sancai+'s'
            tup_sancai_score = (name,sancai_score.get(sancai,5))
            sancai_500.append(tup_sancai_score)
    sancai_500_new = sorted(sancai_500, key=lambda x,:x[1],reverse=True)
    #三才算分
    good_200 = []
    for sancai in sancai_500_new:
        if len(good_200)>150:
            break
        good_200.append(sancai[0])
        tup_wuge_score = (sancai[0],bh_wg_dict.get(di_500.get(sancai[0],0),0)+bh_wg_dict.get(ren_500.get(sancai[0],0),0)+bh_wg_dict.get(zong_500.get(sancai[0],0),0))
        wuge_150.append(tup_wuge_score)

    #五格算分
    wuge_150_new = sorted(wuge_150, key=lambda x, :x[1],reverse=True)
    good_100=[]
    for wuge in wuge_150_new:
        if len(good_100)>100:
            break;
        good_100.append(wuge[0])
    return  good_100

def get_result(num,names):
    result = []
    if len(names)<100 :
        return result
    if num == 2:
        result.append(names[0])
        result.append(names[10])
    else:
        nameSize = len(names)
        for i in range(num):
            positionTemp = random.randint(0, 1000) % (nameSize-i)
            result.append(names[positionTemp])
            names[positionTemp] = names[nameSize-i-1]

    return  result

def get_two(tonglei,rigan_wx,is_weak,minTong,minYi,wxscore,xing,num,sex,first='',sec=''):
    type = 1
    if sex=='1':
        type = 1
    elif sex=='2':
        type = 2
    names500 = choose_name_from_baze(tonglei,rigan_wx,is_weak,minTong,minYi,wxscore,type,first='',sec='')
    names = cuputer_score(xing,names500)
    return  get_result(num,names)

def get_two_custom(xing,firstWx,secondWx,sex,num):
    if sex=='1':
        type = 1
    elif sex=='2':
        type = 2
    names500 = choose_from_wuxing(firstWx,secondWx,type)
    names = cuputer_score(xing,names500)
    return  get_result(num,names)

def get_one_custom(xing,firstWx,sex,num):
    if sex=='1':
        type = 3
    elif sex=='2':
        type = 4
    names500 = choose_from_wuxing(firstWx,'',type)
    names = cuputer_score(xing,names500)
    return  get_result(num,names)

def get_one(tonglei,rigan_wx,is_weak,minTong,minYi,wxscore,xing,num,sex):
    if sex=='1':
        type = 3
    elif sex=='2':
        type = 4
    names500 = choose_name_from_baze(tonglei,rigan_wx,is_weak,minTong,minYi,wxscore,type)
    names = cuputer_score(xing,names500)
    return  get_result(num,names)

def get_first(tonglei,rigan_wx,is_weak,minTong,minYi,wxscore,xing,num,sex,sec=''):
    if sex=='1':
        type = 5
    elif sex=='2':
        type = 6
    names500 = choose_name_from_baze(tonglei,rigan_wx,is_weak,minTong,minYi,wxscore,type,first='',sec=sec)
    names = cuputer_score(xing,names500)
    return  get_result(num,names)


def get_sec(tonglei,rigan_wx,is_weak,minTong,minYi,wxscore,xing,num,sex,first=''):
    if sex=='1':
        type = 7
    if sex=='2':
        type = 8
    names500 = choose_name_from_baze(tonglei,rigan_wx,is_weak,minTong,minYi,wxscore,type,first=first,sec='')
    names = cuputer_score(xing,names500)
    return  get_result(num,names)

if __name__ == "__main__":
    init_data()
    names = get_two('2019-5-4 15:00','',2,50 )
    print(names)