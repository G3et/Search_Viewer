# -*- coding: utf-8 -*-
import base64
import csv
import json
from configparser import ConfigParser
from jsonpath import jsonpath
import jsonpath
import requests
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QMessageBox, QTableWidgetItem
from configobj import ConfigObj
import mmh3
import shodan
import time
from threading import Thread
from PySide2.QtGui import QIcon
from search_viewer_ui import Ui_MainWindow
from PySide2.QtWidgets import QApplication, QMainWindow


class LoginGui(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(LoginGui, self).__init__()   # 调用父类的初始化方法
        self.setupUi(self)
        self.button.clicked.connect(self.handleCalc)
        self.clear.clicked.connect(self.clear1)
        self.clear_2.clicked.connect(self.clear_22)
        self.clear_3.clicked.connect(self.clear_33)
        self.clear_7.clicked.connect(self.clear_77)
        self.clear_4.clicked.connect(self.clear_44)
        self.clearrizi.clicked.connect(self.clearrizi1)
        self.clearrizi_2.clicked.connect(self.hunter_clearrizi)
        self.clearrizi_3.clicked.connect(self.clearrizi_33)
        self.clearrizi_7.clicked.connect(self.clearrizi_77)
        self.clearrizi_4.clicked.connect(self.clearrizi_44)
        self.export_2.clicked.connect(self.export_22)
        self.export_3.clicked.connect(self.export_33)
        self.export_4.clicked.connect(self.export_44)
        self.export_8.clicked.connect(self.export_88)
        self.export_5.clicked.connect(self.export_55)
        self.export_6.clicked.connect(self.export_66)
        self.button_2.clicked.connect(self.hunter)
        self.button_3.clicked.connect(self.shodan_search)
        self.button_4.clicked.connect(self.icohash)
        self.button_9.clicked.connect(self.quake_search1)
        self.button_5.clicked.connect(self.zoomeye_search1)
        self.save_config.clicked.connect(self.save_config_all)
        self.fofa_xiugai.clicked.connect(self.fofa_xiugai_all)
        self.hunter_xiugai.clicked.connect(self.hunter_xiugai_all)
        self.shodan_xiugai.clicked.connect(self.shodan_xiugai_all)
        self.quake_xiugai.clicked.connect(self.quake_xiugai_all)
        self.zoomeye_xiugai.clicked.connect(self.zoomeye_xiugai_all)

        # self.fofa.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 表格铺满
        # self.fofa.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 表格禁止输入
        font = self.fofa.horizontalHeader().font()  # 标题加粗
        font.setBold(True)
        self.fofa.horizontalHeader().setFont(font)

        font = self.hunter_tab.horizontalHeader().font()  # 标题加粗
        font.setBold(True)
        self.hunter_tab.horizontalHeader().setFont(font)

        font = self.shodan_tab.horizontalHeader().font()  # 标题加粗
        font.setBold(True)
        self.shodan_tab.horizontalHeader().setFont(font)

        font = self.quake_tab.horizontalHeader().font()  # 标题加粗
        font.setBold(True)
        self.quake_tab.horizontalHeader().setFont(font)

        font = self.zoomeye_tab.horizontalHeader().font()  # 标题加粗
        font.setBold(True)
        self.zoomeye_tab.horizontalHeader().setFont(font)

        t = time.time()
        self.t1 = int(t)

    def save_config_all(self):
        choice = QMessageBox.question(
            self,
            '确认',
            '是否保存？')

        if choice == QMessageBox.Yes:
            config = ConfigObj()
            config.filename = 'config.ini'

            # fofa
            self.your_fofa_email = self.your_fofa_email.text()
            self.your_fofa_api = self.your_fofa_api.text()

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
            self.your_zoomeye_api = self.your_zoomeye_api.text()

            config['zoomeye_api'] = {}
            config['zoomeye_api']['your_zoomeye_api'] = self.your_zoomeye_api

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

    def icohash(self):
        self.textBrowser.clear()
        your_search = self.ico_hash.text()

        self.shuchu.append(f'iconhash正在查询 ==> {your_search}，请稍后...' + '\n')

        thread = Thread(target=self.icohash_threadSend,
                        args=(your_search,)
                        )
        thread.start()

    def icohash_threadSend(self, your_search):
        try:
            r = requests.get(your_search)  # https://www.baidu.com/favicon.ico
            favicon = base64.encodebytes(r.content)
            hash = mmh3.hash(favicon)
            result = 'icon_hash="{}"'.format(hash)
            self.textBrowser.append(result)
            self.shuchu.append(result + '\n')
            self.shuchu.append('icon_hash 已查询完成' + '\n' + '-' * 29)
            print(result)
        except requests.exceptions.MissingSchema as e:
            self.shuchu.append(str(e) + '\n' + '-' * 29)
        except requests.exceptions.ConnectionError as e:
            self.shuchu.append(str(e) + '\n' + '-' * 29)

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
        self.fofa.setRowCount(0)  # 点击查询后不累加
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0"}
        # your_search = self.fofa_search.text()
        qbase64 = base64.b64encode(your_search.encode('utf-8')).decode('ascii')
        num = self.num.currentText()  # 下拉框
        api = 'https://fofa.info/api/v1/search/all?email={}&key={}&qbase64={}&size={}&fields=host,ip,port,title,domain,country,protocol,server'.format(
            self.your_email, self.your_key,
            qbase64, num)
        html = requests.get(url=api, headers=headers)
        print(api)

        if 'errmsg' not in html.text:
            results = html.json()["results"]
            print("共搜索到{}条记录！".format(len(results)))
            result = json.loads(html.text)  # 将str类型的数据转换为dict类型
            size = result['size']  # 转为dict然后查询
            self.label_2.setText(str(size) + ' ' + '条')
            self.shuchu.append('已找到：' + str(size) + ' ' + '条结果' + '\n')
            self.shuchu.append('查询状态：完成' + '\n' + '-' * 29)
            self.host = []
            self.ip = []
            self.port = []
            self.domain = []
            self.protocol = []
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

        else:
            self.shuchu.append('未知错误，请排查' + '\n' + '-' * 29)

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
        print(api)
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
                # print(results)
                ip_str_1 = jsonpath(results, "$..ip_str")
                ports_1 = jsonpath(results, "$..ports")
                domains_1 = jsonpath(results, "$..domains")
                os_1 = jsonpath(results, "$..os")
                country_name_1 = jsonpath(results, "$..country_name")
                org_1 = jsonpath(results, "$..org")
                isp_1 = jsonpath(results, "$..isp")
                last_update_1 = jsonpath(results, "$..last_update")

                # self.ip11 = []
                # self.port11 = []
                # self.domain11 = []
                # self.os_111 = []
                # self.country11 = []
                # self.org_111 = []
                # self.isp111 = []
                # self.last_update_111 = []

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

            self.hunter_your_key = cf.get('quake_api', 'your_api')

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
            "X-QuakeToken": self.hunter_your_key,
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
        response = requests.post(url="https://quake.360.net/api/v3/search/quake_service", headers=headers, json=data)
        user_info = requests.get(url="https://quake.360.net/api/v3/user/info", headers=headers)
        print(response.text)
        result1 = json.loads(response.text)
        code = result1['code']
        print(result1)
        print(code)

        try:
            if code == 'q3007':
                self.shuchu_7.append('积分不足,无法查询' + '\n')

            if code == 'q3005':
                self.shuchu_7.append('调用API过于频繁' + '\n')

            if response.status_code == 200:
                response_dict = user_info.json()
                result = json.loads(response.text)
                host = jsonpath.jsonpath(result, "$.data[*].service.http.host")
                ports = jsonpath.jsonpath(result, "$.data[*].port")
                services = jsonpath.jsonpath(result, "$.data[*].service.http.title")
                locations = jsonpath.jsonpath(result, "$.data[*].location.city_cn")
                isp = jsonpath.jsonpath(result, "$.data[*].location.isp")
                times = jsonpath.jsonpath(result, "$.data[*].time")
                total = jsonpath.jsonpath(result, "$..total")
                month_remaining_credit = response_dict['data']['month_remaining_credit']
                self.xiaohao_4.setText('本月剩余积分：' + str(month_remaining_credit))
                for i in total:
                    a = int(i)
                    self.label_50.setText(str(a) + ' 条')
                    self.shuchu_7.append('已找到：' + str(a) + ' 条结果' + '\n')

                self.ip_quake = []
                self.port_quake = []
                self.title_quake = []
                self.location_quake = []
                self.isp_quake = []
                self.time_quake = []

                host_port_services = {}
                unique_host_port = set()
                for index in range(len(ports)):
                    host_port = f"{host[index]}:{ports[index]}"
                    unique_host_port.add(host_port)
                    if host_port in host_port_services:
                        if times[index] > host_port_services[host_port]["time"]:
                            host_port_services[host_port] = {
                                "host": host[index],
                                "port": ports[index],
                                "service": services[index],
                                "location": locations[index],
                                "isp": isp[index],
                                "time": times[index]
                            }
                    else:
                        host_port_services[host_port] = {
                            "host": host[index],
                            "port": ports[index],
                            "service": services[index],
                            "location": locations[index],
                            "isp": isp[index],
                            "time": times[index]
                        }

                for host_port, data in host_port_services.items():
                    print(f"host: {data['host']}")
                    print(f"port: {data['port']}")
                    print(f"service: {data['service']}")
                    print(f"location: {data['location']}")
                    print(f"isp: {data['isp']}")
                    print(f"time: {data['time']}")
                    print('-' * 20)
                    row = self.quake_tab.rowCount()  # 获取所有列
                    self.quake_tab.insertRow(row)  # 插入row
                    item = QTableWidgetItem()
                    item.setText(str(data['host']))
                    item1 = QTableWidgetItem()
                    item1.setText(str(data['port']))
                    item2 = QTableWidgetItem()
                    item2.setText(str(data['service']))
                    item3 = QTableWidgetItem()
                    item3.setText(str(data['location']))
                    item4 = QTableWidgetItem()
                    item4.setText(str(data['isp']))
                    item5 = QTableWidgetItem()
                    item5.setText(str(data['time']))

                    self.quake_tab.setItem(row, 0, item)
                    self.quake_tab.setItem(row, 1, item1)
                    self.quake_tab.setItem(row, 2, item2)
                    self.quake_tab.setItem(row, 3, item3)
                    self.quake_tab.setItem(row, 4, item4)
                    self.quake_tab.setItem(row, 5, item5)

                    self.ip_quake.append(data['host'])
                    self.port_quake.append(data['port'])
                    self.title_quake.append(data['service'])
                    self.location_quake.append(data['location'])
                    self.isp_quake.append(data['isp'])
                    self.time_quake.append(data['time'])

                print(f"总数：{total.pop(0)}")
                print(f"去重总数: {len(unique_host_port)}")
                quchong = len(unique_host_port)
                self.xiaohao_3.setText('去重后：' + str(quchong) + ' 条')
                self.shuchu_7.append('去重后：' + str(quchong) + ' 条结果' + '\n' + '-' * 29)


            elif '/quake/login' in response.text:
                self.shuchu_7.append('API有误' + '\n' + '-' * 29)

            else:
                print('请求失败')
        except:
            self.shuchu_7.append('查询出错,请重新输入' + '\n' + '-' * 29)

    def zoomeye_search1(self):
        try:
            cf = ConfigParser()
            cf.read('config.ini')

            self.zoomeye_api = cf.get('zoomeye_api', 'your_zoomeye_api')
            is_web = self.num_6.currentText()
            if is_web == '关联域名':
                a = '0'
                print(a)
            elif is_web == '子域名':
                a = '1'
            elif is_web == '主机设备':
                a = '2'
            elif is_web == 'web应用':
                a = '3'
                print(a)

            self.zoomeye_tab.setRowCount(0)  # 点击查询后不累加
            search = self.zoomeye_search.text()
            self.shuchu_4.append(f'Zoomeye正在查询 ==> {search}，请稍后...' + '\n')
            thread = Thread(target=self.zoomeye_threadSend,
                            args=(search, a)
                            )
            thread.start()
        except:
            QMessageBox.information(
                self,
                '提示',
                '请先配置Zoomeye API  ')

    def zoomeye_threadSend(self, search, a):
        headers = {'API-KEY': self.zoomeye_api}
        page = self.zoomeye_page.text()
        self.shengyu = requests.get('https://api.zoomeye.org/resources-info', headers=headers).json()['resources']['search']
        print(
            f"剩余搜索次数: {requests.get('https://api.zoomeye.org/resources-info', headers=headers).json()['resources']['search']}")

        if a in ('0', '1'):
            try:
                result = requests.get(f"https://api.zoomeye.org/domain/search?q={search}&type={a}&page={page}",headers=headers).json()
                print(result)
                name = jsonpath.jsonpath(result, "$.list[*].name")
                timestamp = jsonpath.jsonpath(result, "$.list[*].timestamp")
                ip_list = jsonpath.jsonpath(result, "$.list[*].ip")
                total = result['total']
                print(f"总数: {result['total']}")
                print(f"name: {name}")
                print(f"timestamp: {timestamp}")
                ip_list = [item for sublist in ip_list for item in sublist]
                print(f"ip_list: {ip_list}")

                self.shuchu_4.append('已找到：' + str(total) + ' ' + '条结果' + '\n')
                self.shuchu_4.append('查询状态：完成' + '\n' + '-' * 29)
                self.shengyu_2.setText('本月剩余积分：' + str(self.shengyu))
                self.label_21.setText(str(total) + ' 条')

                self.host1 = []
                self.timestamp1 = []
                self.ip_list1 = []
                for i in range(len(name)):
                    try:
                        host1 = name[i]
                        timestamp1 = timestamp[i]
                        if i < len(ip_list):
                            ip_list1 = ip_list[i]
                        else:
                            ip_list1 = '无IP'

                        row = self.zoomeye_tab.rowCount()  # 获取所有列
                        self.zoomeye_tab.insertRow(row)  # 插入row
                        item = QTableWidgetItem()
                        item.setText(host1)
                        item1 = QTableWidgetItem()
                        item1.setText(str(ip_list1))
                        item2 = QTableWidgetItem()
                        item2.setText(timestamp1)

                        self.zoomeye_tab.setItem(row, 8, item)
                        self.zoomeye_tab.setItem(row, 0, item1)
                        self.zoomeye_tab.setItem(row, 7, item2)

                        self.host1.append(host1)
                        self.ip_list1.append(ip_list1)
                        self.timestamp1.append(timestamp1)
                    except:
                        self.shuchu_4.append('查询出错了' + '\n' + '-' * 29)
            except:
                self.shuchu_4.append('请输入Zoomeye语法进行查询' + '\n' + '-' * 29)

        elif a == '2':
            try:
                result = requests.get(f"https://api.zoomeye.org/host/search?query={search}&page={page}&facets=app,os",
                                      headers=headers).json()  # 主机设备搜索
                # print(result)
                total = result['total']
                self.zoomeye_ip = jsonpath.jsonpath(result, "$.matches[*].ip")
                print(self.zoomeye_ip)
                self.zoomeye_port = jsonpath.jsonpath(result, "$.matches[*].portinfo.port")
                self.zoomeye_service = jsonpath.jsonpath(result, "$.matches[*].portinfo.service")
                self.zoomeye_title = jsonpath.jsonpath(result, "$.matches[*].portinfo.title")
                # print(zoomeye_title)
                self.zoomeye_timestamp = jsonpath.jsonpath(result, "$.matches[*].timestamp")
                self.zoomeye_geoinfo = jsonpath.jsonpath(result, "$.matches[*].geoinfo.city.names.zh-CN")
                self.zoomeye_isp = jsonpath.jsonpath(result, "$.matches[*].geoinfo.isp")
                self.zoomeye_app = jsonpath.jsonpath(result, "$.matches[*].portinfo.app")

                self.shuchu_4.append('已找到：' + str(total) + ' ' + '条结果' + '\n')
                self.shuchu_4.append('查询状态：完成' + '\n' + '-' * 29)
                self.shengyu_2.setText('本月剩余积分：' + str(self.shengyu))
                self.label_21.setText(str(total) + ' 条')

                self.zoomeye_tab.setRowCount(len(self.zoomeye_ip))  # 设置表格行数为结果数量

                for i in range(len(self.zoomeye_ip)):
                    print(str(self.zoomeye_ip[i]))
                    item = QTableWidgetItem(str(self.zoomeye_ip[i]))
                    self.zoomeye_tab.setItem(i, 0, item)
                    item1 = QTableWidgetItem(str(self.zoomeye_port[i]))
                    self.zoomeye_tab.setItem(i, 1, item1)
                    item3 = QTableWidgetItem(str(self.zoomeye_service[i]))
                    self.zoomeye_tab.setItem(i, 3, item3)
                    item2 = QTableWidgetItem(str(self.zoomeye_title[i]))
                    self.zoomeye_tab.setItem(i, 2, item2)
                    item4 = QTableWidgetItem(str(self.zoomeye_geoinfo[i]))
                    self.zoomeye_tab.setItem(i, 4, item4)
                    item5 = QTableWidgetItem(str(self.zoomeye_isp[i]))
                    self.zoomeye_tab.setItem(i, 5, item5)
                    item6 = QTableWidgetItem(str(self.zoomeye_app[i]))
                    self.zoomeye_tab.setItem(i, 6, item6)
                    item7 = QTableWidgetItem(str(self.zoomeye_timestamp[i]))
                    self.zoomeye_tab.setItem(i, 7, item7)

            except:
                self.shuchu_4.append('请输入Zoomeye语法进行查询' + '\n' + '-' * 29)

        # elif a == '3': # web应用
        #     try:
        #         result = requests.get(f"https://api.zoomeye.org/web/search?query={search}&page={page}&facets=app,os",
        #                               headers=headers).json()
        #         total = result['total']
        #         zoomeye_ip = jsonpath.jsonpath(result, "$.matches[*].ip")
        #         flat_list = [item for sublist in zoomeye_ip for item in sublist]
        #         zoomeye_title = jsonpath.jsonpath(result, "$.matches[*].title")
        #         zoomeye_timestamp = jsonpath.jsonpath(result, "$.matches[*].timestamp")
        #         zoomeye_geoinfo = jsonpath.jsonpath(result, "$.matches[*].geoinfo.city.names.zh-CN")
        #         zoomeye_isp = jsonpath.jsonpath(result, "$.matches[*].geoinfo.isp")
        #         zoomeye_domain = jsonpath.jsonpath(result, "$.matches[*].site")
        #         print(total)
        #         print(flat_list)
        #         print(zoomeye_title)
        #         print(zoomeye_timestamp)
        #         print(zoomeye_geoinfo)
        #         print(zoomeye_isp)
        #         print(zoomeye_domain)
        #
        #         self.shuchu_4.append('已找到：' + str(total) + ' ' + '条结果' + '\n')
        #         self.shuchu_4.append('查询状态：完成' + '\n' + '-' * 29)
        #         self.shengyu_2.setText('本月剩余积分：' + str(self.shengyu))
        #         self.label_21.setText(str(total) + ' 条')
        #
        #         self.zoomeye_tab.setRowCount(len(flat_list))  # 设置表格行数为结果数量
        #
        #         for i in range(len(flat_list)):
        #             item = QTableWidgetItem(str(flat_list[i]))
        #             self.zoomeye_tab.setItem(i, 0, item)
        #             item2 = QTableWidgetItem(str(zoomeye_title[i]))
        #             self.zoomeye_tab.setItem(i, 2, item2)
        #             item4 = QTableWidgetItem(str(zoomeye_geoinfo[i]))
        #             self.zoomeye_tab.setItem(i, 4, item4)
        #             item5 = QTableWidgetItem(str(zoomeye_isp[i]))
        #             self.zoomeye_tab.setItem(i, 5, item5)
        #             item6 = QTableWidgetItem(str(zoomeye_domain[i]))
        #             self.zoomeye_tab.setItem(i, 8, item6)
        #             item7 = QTableWidgetItem(str(zoomeye_timestamp[i]))
        #             self.zoomeye_tab.setItem(i, 7, item7)
        #     except:
        #         self.shuchu_4.append('请输入Zoomeye语法进行查询' + '\n' + '-' * 29)

    def clear1(self):
        self.fofa.setRowCount(0)
        self.label_2.setText('0 条')
        self.textBrowser.clear()
        # 设置标题栏复原
        self.fofa.setColumnWidth(0, 137)
        self.fofa.setColumnWidth(1, 137)
        self.fofa.setColumnWidth(2, 137)
        self.fofa.setColumnWidth(3, 137)
        self.fofa.setColumnWidth(4, 137)
        self.fofa.setColumnWidth(5, 137)
        self.fofa.setColumnWidth(6, 137)
        self.fofa.setColumnWidth(7, 137)

    def clear_22(self):
        self.hunter_tab.setRowCount(0)
        self.hunter_page.setText(str(1))
        self.label_4.setText('0 条')
        # 设置标题栏复原
        self.hunter_tab.setColumnWidth(0, 101)
        self.hunter_tab.setColumnWidth(1, 101)
        self.hunter_tab.setColumnWidth(2, 101)
        self.hunter_tab.setColumnWidth(3, 101)
        self.hunter_tab.setColumnWidth(4, 101)
        self.hunter_tab.setColumnWidth(5, 101)
        self.hunter_tab.setColumnWidth(6, 101)
        self.hunter_tab.setColumnWidth(7, 101)
        self.hunter_tab.setColumnWidth(8, 101)
        self.hunter_tab.setColumnWidth(9, 101)
        self.hunter_tab.setColumnWidth(10, 101)

    def clear_33(self):
        self.shodan_tab.setRowCount(0)
        self.shodan_page.setText(str(1))
        self.label_8.setText('0 条')
        # 设置标题栏复原
        self.shodan_tab.setColumnWidth(0, 139)
        self.shodan_tab.setColumnWidth(1, 139)
        self.shodan_tab.setColumnWidth(2, 139)
        self.shodan_tab.setColumnWidth(3, 139)
        self.shodan_tab.setColumnWidth(4, 139)
        self.shodan_tab.setColumnWidth(5, 139)
        self.shodan_tab.setColumnWidth(6, 139)
        self.shodan_tab.setColumnWidth(7, 139)
        self.shodan_tab.setColumnWidth(8, 139)

    def clear_77(self):
        self.quake_tab.setRowCount(0)
        self.label_50.setText('0 条')
        self.xiaohao_3.setText('去重后：')
        # 设置标题栏复原
        self.quake_tab.setColumnWidth(0, 187)
        self.quake_tab.setColumnWidth(1, 187)
        self.quake_tab.setColumnWidth(2, 187)
        self.quake_tab.setColumnWidth(3, 187)
        self.quake_tab.setColumnWidth(4, 187)
        self.quake_tab.setColumnWidth(5, 187)

    def clear_44(self):
        self.zoomeye_tab.setRowCount(0)
        self.zoomeye_page.setText(str(1))
        self.label_21.setText('0 条')
        # 设置标题栏复原
        self.zoomeye_tab.setColumnWidth(0, 125)
        self.zoomeye_tab.setColumnWidth(1, 125)
        self.zoomeye_tab.setColumnWidth(2, 125)
        self.zoomeye_tab.setColumnWidth(3, 125)
        self.zoomeye_tab.setColumnWidth(4, 125)
        self.zoomeye_tab.setColumnWidth(5, 125)
        self.zoomeye_tab.setColumnWidth(6, 125)
        self.zoomeye_tab.setColumnWidth(7, 125)
        self.zoomeye_tab.setColumnWidth(8, 125)

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

    def export_22(self):
        choice = QMessageBox.question(
            self,
            '确认',
            '确定导出吗？')

        if choice == QMessageBox.Yes:
            header = ['HOST', 'IP', '端口', '域名', '协议']
            with open(f"Fofa_{self.t1}.csv", "w", newline='') as f:
                writer = csv.writer(f)
                writer.writerow(header)
                ids = list(set(self.host))
                for i in range(len(ids)):
                    content = [self.host[i], self.ip[i], self.port[i], self.domain[i], self.protocol[i]]
                    writer.writerow(content)
            QMessageBox.information(
                self,
                '完成',
                '导出成功，请在软件目录下查看')
        if choice == QMessageBox.No:
            pass

    def export_33(self):
        choice = QMessageBox.question(
            self,
            '确认',
            '确定导出吗？')

        if choice == QMessageBox.Yes:
            header = ['HOST', 'IP', '端口', '域名', '协议', '国家', '状态码']
            with open(f"Hunter_{self.t1}.csv", "w", newline='') as f:
                writer = csv.writer(f)
                writer.writerow(header)
                ids = list(set(self.host1))
                for i in range(len(ids)):
                    content = [self.host1[i], self.ip1[i], self.port1[i], self.domain1[i], self.protocol1[i],
                               self.country1[i], self.status_code1[i]]
                    writer.writerow(content)
            QMessageBox.information(
                self,
                '完成',
                '导出成功，请在软件目录下查看  ')
        if choice == QMessageBox.No:
            pass

    def export_44(self):
        choice = QMessageBox.question(
            self,
            '确认',
            '确定导出吗？')

        if choice == QMessageBox.Yes:
            header = ['IP', '端口', '域名', '国家', '更新时间']
            with open(f"Shodan_{self.t1}.csv", "w", newline='') as f:
                writer = csv.writer(f)
                writer.writerow(header)
                ids = list(set(self.ip11))
                for i in range(len(ids)):
                    content = [self.ip11[i], self.port11[i], self.domain11[i], self.country11[i],
                               self.last_update_111[i]]
                    writer.writerow(content)
            QMessageBox.information(
                self,
                '完成',
                '导出成功，请在软件目录下查看')
        if choice == QMessageBox.No:
            pass

    def export_88(self):
        choice = QMessageBox.question(
            self,
            '确认',
            '确定导出吗？')

        if choice == QMessageBox.Yes:
            header = ['IP', '端口', '标题', '地址', '提供商', '时间']
            with open(f"Quake_{self.t1}.csv", "w", newline='') as f:
                writer = csv.writer(f)
                writer.writerow(header)
                ids = list(set(self.ip_quake))
                for i in range(len(ids)):
                    content = [self.ip_quake[i], self.port_quake[i], self.title_quake[i], self.location_quake[i],
                               self.isp_quake[i], self.time_quake[i]]
                    writer.writerow(content)
            QMessageBox.information(
                self,
                '完成',
                '导出成功，请在软件目录下查看')
        if choice == QMessageBox.No:
            pass

    def export_55(self):
        choice = QMessageBox.question(
            self,
            '确认',
            '确定导出吗？')
        try:
            if choice == QMessageBox.Yes:
                header = ['IP', '域名', '时间']
                with open(f"Zoomeye_{self.t1}.csv", "w", newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(header)
                    ids = list(set(self.host1))
                    for i in range(len(ids)):
                        content = [self.ip_list1[i], self.host1[i], self.timestamp1[i]]
                        writer.writerow(content)
                QMessageBox.information(
                    self,
                    '完成',
                    '导出成功，请在软件目录下查看')
            if choice == QMessageBox.No:
                pass
        except:
            QMessageBox.information(
                self,
                '提示',
                '请点击导出主机设备')

    def export_66(self):
        choice = QMessageBox.question(
            self,
            '确认',
            '确定导出吗？')

        try:
            if choice == QMessageBox.Yes:
                header = ['IP', '端口', '标题', '城市', 'ISP', '时间']
                with open(f"Zoomeye_{self.t1}.csv", "w", newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(header)
                    ids = list(self.zoomeye_ip)
                    for i in range(len(ids)):
                        content = [self.zoomeye_ip[i], self.zoomeye_port[i],self.zoomeye_title[i], self.zoomeye_geoinfo[i], self.zoomeye_isp[i], self.zoomeye_timestamp[i]]
                        writer.writerow(content)
                QMessageBox.information(
                    self,
                    '完成',
                    '导出成功，请在软件目录下查看')
            if choice == QMessageBox.No:
                pass
        except:
            QMessageBox.information(
                self,
                '提示',
                '请点击导出关联域名/子域名')

    def resizeEvent(self, event):
        print("Window resized:", event.size().width(), event.size().height())
        self.width = event.size().width()
        self.height = event.size().height()


if __name__ == '__main__':
    app = QApplication([])
    gui = LoginGui()
    gui.show()
    app.exec_()
