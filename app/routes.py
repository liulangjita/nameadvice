from app import app
from flask import render_template,flash,redirect,url_for,request
from app.forms import LoginForm
import models
import json
import time

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'duke'}
    posts = [
        {
            'author': {'username': '刘'},
            'body': '这是模板模块中的循环例子～1'

        },
        {
            'author': {'username': '忠强'},
            'body': '这是模板模块中的循环例子～2'
        }
    ]
    return render_template('index.html', title='我的', user=user, posts=posts)

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    #验证表格中的数据格式是否正确
    if form.validate_on_submit():
        #闪现的信息会出现在页面，当然在页面上要设置
        flash('用户登录的名户名是:{} , 是否记住我:{}'.format(
            form.username.data,form.remember_me.data))
        #重定向至首页
        return redirect(url_for('index'))
    #首次登录/数据格式错误都会是在登录界面
    return render_template('login.html',title='登录',form=form)

@app.route('/query',methods=['GET','POST'])
def query():
    if len(models.wx_dict)==0:
        models.init_data()
    tonglei = request.values['tonglei']
    rigan_wx = request.values['rigan_wx']
    is_weak = request.values['is_weak']
    minTong = request.values['minTong']
    minYi = request.values['minYi']
    bazi = request.values['bazi']
    xing = request.values['xing']
    ret = models.get_two(tonglei,rigan_wx,is_weak,minTong,minYi,bazi,type,xing,50)
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
    date = request.values['date']
    birthdaytime = request.values['time']
    birthdayStr = date + ' '+ birthdaytime
    birthday=time.strptime(birthdayStr,'%Y-%m-%d %H:%M:%S');
    ret = models.get_bazi_from_date(birthday.tm_year,birthday.tm_mon,birthday.tm_mday,birthday.tm_hour,birthday.tm_min)
    return  json.dumps(ret,ensure_ascii=False)