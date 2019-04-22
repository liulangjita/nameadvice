from app import app
from flask import render_template,flash,redirect,url_for,request
from app.forms import LoginForm
import models
import json
import time

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='我的')


@app.route('/query',methods=['GET','POST'])
def query():
    if len(models.wx_dict)==0:
        models.init_data()
    tonglei = request.values['tonglei']
    rigan_wx = request.values['rigan_wx']
    is_weak = request.values['is_weak']
    minTong = request.values['minTong']
    minYi = request.values['minYi']
    wuxingscore = request.values['wuxingscore']
    xing = request.values['xing']
    sex = request.values['sex']
    doublename = request.values['doublename']
    firstname = request.values['firstname']
    secname = request.values['secname']
    if doublename == '1':
        ret = models.get_one(tonglei,rigan_wx,is_weak,minTong,minYi,wuxingscore.split(','),xing,50,sex)
    else:
        if len(firstname) == 1:
            ret = models.get_sec(tonglei, rigan_wx, is_weak, minTong, minYi, wuxingscore.split(','), xing, 50, sex,first=firstname)
        elif len(secname) == 1:
            ret = models.get_first(tonglei, rigan_wx, is_weak, minTong, minYi, wuxingscore.split(','), xing, 50, sex,sec=secname)
        else:
            ret = models.get_two(tonglei,rigan_wx,is_weak,minTong,minYi,wuxingscore.split(','),xing,50,sex)
    return  json.dumps(ret,ensure_ascii=False)

@app.route('/querycustom',methods=['GET','POST'])
def querycustom():
    if len(models.wx_dict)==0:
        models.init_data()
    firstWx = request.values['firstWx']
    secondWx = request.values['secondWx']
    xing = request.values['xing']
    sex = request.values['sex']
    doublename = request.values['doublename']
    if doublename == '1':
        ret = models.get_one_custom(xing,firstWx,sex,50)
    else:
        ret = models.get_two_custom(xing,firstWx,secondWx,sex,50)
    return  json.dumps(ret,ensure_ascii=False)


@app.route('/analyse_bazi',methods=['GET','POST'])
def analyse_bazi():
    if len(models.wx_dict)==0:
        models.init_data()
    date = request.values['date']
    birthdaytime = request.values['time']
    birthdayStr = date + ' '+ birthdaytime
    birthday=time.strptime(birthdayStr,'%Y-%m-%d %H:%M:%S');
    ret = models.get_bazi_from_date(birthday.tm_year,birthday.tm_mon,birthday.tm_mday,birthday.tm_hour,birthday.tm_min)
    return  json.dumps(ret,ensure_ascii=False)


@app.route('/analyse_mingzi',methods=['GET','POST'])
def analyse_mingzi():
    if len(models.wx_dict)==0:
        models.init_data()
    xing = request.values['xing']
    ming = request.values['ming']
    ret = models.analyse_mingzi(xing,ming)
    return  json.dumps(ret,ensure_ascii=False)