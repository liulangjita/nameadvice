

# Create your models here.
import ctypes
import time
import random

class wx_method(object):
    wx_dict = {}
    bh_dict = {}
    bh_wg_dict = {1:1,3:1,5:1,6:1,7:1,8:1,11:1,13:1,15:1,16:1,17:1,18:1,21:1,23:1,24:1,25:1,29:1,31:1,32:1,33:1,35:1,37:1,39:1,41:1,45:1,47:1,48:1,52:1,55:1,57:1,61:1,63:1,65:1,67:1,68:1,81:1,
                  2:0,4:0,9:0,10:0,12:0,14:0,19:0,20:0,22:0,26:0,27:0,28:0,30:0,36:0,34:0,38:0,40:0,42:0,43:0,44:0,46:0,49:0,50:0,51:0,53:0,54:0,56:0,58:0,59:0,60:0,62:0,64:0,66:0,69:0,70:0,71:0,72:0,73:0,74:0,75:0,76:0,77:0,78:0,79:0,80:0}
    mand_arr = []
    womand_arr = []
    man_arr = []
    woman_arr = []
    wx_score=[]

    WuXingTable = ['金', '木', '水', '火', '土' ]

    TianGan_WuXingProp = [1, 1, 3, 3, 4,4, 0, 0, 2, 2]
    DiZhi_WuXingProp = [2, 4, 1, 1, 4,3, 3, 4, 0, 0, 4, 2]
    GenerationSourceTable = [4, 2, 0, 1,3]
    TianGan = '甲乙丙丁戊己庚辛壬癸'
    DiZhi = '子丑寅卯辰巳午未申酉戌亥'
    bazi=[]
    good_500=[]
    good_200=[]
    good_100=[]
    tian=0
    di_500={}
    ren_500={}
    zong_500={}
    sancai_score={'mmm':10,'mmh':10,'mmt':10,'mmj':4,'mms':6,
                  'mhm':10,'mhh':8,'mht':10,'mhj':4,'mhs':0,
                  'mtm':0,'mth':8,'mtt':9,'mtj':6,'mts':0,
                  'mjm':0,'mjh':0,'mjt':4,'mjj':0,'mjs':0,
                  'msm':10,'msh':4,'mst':4,'msj':10,'mss':10,
                  'hmm':10,'hmh':10,'hmt':10,'hmj':4,'hms':8,
                  'hhm':10,'hhh':8,'hht':10,'hhj':0,'hhs':0,
                  'htm':6,'hth':10,'htt':10,'htj':10,'hts':6,
                  'hjm':0,'hjh':0,'hjt':5,'hjj':0,'hjs':0,
                  'hsm':4,'hsh':0,'hst':0,'hsj':0,'hss':0,
                  'tmm':8,'tmh':8,'tmt':4,'tmj':0,'tms':4,
                  'thm':10,'thh':10,'tht':10,'thj':6,'ths':0,
                  'ttm':8,'tth':10,'ttt':10,'ttj':10,'tts':4,
                  'tjm':4,'tjh':4,'tjt':10,'tjj':10,'tjs':10,
                  'tsm':4,'tsh':0,'tst':0,'tsj':5,'tss':0,
                  'jmm':4,'jmh':4,'jmt':4,'jmj':0,'jms':4,
                  'jhm':4,'jhh':5,'jht':5,'jhj':0,'jhs':0,
                  'jtm':8,'jth':10,'jtt':10,'jtj':10,'jts':6,
                  'jjm':0,'jjh':0,'jjt':10,'jjj':8,'jjs':8,
                  'jsm':10,'jsh':4,'jst':9,'jsj':10,'jss':8,
                  'smm':10,'smh':10,'smt':10,'smj':4,'sms':10,
                  'shm':8,'shh':0,'sht':4,'shj':0,'shs':0,
                  'stm':0,'sth':8,'stt':8,'stj':8,'sts':0,
                  'sjm':4,'sjh':4,'sjt':10,'sjj':8,'sjs':10,
                  'ssm':10,'ssh':0,'sst':0,'ssj':10,'sss':8}

    def ComputeGanIndex(self,gan):
         for i in range(0,10):
            if(self.TianGan[i] == gan):
                break;
         if i >= 10:
             return -1;
         return i;

    def ComputeZhiIndex(self, zhi):
         for i in range(0,12):
            if(self.DiZhi[i] == zhi):
                break;
         if i >= 12:
             return -1;
         return i;

    def init_data(self):
        data_lines_j = open('data/j.txt',encoding='utf-8').readlines()
        data_lines_m = open('data/m.txt',encoding='utf-8').readlines()
        data_lines_s = open('data/s.txt',encoding='utf-8').readlines()
        data_lines_h = open('data/h.txt',encoding='utf-8').readlines()
        data_lines_t = open('data/t.txt',encoding='utf-8').readlines()
        for line in data_lines_j:  # 去掉头部无用信息
            l = line.strip().split(':')
            if len(l)==2:
                for word in l[1]:
                    self.wx_dict[word]='j'
                    self.bh_dict[word]=int(l[0])
        for line in data_lines_m:  # 去掉头部无用信息
            l = line.strip().split(':')
            if len(l)==2:
                for word in l[1]:
                    self.wx_dict[word]='m'
                    self.bh_dict[word]=int(l[0])
        for line in data_lines_s:  # 去掉头部无用信息
            l = line.strip().split(':')
            if len(l)==2:
                for word in l[1]:
                    self.wx_dict[word]='s'
                    self.bh_dict[word]=int(l[0])
        for line in data_lines_h:  # 去掉头部无用信息
            l = line.strip().split(':')
            if len(l)==2:
                for word in l[1]:
                    self.wx_dict[word]='h'
                    self.bh_dict[word]=int(l[0])
        for line in data_lines_t:  # 去掉头部无用信息
            l = line.strip().split(':')
            if len(l)==2:
                for word in l[1]:
                    self.wx_dict[word]='t'
                    self.bh_dict[word]=int(l[0])

        data_lines_all = open('data/bh.txt',encoding='utf-8').readlines()
        for line in data_lines_all:  # 去掉头部无用信息
            l = line.strip().split(':')
            if len(l)==2:
                for word in l[1]:
                    self.bh_dict[word]=int(l[0])

        man=open('data/man.txt',encoding='utf-8').read()
        woman=open('data/woman.txt',encoding='utf-8').read()
        for word in man:
            self.man_arr.append(word)

        for word in woman:
            self.woman_arr.append(word)


        dman=open('data/mand.txt',encoding='utf-8').readlines()
        dwoman=open('data/womand.txt',encoding='utf-8').readlines()

        for line in dman:
            line = line.strip()
            if len(line)==2:
                self.mand_arr.append(line)

        for line in dwoman:
            line = line.strip()
            if len(line)==2:
                self.womand_arr.append(line)

    def get_bazi_from_date(self,year,month,day,hour,minute):
        dll = ctypes.windll.LoadLibrary('data/valuatedll.dll')
        test_result = dll.GetScoreFromDate(year,month,day,hour,minute)

        size = -1
        test_result = ctypes.string_at(test_result, size)
        tt = test_result.decode('utf-8')
        strtemp=tt.split(',')
        wx_score_lei = []
        wx_score_lei_temp = []
        score =[0,0,0,0,0]
        for i in range(0,6):
            if i<5:
                wx_score_lei.append(float(strtemp[i]))
                wx_score_lei_temp.append(float(strtemp[i]))
            elif i==5:
                 for j in range(0,8):
                    self.bazi.append(strtemp[i][j])
                    wx_index = 0
                    if j%2==0:
                        wx_index = self.TianGan_WuXingProp[self.ComputeGanIndex(strtemp[i][j])]
                    else:
                        wx_index = self.DiZhi_WuXingProp[self.ComputeZhiIndex(strtemp[i][j])]
                    score[wx_index]=score[wx_index]+1
        rigan_wx=self.TianGan_WuXingProp[self.ComputeGanIndex(strtemp[5][4])]
        tonglei=self.GenerationSourceTable[rigan_wx]
        tonglei_score=wx_score_lei[rigan_wx]+wx_score_lei[tonglei]
        yilei_score=wx_score_lei[0]+wx_score_lei[1]+wx_score_lei[2]+wx_score_lei[3]+wx_score_lei[4]-tonglei_score
        is_weak=True
        if tonglei_score>yilei_score:
            is_weak=False
        minTong = min(wx_score_lei[tonglei],wx_score_lei[rigan_wx])
        tempRi = wx_score_lei_temp[rigan_wx]
        tempTong = wx_score_lei_temp[tonglei]
        wx_score_lei_temp.remove(tempRi)
        wx_score_lei_temp.remove(tempTong)
        minYi = min(wx_score_lei_temp)
        for i in range(0,5):
            if score[i]==0:
                score[i]=-5
            elif score[i]==1:
                score[i]=-1
            elif score[i]==2:
                score[i]=0
            elif score[i]==3:
                score[i]=2
            else:
                score[i]=3
            if i==tonglei or i==rigan_wx:
                if is_weak:
                    score[i]=score[i]-3
                    if wx_score_lei[i]==minTong:
                        score[i]=score[i]-1
                    if i==rigan_wx:
                        score[i]=score[i]-1
            else:
                if not is_weak:
                    score[i]=score[i]-3
                    if wx_score_lei[i]==minYi:
                        score[i]=score[i]-1
                    if i==rigan_wx:
                        score[i]=score[i]-1
        self.wx_score=score




    def choose_name_from_baze(self,type,xing,first='',sec=''):
        self.name_score = []
        self.good_500 = []
        wxIndexDic={'j':0,'m':1,'s':2,'h':3,'t':4}
        total_arr = []
        if type==1:
            total_arr = self.mand_arr
        elif type == 2:
            total_arr = self.womand_arr
        elif type == 3 or type == 5 or type == 7:
            total_arr = self.man_arr
        elif type == 4 or type == 6 or type == 8:
            total_arr = self.woman_arr
        if type==1 or type == 2:
            for name in total_arr:
                score_name=0
                wxName = self.wx_dict.get(name[0])
                if wxName != None:
                    wxIndex = wxIndexDic.get(wxName)
                    score_name=score_name+self.wx_score[wxIndex]
                wxName = self.wx_dict.get(name[1])
                if wxName != None:
                    wxIndexOld = wxIndex
                    wxIndex = wxIndexDic.get(wxName)
                    if wxIndexOld==wxIndex:
                        score_name=score_name+1
                    score_name=score_name+self.wx_score[wxIndex]
                if name[0]==name[1]:
                    score_name=score_name+1
                tup_score_name = (name,score_name)
                self.name_score.append(tup_score_name)
        elif type == 3 or type==4:
            for name in total_arr:
                score_name=0
                wxName = self.wx_dict.get(name[0])
                if wxName != None:
                    wxIndex = wxIndexDic.get(wxName)
                    score_name=score_name+self.wx_score[wxIndex]
                tup_score_name = (name,score_name)
                self.name_score.append(tup_score_name)
        elif type == 5 or type == 6:
            for name in total_arr:
                score_name=0
                wxName = self.wx_dict.get(name[0])
                if wxName != None:
                    wxIndex = wxIndexDic.get(wxName)
                    score_name=score_name+self.wx_score[wxIndex]
                wxName = self.wx_dict.get(sec)
                if wxName != None:
                    wxIndexOld = wxIndex
                    wxIndex = wxIndexDic.get(wxName)
                    if wxIndexOld==wxIndex:
                        score_name=score_name+1
                    score_name=score_name+self.wx_score[wxIndex]
                if name[0]==sec:
                    score_name=score_name+1
                tup_score_name = (name+sec,score_name)
                self.name_score.append(tup_score_name)
        elif type == 7 or type == 8:
            for name in total_arr:
                score_name=0
                wxName = self.wx_dict.get(first)
                if wxName != None:
                    wxIndex = wxIndexDic.get(wxName)
                    score_name=score_name+self.wx_score[wxIndex]
                wxName = self.wx_dict.get(name[0])
                if wxName != None:
                    wxIndexOld = wxIndex
                    wxIndex = wxIndexDic.get(wxName)
                    if wxIndexOld==wxIndex:
                        score_name=score_name+1
                    score_name=score_name+self.wx_score[wxIndex]
                if name[0]==first:
                    score_name=score_name+1
                tup_score_name = (first+name,score_name)
                self.name_score.append(tup_score_name)
        tup_score_name_new = sorted(self.name_score, key=lambda x,:x[1])
        for name_good in tup_score_name_new:
            self.good_500.append(name_good[0])
            if len(self.good_500)==300:
                break
        return  self.good_500

    def cuputer_score(self,xing):
        sancai_500 = []
        wuge_150=[]
        if  len(xing)==1:
            tian = self.bh_dict.get(xing[0],10)+1
            for name in self.good_500:
                self.ren_500[name]=self.bh_dict.get(xing[0],10)+self.bh_dict.get(name[0],10)
                if(len(name)==2):
                    self.di_500[name]=self.bh_dict.get(name[0],10)+self.bh_dict.get(name[1],10)
                    self.zong_500[name]=self.bh_dict.get(name[0],10)+self.bh_dict.get(name[1],10)+self.bh_dict.get(xing[0],10)
                else:
                    self.di_500[name]=self.bh_dict.get(name[0],10)+1
                    self.zong_500[name]=self.bh_dict.get(name[0],10)+self.bh_dict.get(xing[0],10)
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

                if self.ren_500[name]%10==1 or self.ren_500[name]%10==2:
                    sancai=sancai+'m'
                elif self.ren_500[name]%10==3 or self.ren_500[name]%10==4:
                    sancai=sancai+'h'
                elif self.ren_500[name]%10==5 or self.ren_500[name]%10==6:
                    sancai=sancai+'t'
                elif self.ren_500[name]%10==7 or self.ren_500[name]%10==8:
                    sancai=sancai+'j'
                elif self.ren_500[name]%10==9 or self.ren_500[name]%10==0:
                    sancai=sancai+'s'

                if self.di_500[name]%10==1 or self.di_500[name]%10==2:
                    sancai=sancai+'m'
                elif self.di_500[name]%10==3 or self.di_500[name]%10==4:
                    sancai=sancai+'h'
                elif self.di_500[name]%10==5 or self.di_500[name]%10==6:
                    sancai=sancai+'t'
                elif self.di_500[name]%10==7 or self.di_500[name]%10==8:
                    sancai=sancai+'j'
                elif self.di_500[name]%10==9 or self.di_500[name]%10==0:
                    sancai=sancai+'s'
                tup_sancai_score = (name,self.sancai_score.get(sancai,10))
                sancai_500.append(tup_sancai_score)
        else:
            tian = self.bh_dict.get(xing[0],10)+self.bh_dict.get(xing[1],10)
            for name in self.good_500:
                self.ren_500[name]=self.bh_dict.get(xing[1],10)+self.bh_dict.get(name[0],10)
                if(len(name)==2):
                    self.di_500[name]=self.bh_dict.get(name[0],10)+self.bh_dict.get(name[1],10)
                    self.zong_500[name]=self.bh_dict.get(name[0],10)+self.bh_dict.get(name[1],10)+self.bh_dict.get(xing[0],10)+self.bh_dict.get(xing[1],10)
                else:
                    self.di_500[name]=self.bh_dict.get(name[0],10)+1
                    self.zong_500[name]=self.bh_dict.get(name[0],10)+self.bh_dict.get(xing[0],10)+self.bh_dict.get(xing[1],10)
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

                if self.ren_500[name]%10==1 or self.ren_500[name]%10==2:
                    sancai=sancai+'m'
                elif self.ren_500[name]%10==3 or self.ren_500[name]%10==4:
                    sancai=sancai+'h'
                elif self.ren_500[name]%10==5 or self.ren_500[name]%10==6:
                    sancai=sancai+'t'
                elif self.ren_500[name]%10==7 or self.ren_500[name]%10==8:
                    sancai=sancai+'j'
                elif self.ren_500[name]%10==9 or self.ren_500[name]%10==0:
                    sancai=sancai+'s'

                if self.di_500[name]%10==1 or self.di_500[name]%10==2:
                    sancai=sancai+'m'
                elif self.di_500[name]%10==3 or self.di_500[name]%10==4:
                    sancai=sancai+'h'
                elif self.di_500[name]%10==5 or self.di_500[name]%10==6:
                    sancai=sancai+'t'
                elif self.di_500[name]%10==7 or self.di_500[name]%10==8:
                    sancai=sancai+'j'
                elif self.di_500[name]%10==9 or self.di_500[name]%10==0:
                    sancai=sancai+'s'
                tup_sancai_score = (name,self.sancai_score.get(sancai,5))
                sancai_500.append(tup_sancai_score)
        sancai_500_new = sorted(sancai_500, key=lambda x,:x[1],reverse=True)
        #三才算分
        self.good_200 = []
        for sancai in sancai_500_new:
            if len(self.good_200)>150:
                break
            self.good_200.append(sancai[0])
            tup_wuge_score = (sancai[0],self.bh_wg_dict.get(self.di_500.get(sancai[0],0),0)+self.bh_wg_dict.get(self.ren_500.get(sancai[0],0),0)+self.bh_wg_dict.get(self.zong_500.get(sancai[0],0),0))
            wuge_150.append(tup_wuge_score)

        #五格算分
        wuge_150_new = sorted(wuge_150, key=lambda x, :x[1],reverse=True)
        self.good_100=[]
        for wuge in wuge_150_new:
            if len(self.good_100)>100:
                break;
            self.good_100.append(wuge[0])


        return  self.good_100

    def get_result(self,num,names):
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

    def get_two(self,date,birthdaytime,xing,sex,num):
        if sex=='1':
            type = 1
        elif sex=='2':
            type = 2
        birthdayStr = date + ' '+ birthdaytime
        birthday=time.strptime(birthdayStr,'%Y-%m-%d %H:%M:%S');
        self.get_bazi_from_date(birthday.tm_year,birthday.tm_mon,birthday.tm_mday,birthday.tm_hour,birthday.tm_min)
        names = self.choose_name_from_baze(type,xing)
        names = self.cuputer_score(xing)


        return  self.get_result(num,names)

    def get_one(self,birthdayStr,xing,sex,num):
        if sex==1:
            type = 3
        elif sex==2:
            type = 4
        birthday=time.strptime(birthdayStr,'%Y-%m-%d %H:%M');
        self.get_bazi_from_date(birthday.tm_year,birthday.tm_mon,birthday.tm_mday,birthday.tm_hour,birthday.tm_min)
        names = self.choose_name_from_baze(type,xing)
        names = self.cuputer_score(xing)
        return    self.get_result(num,names)

    def get_first(self,birthdayStr,xing,sec,sex,num):
        if sex==1:
            type = 5
        elif sex==2:
            type = 6
        birthday=time.strptime(birthdayStr,'%Y-%m-%d %H:%M');
        self.get_bazi_from_date(birthday.tm_year,birthday.tm_mon,birthday.tm_mday,birthday.tm_hour,birthday.tm_min)
        names = self.choose_name_from_baze(type,xing,'',sec)
        names = self.cuputer_score(xing)
        return    self.get_result(num,names)


    def get_sec(self,birthdayStr,xing,first,sex,num):
        if sex==1:
            type = 7
        if sex==2:
            type = 8
        birthday=time.strptime(birthdayStr,'%Y-%m-%d %H:%M');
        self.get_bazi_from_date(birthday.tm_year,birthday.tm_mon,birthday.tm_mday,birthday.tm_hour,birthday.tm_min)
        names = self.choose_name_from_baze(type,xing,first,'')
        names = self.cuputer_score(xing)
        return    self.get_result(num,names)

if __name__ == "__main__":
    ww = wx_method();
    ww.init_data()
    names = ww.get_two('1988-5-5 17:58','闫',2,50 )
    print(names)