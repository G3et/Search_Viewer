# -*- coding: utf-8 -*-
import base64
import csv
import json
from jsonpath import jsonpath
import jsonpath
import requests
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QMessageBox, QTableWidgetItem
import shodan
import time
from threading import Thread
from PySide2.QtGui import QIcon
import resources_rc
import threading
import re
import urllib.parse
from iconhash import IconHash
from PySide2.QtWidgets import QApplication, QMainWindow
from configparser import ConfigParser
from configobj import ConfigObj
from Search_Viewer_ui import Ui_MainWindow


def set_table_header_bold(table):
    font = table.horizontalHeader().font()
    font.setBold(True)
    table.horizontalHeader().setFont(font)


class LoginGui(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(LoginGui, self).__init__()   # 调用父类的初始化方法
        self.setupUi(self)                 #  调用Ui_MainWindow的setupUi方法布置界面
        self.button.clicked.connect(self.handleCalc)
        self.clear.clicked.connect(self.clear1)
        self.clear_2.clicked.connect(self.clear_22)
        self.clear_3.clicked.connect(self.clear_33)
        self.clear_7.clicked.connect(self.clear_77)
        self.clear_4.clicked.connect(self.clear_44)
        self.Censys_clearjieguo.clicked.connect(self.Censys_clearjieguo1)
        self.clearrizi.clicked.connect(self.clearrizi1)
        self.clearrizi_2.clicked.connect(self.hunter_clearrizi)
        self.clearrizi_3.clicked.connect(self.clearrizi_33)
        self.clearrizi_7.clicked.connect(self.clearrizi_77)
        self.clearrizi_4.clicked.connect(self.clearrizi_44)
        self.Censys_clearrizi.clicked.connect(self.Censys_clearrizi1)
        self.export_2.clicked.connect(self.export_22)
        self.export_3.clicked.connect(self.export_33)
        self.export_4.clicked.connect(self.export_44)
        self.export_8.clicked.connect(self.export_quake)
        self.export_6.clicked.connect(self.export_zoomeye)
        self.Censys_export.clicked.connect(self.Censys_export_1)
        self.button_2.clicked.connect(self.hunter)
        self.button_3.clicked.connect(self.shodan_search)
        self.icon_hash = IconHash(self)  # 创建IconHash的实例对象
        self.button_4.clicked.connect(self.icon_hash.icohash)  # 绑定icohash方法
        self.button_9.clicked.connect(self.quake_search1)
        self.button_5.clicked.connect(self.zoomeye_search1)
        self.Censys_search_1.clicked.connect(self.Censys)
        self.save_config.clicked.connect(self.save_config_all)
        self.fofa_xiugai.clicked.connect(self.fofa_xiugai_all)
        self.hunter_xiugai.clicked.connect(self.hunter_xiugai_all)
        self.shodan_xiugai.clicked.connect(self.shodan_xiugai_all)
        self.quake_xiugai.clicked.connect(self.quake_xiugai_all)
        self.zoomeye_xiugai.clicked.connect(self.zoomeye_xiugai_all)
        self.censys_xiugai.clicked.connect(self.censys_xiugai_all)
        self.Censys_next.clicked.connect(self.Censys_n)
        self.Censys_prev.clicked.connect(self.Censys_p)
        self.next_cursor = ""
        self.prev_cursor = ""

        set_table_header_bold(self.fofa)
        set_table_header_bold(self.hunter_tab)
        set_table_header_bold(self.shodan_tab)
        set_table_header_bold(self.quake_tab)
        set_table_header_bold(self.zoomeye_tab)
        set_table_header_bold(self.Censys_tab)

    def save_config_all(self):
        choice = QMessageBox.question(
            self,
            '确认',
            '是否保存？')

        if choice == QMessageBox.Yes:
            config = ConfigObj()
            config.filename = 'config.ini'

            # fofa
            your_fofa_email = self.your_fofa_email.text()
            your_fofa_api = self.your_fofa_api.text()

            config['fofa_email'] = {}
            config['fofa_email']['your_email'] = self.your_fofa_email

            config['fofa_key'] = {}
            config['fofa_key']['fofa_key'] = self.your_fofa_api

            # hunter
            your_hunter_api = self.your_hunter_api.text()

            config['hunter_api'] = {}
            config['hunter_api']['your_api'] = your_hunter_api

            # shodan
            your_shodan_api = self.your_shodan_api.text()

            config['shodan_api'] = {}
            config['shodan_api']['your_api'] = your_shodan_api

            # quake
            your_quake_api = self.your_quake_api.text()

            config['quake_api'] = {}
            config['quake_api']['your_api'] = your_quake_api

            # zoomeye
            your_zoomeye_api = self.your_zoomeye_api.text()

            config['zoomeye_api'] = {}
            config['zoomeye_api']['your_zoomeye_api'] = self.your_zoomeye_api

            # censys
            your_censys_uid = self.your_censys_uid.text()
            your_censys_secret = self.your_censys_secret.text()

            config['censys_uid'] = {}
            config['censys_uid']['censys_uid'] = self.your_censys_uid

            config['censys_secret'] = {}
            config['censys_secret']['censys_secret'] = self.your_censys_secret

            config.write()
            QMessageBox.information(
                self,
                '成功',
                '配置成功  ')
        if choice == QMessageBox.No:
            pass

    def fofa_xiugai_all(self):
        choice = QMessageBox.question(
            self,
            '确认',
            '是否修改FOFA配置？')
        try:

            if choice == QMessageBox.Yes:
                conf_ini = "config.ini"
                config = ConfigObj(conf_ini, encoding='UTF8')
                config['fofa_email']['your_email'] = self.your_fofa_email.text()
                config['fofa_key']['fofa_key'] = self.your_fofa_api.text()
                config.write()
                QMessageBox.information(
                    self,
                    '成功',
                    '修改成功  ')
            if choice == QMessageBox.No:
                pass
        except:
            QMessageBox.information(
                self,
                '提示',
                '检测到你第一次配置，请先点击保存  ')

    def hunter_xiugai_all(self):
        choice = QMessageBox.question(
            self,
            '确认',
            '是否修改鹰图配置？')
        try:

            if choice == QMessageBox.Yes:
                conf_ini = "config.ini"
                config = ConfigObj(conf_ini, encoding='UTF8')
                config['hunter_api']['your_api'] = self.your_hunter_api.text()
                config.write()
                QMessageBox.information(
                    self,
                    '成功',
                    '修改成功  ')
            if choice == QMessageBox.No:
                pass
        except:
            QMessageBox.information(
                self,
                '提示',
                '检测到你第一次配置，请先点击保存  ')

    def shodan_xiugai_all(self):
        choice = QMessageBox.question(
            self,
            '确认',
            '是否修改shodan配置？')
        try:

            if choice == QMessageBox.Yes:
                conf_ini = "config.ini"
                config = ConfigObj(conf_ini, encoding='UTF8')
                config['shodan_api']['your_api'] = self.your_shodan_api.text()
                config.write()
                QMessageBox.information(
                    self,
                    '成功',
                    '修改成功  ')
            if choice == QMessageBox.No:
                pass
        except:
            QMessageBox.information(
                self,
                '提示',
                '检测到你第一次配置，请先点击保存  ')

    def quake_xiugai_all(self):
        choice = QMessageBox.question(
            self,
            '确认',
            '是否修改quake配置？')
        try:
            if choice == QMessageBox.Yes:
                conf_ini = "config.ini"
                config = ConfigObj(conf_ini, encoding='UTF8')
                config['quake_api']['your_api'] = self.your_quake_api.text()
                config.write()
                QMessageBox.information(
                    self,
                    '成功',
                    '修改成功  ')
            if choice == QMessageBox.No:
                pass
        except:
            QMessageBox.information(
                self,
                '提示',
                '检测到你第一次配置，请先点击保存  ')

    def zoomeye_xiugai_all(self):
        choice = QMessageBox.question(
            self,
            '确认',
            '是否修改Zoomeye配置？')
        try:
            if choice == QMessageBox.Yes:
                conf_ini = "config.ini"
                config = ConfigObj(conf_ini, encoding='UTF8')
                config['zoomeye_api']['your_zoomeye_api'] = self.your_zoomeye_api.text()
                config.write()
                QMessageBox.information(
                    self,
                    '成功',
                    '修改成功  ')
            if choice == QMessageBox.No:
                pass
        except:
            QMessageBox.information(
                self,
                '提示',
                '检测到你第一次配置，请先点击保存  ')

    def censys_xiugai_all(self):
        choice = QMessageBox.question(
            self,
            '确认',
            '是否修改FOFA配置？')
        try:

            if choice == QMessageBox.Yes:
                conf_ini = "config.ini"
                config = ConfigObj(conf_ini, encoding='UTF8')
                config['censys_uid']['censys_uid'] = self.your_censys_uid.text()
                config['censys_secret']['censys_secret'] = self.your_censys_secret.text()
                config.write()
                QMessageBox.information(
                    self,
                    '成功',
                    '修改成功  ')
            if choice == QMessageBox.No:
                pass
        except:
            QMessageBox.information(
                self,
                '提示',
                '检测到你第一次配置，请先点击保存  ')

    def handleCalc(self):
        try:
            cf = ConfigParser()
            cf.read('config.ini')

            self.your_key = cf.get('fofa_key', 'fofa_key')
            self.your_email = cf.get('fofa_email', 'your_email')

            your_search = self.fofa_search.text()

            self.shuchu.append(f'fofa正在查询 ==> {your_search}，请稍后...' + '\n')

            thread = Thread(target=self.fofa_threadSend,
                            args=(your_search,)
                            )
            thread.start()
        except:
            QMessageBox.information(
                self,
                '提示',
                '请先配置FOFA API  ')

    def fofa_threadSend(self, your_search):
        try:
            self.fofa.setRowCount(0)  # 点击查询后不累加
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0"}
            qbase64 = base64.b64encode(your_search.encode('utf-8')).decode('ascii')
            num = self.num.currentText()  # 下拉框
            api = 'https://fofa.info/api/v1/search/all?email={}&key={}&qbase64={}&size={}&fields=host,ip,port,title,domain,country,protocol,server'.format(
                self.your_email, self.your_key,
                qbase64, num)
            html = requests.get(url=api, headers=headers)
            # print(api)

            if 'errmsg' not in html.text:
                results = html.json()["results"]
                print("共搜索到{}条记录！".format(len(results)))
                result = json.loads(html.text)  # 将str类型的数据转换为dict类型
                size = result['size']  # 转为dict然后查询
                self.label_2.setText(str(size) + ' ' + '条')
                self.shuchu.append('已找到：' + str(size) + ' ' + '条结果' + '\n')
                QApplication.processEvents()  # 刷新界面
                self.shuchu.append('查询状态：完成' + '\n' + '-' * 29)
                self.host = []
                self.ip = []
                self.port = []
                self.domain = []
                self.protocol = []
                self.fofa_title = []
                for link in result['results']:
                    host = link[0]
                    ip = link[1]
                    port = link[2]
                    title = link[3]
                    domain = link[4]
                    country = link[5]
                    protocol = link[6]
                    server = link[7]

                    row = self.fofa.rowCount()  # 获取所有列
                    self.fofa.insertRow(row)  # 插入row
                    QApplication.processEvents()
                    item = QTableWidgetItem()
                    item.setText(host)
                    item1 = QTableWidgetItem()
                    item1.setText(ip)
                    item2 = QTableWidgetItem()
                    item2.setText(port)
                    item3 = QTableWidgetItem()
                    item3.setText(title)  # \u 编码问题
                    item4 = QTableWidgetItem()
                    item4.setText(domain)
                    item5 = QTableWidgetItem()
                    item5.setText(country)
                    item6 = QTableWidgetItem()
                    item6.setText(protocol)
                    item7 = QTableWidgetItem()
                    item7.setText(server)

                    self.fofa.setItem(row, 0, item)
                    self.fofa.setItem(row, 1, item1)
                    self.fofa.setItem(row, 2, item2)
                    self.fofa.setItem(row, 3, item3)
                    self.fofa.setItem(row, 4, item4)
                    self.fofa.setItem(row, 5, item5)
                    self.fofa.setItem(row, 6, item6)
                    self.fofa.setItem(row, 7, item7)

                    self.host.append(host)
                    self.fofa_title.append(title)
                    self.ip.append(ip)
                    self.port.append(port)
                    self.domain.append(domain)
                    self.protocol.append(protocol)

            elif '[-700] 账号无效' in html.text:
                self.shuchu.append('API信息有误' + '\n' + '-' * 29)

            elif '[-700] Account Invalid' in html.text:
                self.shuchu.append('API信息有误' + '\n' + '-' * 29)

            elif '[-4] 参数错误' in html.text:
                self.shuchu.append('搜索内容不能为空' + '\n' + '-' * 29)

            elif '[-4] Params Error' in html.text:
                self.shuchu.append('搜索内容不能为空' + '\n' + '-' * 29)

            elif '[820003] F币余额不足' in html.text:
                self.shuchu.append('F币余额不足，注册会员请直接使用fofa官网查询' + '\n' + '-' * 29)

            elif '[820003] F Coins Insufficient Balance' in html.text:
                self.shuchu.append('F币余额不足，注册会员请直接使用fofa官网查询' + '\n' + '-' * 29)

            elif '[45022]' in html.text:
                self.shuchu.append('今日请求次数已达上限，继续调取将扣除F点' + '\n' + '-' * 29)
            elif '[820031]' in html.text:
                self.shuchu.append('F点余额不足' + '\n' + '-' * 29)
            else:
                self.shuchu.append('未知错误，请排查' + '\n' + '-' * 29)
        except Exception as e:
            print(e)

    def hunter(self):
        try:
            cf = ConfigParser()
            cf.read('config.ini')

            self.hunter_your_key = cf.get('hunter_api', 'your_api')
            # your_key_eval = eval(your_key)
            is_web = self.num_3.currentText()
            if is_web == 'web资产':
                a = '1'
                print(a)
            elif is_web == '非web资产':
                a = '2'
            elif is_web == '全部':
                a = '3'

            self.hunter_tab.setRowCount(0)  # 点击查询后不累加
            search = self.hunter_search.text()
            self.shuchu_2.append(f'鹰图正在查询 ==> {search}，请稍后...' + '\n')
            thread = Thread(target=self.hunter_threadSend,
                            args=(search, a)
                            )
            thread.start()
        except:
            QMessageBox.information(
                self,
                '提示',
                '请先配置鹰图API  ')

    def hunter_threadSend(self, search, a):
        search = base64.urlsafe_b64encode(search.encode("utf-8")).decode('ascii')
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0"}
        page_size = self.num_2.currentText()
        hunter_page1 = self.hunter_page.text()
        api = f'https://hunter.qianxin.com/openApi/search?&api-key={self.hunter_your_key}&search={search}&page={hunter_page1}&page_size={page_size}&is_web={a}&start_time="2000-01-01 00:00:00"&end_time="2030-03-01 00:00:00"'  # page_size展示页 page页码
        # print(api)
        html = requests.get(url=api, headers=headers)
        # print(html.text)

        json_data = html.json()
        print(json_data['code'])
        # print(json_data)

        if '"total":0' in html.text:
            self.shuchu_2.append('鹰图提示：' + '未找到记录' + '\n' + '-' * 29)

        if 'account_type' in html.text:
            total = jsonpath.jsonpath(json_data, "$..total")
            consume_quota = jsonpath.jsonpath(json_data, "$..consume_quota")
            rest_quota = jsonpath.jsonpath(json_data, "$..rest_quota")
            self.xiaohao.setText(','.join(str(i) for i in consume_quota))  # 去掉列表中的双引号
            self.shengyu.setText(','.join(str(a) for a in rest_quota))

            host = [arr['url'] for arr in json_data['data']['arr']]
            ip = [arr['ip'] for arr in json_data['data']['arr']]
            port = [arr['port'] for arr in json_data['data']['arr']]
            web_title = [arr['web_title'] for arr in json_data['data']['arr']]
            domain = [arr['domain'] for arr in json_data['data']['arr']]
            protocol = [arr['protocol'] for arr in json_data['data']['arr']]
            status_code = [arr['status_code'] for arr in json_data['data']['arr']]
            company = [arr['company'] for arr in json_data['data']['arr']]
            country = [arr['country'] for arr in json_data['data']['arr']]
            updated_at = [arr['updated_at'] for arr in json_data['data']['arr']]
            isp = [arr['isp'] for arr in json_data['data']['arr']]
            self.host1 = []
            self.ip1 = []
            self.port1 = []
            self.web_title1 = []
            self.domain1 = []
            self.protocol1 = []
            self.status_code1 = []
            self.company1 = []
            self.country1 = []
            self.updated_at1 = []
            self.isp1 = []
            for i in range(len(host)):
                host1 = host[i]
                ip1 = ip[i]
                port1 = port[i]
                web_title1 = web_title[i]
                domain1 = domain[i]
                protocol1 = protocol[i]
                status_code1 = status_code[i]
                company1 = company[i]
                country1 = country[i]
                updated_at1 = updated_at[i]
                isp1 = isp[i]

                row = self.hunter_tab.rowCount()  # 获取所有列
                self.hunter_tab.insertRow(row)  # 插入row
                item = QTableWidgetItem()
                item.setText(host1)
                item1 = QTableWidgetItem()
                item1.setText(ip1)
                item2 = QTableWidgetItem()
                item2.setText(str(port1))
                item3 = QTableWidgetItem()
                item3.setText(web_title1)
                item4 = QTableWidgetItem()
                item4.setText(domain1)
                item5 = QTableWidgetItem()
                item5.setText(protocol1)
                item6 = QTableWidgetItem()
                item6.setText(str(status_code1))
                item7 = QTableWidgetItem()
                item7.setText(company1)
                item8 = QTableWidgetItem()
                item8.setText(country1)
                item9 = QTableWidgetItem()
                item9.setText(updated_at1)
                item10 = QTableWidgetItem()
                item10.setText(isp1)

                self.hunter_tab.setItem(row, 0, item)
                self.hunter_tab.setItem(row, 1, item1)
                self.hunter_tab.setItem(row, 2, item2)
                self.hunter_tab.setItem(row, 3, item3)
                self.hunter_tab.setItem(row, 4, item4)
                self.hunter_tab.setItem(row, 5, item5)
                self.hunter_tab.setItem(row, 6, item6)
                self.hunter_tab.setItem(row, 7, item7)
                self.hunter_tab.setItem(row, 8, item8)
                self.hunter_tab.setItem(row, 9, item9)
                self.hunter_tab.setItem(row, 10, item10)

                self.host1.append(host1)
                self.ip1.append(ip1)
                self.port1.append(port1)
                self.web_title1.append(web_title1)
                self.domain1.append(domain1)
                self.protocol1.append(protocol1)
                self.status_code1.append(status_code1)
                self.company1.append(company1)
                self.country1.append(country1)
                self.updated_at1.append(updated_at1)
                self.ip1.append(ip1)

            for i in total:
                a = int(i)
                self.label_4.setText(str(a) + ' ' + '条')
                self.shuchu_2.append('已找到：' + str(a) + ' 条结果' + '\n')

        elif '搜索内容不能为空' in html.text:
            self.shuchu_2.append('搜索内容不能为空' + '\n')

        elif '大牛，您的积分用完了，明天再试试' in html.text:
            self.shuchu_2.append('大牛，您的积分用完了，明天再试试' + '\n')

        elif '令牌过期' in html.text:
            self.shuchu_2.append('API 信息有误' + '\n')

        elif '令牌缺失' in html.text:
            self.shuchu_2.append('请先配置 API' + '\n')

        elif '存在违规字符' in html.text:
            self.shuchu_2.append('存在违规字符' + '\n')

        elif '请求太多啦，稍后再试试' in html.text:
            self.shuchu_2.append('请求太多啦，稍后再试试' + '\n')

        elif json_data['code'] == 400:
            self.shuchu_2.append('语法有误，请排查' + '\n')

        else:
            self.shuchu_2.append('未知错误，请排查' + '\n')

        self.shuchu_2.append('查询状态：完成' + '\n' + '-' * 29)

    def shodan_search(self):
        try:
            cf = ConfigParser()
            cf.read('config.ini')
            self.shodan_api = cf.get('shodan_api', 'your_api')
            # shodan_api_eval = eval(shodan_api)
            search_host = self.shodan_search1.text()
            page = self.shodan_page.text()
            shodan_api = cf.get('shodan_api', 'your_api')
            self.api = shodan.Shodan(shodan_api)
            self.host = self.num_4.currentText()
            self.shuchu_3.append(f'shodan正在查询 ==> {search_host}，速度稍慢，请耐心等待...' + '\n')
            thread = Thread(target=self.shodan_threadSend,
                            args=(search_host, page)
                            )
            thread.start()
        except:
            QMessageBox.information(
                self,
                '提示',
                '请先配置shodan API  ')

    def shodan_threadSend(self, search_host, page):
        if self.host == 'HOST':
            try:
                results = self.api.search(search_host, page=page)  # 搜索apache，返回 JSON格式的数据
                print("Results found:" + str(results['total']))
                total = str(results['total'])
                self.label_8.setText(total + ' ' + '条')
                self.shuchu_3.append('已找到：' + total + ' 条结果' + '\n')
                self.ip11 = []
                self.port11 = []
                self.domain11 = []
                self.os11 = []
                self.country11 = []
                self.org11 = []
                self.isp11 = []
                self.last_update_111 = []

                self.isp11 = []
                for result in results['matches']:
                    ip_str1 = result['ip_str']
                    port1 = result['port']
                    domains1 = result['domains']
                    os1 = result['os']
                    country_name1 = result['location']['country_name']
                    org1 = result['org']
                    isp1 = result['isp']
                    timestamp1 = result['timestamp']

                    row = self.shodan_tab.rowCount()  # 获取所有列
                    self.shodan_tab.insertRow(row)  # 插入row
                    item = QTableWidgetItem()
                    item.setText(str(ip_str1))
                    item1 = QTableWidgetItem()
                    item1.setText(str(port1))
                    item2 = QTableWidgetItem()
                    item2.setText(','.join(domains1))
                    item3 = QTableWidgetItem()
                    item3.setText(str(os1))
                    item4 = QTableWidgetItem()
                    item4.setText(str(country_name1))
                    item5 = QTableWidgetItem()
                    item5.setText(str(org1))
                    item6 = QTableWidgetItem()
                    item6.setText(str(isp1))
                    item7 = QTableWidgetItem()
                    item7.setText(str(timestamp1))

                    self.shodan_tab.setItem(row, 0, item)
                    self.shodan_tab.setItem(row, 1, item1)
                    self.shodan_tab.setItem(row, 2, item2)
                    self.shodan_tab.setItem(row, 3, item3)
                    self.shodan_tab.setItem(row, 4, item4)
                    self.shodan_tab.setItem(row, 5, item5)
                    self.shodan_tab.setItem(row, 6, item6)
                    self.shodan_tab.setItem(row, 7, item7)

                    self.ip11.append(ip_str1)
                    self.port11.append(port1)
                    self.domain11.append(','.join(domains1))
                    self.os11.append(os1)
                    self.country11.append(country_name1)
                    self.org11.append(org1)
                    self.isp11.append(isp1)
                    self.last_update_111.append(timestamp1)


            except shodan.APIError as e:
                self.shuchu_3.append('shodan提示：' + str(e) + '\n' + '-' * 29)
                print('[-]Error:', e)

            self.shuchu_3.append('查询状态：完成' + '\n' + '-' * 29)


        elif self.host == 'IP':
            try:
                results = self.api.host(search_host)
                ip_str_1 = jsonpath(results, "$..ip_str")
                ports_1 = jsonpath(results, "$..ports")
                domains_1 = jsonpath(results, "$..domains")
                os_1 = jsonpath(results, "$..os")
                country_name_1 = jsonpath(results, "$..country_name")
                org_1 = jsonpath(results, "$..org")
                isp_1 = jsonpath(results, "$..isp")
                last_update_1 = jsonpath(results, "$..last_update")

                for i in range(len(ip_str_1)):
                    ip_str11 = ip_str_1[i]
                    ports_11 = ports_1[i]
                    domains_11 = domains_1[i]
                    os_11 = os_1[i]
                    country_name_11 = country_name_1[i]
                    org_11 = org_1[i]
                    isp_11 = isp_1[i]
                    last_update_11 = last_update_1[i]

                    row = self.shodan_tab.rowCount()  # 获取所有列
                    self.shodan_tab.insertRow(row)  # 插入row
                    item = QTableWidgetItem()
                    item.setText(str(ip_str11))
                    item1 = QTableWidgetItem()
                    item1.setText((',').join(str(x) for x in ports_11))
                    item2 = QTableWidgetItem()
                    item2.setText(str(','.join(domains_11)))
                    item3 = QTableWidgetItem()
                    item3.setText(str(os_11))
                    item4 = QTableWidgetItem()
                    item4.setText(str(country_name_11))
                    item5 = QTableWidgetItem()
                    item5.setText(str(org_11))
                    item6 = QTableWidgetItem()
                    item6.setText(str(isp_11))
                    item7 = QTableWidgetItem()
                    item7.setText(str(last_update_11))

                    self.shodan_tab.setItem(row, 0, item)
                    self.shodan_tab.setItem(row, 1, item1)
                    self.shodan_tab.setItem(row, 2, item2)
                    self.shodan_tab.setItem(row, 3, item3)
                    self.shodan_tab.setItem(row, 4, item4)
                    self.shodan_tab.setItem(row, 5, item5)
                    self.shodan_tab.setItem(row, 6, item6)
                    self.shodan_tab.setItem(row, 7, item7)

                    self.ip11.append(ip_str11)
                    self.port11.append((',').join(str(x) for x in ports_11))
                    self.domain11.append(','.join(domains_11))
                    self.os11.append(os_11)
                    self.country11.append(country_name_11)
                    self.org11.append(org_11)
                    self.isp11.append(isp_11)
                    self.last_update_111.append(last_update_11)

                    self.shuchu_3.append('查询状态：完成' + '\n' + '-' * 29)

            except shodan.APIError as e:
                self.shuchu_3.append('shodan提示：' + str(e) + '\n')
                print('[-]Error:', e)
            self.shuchu_3.append('查询状态：完成' + '\n' + '-' * 29)

    def quake_search1(self):
        try:
            cf = ConfigParser()
            cf.read('config.ini')

            self.quake_your_key = cf.get('quake_api', 'your_api')

            self.quake_tab.setRowCount(0)  # 点击查询后不累加
            search = self.quake_search.text()
            # page1 = self.quake_page.text()
            self.shuchu_7.append(f'quake正在查询 ==> {search}，请稍后...' + '\n')
            thread = Thread(target=self.quake_threadSend,
                            args=(search,)
                            )
            thread.start()
        except:
            QMessageBox.information(
                self,
                '提示',
                '请先配置QUAKE API  ')

    def quake_threadSend(self, search):
        headers = {
            "X-QuakeToken": self.quake_your_key,
            "Content-Type": "application/json"
        }

        page = self.num_10.currentText()
        print(page)
        data = {
            "query": search,
            "start": 0,
            "size": page,
            "ignore_cache": False,
            "start_time": "2000-12-01 00:00:00",
            "end_time": "2090-12-02 00:00:00"
        }
        try:
            response = requests.post(url="https://quake.360.net/api/v3/search/quake_service", headers=headers, json=data)
            resp = response.json()
            print(json.dumps(resp).encode('utf-8'))
            print(search)
        except:
            self.shuchu_7.append('请先配置quake api' + '\n' + '-' * 29)

        user_info = requests.get(url="https://quake.360.net/api/v3/user/info", headers=headers)
        print(user_info.text)
        # print(response.text)
        result1 = json.loads(response.text)
        code = result1['code']
        # print(result1)
        print(code)

        self.quake_ip = []
        self.quake_port = []
        self.quake_hostname = []
        self.quake_org = []
        self.quake_location = []
        self.quake_status_code = []
        self.quake_title = []
        try:
            if code == 'q3007':
                self.shuchu_7.append('积分不足,无法查询' + '\n')

            if code == 'q3005':
                self.shuchu_7.append('调用API过于频繁' + '\n')

            if code == 'u3017':
                self.shuchu_7.append('暂不支持该字段查询' + '\n')

            if response.status_code == 200:
                total = resp['meta']['pagination']['total']
                print(total)
                for item in resp["data"]:
                    ip = item.get("ip", "N/A")
                    port = item.get("port", "N/A")
                    hostname = item.get("hostname", "N/A")
                    org = item.get("org", "N/A")
                    location = item.get("location", {}).get("province_en", "N/A")
                    http_service = item.get("service", {}).get("http", {})
                    status_code = http_service.get("status_code", "N/A")
                    title = http_service.get("title", "N/A")

                    row = self.quake_tab.rowCount()  # 获取所有列
                    self.quake_tab.insertRow(row)  # 插入row
                    item = QTableWidgetItem()
                    item.setText(ip)
                    item1 = QTableWidgetItem()
                    item1.setText(str(port))
                    item2 = QTableWidgetItem()
                    item2.setText(str(title))
                    item3 = QTableWidgetItem()
                    item3.setText(str(status_code))
                    item4 = QTableWidgetItem()
                    item4.setText(str(location))
                    item5 = QTableWidgetItem()
                    item5.setText(str(org))
                    item6 = QTableWidgetItem()
                    item6.setText(str(hostname))

                    self.quake_tab.setItem(row, 0, item)
                    self.quake_tab.setItem(row, 1, item1)
                    self.quake_tab.setItem(row, 2, item2)
                    self.quake_tab.setItem(row, 3, item3)
                    self.quake_tab.setItem(row, 4, item4)
                    self.quake_tab.setItem(row, 5, item5)
                    self.quake_tab.setItem(row, 6, item6)

                    self.quake_ip.append(ip)
                    self.quake_port.append(port)
                    self.quake_hostname.append(hostname)
                    self.quake_org.append(org)
                    self.quake_location.append(location)
                    self.quake_status_code.append(status_code)
                    self.quake_title.append(title)

                self.label_50.setText(str(total) + ' 条')
                self.shuchu_7.append('已找到：' + str(total) + ' ' + '条结果' + '\n' + '-' * 29)


            elif '/quake/login' in response.text:
                self.shuchu_7.append('API有误' + '\n' + '-' * 29)

            else:
                self.shuchu_7.append('未知错误，请排查' + '\n' + '-' * 29)
        except:
            self.shuchu_7.append('查询出错,请重新输入' + '\n' + '-' * 29)

    def zoomeye_search1(self):
        try:
            cf = ConfigParser()
            cf.read('config.ini')

            self.zoomeye_api = cf.get('zoomeye_api', 'your_zoomeye_api')
            self.zoomeye_tab.setRowCount(0)  # 点击查询后不累加
            search = self.zoomeye_search.text()
            self.shuchu_4.append(f'Zoomeye正在查询 ==> {search}，请稍后...' + '\n')
            thread = Thread(target=self.zoomeye_threadSend,
                            args=(search,)
                            )
            thread.start()
        except:
            QMessageBox.information(
                self,
                '提示',
                '请先配置Zoomeye API  ')

    def zoomeye_threadSend(self, search):
        headers = {'API-KEY': self.zoomeye_api}
        page = self.zoomeye_page.text()
        try:
            shengyu = requests.get('https://api.zoomeye.org/resources-info', headers=headers).json()['quota_info']['remain_total_quota']
        except:
            self.shuchu_4.append('请先配置zoomeye api' + '\n' + '-' * 29)
        print(shengyu)
        query_string = f"query={urllib.parse.quote(search)}&page={page}"
        url = f"https://api.zoomeye.org/host/search?{query_string}"

        response = requests.get(url, headers=headers)
        result = json.loads(response.text)
        # print(result)
        try:
            code = result['code']
        except KeyError:
            print("未查询到code")
        self.zoomeye_ip = []
        self.zoomeye_port = []
        self.zoomeye_org = []
        self.zoomeye_server = []
        self.zoomeye_timestamp = []
        self.zoomeye_city = []
        #self.zoomeye_isp = []
        self.zoomeye_app = []
        try:
            if code == 60000:
                total = result['total']
                print("总数：" + str(total))
                for match in result['matches']:
                    ip = match['ip']
                    port = match['portinfo']['port']
                    org = match['geoinfo']['organization']
                    server = match['portinfo']['extrainfo']
                    timestamp = match['timestamp']
                    city = match['geoinfo']['city']['names']['en']
                    #isp = match['geoinfo']['isp']
                    app = match['portinfo']['app']

                    row = self.zoomeye_tab.rowCount()  # 获取所有列
                    self.zoomeye_tab.insertRow(row)  # 插入row
                    item = QTableWidgetItem()
                    item.setText(ip)
                    item1 = QTableWidgetItem()
                    item1.setText(str(port))
                    item2 = QTableWidgetItem()
                    item2.setText(str(server))
                    item3 = QTableWidgetItem()
                    item3.setText(str(city))
                    #item4 = QTableWidgetItem()
                    #item4.setText(str(isp))
                    item5 = QTableWidgetItem()
                    item5.setText(str(app))
                    item6 = QTableWidgetItem()
                    item6.setText(str(org))
                    item8 = QTableWidgetItem()
                    item8.setText(str(timestamp))

                    self.zoomeye_tab.setItem(row, 0, item)
                    self.zoomeye_tab.setItem(row, 1, item1)
                    self.zoomeye_tab.setItem(row, 2, item2)
                    self.zoomeye_tab.setItem(row, 3, item3)
                    #self.zoomeye_tab.setItem(row, 4, item4)
                    self.zoomeye_tab.setItem(row, 5, item5)
                    self.zoomeye_tab.setItem(row, 6, item6)
                    self.zoomeye_tab.setItem(row, 7, item8)

                    self.zoomeye_ip.append(ip)
                    self.zoomeye_port.append(port)
                    self.zoomeye_server.append(server)
                    self.zoomeye_city.append(city)
                    #self.zoomeye_isp.append(isp)
                    self.zoomeye_app.append(app)
                    self.zoomeye_org.append(org)
                    self.zoomeye_timestamp.append(timestamp)

            elif code == 50003:
                self.shuchu_4.append('IP地址查询今天达到最大限制' + '\n' + '-' * 29)

            elif code == 50005:
                self.shuchu_4.append('没有下一页了,请返回上一页' + '\n' + '-' * 29)

            self.label_21.setText(str(total) + ' ' + '条')
            self.shengyu_2.setText("本月剩余积分：" + str(shengyu))
            self.shuchu_4.append('已找到：' + str(total) + ' 条结果' + '\n')
            self.shuchu_4.append('查询状态：完成' + '\n' + '-' * 29)

        except:
            self.shuchu_4.append('请输入Zoomeye语法进行查询' + '\n'+ '-' * 29)

    def Censys(self):
        try:
            cf = ConfigParser()
            cf.read('config.ini')

            self.your_censys_uidccensys = cf.get('censys_uid', 'censys_uid')
            self.your_censys_secretcensys = cf.get('censys_secret', 'censys_secret')

            self.Censys_tab.setRowCount(0)
            is_web = self.Censys_num.currentText()
            self.Censys_searchkey = self.Censys_search.text()

            if is_web == 'Hosts':
                api_url = f"https://search.censys.io/api/v2/hosts/search?q={self.Censys_searchkey}&per_page=100"
            elif is_web == 'IP':
                api_url = f"https://search.censys.io/api/v2/hosts/{self.Censys_searchkey}"

            self.shuchu_5.append(f'Censys正在查询 ==> {self.Censys_searchkey}，请稍后...' + '\n')

            thread = threading.Thread(target=self.Censys_threadSend, args=(api_url,))
            thread.start()

        except:
            QMessageBox.information(
                self,
                '提示',
                '请先配置Censys API  ')

    def Censys_threadSend(self, api_url, cursor=""):
        ip_pattern = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(\/\d{1,2})?$')

        self.ip_address = []
        self.censys_domain = []
        self.censys_port = []
        self.censys_title = []
        self.censys_extended_service_name = []
        self.censys_country = []
        self.censys_request_method = []
        self.censys_status_code = []
        try:
            if ip_pattern.match(self.Censys_searchkey):
                res = requests.get(api_url, auth=(self.your_censys_uidccensys, self.your_censys_secretcensys))
                json_ip = res.text
                print(json_ip)
                if '"code": 200' in json_ip:
                    json_data = json.loads(json_ip)
                    ip_address = json_data['result']['ip']
                    country = json_data['result']['location']['country']
                    for service in json_data['result']['services']:
                        port = service['port']
                        extended_service_name = service['extended_service_name']
                        if 'http' in service:
                            request_method = service['http']['request']['method']
                            status_code = service['http']['response']['status_code']
                            try:
                                html_title = service['http']['response']['html_title']
                            except KeyError:
                                html_title = None
                        else:
                            request_method = None
                            status_code = None
                            html_title = None
                        if 'tls' in service:
                            domain = service['tls']['certificates']['leaf_data']['subject_dn']
                        else:
                            domain = None

                        row = self.Censys_tab.rowCount()  # 获取所有列
                        self.Censys_tab.insertRow(row)  # 插入row
                        item = QTableWidgetItem()
                        item.setText(ip_address)
                        item1 = QTableWidgetItem()
                        item1.setText(str(domain))
                        item2 = QTableWidgetItem()
                        item2.setText(str(port))
                        item3 = QTableWidgetItem()
                        item3.setText(str(html_title))
                        item4 = QTableWidgetItem()
                        item4.setText(str(extended_service_name))
                        item5 = QTableWidgetItem()
                        item5.setText(str(country))
                        item6 = QTableWidgetItem()
                        item6.setText(str(request_method))
                        item7 = QTableWidgetItem()
                        item7.setText(str(status_code))

                        self.Censys_tab.setItem(row, 0, item)
                        self.Censys_tab.setItem(row, 1, item1)
                        self.Censys_tab.setItem(row, 2, item2)
                        self.Censys_tab.setItem(row, 3, item3)
                        self.Censys_tab.setItem(row, 4, item4)
                        self.Censys_tab.setItem(row, 6, item5)
                        self.Censys_tab.setItem(row, 7, item6)
                        self.Censys_tab.setItem(row, 8, item7)

                        self.ip_address.append(ip_address)
                        self.censys_domain.append(domain)
                        self.censys_port.append(port)
                        self.censys_title.append(html_title)
                        self.censys_extended_service_name.append(extended_service_name)
                        self.censys_country.append(country)
                        self.censys_request_method.append(request_method)
                        self.censys_status_code.append(status_code)

                elif 'Too Many Requests' in json_ip:
                    self.shuchu_5.append('请求太多,您已使用了此计费期间的全部配额' + '\n')

                elif 'Access was denied for this resource or feature' in json_ip:
                    self.shuchu_5.append('API 错误' + '\n')
                else:
                    self.shuchu_5.append('未知错误,请排查' + '\n')

                self.shuchu_5.append('查询状态：完成' + '\n' + '-' * 29)


            else:
                self.page_size = 100  # 每页数据大小
                # cursor = self.next_cursor  # 游标初始值为空字符串
                res_url = f"{api_url}/hosts/search?q={self.Censys_searchkey}&per_page={self.page_size}&cursor={cursor}"  # &cursor={cursor}
                res = requests.get(res_url, auth=(self.your_censys_uidccensys, self.your_censys_secretcensys))
                json_obj = res.json()
                json_obj1 = res.text
                # print(json_obj)
                if '"code": 200' in json_obj1:
                    total = json_obj["result"]["total"]
                    hits = json_obj["result"]["hits"]
                    self.next_cursor = json_obj["result"]["links"].get("next", "")  # 如果没有下一页，则默认为空字符串
                    self.prev_cursor = json_obj["result"]["links"].get("prev", "")  #
                    print("点击查询的上一页：" + self.next_cursor)
                    print("点击查询的下一页：" + self.prev_cursor)
                    print("查询结果总数：", total)

                    # self.censys_ip = []
                    # self.censys_port1 = []
                    # self.censys_extended_service_name1 = []
                    # self.censys_network = []
                    # self.censys_country1 = []
                    for hit in hits:
                        country = hit["location"]["country"]
                        # print("国家：" + country)
                        ip = hit["ip"]
                        # print("ip:" + ip)
                        name = hit["autonomous_system"]["name"]
                        # print("网络名称:" + name)
                        services = hit["services"]
                        if services:  # 如果服务列表非空
                            ports = []  # 新增端口列表
                            extended_service_names = []  # 新增扩展服务名称列表
                            for service in services:  # 遍历所有服务
                                port = service.get("port")
                                if port is not None:
                                    extended_service_name = service.get("extended_service_name", "")
                                    ports.append(str(port))  # 将端口加入列表
                                    extended_service_names.append(extended_service_name)  # 将扩展服务名称加入列表
                            if not ports:  # 如果没有找到端口
                                ports.append("-")
                                extended_service_names.append("-")
                            port1 = ",".join(ports)  # 将端口列表拼接成字符串
                            extended_service_name1 = ",".join(extended_service_names)  # 将扩展服务名称列表拼接成字符串

                        else:
                            # print("没有找到服务信息")
                            port1 = "-"
                            extended_service_name1 = "-"

                        # print("-" * 20)
                        row = self.Censys_tab.rowCount()  # 获取所有列
                        self.Censys_tab.insertRow(row)  # 插入row
                        item = QTableWidgetItem()
                        item.setText(ip)
                        item1 = QTableWidgetItem()
                        item1.setText(port1)
                        item2 = QTableWidgetItem()
                        item2.setText(extended_service_name1)
                        item3 = QTableWidgetItem()
                        item3.setText(name)
                        item4 = QTableWidgetItem()
                        item4.setText(country)

                        self.Censys_tab.setItem(row, 0, item)
                        self.Censys_tab.setItem(row, 2, item1)
                        self.Censys_tab.setItem(row, 4, item2)
                        self.Censys_tab.setItem(row, 5, item3)
                        self.Censys_tab.setItem(row, 6, item4)
                        self.ip_address.append(ip)
                        self.censys_port.append(port1)
                        self.censys_extended_service_name.append(extended_service_name1)
                        self.censys_request_method.append(name)
                        self.censys_country.append(country)

                    self.label_12.setText(str(total) + ' ' + '条')
                    self.shuchu_5.append('已找到：' + str(total) + ' 条结果' + '\n')

                elif 'Too Many Requests' in json_obj1:
                    self.shuchu_5.append('请求太多,您已使用了此计费期间的全部配额' + '\n')

                elif 'Access was denied for this resource or feature' in json_obj1:
                    self.shuchu_5.append('API 错误' + '\n')
                else:
                    self.shuchu_5.append('请检查语法是否正确！！！' + '\n')
                self.shuchu_5.append('查询状态：完成' + '\n' + '-' * 29)

        except:
            self.shuchu_5.append('请检查语法是否正确！！！' + '\n' + '-' * 29)

    def Censys_n(self, direction="next"):
        self.Censys_tab.setRowCount(0)
        self.shuchu_5.append(f'Censys正在努力的翻页中，请稍后...' + '\n')
        if direction == "prev":
            cursor = self.prev_cursor
        else:
            cursor = self.next_cursor

        if cursor == "":
            self.shuchu_5.append('已经翻到头了~' + '\n' + '-' * 29)
        else:
            print(("下一页" if direction == "next" else "上一页") + '：' + cursor)
            thread = threading.Thread(target=self.Censys_threadSend, args=("https://search.censys.io/api/v2", cursor))
            thread.start()

    def Censys_p(self):
        self.Censys_n(direction="prev")

    def clear1(self):
        self.fofa.setRowCount(0)
        self.label_2.setText('0 条')
        self.textBrowser.clear()
        # 设置标题栏复原
        self.fofa.setColumnWidth(0, 113)
        self.fofa.setColumnWidth(1, 113)
        self.fofa.setColumnWidth(2, 113)
        self.fofa.setColumnWidth(3, 113)
        self.fofa.setColumnWidth(4, 113)
        self.fofa.setColumnWidth(5, 113)
        self.fofa.setColumnWidth(6, 113)
        self.fofa.setColumnWidth(7, 113)

    def clear_22(self):
        self.hunter_tab.setRowCount(0)
        self.hunter_page.setText(str(1))
        self.label_4.setText('0 条')
        # 设置标题栏复原
        self.hunter_tab.setColumnWidth(0, 84)
        self.hunter_tab.setColumnWidth(1, 84)
        self.hunter_tab.setColumnWidth(2, 84)
        self.hunter_tab.setColumnWidth(3, 84)
        self.hunter_tab.setColumnWidth(4, 84)
        self.hunter_tab.setColumnWidth(5, 84)
        self.hunter_tab.setColumnWidth(6, 84)
        self.hunter_tab.setColumnWidth(7, 84)
        self.hunter_tab.setColumnWidth(8, 84)
        self.hunter_tab.setColumnWidth(9, 84)
        self.hunter_tab.setColumnWidth(10, 84)

    def clear_33(self):
        self.shodan_tab.setRowCount(0)
        self.shodan_page.setText(str(1))
        self.label_8.setText('0 条')
        # 设置标题栏复原
        self.shodan_tab.setColumnWidth(0, 116)
        self.shodan_tab.setColumnWidth(1, 116)
        self.shodan_tab.setColumnWidth(2, 116)
        self.shodan_tab.setColumnWidth(3, 116)
        self.shodan_tab.setColumnWidth(4, 116)
        self.shodan_tab.setColumnWidth(5, 116)
        self.shodan_tab.setColumnWidth(6, 116)
        self.shodan_tab.setColumnWidth(7, 116)
        self.shodan_tab.setColumnWidth(8, 116)

    def clear_77(self):
        self.quake_tab.setRowCount(0)
        self.label_50.setText('0 条')
        # 设置标题栏复原
        self.quake_tab.setColumnWidth(0, 132)
        self.quake_tab.setColumnWidth(1, 132)
        self.quake_tab.setColumnWidth(2, 132)
        self.quake_tab.setColumnWidth(3, 132)
        self.quake_tab.setColumnWidth(4, 132)
        self.quake_tab.setColumnWidth(5, 132)
        self.quake_tab.setColumnWidth(6, 132)

    def clear_44(self):
        self.zoomeye_tab.setRowCount(0)
        self.zoomeye_page.setText(str(1))
        self.label_21.setText('0 条')
        # 设置标题栏复原
        self.zoomeye_tab.setColumnWidth(0, 115)
        self.zoomeye_tab.setColumnWidth(1, 115)
        self.zoomeye_tab.setColumnWidth(2, 115)
        self.zoomeye_tab.setColumnWidth(3, 115)
        self.zoomeye_tab.setColumnWidth(4, 115)
        self.zoomeye_tab.setColumnWidth(5, 115)
        self.zoomeye_tab.setColumnWidth(6, 115)
        self.zoomeye_tab.setColumnWidth(7, 115)

    def Censys_clearjieguo1(self):
        self.Censys_tab.setRowCount(0)
        self.label_12.setText('0 条')
        # 设置标题栏复原
        self.Censys_tab.setColumnWidth(0, 102)
        self.Censys_tab.setColumnWidth(1, 102)
        self.Censys_tab.setColumnWidth(2, 102)
        self.Censys_tab.setColumnWidth(3, 102)
        self.Censys_tab.setColumnWidth(4, 102)
        self.Censys_tab.setColumnWidth(5, 102)
        self.Censys_tab.setColumnWidth(6, 102)
        self.Censys_tab.setColumnWidth(7, 102)
        self.Censys_tab.setColumnWidth(8, 102)

    def clearrizi1(self):
        self.shuchu.clear()

    def hunter_clearrizi(self):
        self.shuchu_2.clear()

    def clearrizi_33(self):
        self.shuchu_3.clear()

    def clearrizi_77(self):
        self.shuchu_7.clear()

    def clearrizi_44(self):
        self.shuchu_4.clear()

    def Censys_clearrizi1(self):
        self.shuchu_5.clear()

    def export_22(self):
        choice = QMessageBox.question(
            self,
            '确认',
            '确定导出吗？')

        try:
            if choice == QMessageBox.Yes:
                t = time.time()
                self.date_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(t))
                header = ['HOST', 'IP', '端口', '域名', '协议', '标题']
                ids = list(set(self.host))
                content_list = []
                for i in range(len(ids)):
                    content = [self.host[i], self.ip[i], self.port[i], self.domain[i], self.protocol[i],
                               self.fofa_title[i]]
                    content_list.append(content)

                if len(content_list) > 0:
                    with open(f"Fofa_{self.date_time}.csv", "w", newline='', encoding='utf-8') as f:
                        writer = csv.writer(f)
                        writer.writerow(header)
                        for row in content_list:
                            try:
                                writer.writerow(row)
                            except UnicodeEncodeError:
                                continue

                    QMessageBox.information(
                        self,
                        '完成',
                        '导出成功，请在软件目录下查看')
                else:
                    QMessageBox.information(
                        self,
                        '提示',
                        '导出失败，没有可导出的数据！')
            elif choice == QMessageBox.No:
                pass
        except Exception as e:
            print(e)
            QMessageBox.information(
                self,
                '提示',
                f'导出失败: {e}，请重试！')

    def export_33(self):
        choice = QMessageBox.question(
            self,
            '确认',
            '确定导出吗？')

        try:
            if choice == QMessageBox.Yes:
                t = time.time()
                self.date_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(t))
                header = ['HOST', 'IP', '端口', '域名', '协议', '国家', '状态码']
                ids = list(set(self.host1))
                content_list = []
                for i in range(len(ids)):
                    content = [self.host1[i], self.ip1[i], self.port1[i], self.domain1[i], self.protocol1[i],
                               self.country1[i], self.status_code1[i]]
                    content_list.append(content)

                if len(content_list) > 0:
                    with open(f"Hunter_{self.date_time}.csv", "w", newline='') as f:
                        writer = csv.writer(f)
                        writer.writerow(header)
                        writer.writerows(content_list)

                        for row in content_list:
                            try:
                                writer.writerow(row)
                            except UnicodeEncodeError:
                                continue

                    QMessageBox.information(
                        self,
                        '完成',
                        '导出成功，请在软件目录下查看  ')
                else:
                    QMessageBox.information(
                        self,
                        '提示',
                        '导出失败，没有可导出的数据！')

            elif choice == QMessageBox.No:
                pass


        except Exception as e:
            QMessageBox.information(
                self,
                '提示',
                f'导出失败: {e}，请重试！')

    def export_44(self):
        choice = QMessageBox.question(
            self,
            '确认',
            '确定导出吗？')

        try:
            if choice == QMessageBox.Yes:
                t = time.time()
                self.date_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(t))
                header = ['IP', '端口', '域名', '国家', '更新时间']
                ids = list(set(self.ip11))
                content_list = []
                for i in range(len(ids)):
                    content = [self.ip11[i], self.port11[i], self.domain11[i], self.country11[i],
                               self.last_update_111[i]]
                    content_list.append(content)

                if len(content_list) > 0:
                    with open(f"Shodan_{self.date_time}.csv", "w", newline='') as f:
                        writer = csv.writer(f)
                        writer.writerow(header)
                        writer.writerows(content_list)

                        for row in content_list:
                            try:
                                writer.writerow(row)
                            except UnicodeEncodeError:
                                continue

                    QMessageBox.information(
                        self,
                        '完成',
                        '导出成功，请在软件目录下查看')
                else:
                    QMessageBox.information(
                        self,
                        '提示',
                        '导出失败，没有可导出的数据！')

            elif choice == QMessageBox.No:
                pass

        except Exception as e:
            QMessageBox.information(
                self,
                '提示',
                f'导出失败: {e}，请重试！')

    def export_quake(self):
        choice = QMessageBox.question(
            self,
            '确认',
            '确定导出吗？'
        )
        try:
            if choice == QMessageBox.Yes:
                t = time.time()
                self.date_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(t))
                header = ['IP', '端口', '标题', '状态', '地址', 'org', 'hostname']
                ids = list(set(self.quake_ip))
                content_list = []
                for i in range(len(ids)):
                    content = [self.quake_ip[i], self.quake_port[i], self.quake_title[i], self.quake_status_code[i],
                               self.quake_location[i], self.quake_org[i], self.quake_hostname[i]]
                    content_list.append(content)

                if len(content_list) > 0:
                    with open(f"Quake_{self.date_time}.csv", "w", newline='') as f:
                        writer = csv.writer(f)
                        writer.writerow(header)
                        writer.writerows(content_list)

                        for row in content_list:
                            try:
                                writer.writerow(row)
                            except UnicodeEncodeError:
                                continue

                    QMessageBox.information(
                        self,
                        '完成',
                        '导出成功，请在软件目录下查看')
                else:
                    QMessageBox.information(
                        self,
                        '提示',
                        '导出失败：没有数据可供导出！')
            elif choice == QMessageBox.No:
                pass
        except Exception as e:
            QMessageBox.information(
                self,
                '提示',
                f'导出失败: {e}，请重试！')

    def export_zoomeye(self):
        choice = QMessageBox.question(
            self,
            '确认',
            '确定导出吗？')

        try:
            if choice == QMessageBox.Yes:
                t = time.time()
                self.date_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(t))
                header = ['IP', '端口', 'Server', '城市', 'ISP', 'App', '组织', '时间']
                ids = list(self.zoomeye_ip)
                content_list = []
                for i in range(len(ids)):
                    content = [self.zoomeye_ip[i], self.zoomeye_port[i], self.zoomeye_server[i],
                               self.zoomeye_city[i], self.zoomeye_isp[i], self.zoomeye_app[i], self.zoomeye_org[i],
                               self.zoomeye_timestamp[i]]
                    content_list.append(content)

                with open(f"Zoomeye_{self.date_time}.csv", "w", newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(header)
                    writer.writerows(content_list)

                    for row in content_list:
                        try:
                            writer.writerow(row)
                        except UnicodeEncodeError:
                            continue

                QMessageBox.information(
                    self,
                    '完成',
                    '导出成功，请在软件目录下查看')
            elif choice == QMessageBox.No:
                pass
        except Exception as e:
            QMessageBox.information(
                self,
                '提示',
                f'导出失败: {e}，请重试！')

    def Censys_export_1(self):
        choice = QMessageBox.question(
            self,
            '确认',
            '确定导出吗？')

        try:
            if choice == QMessageBox.Yes:
                t = time.time()
                self.date_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(t))
                header = ['IP', '域名', '标题', 'Protocol', '国家']
                content_list = []

                for i in range(len(self.ip_address)):
                    ip = self.ip_address[i] if i < len(self.ip_address) else ''
                    domain = self.censys_domain[i] if i < len(self.censys_domain) else ''
                    title = self.censys_title[i] if i < len(self.censys_title) else ''
                    extended_service_name = self.censys_extended_service_name[i] if i < len(
                        self.censys_extended_service_name) else ''
                    country = self.censys_country[i] if i < len(self.censys_country) else ''
                    # request_method = self.censys_request_method[i] if i < len(self.censys_request_method) else ''
                    # status_code = self.censys_status_code[i] if i < len(self.censys_status_code) else ''

                    # 将端口列表和协议列表转换为字符串，多个元素用逗号分隔
                    # port_str = ",".join([str(port) for port in self.censys_port[i] if port]) if isinstance(
                    #     self.censys_port[i], list) and i < len(
                    #     self.censys_port) else ''

                    content = [ip, domain, title, extended_service_name, country]
                    content_list.append(content)

                with open(f"Censys_{self.date_time}.csv", "w", newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(header)
                    writer.writerows(content_list)

                    for row in content_list:
                        try:
                            writer.writerow(row)
                        except UnicodeEncodeError:
                            continue

                QMessageBox.information(
                    self,
                    '完成',
                    '导出成功，请在软件目录下查看')
            elif choice == QMessageBox.No:
                pass
        except Exception as e:
            QMessageBox.information(
                self,
                '提示',
                f'导出失败: {e}，请重试！')

if __name__ == '__main__':
    app = QApplication([])
    app.setWindowIcon(QIcon(':/E:/favicon.ico'))
    gui = LoginGui()
    gui.show()
    app.exec_()
