# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'search_viewer_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1240, 700)
        MainWindow.setMaximumSize(QSize(1240, 700))
        icon = QIcon()
        icon.addFile(u":/E:/favicon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actionfofa = QAction(MainWindow)
        self.actionfofa.setObjectName(u"actionfofa")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QRect(0, 0, 1531, 891))
        self.tabWidget.setMaximumSize(QSize(10800, 977))
        font = QFont()
        font.setPointSize(9)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet(u"QPushButton\n"
"{\n"
"    background-color: rgb(75, 173, 238); /*\u80cc\u666f\u8272*/\n"
"    border-style: outset;    /* \u8fb9\u754c\u5185\u51f9 */\n"
"    border-width: 1px;     /* \u8fb9\u8fb9\u754c\u5bbd\u5ea6 */\n"
"    border-radius:16px; /* \u8fb9\u754c\u5706\u6ed1 */\n"
"    font: bold 16px;     /* \u5b57\u4f53\u5927\u5c0f */\n"
"    min-width:2em;\n"
"    color:white; /* \u5b57\u4f53\u989c\u8272 */\n"
"    border-radius: 15px;\n"
"\n"
"}\n"
"/* \u9f20\u6807\u7ecf\u8fc7\u6539\u53d8\u6309\u94ae\u989c\u8272 */\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(0, 150, 0);\n"
"}\n"
"")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget_2 = QTabWidget(self.tab_4)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setGeometry(QRect(200, 30, 811, 561))
        self.tabWidget_2.setMaximumSize(QSize(16777215, 16777215))
        self.tabWidget_2.setFocusPolicy(Qt.TabFocus)
        self.tabWidget_2.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget_2.setAutoFillBackground(False)
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.textBrowser_5 = QTextBrowser(self.tab_8)
        self.textBrowser_5.setObjectName(u"textBrowser_5")
        self.textBrowser_5.setGeometry(QRect(0, 0, 805, 536))
        self.textBrowser_5.setMaximumSize(QSize(16777215, 16777215))
        self.tabWidget_2.addTab(self.tab_8, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.textBrowser_6 = QTextBrowser(self.tab_9)
        self.textBrowser_6.setObjectName(u"textBrowser_6")
        self.textBrowser_6.setGeometry(QRect(0, 0, 805, 536))
        self.textBrowser_6.setMaximumSize(QSize(16777215, 16777215))
        self.tabWidget_2.addTab(self.tab_9, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.textBrowser_7 = QTextBrowser(self.tab_10)
        self.textBrowser_7.setObjectName(u"textBrowser_7")
        self.textBrowser_7.setGeometry(QRect(0, 0, 805, 536))
        self.textBrowser_7.setMaximumSize(QSize(16777215, 16777215))
        self.tabWidget_2.addTab(self.tab_10, "")
        self.tab_11 = QWidget()
        self.tab_11.setObjectName(u"tab_11")
        self.textBrowser_8 = QTextBrowser(self.tab_11)
        self.textBrowser_8.setObjectName(u"textBrowser_8")
        self.textBrowser_8.setGeometry(QRect(0, 0, 805, 536))
        self.textBrowser_8.setMaximumSize(QSize(16777215, 16777215))
        self.tabWidget_2.addTab(self.tab_11, "")
        self.tab_12 = QWidget()
        self.tab_12.setObjectName(u"tab_12")
        self.textBrowser_9 = QTextBrowser(self.tab_12)
        self.textBrowser_9.setObjectName(u"textBrowser_9")
        self.textBrowser_9.setGeometry(QRect(0, 0, 805, 536))
        self.textBrowser_9.setMaximumSize(QSize(16777215, 16777215))
        self.tabWidget_2.addTab(self.tab_12, "")
        self.tab_14 = QWidget()
        self.tab_14.setObjectName(u"tab_14")
        self.textBrowser_10 = QTextBrowser(self.tab_14)
        self.textBrowser_10.setObjectName(u"textBrowser_10")
        self.textBrowser_10.setGeometry(QRect(0, 0, 805, 536))
        self.textBrowser_10.setMaximumSize(QSize(16777215, 16777215))
        self.tabWidget_2.addTab(self.tab_14, "")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 10, 60, 31))
        self.button = QPushButton(self.tab)
        self.button.setObjectName(u"button")
        self.button.setGeometry(QRect(830, 10, 141, 41))
        self.button.setCursor(QCursor(Qt.PointingHandCursor))
        self.button.setStyleSheet(u"QPushButton\n"
"{\n"
"    background-color: rgb(75, 173, 238); /*\u80cc\u666f\u8272*/\n"
"    border-style: outset;    /* \u8fb9\u754c\u5185\u51f9 */\n"
"    border-width: 1px;     /* \u8fb9\u8fb9\u754c\u5bbd\u5ea6 */\n"
"    border-radius:16px; /* \u8fb9\u754c\u5706\u6ed1 */\n"
"    font: bold 16px;     /* \u5b57\u4f53\u5927\u5c0f */\n"
"    min-width:2em;\n"
"    color:white; /* \u5b57\u4f53\u989c\u8272 */\n"
"    border-radius: 15px;\n"
"\n"
"}\n"
"/* \u9f20\u6807\u7ecf\u8fc7\u6539\u53d8\u6309\u94ae\u989c\u8272 */\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(0, 150, 0);\n"
"}\n"
"")
        self.fofa_search = QLineEdit(self.tab)
        self.fofa_search.setObjectName(u"fofa_search")
        self.fofa_search.setGeometry(QRect(100, 10, 491, 31))
        self.fofa_search.setStyleSheet(u"QLineEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 2px solid gray;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #88d, stop: 0.1 #99e, stop: 0.49 #77c, stop: 0.5 #66b, stop: 1 #77c);\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 10px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"min-width: 50px;\n"
"max-width: 50px;\n"
"min-height: 13px;\n"
"max-height: 13px;\n"
"}")
        self.num = QComboBox(self.tab)
        self.num.addItem("")
        self.num.addItem("")
        self.num.addItem("")
        self.num.addItem("")
        self.num.addItem("")
        self.num.setObjectName(u"num")
        self.num.setGeometry(QRect(660, 10, 131, 31))
        self.num.setCursor(QCursor(Qt.PointingHandCursor))
        self.num.setStyleSheet(u"/* \u672a\u4e0b\u62c9\u65f6\uff0cQComboBox\u7684\u6837\u5f0f */\n"
"QComboBox {\n"
"    border: 1px solid gray;   /* \u8fb9\u6846 */\n"
"    border-radius:9px;   /* \u5706\u89d2 */\n"
"    padding: 0px 0px 0px 10px; /* \u4e0a\u5185\u8fb9\u8ddd\u3001\u53f3\u5185\u8fb9\u8ddd\u3001\u4e0b\u5185\u8fb9\u8ddd\u3001\u5de6\u5185\u8fb9\u8ddd */\n"
"    color: rgba(51,51,51,1);\n"
"    /*font: normal normal 15px \"Microsoft YaHei\";*/\n"
"    background: transparent;\n"
"    text-align: AlignHCenter;\n"
"\n"
"    color:rgb(123,123,123);/*\u5b57\u4f53\u989c\u8272*/\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* \u4e0b\u62c9\u540e\uff0c\u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u6837\u5f0f */\n"
"QComboBox QAbstractItemView {\n"
"    outline: 0px solid gray;   /* \u9009\u5b9a\u9879\u7684\u865a\u6846 */\n"
"    border-radius:10px;   /* \u5706\u89d2 */\n"
"\n"
"    color:rgb(123,123,123);\n"
"}\n"
"\n"
"/* \u4e0b\u62c9\u540e\uff0c\u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u6bcf\u9879\u7684\u6837\u5f0f */\n"
"QComboBox QAbstrac"
                        "tItemView::item {\n"
"\n"
"    min-height: 26px;/*\u6bcf\u9879\u9ad8\u5ea6*/\n"
"}\n"
"\n"
"/* \u4e0b\u62c9\u540e\uff0c\u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u8d8a\u8fc7\u6bcf\u9879\u7684\u6837\u5f0f */\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    color:rgb(255,255,255);\n"
"}\n"
"\n"
"/* \u4e0b\u62c9\u540e\uff0c\u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u88ab\u9009\u62e9\u7684\u6bcf\u9879\u7684\u6837\u5f0f */\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    color:rgb(255,255,255);\n"
"\n"
"}")
        self.clear = QPushButton(self.tab)
        self.clear.setObjectName(u"clear")
        self.clear.setGeometry(QRect(830, 70, 141, 41))
        self.clear.setCursor(QCursor(Qt.PointingHandCursor))
        self.clear.setStyleSheet(u"QPushButton\n"
"{\n"
"    background-color: rgb(75, 173, 238); /*\u80cc\u666f\u8272*/\n"
"    border-style: outset;    /* \u8fb9\u754c\u5185\u51f9 */\n"
"    border-width: 1px;     /* \u8fb9\u8fb9\u754c\u5bbd\u5ea6 */\n"
"    border-radius:16px; /* \u8fb9\u754c\u5706\u6ed1 */\n"
"    font: bold 16px;     /* \u5b57\u4f53\u5927\u5c0f */\n"
"    min-width:2em;\n"
"    color:white; /* \u5b57\u4f53\u989c\u8272 */\n"
"    border-radius: 15px;\n"
"\n"
"}\n"
"/* \u9f20\u6807\u7ecf\u8fc7\u6539\u53d8\u6309\u94ae\u989c\u8272 */\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(0, 150, 0);\n"
"}\n"
"")
        self.export_2 = QPushButton(self.tab)
        self.export_2.setObjectName(u"export_2")
        self.export_2.setGeometry(QRect(1010, 10, 201, 41))
        self.export_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.export_2.setStyleSheet(u"QPushButton\n"
"{\n"
"    background-color: rgb(75, 173, 238); /*\u80cc\u666f\u8272*/\n"
"    border-style: outset;    /* \u8fb9\u754c\u5185\u51f9 */\n"
"    border-width: 1px;     /* \u8fb9\u8fb9\u754c\u5bbd\u5ea6 */\n"
"    border-radius:16px; /* \u8fb9\u754c\u5706\u6ed1 */\n"
"    font: bold 16px;     /* \u5b57\u4f53\u5927\u5c0f */\n"
"    min-width:2em;\n"
"    color:white; /* \u5b57\u4f53\u989c\u8272 */\n"
"    border-radius: 15px;\n"
"\n"
"}\n"
"/* \u9f20\u6807\u7ecf\u8fc7\u6539\u53d8\u6309\u94ae\u989c\u8272 */\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(0, 150, 0);\n"
"}\n"
"")
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QRect(100, 110, 271, 31))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setWeight(50)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.label_2.setFont(font1)
        self.label_2.setFocusPolicy(Qt.NoFocus)
        self.label_2.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setFrameShadow(QFrame.Plain)
        self.label_2.setLineWidth(1)
        self.label_2.setTextFormat(Qt.AutoText)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_2.setTextInteractionFlags(Qt.LinksAccessibleByMouse)
        self.label_10 = QLabel(self.tab)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(30, 70, 60, 31))
        self.ico_hash = QLineEdit(self.tab)
        self.ico_hash.setObjectName(u"ico_hash")
        self.ico_hash.setGeometry(QRect(100, 70, 241, 31))
        self.ico_hash.setStyleSheet(u"QLineEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 2px solid gray;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #88d, stop: 0.1 #99e, stop: 0.49 #77c, stop: 0.5 #66b, stop: 1 #77c);\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 10px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"min-width: 50px;\n"
"max-width: 50px;\n"
"min-height: 13px;\n"
"max-height: 13px;\n"
"}")
        self.button_4 = QPushButton(self.tab)
        self.button_4.setObjectName(u"button_4")
        self.button_4.setGeometry(QRect(660, 70, 131, 41))
        self.button_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_4.setStyleSheet(u"QPushButton\n"
"{\n"
"    background-color: rgb(75, 173, 238); /*\u80cc\u666f\u8272*/\n"
"    border-style: outset;    /* \u8fb9\u754c\u5185\u51f9 */\n"
"    border-width: 1px;     /* \u8fb9\u8fb9\u754c\u5bbd\u5ea6 */\n"
"    border-radius:16px; /* \u8fb9\u754c\u5706\u6ed1 */\n"
"    font: bold 16px;     /* \u5b57\u4f53\u5927\u5c0f */\n"
"    min-width:2em;\n"
"    color:white; /* \u5b57\u4f53\u989c\u8272 */\n"
"    border-radius: 15px;\n"
"\n"
"}\n"
"/* \u9f20\u6807\u7ecf\u8fc7\u6539\u53d8\u6309\u94ae\u989c\u8272 */\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(0, 150, 0);\n"
"}\n"
"")
        self.textBrowser = QTextBrowser(self.tab)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(360, 70, 231, 31))
        self.textBrowser.setStyleSheet(u"QTextBrowser {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 2px solid gray;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #88d, stop: 0.1 #99e, stop: 0.49 #77c, stop: 0.5 #66b, stop: 1 #77c);\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 10px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"min-width: 50px;\n"
"max-width: 50px;\n"
"min-height: 13px;\n"
"max-height: 13px;\n"
"}")
        self.shuchu = QTextBrowser(self.tab)
        self.shuchu.setObjectName(u"shuchu")
        self.shuchu.setGeometry(QRect(1020, 150, 201, 501))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(255, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush1)
        brush2 = QBrush(QColor(255, 0, 0, 128))
        brush2.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        brush3 = QBrush(QColor(120, 120, 120, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        brush4 = QBrush(QColor(0, 0, 0, 128))
        brush4.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.shuchu.setPalette(palette)
        self.label_31 = QLabel(self.tab)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(1010, 110, 60, 31))
        self.label_32 = QLabel(self.tab)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setEnabled(True)
        self.label_32.setGeometry(QRect(30, 110, 60, 31))
        self.clearrizi = QPushButton(self.tab)
        self.clearrizi.setObjectName(u"clearrizi")
        self.clearrizi.setGeometry(QRect(1010, 70, 201, 41))
        self.clearrizi.setCursor(QCursor(Qt.PointingHandCursor))
        self.clearrizi.setStyleSheet(u"QPushButton\n"
"{\n"
"    background-color: rgb(75, 173, 238); /*\u80cc\u666f\u8272*/\n"
"    border-style: outset;    /* \u8fb9\u754c\u5185\u51f9 */\n"
"    border-width: 1px;     /* \u8fb9\u8fb9\u754c\u5bbd\u5ea6 */\n"
"    border-radius:16px; /* \u8fb9\u754c\u5706\u6ed1 */\n"
"    font: bold 16px;     /* \u5b57\u4f53\u5927\u5c0f */\n"
"    min-width:2em;\n"
"    color:white; /* \u5b57\u4f53\u989c\u8272 */\n"
"    border-radius: 15px;\n"
"\n"
"}\n"
"/* \u9f20\u6807\u7ecf\u8fc7\u6539\u53d8\u6309\u94ae\u989c\u8272 */\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(0, 150, 0);\n"
"}\n"
"")
        self.fofa = QTableWidget(self.tab)
        if (self.fofa.columnCount() < 8):
            self.fofa.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.fofa.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.fofa.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.fofa.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.fofa.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.fofa.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.fofa.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.fofa.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.fofa.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.fofa.setObjectName(u"fofa")
        self.fofa.setGeometry(QRect(30, 150, 971, 501))
        self.fofa.setColumnCount(8)
        self.fofa.horizontalHeader().setDefaultSectionSize(113)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QRect(100, 110, 231, 31))
        self.label_4.setFont(font1)
        self.label_4.setFocusPolicy(Qt.NoFocus)
        self.label_4.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label_4.setLayoutDirection(Qt.LeftToRight)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setFrameShadow(QFrame.Plain)
        self.label_4.setLineWidth(1)
        self.label_4.setTextFormat(Qt.AutoText)
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_4.setTextInteractionFlags(Qt.LinksAccessibleByMouse)
        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 10, 60, 31))
        self.button_2 = QPushButton(self.tab_2)
        self.button_2.setObjectName(u"button_2")
        self.button_2.setGeometry(QRect(830, 10, 141, 41))
        self.button_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.clear_2 = QPushButton(self.tab_2)
        self.clear_2.setObjectName(u"clear_2")
        self.clear_2.setGeometry(QRect(830, 70, 141, 41))
        self.clear_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.hunter_search = QLineEdit(self.tab_2)
        self.hunter_search.setObjectName(u"hunter_search")
        self.hunter_search.setGeometry(QRect(100, 10, 491, 31))
        self.hunter_search.setStyleSheet(u"QLineEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 2px solid gray;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #88d, stop: 0.1 #99e, stop: 0.49 #77c, stop: 0.5 #66b, stop: 1 #77c);\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 10px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"min-width: 50px;\n"
"max-width: 50px;\n"
"min-height: 13px;\n"
"max-height: 13px;\n"
"}")
        self.export_3 = QPushButton(self.tab_2)
        self.export_3.setObjectName(u"export_3")
        self.export_3.setGeometry(QRect(1010, 10, 201, 41))
        self.export_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.num_2 = QComboBox(self.tab_2)
        self.num_2.addItem("")
        self.num_2.addItem("")
        self.num_2.addItem("")
        self.num_2.addItem("")
        self.num_2.setObjectName(u"num_2")
        self.num_2.setGeometry(QRect(660, 10, 91, 31))
        self.num_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.num_2.setStyleSheet(u"/* \u672a\u4e0b\u62c9\u65f6\uff0cQComboBox\u7684\u6837\u5f0f */\n"
"QComboBox {\n"
"    border: 1px solid gray;   /* \u8fb9\u6846 */\n"
"    border-radius:9px;   /* \u5706\u89d2 */\n"
"    padding: 0px 0px 0px 10px; /* \u4e0a\u5185\u8fb9\u8ddd\u3001\u53f3\u5185\u8fb9\u8ddd\u3001\u4e0b\u5185\u8fb9\u8ddd\u3001\u5de6\u5185\u8fb9\u8ddd */\n"
"    color: rgba(51,51,51,1);\n"
"    /*font: normal normal 15px \"Microsoft YaHei\";*/\n"
"    background: transparent;\n"
"    text-align: AlignHCenter;\n"
"\n"
"    color:rgb(123,123,123);/*\u5b57\u4f53\u989c\u8272*/\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* \u4e0b\u62c9\u540e\uff0c\u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u6837\u5f0f */\n"
"QComboBox QAbstractItemView {\n"
"    outline: 0px solid gray;   /* \u9009\u5b9a\u9879\u7684\u865a\u6846 */\n"
"    border-radius:10px;   /* \u5706\u89d2 */\n"
"\n"
"    color:rgb(123,123,123);\n"
"}\n"
"\n"
"/* \u4e0b\u62c9\u540e\uff0c\u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u6bcf\u9879\u7684\u6837\u5f0f */\n"
"QComboBox QAbstrac"
                        "tItemView::item {\n"
"\n"
"    min-height: 26px;/*\u6bcf\u9879\u9ad8\u5ea6*/\n"
"}\n"
"\n"
"/* \u4e0b\u62c9\u540e\uff0c\u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u8d8a\u8fc7\u6bcf\u9879\u7684\u6837\u5f0f */\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    color:rgb(255,255,255);\n"
"}\n"
"\n"
"/* \u4e0b\u62c9\u540e\uff0c\u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u88ab\u9009\u62e9\u7684\u6bcf\u9879\u7684\u6837\u5f0f */\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    color:rgb(255,255,255);\n"
"\n"
"}")
        self.num_2.setMaxVisibleItems(10)
        self.hunter_tab = QTableWidget(self.tab_2)
        if (self.hunter_tab.columnCount() < 11):
            self.hunter_tab.setColumnCount(11)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.hunter_tab.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.hunter_tab.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.hunter_tab.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.hunter_tab.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.hunter_tab.setHorizontalHeaderItem(4, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.hunter_tab.setHorizontalHeaderItem(5, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.hunter_tab.setHorizontalHeaderItem(6, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.hunter_tab.setHorizontalHeaderItem(7, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.hunter_tab.setHorizontalHeaderItem(8, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.hunter_tab.setHorizontalHeaderItem(9, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.hunter_tab.setHorizontalHeaderItem(10, __qtablewidgetitem18)
        self.hunter_tab.setObjectName(u"hunter_tab")
        self.hunter_tab.setGeometry(QRect(30, 150, 971, 501))
        self.hunter_tab.horizontalHeader().setDefaultSectionSize(84)
        self.xiaohao = QLabel(self.tab_2)
        self.xiaohao.setObjectName(u"xiaohao")
        self.xiaohao.setEnabled(False)
        self.xiaohao.setGeometry(QRect(330, 110, 191, 31))
        self.xiaohao.setFont(font1)
        self.xiaohao.setFocusPolicy(Qt.NoFocus)
        self.xiaohao.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.xiaohao.setLayoutDirection(Qt.LeftToRight)
        self.xiaohao.setAutoFillBackground(False)
        self.xiaohao.setFrameShadow(QFrame.Plain)
        self.xiaohao.setLineWidth(1)
        self.xiaohao.setTextFormat(Qt.AutoText)
        self.xiaohao.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.xiaohao.setTextInteractionFlags(Qt.LinksAccessibleByMouse)
        self.shengyu = QLabel(self.tab_2)
        self.shengyu.setObjectName(u"shengyu")
        self.shengyu.setEnabled(False)
        self.shengyu.setGeometry(QRect(760, 110, 191, 31))
        self.shengyu.setFont(font1)
        self.shengyu.setFocusPolicy(Qt.NoFocus)
        self.shengyu.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.shengyu.setLayoutDirection(Qt.LeftToRight)
        self.shengyu.setAutoFillBackground(False)
        self.shengyu.setFrameShadow(QFrame.Plain)
        self.shengyu.setLineWidth(1)
        self.shengyu.setTextFormat(Qt.AutoText)
        self.shengyu.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.shengyu.setTextInteractionFlags(Qt.LinksAccessibleByMouse)
        self.hunter_page = QLineEdit(self.tab_2)
        self.hunter_page.setObjectName(u"hunter_page")
        self.hunter_page.setGeometry(QRect(490, 70, 101, 31))
        self.hunter_page.setStyleSheet(u"QLineEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 2px solid gray;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #88d, stop: 0.1 #99e, stop: 0.49 #77c, stop: 0.5 #66b, stop: 1 #77c);\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 10px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"min-width: 50px;\n"
"max-width: 50px;\n"
"min-height: 13px;\n"
"max-height: 13px;\n"
"}")
        self.clearrizi_2 = QPushButton(self.tab_2)
        self.clearrizi_2.setObjectName(u"clearrizi_2")
        self.clearrizi_2.setGeometry(QRect(1010, 70, 201, 41))
        self.clearrizi_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.clearrizi_2.setStyleSheet(u"QPushButton\n"
"{\n"
"    background-color: rgb(75, 173, 238); /*\u80cc\u666f\u8272*/\n"
"    border-style: outset;    /* \u8fb9\u754c\u5185\u51f9 */\n"
"    border-width: 1px;     /* \u8fb9\u8fb9\u754c\u5bbd\u5ea6 */\n"
"    border-radius:16px; /* \u8fb9\u754c\u5706\u6ed1 */\n"
"    font: bold 16px;     /* \u5b57\u4f53\u5927\u5c0f */\n"
"    min-width:2em;\n"
"    color:white; /* \u5b57\u4f53\u989c\u8272 */\n"
"    border-radius: 15px;\n"
"\n"
"}\n"
"/* \u9f20\u6807\u7ecf\u8fc7\u6539\u53d8\u6309\u94ae\u989c\u8272 */\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(0, 150, 0);\n"
"}\n"
"")
        self.shuchu_2 = QTextBrowser(self.tab_2)
        self.shuchu_2.setObjectName(u"shuchu_2")
        self.shuchu_2.setGeometry(QRect(1020, 150, 201, 501))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.shuchu_2.setPalette(palette1)
        self.shuchu_2.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.label_33 = QLabel(self.tab_2)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(1020, 110, 60, 31))
        self.label_34 = QLabel(self.tab_2)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setEnabled(True)
        self.label_34.setGeometry(QRect(30, 110, 60, 31))
        self.num_3 = QComboBox(self.tab_2)
        self.num_3.addItem("")
        self.num_3.addItem("")
        self.num_3.addItem("")
        self.num_3.setObjectName(u"num_3")
        self.num_3.setGeometry(QRect(100, 70, 111, 31))
        self.num_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.num_3.setStyleSheet(u"/* \u672a\u4e0b\u62c9\u65f6\uff0cQComboBox\u7684\u6837\u5f0f */\n"
"QComboBox {\n"
"    border: 1px solid gray;   /* \u8fb9\u6846 */\n"
"    border-radius:9px;   /* \u5706\u89d2 */\n"
"    padding: 0px 0px 0px 10px; /* \u4e0a\u5185\u8fb9\u8ddd\u3001\u53f3\u5185\u8fb9\u8ddd\u3001\u4e0b\u5185\u8fb9\u8ddd\u3001\u5de6\u5185\u8fb9\u8ddd */\n"
"    color: rgba(51,51,51,1);\n"
"    /*font: normal normal 15px \"Microsoft YaHei\";*/\n"
"    background: transparent;\n"
"    text-align: AlignHCenter;\n"
"\n"
"    color:rgb(123,123,123);/*\u5b57\u4f53\u989c\u8272*/\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* \u4e0b\u62c9\u540e\uff0c\u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u6837\u5f0f */\n"
"QComboBox QAbstractItemView {\n"
"    outline: 0px solid gray;   /* \u9009\u5b9a\u9879\u7684\u865a\u6846 */\n"
"    border-radius:10px;   /* \u5706\u89d2 */\n"
"\n"
"    color:rgb(123,123,123);\n"
"}\n"
"\n"
"/* \u4e0b\u62c9\u540e\uff0c\u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u6bcf\u9879\u7684\u6837\u5f0f */\n"
"QComboBox QAbstrac"
                        "tItemView::item {\n"
"\n"
"    min-height: 26px;/*\u6bcf\u9879\u9ad8\u5ea6*/\n"
"}\n"
"\n"
"/* \u4e0b\u62c9\u540e\uff0c\u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u8d8a\u8fc7\u6bcf\u9879\u7684\u6837\u5f0f */\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    color:rgb(255,255,255);\n"
"}\n"
"\n"
"/* \u4e0b\u62c9\u540e\uff0c\u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u88ab\u9009\u62e9\u7684\u6bcf\u9879\u7684\u6837\u5f0f */\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    color:rgb(255,255,255);\n"
"\n"
"}")
        self.num_3.setMaxVisibleItems(10)
        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 70, 60, 31))
        self.label_15 = QLabel(self.tab_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(440, 70, 60, 31))
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.shodan_search1 = QLineEdit(self.tab_3)
        self.shodan_search1.setObjectName(u"shodan_search1")
        self.shodan_search1.setGeometry(QRect(100, 10, 521, 31))
        self.shodan_search1.setStyleSheet(u"QLineEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 2px solid gray;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #88d, stop: 0.1 #99e, stop: 0.49 #77c, stop: 0.5 #66b, stop: 1 #77c);\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 10px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"min-width: 50px;\n"
"max-width: 50px;\n"
"min-height: 13px;\n"
"max-height: 13px;\n"
"}")
        self.export_4 = QPushButton(self.tab_3)
        self.export_4.setObjectName(u"export_4")
        self.export_4.setGeometry(QRect(1010, 10, 201, 41))
        self.export_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_8 = QLabel(self.tab_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setEnabled(True)
        self.label_8.setGeometry(QRect(100, 110, 231, 31))
        self.label_8.setFont(font1)
        self.label_8.setFocusPolicy(Qt.NoFocus)
        self.label_8.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label_8.setLayoutDirection(Qt.LeftToRight)
        self.label_8.setAutoFillBackground(False)
        self.label_8.setFrameShadow(QFrame.Plain)
        self.label_8.setLineWidth(1)
        self.label_8.setTextFormat(Qt.AutoText)
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_8.setTextInteractionFlags(Qt.LinksAccessibleByMouse)
        self.shodan_tab = QTableWidget(self.tab_3)
        if (self.shodan_tab.columnCount() < 8):
            self.shodan_tab.setColumnCount(8)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.shodan_tab.setHorizontalHeaderItem(0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.shodan_tab.setHorizontalHeaderItem(1, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.shodan_tab.setHorizontalHeaderItem(2, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.shodan_tab.setHorizontalHeaderItem(3, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.shodan_tab.setHorizontalHeaderItem(4, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.shodan_tab.setHorizontalHeaderItem(5, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.shodan_tab.setHorizontalHeaderItem(6, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.shodan_tab.setHorizontalHeaderItem(7, __qtablewidgetitem26)
        self.shodan_tab.setObjectName(u"shodan_tab")
        self.shodan_tab.setGeometry(QRect(30, 150, 971, 501))
        self.shodan_tab.horizontalHeader().setDefaultSectionSize(116)
        self.clear_3 = QPushButton(self.tab_3)
        self.clear_3.setObjectName(u"clear_3")
        self.clear_3.setGeometry(QRect(830, 70, 141, 41))
        self.clear_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_3 = QPushButton(self.tab_3)
        self.button_3.setObjectName(u"button_3")
        self.button_3.setGeometry(QRect(830, 10, 141, 41))
        self.button_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.shodan_page = QLineEdit(self.tab_3)
        self.shodan_page.setObjectName(u"shodan_page")
        self.shodan_page.setGeometry(QRect(520, 70, 101, 31))
        self.shodan_page.setStyleSheet(u"QLineEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 2px solid gray;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #88d, stop: 0.1 #99e, stop: 0.49 #77c, stop: 0.5 #66b, stop: 1 #77c);\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 10px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"min-width: 50px;\n"
"max-width: 50px;\n"
"min-height: 13px;\n"
"max-height: 13px;\n"
"}")
        self.clearrizi_3 = QPushButton(self.tab_3)
        self.clearrizi_3.setObjectName(u"clearrizi_3")
        self.clearrizi_3.setGeometry(QRect(1010, 70, 201, 41))
        self.clearrizi_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.clearrizi_3.setStyleSheet(u"QPushButton\n"
"{\n"
"    background-color: rgb(75, 173, 238); /*\u80cc\u666f\u8272*/\n"
"    border-style: outset;    /* \u8fb9\u754c\u5185\u51f9 */\n"
"    border-width: 1px;     /* \u8fb9\u8fb9\u754c\u5bbd\u5ea6 */\n"
"    border-radius:16px; /* \u8fb9\u754c\u5706\u6ed1 */\n"
"    font: bold 16px;     /* \u5b57\u4f53\u5927\u5c0f */\n"
"    min-width:2em;\n"
"    color:white; /* \u5b57\u4f53\u989c\u8272 */\n"
"    border-radius: 15px;\n"
"\n"
"}\n"
"/* \u9f20\u6807\u7ecf\u8fc7\u6539\u53d8\u6309\u94ae\u989c\u8272 */\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(0, 150, 0);\n"
"}\n"
"")
        self.label_35 = QLabel(self.tab_3)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(1020, 110, 60, 31))
        self.shuchu_3 = QTextBrowser(self.tab_3)
        self.shuchu_3.setObjectName(u"shuchu_3")
        self.shuchu_3.setGeometry(QRect(1020, 150, 201, 501))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.shuchu_3.setPalette(palette2)
        self.label_36 = QLabel(self.tab_3)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setEnabled(True)
        self.label_36.setGeometry(QRect(30, 110, 60, 31))
        self.num_4 = QComboBox(self.tab_3)
        self.num_4.addItem("")
        self.num_4.addItem("")
        self.num_4.setObjectName(u"num_4")
        self.num_4.setGeometry(QRect(100, 70, 111, 31))
        self.num_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.num_4.setStyleSheet(u"/* \u672a\u4e0b\u62c9\u65f6\uff0cQComboBox\u7684\u6837\u5f0f */\n"
"QComboBox {\n"
"    border: 1px solid gray;   /* \u8fb9\u6846 */\n"
"    border-radius:9px;   /* \u5706\u89d2 */\n"
"    padding: 0px 0px 0px 10px; /* \u4e0a\u5185\u8fb9\u8ddd\u3001\u53f3\u5185\u8fb9\u8ddd\u3001\u4e0b\u5185\u8fb9\u8ddd\u3001\u5de6\u5185\u8fb9\u8ddd */\n"
"    color: rgba(51,51,51,1);\n"
"    /*font: normal normal 15px \"Microsoft YaHei\";*/\n"
"    background: transparent;\n"
"    text-align: AlignHCenter;\n"
"\n"
"    color:rgb(123,123,123);/*\u5b57\u4f53\u989c\u8272*/\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* \u4e0b\u62c9\u540e\uff0c\u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u6837\u5f0f */\n"
"QComboBox QAbstractItemView {\n"
"    outline: 0px solid gray;   /* \u9009\u5b9a\u9879\u7684\u865a\u6846 */\n"
"    border-radius:10px;   /* \u5706\u89d2 */\n"
"\n"
"    color:rgb(123,123,123);\n"
"}\n"
"\n"
"/* \u4e0b\u62c9\u540e\uff0c\u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u6bcf\u9879\u7684\u6837\u5f0f */\n"
"QComboBox QAbstrac"
                        "tItemView::item {\n"
"\n"
"    min-height: 26px;/*\u6bcf\u9879\u9ad8\u5ea6*/\n"
"}\n"
"\n"
"/* \u4e0b\u62c9\u540e\uff0c\u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u8d8a\u8fc7\u6bcf\u9879\u7684\u6837\u5f0f */\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    color:rgb(255,255,255);\n"
"}\n"
"\n"
"/* \u4e0b\u62c9\u540e\uff0c\u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u88ab\u9009\u62e9\u7684\u6bcf\u9879\u7684\u6837\u5f0f */\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    color:rgb(255,255,255);\n"
"\n"
"}")
        self.num_4.setMaxVisibleItems(10)
        self.label_7 = QLabel(self.tab_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 3, 71, 41))
        self.label_9 = QLabel(self.tab_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(30, 70, 60, 31))
        self.label_16 = QLabel(self.tab_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(470, 70, 60, 31))
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.clearrizi_7 = QPushButton(self.tab_6)
        self.clearrizi_7.setObjectName(u"clearrizi_7")
        self.clearrizi_7.setGeometry(QRect(1010, 70, 201, 41))
        self.clearrizi_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.clearrizi_7.setStyleSheet(u"QPushButton\n"
"{\n"
"    background-color: rgb(75, 173, 238); /*\u80cc\u666f\u8272*/\n"
"    border-style: outset;    /* \u8fb9\u754c\u5185\u51f9 */\n"
"    border-width: 1px;     /* \u8fb9\u8fb9\u754c\u5bbd\u5ea6 */\n"
"    border-radius:16px; /* \u8fb9\u754c\u5706\u6ed1 */\n"
"    font: bold 16px;     /* \u5b57\u4f53\u5927\u5c0f */\n"
"    min-width:2em;\n"
"    color:white; /* \u5b57\u4f53\u989c\u8272 */\n"
"    border-radius: 15px;\n"
"\n"
"}\n"
"/* \u9f20\u6807\u7ecf\u8fc7\u6539\u53d8\u6309\u94ae\u989c\u8272 */\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(0, 150, 0);\n"
"}\n"
"")
        self.shuchu_7 = QTextBrowser(self.tab_6)
        self.shuchu_7.setObjectName(u"shuchu_7")
        self.shuchu_7.setGeometry(QRect(1020, 150, 201, 501))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.shuchu_7.setPalette(palette3)
        self.quake_search = QLineEdit(self.tab_6)
        self.quake_search.setObjectName(u"quake_search")
        self.quake_search.setGeometry(QRect(100, 10, 521, 31))
        self.quake_search.setStyleSheet(u"QLineEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 2px solid gray;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #88d, stop: 0.1 #99e, stop: 0.49 #77c, stop: 0.5 #66b, stop: 1 #77c);\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 10px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"min-width: 50px;\n"
"max-width: 50px;\n"
"min-height: 13px;\n"
"max-height: 13px;\n"
"}")
        self.label_45 = QLabel(self.tab_6)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setEnabled(True)
        self.label_45.setGeometry(QRect(30, 110, 60, 31))
        self.quake_tab = QTableWidget(self.tab_6)
        if (self.quake_tab.columnCount() < 7):
            self.quake_tab.setColumnCount(7)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.quake_tab.setHorizontalHeaderItem(0, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.quake_tab.setHorizontalHeaderItem(1, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.quake_tab.setHorizontalHeaderItem(2, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.quake_tab.setHorizontalHeaderItem(3, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.quake_tab.setHorizontalHeaderItem(4, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.quake_tab.setHorizontalHeaderItem(5, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.quake_tab.setHorizontalHeaderItem(6, __qtablewidgetitem33)
        self.quake_tab.setObjectName(u"quake_tab")
        self.quake_tab.setGeometry(QRect(30, 150, 971, 501))
        self.quake_tab.horizontalHeader().setMinimumSectionSize(25)
        self.quake_tab.horizontalHeader().setDefaultSectionSize(132)
        self.quake_tab.horizontalHeader().setHighlightSections(True)
        self.label_46 = QLabel(self.tab_6)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(1020, 110, 60, 31))
        self.label_48 = QLabel(self.tab_6)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(20, 3, 71, 41))
        self.button_9 = QPushButton(self.tab_6)
        self.button_9.setObjectName(u"button_9")
        self.button_9.setGeometry(QRect(830, 10, 141, 41))
        self.button_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.clear_7 = QPushButton(self.tab_6)
        self.clear_7.setObjectName(u"clear_7")
        self.clear_7.setGeometry(QRect(830, 70, 141, 41))
        self.clear_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_50 = QLabel(self.tab_6)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setEnabled(True)
        self.label_50.setGeometry(QRect(100, 110, 231, 31))
        self.label_50.setFont(font1)
        self.label_50.setFocusPolicy(Qt.NoFocus)
        self.label_50.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label_50.setLayoutDirection(Qt.LeftToRight)
        self.label_50.setAutoFillBackground(False)
        self.label_50.setFrameShadow(QFrame.Plain)
        self.label_50.setLineWidth(1)
        self.label_50.setTextFormat(Qt.AutoText)
        self.label_50.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_50.setTextInteractionFlags(Qt.LinksAccessibleByMouse)
        self.export_8 = QPushButton(self.tab_6)
        self.export_8.setObjectName(u"export_8")
        self.export_8.setGeometry(QRect(1010, 10, 201, 41))
        self.export_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.num_10 = QComboBox(self.tab_6)
        self.num_10.addItem("")
        self.num_10.addItem("")
        self.num_10.addItem("")
        self.num_10.addItem("")
        self.num_10.addItem("")
        self.num_10.addItem("")
        self.num_10.setObjectName(u"num_10")
        self.num_10.setGeometry(QRect(100, 70, 111, 31))
        self.num_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.num_10.setStyleSheet(u"/* \u672a\u4e0b\u62c9\u65f6\uff0cQComboBox\u7684\u6837\u5f0f */\n"
"QComboBox {\n"
"    border: 1px solid gray;   /* \u8fb9\u6846 */\n"
"    border-radius:9px;   /* \u5706\u89d2 */\n"
"    padding: 0px 0px 0px 10px; /* \u4e0a\u5185\u8fb9\u8ddd\u3001\u53f3\u5185\u8fb9\u8ddd\u3001\u4e0b\u5185\u8fb9\u8ddd\u3001\u5de6\u5185\u8fb9\u8ddd */\n"
"    color: rgba(51,51,51,1);\n"
"    /*font: normal normal 15px \"Microsoft YaHei\";*/\n"
"    background: transparent;\n"
"    text-align: AlignHCenter;\n"
"\n"
"    color:rgb(123,123,123);/*\u5b57\u4f53\u989c\u8272*/\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* \u4e0b\u62c9\u540e\uff0c\u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u6837\u5f0f */\n"
"QComboBox QAbstractItemView {\n"
"    outline: 0px solid gray;   /* \u9009\u5b9a\u9879\u7684\u865a\u6846 */\n"
"    border-radius:10px;   /* \u5706\u89d2 */\n"
"\n"
"    color:rgb(123,123,123);\n"
"}\n"
"\n"
"/* \u4e0b\u62c9\u540e\uff0c\u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u6bcf\u9879\u7684\u6837\u5f0f */\n"
"QComboBox QAbstrac"
                        "tItemView::item {\n"
"\n"
"    min-height: 26px;/*\u6bcf\u9879\u9ad8\u5ea6*/\n"
"}\n"
"\n"
"/* \u4e0b\u62c9\u540e\uff0c\u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u8d8a\u8fc7\u6bcf\u9879\u7684\u6837\u5f0f */\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    color:rgb(255,255,255);\n"
"}\n"
"\n"
"/* \u4e0b\u62c9\u540e\uff0c\u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u88ab\u9009\u62e9\u7684\u6bcf\u9879\u7684\u6837\u5f0f */\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    color:rgb(255,255,255);\n"
"\n"
"}")
        self.num_10.setMaxVisibleItems(10)
        self.xiaohao_4 = QLabel(self.tab_6)
        self.xiaohao_4.setObjectName(u"xiaohao_4")
        self.xiaohao_4.setEnabled(False)
        self.xiaohao_4.setGeometry(QRect(730, 110, 191, 31))
        self.xiaohao_4.setFont(font1)
        self.xiaohao_4.setFocusPolicy(Qt.NoFocus)
        self.xiaohao_4.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.xiaohao_4.setLayoutDirection(Qt.LeftToRight)
        self.xiaohao_4.setAutoFillBackground(False)
        self.xiaohao_4.setFrameShadow(QFrame.Plain)
        self.xiaohao_4.setLineWidth(1)
        self.xiaohao_4.setTextFormat(Qt.AutoText)
        self.xiaohao_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.xiaohao_4.setTextInteractionFlags(Qt.LinksAccessibleByMouse)
        self.label_49 = QLabel(self.tab_6)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(29, 70, 81, 31))
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.shengyu_2 = QLabel(self.tab_7)
        self.shengyu_2.setObjectName(u"shengyu_2")
        self.shengyu_2.setEnabled(False)
        self.shengyu_2.setGeometry(QRect(700, 110, 191, 31))
        self.shengyu_2.setFont(font1)
        self.shengyu_2.setFocusPolicy(Qt.NoFocus)
        self.shengyu_2.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.shengyu_2.setLayoutDirection(Qt.LeftToRight)
        self.shengyu_2.setAutoFillBackground(False)
        self.shengyu_2.setFrameShadow(QFrame.Plain)
        self.shengyu_2.setLineWidth(1)
        self.shengyu_2.setTextFormat(Qt.AutoText)
        self.shengyu_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.shengyu_2.setTextInteractionFlags(Qt.LinksAccessibleByMouse)
        self.label_18 = QLabel(self.tab_7)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(30, 70, 60, 31))
        self.shuchu_4 = QTextBrowser(self.tab_7)
        self.shuchu_4.setObjectName(u"shuchu_4")
        self.shuchu_4.setGeometry(QRect(1020, 150, 201, 501))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.shuchu_4.setPalette(palette4)
        self.shuchu_4.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.zoomeye_tab = QTableWidget(self.tab_7)
        if (self.zoomeye_tab.columnCount() < 8):
            self.zoomeye_tab.setColumnCount(8)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.zoomeye_tab.setHorizontalHeaderItem(0, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.zoomeye_tab.setHorizontalHeaderItem(1, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.zoomeye_tab.setHorizontalHeaderItem(2, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.zoomeye_tab.setHorizontalHeaderItem(3, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.zoomeye_tab.setHorizontalHeaderItem(4, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.zoomeye_tab.setHorizontalHeaderItem(5, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.zoomeye_tab.setHorizontalHeaderItem(6, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.zoomeye_tab.setHorizontalHeaderItem(7, __qtablewidgetitem41)
        self.zoomeye_tab.setObjectName(u"zoomeye_tab")
        self.zoomeye_tab.setGeometry(QRect(30, 150, 971, 501))
        self.zoomeye_tab.horizontalHeader().setDefaultSectionSize(115)
        self.label_37 = QLabel(self.tab_7)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(1020, 110, 60, 31))
        self.label_19 = QLabel(self.tab_7)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(470, 70, 60, 31))
        self.button_5 = QPushButton(self.tab_7)
        self.button_5.setObjectName(u"button_5")
        self.button_5.setGeometry(QRect(830, 10, 141, 41))
        self.button_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.num_6 = QComboBox(self.tab_7)
        self.num_6.addItem("")
        self.num_6.setObjectName(u"num_6")
        self.num_6.setGeometry(QRect(100, 70, 111, 31))
        self.num_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.num_6.setStyleSheet(u"/* \u672a\u4e0b\u62c9\u65f6\uff0cQComboBox\u7684\u6837\u5f0f */\n"
"QComboBox {\n"
"    border: 1px solid gray;   /* \u8fb9\u6846 */\n"
"    border-radius:9px;   /* \u5706\u89d2 */\n"
"    padding: 0px 0px 0px 10px; /* \u4e0a\u5185\u8fb9\u8ddd\u3001\u53f3\u5185\u8fb9\u8ddd\u3001\u4e0b\u5185\u8fb9\u8ddd\u3001\u5de6\u5185\u8fb9\u8ddd */\n"
"    color: rgba(51,51,51,1);\n"
"    /*font: normal normal 15px \"Microsoft YaHei\";*/\n"
"    background: transparent;\n"
"    text-align: AlignHCenter;\n"
"\n"
"    color:rgb(123,123,123);/*\u5b57\u4f53\u989c\u8272*/\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* \u4e0b\u62c9\u540e\uff0c\u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u6837\u5f0f */\n"
"QComboBox QAbstractItemView {\n"
"    outline: 0px solid gray;   /* \u9009\u5b9a\u9879\u7684\u865a\u6846 */\n"
"    border-radius:10px;   /* \u5706\u89d2 */\n"
"\n"
"    color:rgb(123,123,123);\n"
"}\n"
"\n"
"/* \u4e0b\u62c9\u540e\uff0c\u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u6bcf\u9879\u7684\u6837\u5f0f */\n"
"QComboBox QAbstrac"
                        "tItemView::item {\n"
"\n"
"    min-height: 26px;/*\u6bcf\u9879\u9ad8\u5ea6*/\n"
"}\n"
"\n"
"/* \u4e0b\u62c9\u540e\uff0c\u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u8d8a\u8fc7\u6bcf\u9879\u7684\u6837\u5f0f */\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    color:rgb(255,255,255);\n"
"}\n"
"\n"
"/* \u4e0b\u62c9\u540e\uff0c\u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u88ab\u9009\u62e9\u7684\u6bcf\u9879\u7684\u6837\u5f0f */\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    color:rgb(255,255,255);\n"
"\n"
"}")
        self.num_6.setMaxVisibleItems(10)
        self.zoomeye_search = QLineEdit(self.tab_7)
        self.zoomeye_search.setObjectName(u"zoomeye_search")
        self.zoomeye_search.setGeometry(QRect(100, 10, 521, 31))
        self.zoomeye_search.setStyleSheet(u"QLineEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 2px solid gray;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #88d, stop: 0.1 #99e, stop: 0.49 #77c, stop: 0.5 #66b, stop: 1 #77c);\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 10px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"min-width: 50px;\n"
"max-width: 50px;\n"
"min-height: 13px;\n"
"max-height: 13px;\n"
"}")
        self.zoomeye_page = QLineEdit(self.tab_7)
        self.zoomeye_page.setObjectName(u"zoomeye_page")
        self.zoomeye_page.setGeometry(QRect(520, 70, 101, 31))
        self.zoomeye_page.setStyleSheet(u"QLineEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 2px solid gray;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #88d, stop: 0.1 #99e, stop: 0.49 #77c, stop: 0.5 #66b, stop: 1 #77c);\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 10px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"min-width: 50px;\n"
"max-width: 50px;\n"
"min-height: 13px;\n"
"max-height: 13px;\n"
"}")
        self.label_20 = QLabel(self.tab_7)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(10, 10, 81, 31))
        self.label_21 = QLabel(self.tab_7)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setEnabled(True)
        self.label_21.setGeometry(QRect(100, 110, 231, 31))
        self.label_21.setFont(font1)
        self.label_21.setFocusPolicy(Qt.NoFocus)
        self.label_21.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label_21.setLayoutDirection(Qt.LeftToRight)
        self.label_21.setAutoFillBackground(False)
        self.label_21.setFrameShadow(QFrame.Plain)
        self.label_21.setLineWidth(1)
        self.label_21.setTextFormat(Qt.AutoText)
        self.label_21.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_21.setTextInteractionFlags(Qt.LinksAccessibleByMouse)
        self.clear_4 = QPushButton(self.tab_7)
        self.clear_4.setObjectName(u"clear_4")
        self.clear_4.setGeometry(QRect(830, 70, 141, 41))
        self.clear_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_38 = QLabel(self.tab_7)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setEnabled(True)
        self.label_38.setGeometry(QRect(30, 110, 60, 31))
        self.export_6 = QPushButton(self.tab_7)
        self.export_6.setObjectName(u"export_6")
        self.export_6.setGeometry(QRect(1010, 10, 201, 41))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setBold(True)
        font2.setItalic(False)
        font2.setWeight(75)
        self.export_6.setFont(font2)
        self.export_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.clearrizi_4 = QPushButton(self.tab_7)
        self.clearrizi_4.setObjectName(u"clearrizi_4")
        self.clearrizi_4.setGeometry(QRect(1010, 70, 201, 41))
        self.clearrizi_4.setFont(font2)
        self.clearrizi_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_13 = QWidget()
        self.tab_13.setObjectName(u"tab_13")
        self.Censys_num = QComboBox(self.tab_13)
        self.Censys_num.addItem("")
        self.Censys_num.addItem("")
        self.Censys_num.setObjectName(u"Censys_num")
        self.Censys_num.setGeometry(QRect(100, 70, 111, 31))
        self.Censys_num.setCursor(QCursor(Qt.PointingHandCursor))
        self.Censys_num.setStyleSheet(u"/* \u672a\u4e0b\u62c9\u65f6\uff0cQComboBox\u7684\u6837\u5f0f */\n"
"QComboBox {\n"
"    border: 1px solid gray;   /* \u8fb9\u6846 */\n"
"    border-radius:9px;   /* \u5706\u89d2 */\n"
"    padding: 0px 0px 0px 10px; /* \u4e0a\u5185\u8fb9\u8ddd\u3001\u53f3\u5185\u8fb9\u8ddd\u3001\u4e0b\u5185\u8fb9\u8ddd\u3001\u5de6\u5185\u8fb9\u8ddd */\n"
"    color: rgba(51,51,51,1);\n"
"    /*font: normal normal 15px \"Microsoft YaHei\";*/\n"
"    background: transparent;\n"
"    text-align: AlignHCenter;\n"
"\n"
"    color:rgb(123,123,123);/*\u5b57\u4f53\u989c\u8272*/\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* \u4e0b\u62c9\u540e\uff0c\u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u6837\u5f0f */\n"
"QComboBox QAbstractItemView {\n"
"    outline: 0px solid gray;   /* \u9009\u5b9a\u9879\u7684\u865a\u6846 */\n"
"    border-radius:10px;   /* \u5706\u89d2 */\n"
"\n"
"    color:rgb(123,123,123);\n"
"}\n"
"\n"
"/* \u4e0b\u62c9\u540e\uff0c\u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u6bcf\u9879\u7684\u6837\u5f0f */\n"
"QComboBox QAbstrac"
                        "tItemView::item {\n"
"\n"
"    min-height: 26px;/*\u6bcf\u9879\u9ad8\u5ea6*/\n"
"}\n"
"\n"
"/* \u4e0b\u62c9\u540e\uff0c\u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u8d8a\u8fc7\u6bcf\u9879\u7684\u6837\u5f0f */\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    color:rgb(255,255,255);\n"
"}\n"
"\n"
"/* \u4e0b\u62c9\u540e\uff0c\u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u88ab\u9009\u62e9\u7684\u6bcf\u9879\u7684\u6837\u5f0f */\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    color:rgb(255,255,255);\n"
"\n"
"}")
        self.Censys_num.setMaxVisibleItems(10)
        self.Censys_tab = QTableWidget(self.tab_13)
        if (self.Censys_tab.columnCount() < 9):
            self.Censys_tab.setColumnCount(9)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.Censys_tab.setHorizontalHeaderItem(0, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.Censys_tab.setHorizontalHeaderItem(1, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.Censys_tab.setHorizontalHeaderItem(2, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.Censys_tab.setHorizontalHeaderItem(3, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.Censys_tab.setHorizontalHeaderItem(4, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.Censys_tab.setHorizontalHeaderItem(5, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.Censys_tab.setHorizontalHeaderItem(6, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.Censys_tab.setHorizontalHeaderItem(7, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.Censys_tab.setHorizontalHeaderItem(8, __qtablewidgetitem50)
        self.Censys_tab.setObjectName(u"Censys_tab")
        self.Censys_tab.setGeometry(QRect(30, 150, 971, 501))
        self.Censys_tab.horizontalHeader().setDefaultSectionSize(102)
        self.Censys_clearjieguo = QPushButton(self.tab_13)
        self.Censys_clearjieguo.setObjectName(u"Censys_clearjieguo")
        self.Censys_clearjieguo.setGeometry(QRect(830, 70, 141, 41))
        self.Censys_clearjieguo.setCursor(QCursor(Qt.PointingHandCursor))
        self.Censys_clearrizi = QPushButton(self.tab_13)
        self.Censys_clearrizi.setObjectName(u"Censys_clearrizi")
        self.Censys_clearrizi.setGeometry(QRect(1010, 70, 201, 41))
        self.Censys_clearrizi.setCursor(QCursor(Qt.PointingHandCursor))
        self.Censys_clearrizi.setStyleSheet(u"QPushButton\n"
"{\n"
"    background-color: rgb(75, 173, 238); /*\u80cc\u666f\u8272*/\n"
"    border-style: outset;    /* \u8fb9\u754c\u5185\u51f9 */\n"
"    border-width: 1px;     /* \u8fb9\u8fb9\u754c\u5bbd\u5ea6 */\n"
"    border-radius:16px; /* \u8fb9\u754c\u5706\u6ed1 */\n"
"    font: bold 16px;     /* \u5b57\u4f53\u5927\u5c0f */\n"
"    min-width:2em;\n"
"    color:white; /* \u5b57\u4f53\u989c\u8272 */\n"
"    border-radius: 15px;\n"
"\n"
"}\n"
"/* \u9f20\u6807\u7ecf\u8fc7\u6539\u53d8\u6309\u94ae\u989c\u8272 */\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(0, 150, 0);\n"
"}\n"
"")
        self.Censys_yufa = QLabel(self.tab_13)
        self.Censys_yufa.setObjectName(u"Censys_yufa")
        self.Censys_yufa.setGeometry(QRect(19, 10, 71, 31))
        self.label_39 = QLabel(self.tab_13)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setEnabled(True)
        self.label_39.setGeometry(QRect(30, 110, 60, 31))
        self.label_12 = QLabel(self.tab_13)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setEnabled(True)
        self.label_12.setGeometry(QRect(100, 110, 231, 31))
        self.label_12.setFont(font1)
        self.label_12.setFocusPolicy(Qt.NoFocus)
        self.label_12.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label_12.setLayoutDirection(Qt.LeftToRight)
        self.label_12.setAutoFillBackground(False)
        self.label_12.setFrameShadow(QFrame.Plain)
        self.label_12.setLineWidth(1)
        self.label_12.setTextFormat(Qt.AutoText)
        self.label_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_12.setTextInteractionFlags(Qt.LinksAccessibleByMouse)
        self.Censys_search = QLineEdit(self.tab_13)
        self.Censys_search.setObjectName(u"Censys_search")
        self.Censys_search.setGeometry(QRect(100, 10, 491, 31))
        self.Censys_search.setStyleSheet(u"QLineEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 2px solid gray;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #88d, stop: 0.1 #99e, stop: 0.49 #77c, stop: 0.5 #66b, stop: 1 #77c);\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 10px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"min-width: 50px;\n"
"max-width: 50px;\n"
"min-height: 13px;\n"
"max-height: 13px;\n"
"}")
        self.label_13 = QLabel(self.tab_13)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(30, 70, 60, 31))
        self.label_40 = QLabel(self.tab_13)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(1020, 110, 60, 31))
        self.shuchu_5 = QTextBrowser(self.tab_13)
        self.shuchu_5.setObjectName(u"shuchu_5")
        self.shuchu_5.setGeometry(QRect(1020, 150, 201, 501))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.shuchu_5.setPalette(palette5)
        self.shuchu_5.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.Censys_export = QPushButton(self.tab_13)
        self.Censys_export.setObjectName(u"Censys_export")
        self.Censys_export.setGeometry(QRect(1010, 10, 201, 41))
        self.Censys_export.setCursor(QCursor(Qt.PointingHandCursor))
        self.Censys_search_1 = QPushButton(self.tab_13)
        self.Censys_search_1.setObjectName(u"Censys_search_1")
        self.Censys_search_1.setGeometry(QRect(830, 10, 141, 41))
        self.Censys_search_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.Censys_next = QPushButton(self.tab_13)
        self.Censys_next.setObjectName(u"Censys_next")
        self.Censys_next.setGeometry(QRect(500, 70, 91, 31))
        self.Censys_prev = QPushButton(self.tab_13)
        self.Censys_prev.setObjectName(u"Censys_prev")
        self.Censys_prev.setGeometry(QRect(350, 70, 91, 31))
        self.tabWidget.addTab(self.tab_13, "")
        self.tab_15 = QWidget()
        self.tab_15.setObjectName(u"tab_15")
        self.save_config = QPushButton(self.tab_15)
        self.save_config.setObjectName(u"save_config")
        self.save_config.setGeometry(QRect(900, 560, 181, 51))
        self.save_config.setCursor(QCursor(Qt.PointingHandCursor))
        self.shodan_config_2 = QGroupBox(self.tab_15)
        self.shodan_config_2.setObjectName(u"shodan_config_2")
        self.shodan_config_2.setGeometry(QRect(10, 240, 741, 91))
        self.your_shodan_api = QLineEdit(self.shodan_config_2)
        self.your_shodan_api.setObjectName(u"your_shodan_api")
        self.your_shodan_api.setGeometry(QRect(130, 30, 411, 31))
        self.your_shodan_api.setStyleSheet(u"QLineEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 2px solid gray;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #88d, stop: 0.1 #99e, stop: 0.49 #77c, stop: 0.5 #66b, stop: 1 #77c);\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 10px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"min-width: 50px;\n"
"max-width: 50px;\n"
"min-height: 13px;\n"
"max-height: 13px;\n"
"}")
        self.your_shodan_api.setEchoMode(QLineEdit.Password)
        self.label_68 = QLabel(self.shodan_config_2)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setGeometry(QRect(40, 20, 81, 41))
        self.shodan_xiugai = QPushButton(self.shodan_config_2)
        self.shodan_xiugai.setObjectName(u"shodan_xiugai")
        self.shodan_xiugai.setGeometry(QRect(590, 30, 111, 41))
        self.shodan_xiugai.setCursor(QCursor(Qt.PointingHandCursor))
        self.hunter_config_2 = QGroupBox(self.tab_15)
        self.hunter_config_2.setObjectName(u"hunter_config_2")
        self.hunter_config_2.setGeometry(QRect(10, 140, 741, 91))
        self.your_hunter_api = QLineEdit(self.hunter_config_2)
        self.your_hunter_api.setObjectName(u"your_hunter_api")
        self.your_hunter_api.setGeometry(QRect(130, 30, 411, 31))
        self.your_hunter_api.setStyleSheet(u"QLineEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 2px solid gray;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #88d, stop: 0.1 #99e, stop: 0.49 #77c, stop: 0.5 #66b, stop: 1 #77c);\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 10px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"min-width: 50px;\n"
"max-width: 50px;\n"
"min-height: 13px;\n"
"max-height: 13px;\n"
"}")
        self.your_hunter_api.setEchoMode(QLineEdit.Password)
        self.label_69 = QLabel(self.hunter_config_2)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setGeometry(QRect(40, 20, 81, 41))
        self.hunter_xiugai = QPushButton(self.hunter_config_2)
        self.hunter_xiugai.setObjectName(u"hunter_xiugai")
        self.hunter_xiugai.setGeometry(QRect(590, 30, 111, 41))
        self.hunter_xiugai.setCursor(QCursor(Qt.PointingHandCursor))
        self.groupBox_6 = QGroupBox(self.tab_15)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(780, 0, 421, 521))
        font3 = QFont()
        font3.setPointSize(13)
        self.groupBox_6.setFont(font3)
        self.groupBox_6.setLayoutDirection(Qt.LeftToRight)
        self.label_70 = QLabel(self.groupBox_6)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setGeometry(QRect(20, 20, 391, 171))
        font4 = QFont()
        font4.setFamily(u"\u9ed1\u4f53")
        font4.setPointSize(12)
        self.label_70.setFont(font4)
        self.label_70.setLayoutDirection(Qt.LeftToRight)
        self.label_70.setFrameShadow(QFrame.Plain)
        self.fofa_config_3 = QGroupBox(self.tab_15)
        self.fofa_config_3.setObjectName(u"fofa_config_3")
        self.fofa_config_3.setGeometry(QRect(10, 440, 741, 91))
        self.fofa_config_3.setFont(font)
        self.label_71 = QLabel(self.fofa_config_3)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setGeometry(QRect(30, 30, 101, 31))
        self.your_zoomeye_api = QLineEdit(self.fofa_config_3)
        self.your_zoomeye_api.setObjectName(u"your_zoomeye_api")
        self.your_zoomeye_api.setGeometry(QRect(130, 30, 411, 31))
        self.your_zoomeye_api.setStyleSheet(u"QLineEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 2px solid gray;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #88d, stop: 0.1 #99e, stop: 0.49 #77c, stop: 0.5 #66b, stop: 1 #77c);\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 10px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"min-width: 50px;\n"
"max-width: 50px;\n"
"min-height: 13px;\n"
"max-height: 13px;\n"
"}")
        self.zoomeye_xiugai = QPushButton(self.fofa_config_3)
        self.zoomeye_xiugai.setObjectName(u"zoomeye_xiugai")
        self.zoomeye_xiugai.setGeometry(QRect(590, 30, 111, 41))
        self.zoomeye_xiugai.setCursor(QCursor(Qt.PointingHandCursor))
        self.fofa_config_4 = QGroupBox(self.tab_15)
        self.fofa_config_4.setObjectName(u"fofa_config_4")
        self.fofa_config_4.setGeometry(QRect(10, 10, 741, 121))
        self.fofa_config_4.setFont(font)
        self.label_72 = QLabel(self.fofa_config_4)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setGeometry(QRect(40, 20, 81, 31))
        self.label_73 = QLabel(self.fofa_config_4)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setGeometry(QRect(50, 60, 81, 41))
        self.your_fofa_email = QLineEdit(self.fofa_config_4)
        self.your_fofa_email.setObjectName(u"your_fofa_email")
        self.your_fofa_email.setGeometry(QRect(130, 20, 411, 31))
        self.your_fofa_email.setStyleSheet(u"QLineEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 2px solid gray;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #88d, stop: 0.1 #99e, stop: 0.49 #77c, stop: 0.5 #66b, stop: 1 #77c);\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 10px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"min-width: 50px;\n"
"max-width: 50px;\n"
"min-height: 13px;\n"
"max-height: 13px;\n"
"}")
        self.your_fofa_api = QLineEdit(self.fofa_config_4)
        self.your_fofa_api.setObjectName(u"your_fofa_api")
        self.your_fofa_api.setGeometry(QRect(130, 70, 411, 31))
        self.your_fofa_api.setStyleSheet(u"QLineEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 2px solid gray;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #88d, stop: 0.1 #99e, stop: 0.49 #77c, stop: 0.5 #66b, stop: 1 #77c);\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 10px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"min-width: 50px;\n"
"max-width: 50px;\n"
"min-height: 13px;\n"
"max-height: 13px;\n"
"}")
        self.your_fofa_api.setEchoMode(QLineEdit.Password)
        self.fofa_xiugai = QPushButton(self.fofa_config_4)
        self.fofa_xiugai.setObjectName(u"fofa_xiugai")
        self.fofa_xiugai.setGeometry(QRect(590, 40, 111, 41))
        self.fofa_xiugai.setCursor(QCursor(Qt.PointingHandCursor))
        self.shodan_config_4 = QGroupBox(self.tab_15)
        self.shodan_config_4.setObjectName(u"shodan_config_4")
        self.shodan_config_4.setGeometry(QRect(10, 340, 741, 91))
        self.your_quake_api = QLineEdit(self.shodan_config_4)
        self.your_quake_api.setObjectName(u"your_quake_api")
        self.your_quake_api.setGeometry(QRect(130, 30, 411, 31))
        self.your_quake_api.setStyleSheet(u"QLineEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 2px solid gray;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #88d, stop: 0.1 #99e, stop: 0.49 #77c, stop: 0.5 #66b, stop: 1 #77c);\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 10px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"min-width: 50px;\n"
"max-width: 50px;\n"
"min-height: 13px;\n"
"max-height: 13px;\n"
"}")
        self.your_quake_api.setEchoMode(QLineEdit.Password)
        self.label_74 = QLabel(self.shodan_config_4)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setGeometry(QRect(40, 20, 81, 41))
        self.quake_xiugai = QPushButton(self.shodan_config_4)
        self.quake_xiugai.setObjectName(u"quake_xiugai")
        self.quake_xiugai.setGeometry(QRect(590, 30, 111, 41))
        self.quake_xiugai.setCursor(QCursor(Qt.PointingHandCursor))
        self.fofa_config_5 = QGroupBox(self.tab_15)
        self.fofa_config_5.setObjectName(u"fofa_config_5")
        self.fofa_config_5.setGeometry(QRect(10, 540, 741, 131))
        self.fofa_config_5.setFont(font)
        self.label_76 = QLabel(self.fofa_config_5)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setGeometry(QRect(40, 30, 101, 31))
        self.your_censys_uid = QLineEdit(self.fofa_config_5)
        self.your_censys_uid.setObjectName(u"your_censys_uid")
        self.your_censys_uid.setGeometry(QRect(130, 30, 411, 31))
        self.your_censys_uid.setStyleSheet(u"QLineEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 2px solid gray;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #88d, stop: 0.1 #99e, stop: 0.49 #77c, stop: 0.5 #66b, stop: 1 #77c);\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 10px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"min-width: 50px;\n"
"max-width: 50px;\n"
"min-height: 13px;\n"
"max-height: 13px;\n"
"}")
        self.censys_xiugai = QPushButton(self.fofa_config_5)
        self.censys_xiugai.setObjectName(u"censys_xiugai")
        self.censys_xiugai.setGeometry(QRect(590, 50, 111, 41))
        self.censys_xiugai.setCursor(QCursor(Qt.PointingHandCursor))
        self.your_censys_secret = QLineEdit(self.fofa_config_5)
        self.your_censys_secret.setObjectName(u"your_censys_secret")
        self.your_censys_secret.setGeometry(QRect(130, 80, 411, 31))
        self.your_censys_secret.setStyleSheet(u"QLineEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 2px solid gray;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #88d, stop: 0.1 #99e, stop: 0.49 #77c, stop: 0.5 #66b, stop: 1 #77c);\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 10px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"min-width: 50px;\n"
"max-width: 50px;\n"
"min-height: 13px;\n"
"max-height: 13px;\n"
"}")
        self.label_77 = QLabel(self.fofa_config_5)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setGeometry(QRect(30, 80, 101, 31))
        self.label_3 = QLabel(self.tab_15)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(850, 620, 331, 31))
        self.tabWidget.addTab(self.tab_15, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.groupBox_2 = QGroupBox(self.tab_5)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(20, 10, 571, 651))
        self.groupBox_2.setFont(font)
        self.groupBox_3 = QGroupBox(self.tab_5)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(620, 10, 571, 651))
        self.groupBox_3.setFont(font)
        self.textBrowser_3 = QTextBrowser(self.groupBox_3)
        self.textBrowser_3.setObjectName(u"textBrowser_3")
        self.textBrowser_3.setGeometry(QRect(30, 30, 501, 601))
        self.textBrowser_4 = QTextBrowser(self.tab_5)
        self.textBrowser_4.setObjectName(u"textBrowser_4")
        self.textBrowser_4.setGeometry(QRect(40, 40, 521, 601))
        self.tabWidget.addTab(self.tab_5, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(0)
        self.num_2.setCurrentIndex(1)
        self.num_3.setCurrentIndex(0)
        self.num_4.setCurrentIndex(0)
        self.num_10.setCurrentIndex(0)
        self.num_6.setCurrentIndex(0)
        self.Censys_num.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Search_Viewer v3.0   Author\uff1aG3et", None))
        self.actionfofa.setText(QCoreApplication.translate("MainWindow", u"fofa", None))
#if QT_CONFIG(shortcut)
        self.actionfofa.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+A", None))
#endif // QT_CONFIG(shortcut)
        self.textBrowser_5.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">title=&quot;beijing&quot;			\u4ece\u6807\u9898\u4e2d\u641c\u7d22&quot;\u5317\u4eac&quot;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">header=&quot;elastic&quot;			\u4ecehttp\u5934\u4e2d\u641c\u7d22&quot;elastic&quot;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right"
                        ":0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">body=&quot;\u7f51\u7edc\u7a7a\u95f4\u6d4b\u7ed8&quot;			\u4ecehtml\u6b63\u6587\u4e2d\u641c\u7d22&quot;\u7f51\u7edc\u7a7a\u95f4\u6d4b\u7ed8&quot;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">fid=&quot;sSXXGNUO2FefBTcCLIT/2Q==&quot;		\u67e5\u627e\u76f8\u540c\u7684\u7f51\u7ad9\u6307\u7eb9</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">domain=&quot;qq.com&qu"
                        "ot;			\u641c\u7d22\u6839\u57df\u540d\u5e26\u6709qq.com\u7684\u7f51\u7ad9</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">icp=&quot;\u4eacICP\u8bc1030173\u53f7&quot;			\u67e5\u627e\u5907\u6848\u53f7\u4e3a&quot;\u4eacICP\u8bc1030173\u53f7&quot;\u7684\u7f51\u7ad9</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">js_name=&quot;js/jquery.js&quot;			\u67e5\u627e\u7f51\u7ad9\u6b63\u6587\u4e2d\u5305\u542bjs/jquery.js\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0p"
                        "x; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">js_md5=&quot;82ac3f14327a8b7ba49baa208d4eaa15&quot;	\u67e5\u627ejs\u6e90\u7801\u4e0e\u4e4b\u5339\u914d\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">cname=&quot;ap21.inst.siteforce.com&quot;		\u67e5\u627ecname\u4e3a&quot;ap21.inst.siteforce.com&quot;\u7684\u7f51\u7ad9</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">cname_domain=&quot;sitefor"
                        "ce.com&quot;		\u67e5\u627ecname\u5305\u542b&quot;siteforce.com&quot;\u7684\u7f51\u7ad9</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">cloud_name=&quot;Aliyundun&quot;			\u901a\u8fc7\u4e91\u670d\u52a1\u540d\u79f0\u641c\u7d22\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">product=&quot;NGINX&quot;			\u641c\u7d22\u6b64\u4ea7\u54c1\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\""
                        " margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">category=&quot;\u670d\u52a1&quot;			\u641c\u7d22\u6b64\u4ea7\u54c1\u5206\u7c7b\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">icon_hash=&quot;-247388890&quot;			\u641c\u7d22\u4f7f\u7528\u6b64 icon \u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">host=&quot;.gov.cn&quot;			\u4eceurl\u4e2d\u641c\u7d22&quot;.gov.cn&quot;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom"
                        ":0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">port=&quot;6379&quot;				\u67e5\u627e\u5bf9\u5e94&quot;6379&quot;\u7aef\u53e3\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ip=&quot;1.1.1.1&quot;				\u4eceip\u4e2d\u641c\u7d22\u5305\u542b&quot;1.1.1.1&quot;\u7684\u7f51\u7ad9</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ip=&quot;220.181.111.1/24&quot;"
                        "			\u67e5\u8be2IP\u4e3a&quot;220.181.111.1&quot;\u7684C\u7f51\u6bb5\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">status_code=&quot;402&quot;			\u67e5\u8be2\u670d\u52a1\u5668\u72b6\u6001\u4e3a&quot;402&quot;\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">protocol=&quot;quic&quot;			\u67e5\u8be2quic\u534f\u8bae\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" mar"
                        "gin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">country=&quot;CN&quot;				\u641c\u7d22\u6307\u5b9a\u56fd\u5bb6(\u7f16\u7801)\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">region=&quot;Xinjiang Uyghur Autonomous Region&quot;	\u641c\u7d22\u6307\u5b9a\u884c\u653f\u533a\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">city=&quot;\u00dcr\u00fcmqi&quot;				\u641c\u7d22\u6307\u5b9a\u57ce\u5e02\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:"
                        "empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">cert=&quot;baidu&quot;				\u641c\u7d22\u8bc1\u4e66(https\u6216\u8005imaps\u7b49)\u4e2d\u5e26\u6709baidu\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">cert.subject=&quot;Oracle Corporation&quot;		\u641c\u7d22\u8bc1\u4e66\u6301\u6709\u8005\u662fOracle Corporation\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px"
                        "; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">cert.issuer=&quot;DigiCert&quot;			\u641c\u7d22\u8bc1\u4e66\u9881\u53d1\u8005\u4e3aDigiCert Inc\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">cert.is_valid=true			\u9a8c\u8bc1\u8bc1\u4e66\u662f\u5426\u6709\u6548\uff0ctrue\u6709\u6548\uff0cfalse\u65e0\u6548</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">cert.is_match=true			\u8bc1\u4e66\u548c\u57df\u540d\u662f\u5426\u5339\u914d\uff1btrue\u5339\u914d\u3001false\u4e0d\u5339\u914d</p>\n"
"<p style=\"-qt-paragra"
                        "ph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">cert.is_expired=false			\u8bc1\u4e66\u662f\u5426\u8fc7\u671f\uff1btrue\u8fc7\u671f\u3001false\u672a\u8fc7\u671f</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">jarm=&quot;2ad...83e81&quot;			\u641c\u7d22JARM\u6307\u7eb9</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">banner=&quot;"
                        "users&quot; &amp;&amp; protocol=&quot;ftp&quot;		\u641c\u7d22FTP\u534f\u8bae\u4e2d\u5e26\u6709users\u6587\u672c\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">type=&quot;service&quot;			\u641c\u7d22\u6240\u6709\u534f\u8bae\u8d44\u4ea7\uff0c\u652f\u6301subdomain\u548cservice\u4e24\u79cd</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">os=&quot;centos&quot;				\u641c\u7d22CentOS\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent"
                        ":0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">server==&quot;Microsoft-IIS/10&quot;			\u641c\u7d22IIS 10\u670d\u52a1\u5668</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">app=&quot;Microsoft-Exchange&quot;			\u641c\u7d22Microsoft-Exchange\u8bbe\u5907</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">asn=&quot;19551&quot;				\u641c\u7d22\u6307\u5b9aasn\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px"
                        "; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">org=&quot;LLC Baxet&quot;			\u641c\u7d22\u6307\u5b9aorg(\u7ec4\u7ec7)\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">base_protocol=&quot;udp&quot;			\u641c\u7d22\u6307\u5b9audp\u534f\u8bae\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">is_fraud=false			\u6392\u9664\u4eff\u5192"
                        "/\u6b3a\u8bc8\u6570\u636e</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">is_honeypot=false			\u6392\u9664\u871c\u7f50\u6570\u636e</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">is_ipv6=true				\u641c\u7d22ipv6\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">is_domain=true			\u641c"
                        "\u7d22\u57df\u540d\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">is_cloud=true				\u7b5b\u9009\u4f7f\u7528\u4e86\u4e91\u670d\u52a1\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">port_size=&quot;6&quot;				\u67e5\u8be2\u5f00\u653e\u7aef\u53e3\u6570\u91cf\u7b49\u4e8e&quot;6&quot;\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-b"
                        "ottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">port_size_gt=&quot;6&quot;			\u67e5\u8be2\u5f00\u653e\u7aef\u53e3\u6570\u91cf\u5927\u4e8e&quot;6&quot;\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">port_size_lt=&quot;12&quot;			\u67e5\u8be2\u5f00\u653e\u7aef\u53e3\u6570\u91cf\u5c0f\u4e8e&quot;12&quot;\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ip_ports=&quot;80,161&quot;			\u641c\u7d22\u540c\u65f6\u5f00\u653e80\u548c161\u7aef\u53e3\u7684ip</p>\n"
"<p style=\""
                        "-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ip_country=&quot;CN&quot;			\u641c\u7d22\u4e2d\u56fd\u7684ip\u8d44\u4ea7(\u4ee5ip\u4e3a\u5355\u4f4d\u7684\u8d44\u4ea7\u6570\u636e)</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ip_region=&quot;Zhejiang&quot;			\u641c\u7d22\u6307\u5b9a\u884c\u653f\u533a\u7684ip\u8d44\u4ea7(\u4ee5ip\u4e3a\u5355\u4f4d\u7684\u8d44\u4ea7\u6570\u636e)</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\""
                        " margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ip_city=&quot;Hangzhou&quot;			\u641c\u7d22\u6307\u5b9a\u57ce\u5e02\u7684ip\u8d44\u4ea7(\u4ee5ip\u4e3a\u5355\u4f4d\u7684\u8d44\u4ea7\u6570\u636e)</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u9ad8\u7ea7\u641c\u7d22\uff1a</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"
                        "\">\u903b\u8f91\u8fde\u63a5\u7b26				\u5177\u4f53\u542b\u4e49</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">=				\u5339\u914d\uff0c=&quot;&quot;\u65f6\uff0c\u53ef\u67e5\u8be2\u4e0d\u5b58\u5728\u5b57\u6bb5\u6216\u8005\u503c\u4e3a\u7a7a\u7684\u60c5\u51b5\u3002</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">==				\u5b8c\u5168\u5339\u914d\uff0c==&quot;&quot;\u65f6\uff0c\u53ef\u67e5\u8be2\u5b58\u5728\u4e14\u503c\u4e3a\u7a7a\u7684\u60c5\u51b5\u3002</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left"
                        ":0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&amp;&amp;				\u4e0e</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">||				\u6216\u8005</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">!=				\u4e0d\u5339\u914d\uff0c!=&quot;&quot;\u65f6\uff0c\u53ef\u67e5\u8be2\u503c\u4e3a\u7a7a\u7684\u60c5\u51b5\u3002</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-le"
                        "ft:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">*=				\u6a21\u7cca\u5339\u914d\uff0c\u4f7f\u7528*\u6216\u8005?\u8fdb\u884c\u641c\u7d22\uff0c\u6bd4\u5982banner*=&quot;mys??&quot; (\u4e2a\u4eba\u7248\u53ca\u4ee5\u4e0a\u53ef\u7528)\u3002</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">()				\u786e\u8ba4\u67e5\u8be2\u4f18\u5148\u7ea7\uff0c\u62ec\u53f7\u5185\u5bb9\u4f18\u5148\u7ea7\u6700\u9ad8\u3002</p></body></html>", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"FOFA\u8bed\u6cd5", None))
        self.textBrowser_6.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">icp.web_name=&quot;\u5947\u5b89\u4fe1&quot;				\u641c\u7d22ICP\u5907\u6848\u7f51\u7ad9\u540d\u4e2d\u542b\u6709\u201c\u5947\u5b89\u4fe1&quot;\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">icp.type=&quot;\u4f01\u4e1a&quot;				\u641c\u7d22ICP\u5907\u6848\u4e3b\u4f53\u4e3a\u201c\u4f01\u4e1a&quot;\u7684\u8d44\u4ea7"
                        "</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">icp.name=&quot;\u5947\u5b89\u4fe1&quot;				\u641c\u7d22ICP\u5907\u6848\u5355\u4f4d\u540d\u4e2d\u542b\u6709\u201c\u5947\u5b89\u4fe1&quot;\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">icp.number=&quot;\u4eacICP\u590716020626\u53f7-8\u2033			\u641c\u7d22\u901a\u8fc7\u57df\u540d\u5173\u8054\u7684ICP\u5907\u6848\u53f7\u4e3a&quot;\u4eacICP\u590716020626\u53f7-8&quot;\u7684\u7f51\u7ad9\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0p"
                        "x; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">domain=&quot;qq.com&quot;				\u641c\u7d22\u57df\u540d\u5305\u542b&quot;qq.com&quot;\u7684\u7f51\u7ad9</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">domain.suffix=&quot;qq.com&quot;				\u641c\u7d22\u4e3b\u57df\u4e3aqq.com\u7684\u7f51\u7ad9</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">is_domain=true				\u641c\u7d22\u57df\u540d"
                        "\u6807\u8bb0\u4e0d\u4e3a\u7a7a\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">app.type=&quot;\u5f00\u53d1\u4e0e\u8fd0\u7ef4&quot;				\u67e5\u8be2\u5305\u542b\u7ec4\u4ef6\u5206\u7c7b\u4e3a&quot;\u5f00\u53d1\u4e0e\u8fd0\u7ef4&quot;\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">app.name=&quot;\u5c0f\u7c73 Router&quot;				\u641c\u7d22\u6807\u8bb0\u4e3a&quot;\u5c0f\u7c73 Router\u201c\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margi"
                        "n-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">app.vendor=&quot;PHP&quot;				\u67e5\u8be2\u5305\u542b\u7ec4\u4ef6\u5382\u5546\u4e3a&quot;PHP&quot;\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">app.version=&quot;1.8.1\u2033				\u67e5\u8be2\u5305\u542b\u7ec4\u4ef6\u7248\u672c\u4e3a&quot;1.8.1\u2033\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">header=&quot;ela"
                        "stic&quot;				\u641c\u7d22HTTP\u8bf7\u6c42\u5934\u4e2d\u542b\u6709&quot;elastic\u201c\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">header.status_code=&quot;402\u2033				\u641c\u7d22HTTP\u8bf7\u6c42\u8fd4\u56de\u72b6\u6001\u7801\u4e3a&quot;402&quot;\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">header.server==&quot;Microsoft-IIS/10\u2033			\u641c\u7d22server\u5168\u540d\u4e3a\u201cMicrosoft-IIS/10&quot;\u7684\u670d\u52a1\u5668</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bo"
                        "ttom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">header.content_length=&quot;691\u2033			\u641c\u7d22HTTP\u6d88\u606f\u4e3b\u4f53\u7684\u5927\u5c0f\u4e3a691\u7684\u7f51\u7ad9</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">web.body=&quot;\u7f51\u7edc\u7a7a\u95f4\u6d4b\u7ed8&quot;				\u641c\u7d22\u7f51\u7ad9\u6b63\u6587\u5305\u542b&quot;\u7f51\u7edc\u7a7a\u95f4\u6d4b\u7ed8\u201c\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0p"
                        "x; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">web.title=&quot;\u5317\u4eac&quot;				\u4ece\u7f51\u7ad9\u6807\u9898\u4e2d\u641c\u7d22\u201c\u5317\u4eac&quot;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">web.similar_icon==&quot;17262739310191283300\u2033		\u67e5\u8be2\u7f51\u7ad9icon\u4e0e\u8be5icon\u76f8\u4f3c\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">web.icon=&quot;22eeab765346f14faf564a4709f98548\u2033		\u67e5\u8be2\u7f51\u7ad9icon\u4e0e\u8be5icon\u76f8\u540c\u7684\u8d44\u4ea7<"
                        "/p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">web.similar_id=&quot;3322dfb483ea6fd250b29de488969b35\u2033		\u67e5\u8be2\u4e0e\u8be5\u7f51\u9875\u76f8\u4f3c\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">web.similar=&quot;baidu.com:443\u2033			\u67e5\u8be2\u4e0ebaidu.com:443\u7f51\u7ad9\u7684\u7279\u5f81\u76f8\u4f3c\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" marg"
                        "in-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">after=&quot;2021-01-01\u2033 &amp;&amp; before=&quot;2021-12-21\u2033		\u641c\u7d222021\u5e74\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">cert=&quot;baidu&quot;					\u641c\u7d22\u8bc1\u4e66\u4e2d\u5e26\u6709baidu\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">protocol=&quot;http&quot;				\u641c\u7d22\u534f\u8bae\u4e3a&quot;http\u201c\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:emp"
                        "ty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">protocol.transport=&quot;udp&quot;				\u641c\u7d22\u4f20\u8f93\u5c42\u534f\u8bae\u4e3a&quot;udp\u201c\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">protocol.banner=&quot;nginx&quot;				\u67e5\u8be2\u7aef\u53e3\u54cd\u5e94\u4e2d\u5305\u542b&quot;nginx&quot;\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin"
                        "-right:0px; -qt-block-indent:0; text-indent:0px;\">as.number=&quot;136800\u2033				\u641c\u7d22asn\u4e3a&quot;136800\u2033\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">as.name=&quot;CLOUDFLARENET&quot;				\u641c\u7d22asn\u540d\u79f0\u4e3a&quot;CLOUDFLARENET&quot;\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">as.org=&quot;PDR&quot;					\u641c\u7d22asn\u6ce8\u518c\u673a\u6784\u4e3a&quot;PDR&quot;\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; marg"
                        "in-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ip=&quot;1.1.1.1\u2033					\u641c\u7d22IP\u4e3a &quot;1.1.1.1&quot;\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ip=&quot;220.181.111.1/24\u2033				\u641c\u7d22\u8d77\u59cbIP\u4e3a&quot;220.181.111.1\u201c\u7684C\u6bb5\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ip.port_count&gt;&quot;2\u2033				\u641c"
                        "\u7d22\u5f00\u653e\u7aef\u53e3\u5927\u4e8e2\u7684IP\uff08\u652f\u6301\u7b49\u4e8e\u3001\u5927\u4e8e\u3001\u5c0f\u4e8e\uff09</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">app=&quot;Hikvision \u6d77\u5eb7\u5a01\u89c6 Firmware 5.0+&quot; &amp;&amp; ip.ports=&quot;8000\u2033	\u68c0\u7d22\u4f7f\u7528\u4e86Hikvision\u4e14ip\u5f00\u653e8000\u7aef\u53e3\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ip.ports=&quot;80\u2033 &amp;&amp; ip.ports=&quot;443\u2033			\u67e5\u8be2\u5f00\u653e\u4e8680\u548c443\u7aef\u53e3\u53f7\u7684"
                        "\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ip.port=&quot;6379\u2033				\u641c\u7d22\u5f00\u653e\u7aef\u53e3\u4e3a&quot;6379\u201c\u7684\u8d44\u4ea7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">	</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ip.isp=&quot;\u7535\u4fe1&quot;					\u641c\u7d22\u8fd0\u8425\u5546\u4e3a&quot;\u4e2d\u56fd\u7535\u4fe1&quot;\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0p"
                        "x; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ip.country=&quot;CN&quot; \u6216 ip.country=&quot;\u4e2d\u56fd&quot;			\u641c\u7d22IP\u5bf9\u5e94\u4e3b\u673a\u6240\u5728\u56fd\u4e3a&quot;\u4e2d\u56fd\u201c\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ip.province=&quot;\u6c5f\u82cf&quot;				\u641c\u7d22IP\u5bf9\u5e94\u4e3b\u673a\u5728\u6c5f\u82cf\u7701\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ip.city=&quot;\u5317\u4eac&quot;				\u641c\u7d22IP\u5bf9\u5e94\u4e3b\u673a\u6240\u5728\u57ce"
                        "\u5e02\u4e3a&quot;\u5317\u4eac\u201c\u5e02\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ip.os=&quot;Windows&quot;				\u641c\u7d22\u64cd\u4f5c\u7cfb\u7edf\u6807\u8bb0\u4e3a&quot;Windows\u201c\u7684\u8d44\u4ea7</p></body></html>", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_9), QCoreApplication.translate("MainWindow", u"Hunter\u8bed\u6cd5", None))
        self.textBrowser_7.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">city:\u57ce\u5e02\u540d\u79f0			\u57ce\u5e02\u7684\u540d\u79f0			city:&quot;Beijing&quot;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">country:\u56fd\u5bb6\u6216\u8005\u5730\u533a\u4ee3\u7801		\u56fd\u5bb6\u7684\u7b80\u79f0			country:&quot;CN&quot;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0p"
                        "x; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">geo:\u7ecf\u7eac\u5ea6			\u7ecf\u7eac\u5ea6			geo:&quot;46.9481, 7.4474</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">hostname:\u4e3b\u673a\u540d		\u4e3b\u673a\u540d\u6216\u8005\u57df\u540d		hostname:&quot;baidu.com&quot;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ip:IP\u5730\u5740			IP\u5730\u5740			ip:&quot;11.11.11.1"
                        "1&quot;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">isp:ISP\u4f9b\u5e94\u5546			ISP\u4f9b\u5e94\u5546			isp:&quot;China Telecom&quot;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">org:\u7ec4\u7ec7\u6216\u8005\u516c\u53f8		\u7ec4\u7ec7\u6216\u8005\u516c\u53f8			org:&quot;baidu&quot;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -"
                        "qt-block-indent:0; text-indent:0px;\">os:\u64cd\u4f5c\u7cfb\u7edf			\u64cd\u4f5c\u7cfb\u7edf			os:&quot;Windows 7 or 8&quot;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">port:\u7aef\u53e3\u53f7			\u7aef\u53e3\u53f7			port:80</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">net:CIDR\u683c\u5f0f\u7684IP\u5730\u5740		CIDR\u683c\u5f0f\u7684IP\u5730\u5740		net:&quot;190.30.40.0/24&quot;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"
                        "<br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">version:\u8f6f\u4ef6\u7248\u672c\u53f7		\u8f6f\u4ef6\u7248\u672c			version:&quot;4.4.2&quot;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">http.server:\u670d\u52a1\u7c7b\u578b		http\u8bf7\u6c42\u8fd4\u56de\u4e2dserver\u7684\u7c7b\u578b		http:server:apache</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">http.status:\u8bf7\u6c42\u72b6\u6001\u7801		http\u8bf7\u6c42\u8fd4\u56de\u54cd\u5e94\u7801\u7684\u72b6"
                        "\u6001		http.status:200</p></body></html>", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_10), QCoreApplication.translate("MainWindow", u"Shodan\u8bed\u6cd5", None))
        self.textBrowser_8.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u641c\u7d22 country:C hina country:CN \u90fd\u53ef\u4ee5			country:&quot;China&quot;  || country:&quot;CN&quot;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u7528\u4e8e\u641c\u7d22\u4e2d\u6587\u56fd\u5bb6\u540d\u79f0				country_cn:&quot;\u4e2d\u56fd&quot;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-"
                        "bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u7528\u4e8e\u641c\u7d22\u82f1\u6587\u7701\u4efd\u540d\u79f0				province:&quot;Sichuan&quot;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u7528\u4e8e\u641c\u7d22\u4e2d\u6587\u7701\u4efd\u540d\u79f0				province_cn:&quot;\u56db\u5ddd&quot;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u7528\u4e8e\u641c\u7d22\u82f1"
                        "\u6587\u57ce\u5e02\u540d\u79f0				city:&quot;Chengdu&quot;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u7528\u4e8e\u641c\u7d22\u4e2d\u6587\u57ce\u5e02\u540d\u79f0				city_cn:&quot;\u6210\u90fd&quot;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u8fd9\u91cc\u7684\u5f52\u5c5e\u5e76\u4e0d\u7cbe\u786e\uff0c\u540e\u671fQuake\u4f1a\u63a8\u51fa\u5355\u4f4d\u5f52\u5c5e\u4e13\u7528\u5173\u952e\u8bcd		owner: &quot;tencent.com&quot; owner: &quot;\u6e05\u534e\u5927\u5b66&quot;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; ma"
                        "rgin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u6839\u636eIP\u5212\u5206\u5f52\u5c5e\u7684\u8fd0\u8425\u5546				isp: &quot;\u8054\u901a&quot;	|| isp: &quot;amazon.com&quot;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u7528\u4e8e\u641c\u7d22\u56fe\u7247\u7684\u6807\u7b7e				img_tag: &quot;windows&quot;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u7528"
                        "\u4e8e\u641c\u7d22\u56fe\u7247\u4e2d\u7684\u4fe1\u606f				img_ocr:&quot;admin&quot;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u7528\u4e8e\u641c\u7d22IP\u8d44\u4ea7\u7684\u5e94\u7528\u573a\u666f\uff0c\u5982\uff1aCDN\u3001\u536b\u661f\u4e92\u8054\u7f51\u3001IDC\u673a\u623f\u7b49	sys_tag:&quot;\u536b\u661f\u4e92\u8054\u7f51&quot;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u652f\u6301\u68c0\u7d22\u5355\u4e2aIP\u3001CIDR\u5730\u5740\u6bb5\u3001\u652f\u6301IPv6\u5730\u5740		ip:&quot;1.1.1.1&quot; || ip: &quot;1.1.1.1/16&quot;</p"
                        ">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u53ea\u63a5\u53d7 true \u548c false				is_ipv6:&quot;true&quot;\uff1a\u67e5\u8be2IPv6\u6570\u636e || is_ipv6:&quot;false&quot;\uff1a\u67e5\u8be2IPv4\u6570\u636e</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u53ea\u63a5\u53d7 true \u548c false				is_latest :&quot;true&quot;\uff1a\u67e5\u8be2\u6700\u65b0\u7684\u8d44\u4ea7\u6570\u636e</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br"
                        " /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u641c\u7d22\u5f00\u653e\u7684\u7aef\u53e3				port:&quot;80&quot;\uff1a\u67e5\u8be2\u5f00\u653e80\u7aef\u53e3\u7684\u4e3b\u673a</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u641c\u7d22\u67d0\u4e2a\u4e3b\u673a\u540c\u65f6\u5f00\u653e\u8fc7\u7684\u7aef\u53e3			ports:&quot;80,8080,8000&quot;\uff1a\u67e5\u8be2\u540c\u65f6\u5f00\u653e\u8fc780\u30018080\u30018000\u7aef\u53e3\u7684\u4e3b\u673a</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-b"
                        "lock-indent:0; text-indent:0px;\">\u641c\u7d22\u6ee1\u8db3\u67d0\u4e2a\u7aef\u53e3\u8303\u56f4\u7684\u4e3b\u673a				port:[* TO 80]\uff1a\u67e5\u8be2\u5f00\u653e\u7aef\u53e3\u5c0f\u4e8e\u7b49\u4e8e80\u7684\u4e3b\u673a</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u53ea\u63a5\u53d7tcp\u3001udp				transport:&quot;tcp&quot;\uff1a\u67e5\u8be2tcp\u6570\u636e || transport:&quot;udp&quot;\uff1a\u67e5\u8be2udp\u6570\u636e</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u81ea\u6cbb\u57df\u5f52\u5c5e\u7ec4\u7ec7\u540d\u79f0				org:&quot;No.31"
                        ",Jin-rong Street&quot;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u81ea\u6cbb\u57df\u53f7\u7801					asn:&quot;12345&quot;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u5373rDNS\u6570\u636e					hostname:&quot;50-87-74-222.unifiedlayer.com&quot;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"
                        "\">\u7f51\u7ad9\u57df\u540d\u4fe1\u606f					domain:&quot;360.cn&quot; || domain:*.360.cn</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u64cd\u4f5c\u7cfb\u7edf\u540d\u79f0+\u7248\u672c				os:&quot;Windows&quot;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u5373\u5e94\u7528\u534f\u8bae\u540d\u79f0				service:&quot;http&quot;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-botto"
                        "m:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u641c\u7d22\u67d0\u4e2a\u4e3b\u673a\u540c\u65f6\u652f\u6301\u7684\u534f\u8bae\u4ec5\u5728 \u4e3b\u673a\u6570\u636e\u6a21\u5f0f\u4e0b\u53ef\u7528		services:&quot;rtsp,https,telnet&quot;\uff1a\u652f\u6301rtsp\u3001https\u3001telnet\u7684\u4e3b\u673a</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u7ecf\u8fc7Quake\u6307\u7eb9\u8bc6\u522b\u540e\u7684\u4ea7\u54c1\u540d\u79f0\uff08\u672a\u6765\u4f1a\u88ab\u7cbe\u7ec6\u5316\u8bc6\u522b\u4ea7\u54c1\u66ff\u4ee3\uff09	app:&quot;Apache&quot;Apache\u670d\u52a1\u5668\u4ea7\u54c1</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style="
                        "\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u7ecf\u8fc7Quake\u6307\u7eb9\u8bc6\u522b\u540e\u7684\u4ea7\u54c1\u7248\u672c			app_version:&quot;1.2.1&quot;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u8fd9\u91cc\u662f\u5305\u542b\u7aef\u53e3\u4fe1\u606f\u6700\u4e30\u5bcc\u7684\u5730\u65b9			response:&quot;\u5947\u864e\u79d1\u6280&quot;\uff1a\u7aef\u53e3\u539f\u751f\u8fd4\u56de\u6570\u636e\u4e2d\u5305\u542b&quot;\u5947\u864e\u79d1\u6280&quot;\u7684\u4e3b\u673a</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0p"
                        "x; -qt-block-indent:0; text-indent:0px;\">\u8fd9\u91cc\u5b58\u653e\u4e86\u683c\u5f0f\u89e3\u6790\u540e\u7684\u8bc1\u4e66\u4fe1\u606f\u5b57\u7b26\u4e32			cert:&quot;\u5947\u864e\u79d1\u6280&quot;\uff1a\u5305\u542b&quot;\u5947\u864e\u79d1\u6280&quot;\u7684\u8bc1\u4e66</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u8be5\u5b57\u6bb5\u662f\u5e94\u7528\u7c7b\u578b\u7684\u96c6\u5408\uff0c\u662f\u4e00\u4e2a\u66f4\u9ad8\u5c42\u9762\u5e94\u7528\u7684\u805a\u5408		catalog:&quot;IoT\u7269\u8054\u7f51&quot;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-inde"
                        "nt:0px;\">\u8be5\u5b57\u6bb5\u662f\u5bf9\u5e94\u7528\u8fdb\u884c\u7684\u5206\u7c7b\u7ed3\u679c\uff0c\u6307\u4e00\u7c7b\u7528\u9014\u76f8\u540c\u7684\u8d44\u4ea7		type:&quot;\u9632\u706b\u5899&quot; || type:&quot;VPN&quot;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u5bf9\u4e8e\u6240\u6709\u5e94\u7528\u8fdb\u884c\u5206\u7ea7 				level:&quot;\u786c\u4ef6\u8bbe\u5907\u5c42&quot; || level:&quot;\u5e94\u7528\u4e1a\u52a1\u5c42&quot;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u8be5\u5b57\u6bb5\u6307\u67d0\u4e2a\u5e94\u7528\u8bbe\u5907"
                        "\u7684\u751f\u4ea7\u5382\u5546			vendor:&quot;Sangfor\u6df1\u4fe1\u670d\u79d1\u6280\u80a1\u4efd\u6709\u9650\u516c\u53f8&quot;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0p"
                        "x; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_11), QCoreApplication.translate("MainWindow", u"Quake\u8bed\u6cd5", None))
        self.textBrowser_9.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">app\uff1a\u7ec4\u4ef6\u540d			\u76ee\u6807\u7ec4\u4ef6\u540d\u79f0			app:&quot;Apache httpd&quot;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ver\uff1a\u7ec4\u4ef6\u7248\u672c			\u76ee\u6807\u7ec4\u4ef6\u7248\u672c\u53f7		ver:'2.2.17'</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-lef"
                        "t:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">port\uff1a\u7aef\u53e3\u53f7			\u76ee\u6807\u7cfb\u7edf\u5f00\u53d1\u7aef\u53e3		port:'6379'</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">os\uff1a\u64cd\u4f5c\u7cfb\u7edf			\u76ee\u6807\u64cd\u4f5c\u7cfb\u7edf\u7c7b\u578b		os:linux</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">service\uff1a\u670d\u52a1\u540d		\u76ee\u6807\u8fd0\u884c\u7684"
                        "\u670d\u52a1\u7c7b\u578b		service:webcam</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">hostname\uff1a\u4e3b\u673a\u540d		\u76ee\u6807\u7cfb\u7edf\u7684\u4e3b\u673a\u540d		hostname:google.com</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">country\uff1a\u56fd\u5bb6/\u5730\u533a\u4ee3\u7801		\u76ee\u6807\u7cfb\u7edf\u7684\u5730\u7406\u4f4d\u7f6e		country:CN</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" "
                        "margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">city\uff1a\u57ce\u5e02			\u76ee\u6807\u7cfb\u7edf\u7684\u57ce\u5e02		city:'Shanghai'</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ip\uff1aIP\u5730\u5740			IP\u5730\u5740			ip:10.10.10.1</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">org\uff1a\u7ec4\u7ec7\u673a\u6784			\u7ec4\u7ec7\u673a\u6784			org:'Vimpelcom'</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -"
                        "qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">asn\uff1a\u81ea\u6cbb\u7cfb\u7edf\u53f7		\u81ea\u6cbb\u7cfb\u7edf\u7f16\u53f7			asn:42893</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ssl\uff1aSSL\u8bc1\u4e66\u53f7		SSL\u8bc1\u4e66			ssl:'corp.google.com'</p></body></html>", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_12), QCoreApplication.translate("MainWindow", u"Zoomeye\u8bed\u6cd5", None))
        self.textBrowser_10.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">23.0.0.0/8 or 8.8.8.0/24\u3000\u3000			\u53ef\u4ee5\u4f7f\u7528and or not</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'-apple-system','SF UI Text','Arial','PingFang SC','Hiragino Sans GB','Microsoft YaHei','WenQuanYi Micro Hei','sans-serif','SimHei','SimSun'; color:#4d4d4d;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">80.http.get.status_code: 200\u3000\u3000"
                        "			\u6307\u5b9a\u72b6\u6001</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'-apple-system','SF UI Text','Arial','PingFang SC','Hiragino Sans GB','Microsoft YaHei','WenQuanYi Micro Hei','sans-serif','SimHei','SimSun'; color:#4d4d4d;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">80.http.get.status_code:[200 TO 300]\u3000\u3000		200-300\u4e4b\u95f4\u7684\u72b6\u6001\u7801</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'-apple-system','SF UI Text','Arial','PingFang SC','Hiragino Sans GB','Microsoft YaHei','WenQuanYi Micro Hei','sans-serif','SimHei','SimSun'; color:#4d4d4d;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text"
                        "-indent:0px;\">location.country_code: DE\u3000\u3000			\u56fd\u5bb6</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'-apple-system','SF UI Text','Arial','PingFang SC','Hiragino Sans GB','Microsoft YaHei','WenQuanYi Micro Hei','sans-serif','SimHei','SimSun'; color:#4d4d4d;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">protocols: (\u201c23/telnet\u201d or \u201c21/ftp\u201d)\u3000\u3000		\u534f\u8bae</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'-apple-system','SF UI Text','Arial','PingFang SC','Hiragino Sans GB','Microsoft YaHei','WenQuanYi Micro Hei','sans-serif','SimHei','SimSun'; color:#4d4d4d;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:"
                        "0px; -qt-block-indent:0; text-indent:0px;\">tags: scada\u3000\u3000				\u6807\u7b7e</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'-apple-system','SF UI Text','Arial','PingFang SC','Hiragino Sans GB','Microsoft YaHei','WenQuanYi Micro Hei','sans-serif','SimHei','SimSun'; color:#4d4d4d;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">80.http.get.headers.server\uff1anginx\u3000\u3000			\u670d\u52a1\u5668\u7c7b\u578b\u7248\u672c</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'-apple-system','SF UI Text','Arial','PingFang SC','Hiragino Sans GB','Microsoft YaHei','WenQuanYi Micro Hei','sans-serif','SimHei','SimSun'; color:#4d4d4d;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; ma"
                        "rgin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">autonomous_system.description: University\u3000 		\u7cfb\u7edf\u63cf\u8ff0\u6b63\u5219</p></body></html>", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_14), QCoreApplication.translate("MainWindow", u"Censys\u8bed\u6cd5", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u8bed\u6cd5", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"FOFA\u8bed\u6cd5\uff1a", None))
        self.button.setText(QCoreApplication.translate("MainWindow", u"FOFA\u67e5\u8be2", None))
        self.fofa_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165FOFA\u8bed\u6cd5", None))
        self.num.setItemText(0, QCoreApplication.translate("MainWindow", u"10000", None))
        self.num.setItemText(1, QCoreApplication.translate("MainWindow", u"5000", None))
        self.num.setItemText(2, QCoreApplication.translate("MainWindow", u"2000", None))
        self.num.setItemText(3, QCoreApplication.translate("MainWindow", u"1000", None))
        self.num.setItemText(4, QCoreApplication.translate("MainWindow", u"100", None))

        self.clear.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u7ed3\u679c", None))
        self.export_2.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u6570\u636e", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"0 \u6761", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"ICON_HASH\uff1a", None))
        self.ico_hash.setPlaceholderText(QCoreApplication.translate("MainWindow", u"https://www.baidu.com/favicon.ico", None))
        self.button_4.setText(QCoreApplication.translate("MainWindow", u"ICON\u67e5\u8be2", None))
        self.textBrowser.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8fd4\u56de\u7ed3\u679c\uff1aicon_hash=\"-1588080585\"", None))
        self.shuchu.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u6ce8\u610f\uff1a                        1.\u6700\u9ad8\u652f\u6301\u67e5\u8be210000\u6761\uff0c\u5bfc\u51fa\u540e\u81ea\u52a8\u53bb\u91cd                        2.\u652f\u6301\u67e5\u8be2ICON\uff0c\u8fd4\u56de\u7ed3\u679c\u518d\u653e\u5165FOFA\u8bed\u6cd5\u4e2d\u67e5\u8be2\u5373\u53ef", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"\u65e5\u5fd7\uff1a", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22\u7ed3\u679c\uff1a", None))
        self.clearrizi.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u65e5\u5fd7", None))
        ___qtablewidgetitem = self.fofa.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Host", None));
        ___qtablewidgetitem1 = self.fofa.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"IP", None));
        ___qtablewidgetitem2 = self.fofa.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Port", None));
        ___qtablewidgetitem3 = self.fofa.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Title", None));
        ___qtablewidgetitem4 = self.fofa.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Domain", None));
        ___qtablewidgetitem5 = self.fofa.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Country", None));
        ___qtablewidgetitem6 = self.fofa.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Protocol", None));
        ___qtablewidgetitem7 = self.fofa.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Server", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"FOFA", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"0 \u6761", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u9e70\u56fe\u8bed\u6cd5\uff1a", None))
        self.button_2.setText(QCoreApplication.translate("MainWindow", u"Hunter\u67e5\u8be2", None))
        self.clear_2.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u7ed3\u679c", None))
        self.hunter_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u9e70\u56fe\u8bed\u6cd5", None))
        self.export_3.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u6570\u636e", None))
        self.num_2.setItemText(0, QCoreApplication.translate("MainWindow", u"10", None))
        self.num_2.setItemText(1, QCoreApplication.translate("MainWindow", u"20", None))
        self.num_2.setItemText(2, QCoreApplication.translate("MainWindow", u"50", None))
        self.num_2.setItemText(3, QCoreApplication.translate("MainWindow", u"100", None))

        self.num_2.setCurrentText(QCoreApplication.translate("MainWindow", u"20", None))
        ___qtablewidgetitem8 = self.hunter_tab.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Host", None));
        ___qtablewidgetitem9 = self.hunter_tab.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"IP", None));
        ___qtablewidgetitem10 = self.hunter_tab.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Port", None));
        ___qtablewidgetitem11 = self.hunter_tab.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Title", None));
        ___qtablewidgetitem12 = self.hunter_tab.horizontalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Domain", None));
        ___qtablewidgetitem13 = self.hunter_tab.horizontalHeaderItem(5)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Protocol", None));
        ___qtablewidgetitem14 = self.hunter_tab.horizontalHeaderItem(6)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Status_code", None));
        ___qtablewidgetitem15 = self.hunter_tab.horizontalHeaderItem(7)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Company", None));
        ___qtablewidgetitem16 = self.hunter_tab.horizontalHeaderItem(8)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Country", None));
        ___qtablewidgetitem17 = self.hunter_tab.horizontalHeaderItem(9)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Updated_at", None));
        ___qtablewidgetitem18 = self.hunter_tab.horizontalHeaderItem(10)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"isp", None));
        self.xiaohao.setText(QCoreApplication.translate("MainWindow", u"\u6d88\u8017\u79ef\u5206\uff1a", None))
        self.shengyu.setText(QCoreApplication.translate("MainWindow", u"\u4eca\u65e5\u5269\u4f59\u79ef\u5206\uff1a", None))
        self.hunter_page.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.hunter_page.setPlaceholderText("")
        self.clearrizi_2.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u65e5\u5fd7", None))
        self.shuchu_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.shuchu_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u6ce8\u610f\uff1a                        1.\u9ed8\u8ba4\u5c55\u793a20\u6761\u6570\u636e\uff0c\u6700\u9ad8100\u6761 2.\u53ef\u4ee5\u81ea\u5df1\u8f93\u5165\u9875\u7801\uff0c\u9ed8\u8ba4\u7b2c\u4e00\u9875 3.\u5f53\u65e5\u91cd\u590d\u67e5\u8be2\u7684\u8bed\u53e5\uff0c\u4e0d\u4f1a\u7d2f\u8ba1\u6263\u79ef\u5206", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"\u65e5\u5fd7\uff1a", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22\u7ed3\u679c\uff1a", None))
        self.num_3.setItemText(0, QCoreApplication.translate("MainWindow", u"web\u8d44\u4ea7", None))
        self.num_3.setItemText(1, QCoreApplication.translate("MainWindow", u"\u975eweb\u8d44\u4ea7", None))
        self.num_3.setItemText(2, QCoreApplication.translate("MainWindow", u"\u5168\u90e8", None))

        self.num_3.setCurrentText(QCoreApplication.translate("MainWindow", u"web\u8d44\u4ea7", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u8d44\u4ea7\u7c7b\u578b\uff1a", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u9875\u7801\uff1a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Hunter", None))
        self.shodan_search1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165SHODAN\u8bed\u6cd5", None))
        self.export_4.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u6570\u636e", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"0 \u6761", None))
        ___qtablewidgetitem19 = self.shodan_tab.horizontalHeaderItem(0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"IP", None));
        ___qtablewidgetitem20 = self.shodan_tab.horizontalHeaderItem(1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Port", None));
        ___qtablewidgetitem21 = self.shodan_tab.horizontalHeaderItem(2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Domain", None));
        ___qtablewidgetitem22 = self.shodan_tab.horizontalHeaderItem(3)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"OS", None));
        ___qtablewidgetitem23 = self.shodan_tab.horizontalHeaderItem(4)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Country", None));
        ___qtablewidgetitem24 = self.shodan_tab.horizontalHeaderItem(5)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Org", None));
        ___qtablewidgetitem25 = self.shodan_tab.horizontalHeaderItem(6)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"isp", None));
        ___qtablewidgetitem26 = self.shodan_tab.horizontalHeaderItem(7)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"last_update", None));
        self.clear_3.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u7ed3\u679c", None))
        self.button_3.setText(QCoreApplication.translate("MainWindow", u"Shodan\u67e5\u8be2", None))
        self.shodan_page.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.shodan_page.setPlaceholderText("")
        self.clearrizi_3.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u65e5\u5fd7", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"\u65e5\u5fd7\uff1a", None))
        self.shuchu_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.shuchu_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u6ce8\u610f\uff1a                  1.shodan\u641c\u7d22\u901f\u5ea6\u53ef\u80fd\u6bd4\u5176\u4ed6\u7684\u7a7a\u95f4\u6d4b\u7ed8\u6162\u4e00\u4e9b\uff0c\u70b9\u51fb\u67e5\u8be2\u540e\u6ca1\u5fc5\u8981\u518d\u6b21\u70b9\u51fb\u67e5\u8be2\uff0c\u8bf7\u8010\u5fc3\u7b49\u5f85\u5373\u53ef   2.\u9ed8\u8ba4\u5c55\u793a100\u6761\uff0c\u53ef\u7ffb\u9875       3.\u641c\u7d22\u65b9\u6cd5\uff1a\u5982\u679c\u9700\u8981\u641c\u7d22shodan\u8bed\u53e5\u9009\u62e9HOST\u65b9\u6cd5\uff0c\u5982\u679c\u9700\u8981\u641c\u7d22IP\u9009\u62e9IP\u5373\u53ef\uff0c\u9009\u9519\u53ef\u80fd\u4f1a\u5f71\u54cd\u5230\u641c\u7d22\u7ed3\u679c", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22\u7ed3\u679c\uff1a", None))
        self.num_4.setItemText(0, QCoreApplication.translate("MainWindow", u"HOST", None))
        self.num_4.setItemText(1, QCoreApplication.translate("MainWindow", u"IP", None))

        self.num_4.setCurrentText(QCoreApplication.translate("MainWindow", u"HOST", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Shodan\u8bed\u6cd5\uff1a", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22\u65b9\u6cd5\uff1a", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u9875\u7801\uff1a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Shodan", None))
        self.clearrizi_7.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u65e5\u5fd7", None))
        self.shuchu_7.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.shuchu_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u6ce8\u610f\uff1a                        1.\u6682\u4e0d\u652f\u6301\u76f4\u63a5\u67e5\u8be2\u57df\u540d\uff0c\u652f\u6301Quake\u5176\u4ed6\u8bed\u6cd5                 2.\u5c55\u793a\u7ed3\u679c\u5747\u4e3a\u53bb\u91cd\u540e\u7684\u7ed3\u679c\uff0c\u4e00\u6b21\u6027\u6700\u591a\u67e5\u8be2499\u6761\u6570\u636e", None))
        self.quake_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165Quake\u8bed\u6cd5", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22\u7ed3\u679c\uff1a", None))
        ___qtablewidgetitem27 = self.quake_tab.horizontalHeaderItem(0)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"IP", None));
        ___qtablewidgetitem28 = self.quake_tab.horizontalHeaderItem(1)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Port", None));
        ___qtablewidgetitem29 = self.quake_tab.horizontalHeaderItem(2)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Title", None));
        ___qtablewidgetitem30 = self.quake_tab.horizontalHeaderItem(3)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Status_code", None));
        ___qtablewidgetitem31 = self.quake_tab.horizontalHeaderItem(4)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Location", None));
        ___qtablewidgetitem32 = self.quake_tab.horizontalHeaderItem(5)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Org", None));
        ___qtablewidgetitem33 = self.quake_tab.horizontalHeaderItem(6)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Hostname", None));
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"\u65e5\u5fd7\uff1a", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Quake\u8bed\u6cd5\uff1a", None))
        self.button_9.setText(QCoreApplication.translate("MainWindow", u"Quake\u67e5\u8be2", None))
        self.clear_7.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u7ed3\u679c", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"0 \u6761", None))
        self.export_8.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u6570\u636e", None))
        self.num_10.setItemText(0, QCoreApplication.translate("MainWindow", u"20", None))
        self.num_10.setItemText(1, QCoreApplication.translate("MainWindow", u"10", None))
        self.num_10.setItemText(2, QCoreApplication.translate("MainWindow", u"50", None))
        self.num_10.setItemText(3, QCoreApplication.translate("MainWindow", u"100", None))
        self.num_10.setItemText(4, QCoreApplication.translate("MainWindow", u"200", None))
        self.num_10.setItemText(5, QCoreApplication.translate("MainWindow", u"499", None))

        self.num_10.setCurrentText(QCoreApplication.translate("MainWindow", u"20", None))
        self.xiaohao_4.setText(QCoreApplication.translate("MainWindow", u"\u672c\u6708\u5269\u4f59\u79ef\u5206\uff1a", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"\u9875\u7801\u5927\u5c0f\uff1a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Quake", None))
        self.shengyu_2.setText(QCoreApplication.translate("MainWindow", u"\u672c\u6708\u5269\u4f59\u79ef\u5206\uff1a", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u8d44\u4ea7\u7c7b\u578b\uff1a", None))
        self.shuchu_4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.shuchu_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u6ce8\u610f\uff1a                        1.\u9009\u62e9\u7684\u8d44\u4ea7\u7c7b\u578b\u6bd4\u5982\u662f\u201c\u4e3b\u673a\u8bbe\u5907\u201d\uff0c\u4f60\u5bfc\u51fa\u7684\u65f6\u5019\u4e5f\u5fc5\u987b\u9009\u62e9\u5bfc\u51fa\u201c\u4e3b\u673a\u8bbe\u5907\u201d \u5982\u679c\u9009\u4e86\u53e6\u4e00\u9879\u7cfb\u7edf\u7b2c\u4e00\u6b21\u5219\u4f1a\u81ea\u52a8\u63d0\u793a\uff0c\u7b2c\u4e8c\u6b21\u5219\u4e0d\u4f1a\u63d0\u793a\u76f4\u5230\u9000\u51fa\u540e\u91cd\u65b0\u8fdb\u5165     2.\u5173\u8054\u57df\u540d\u3001\u5b50\u57df\u540d\u9ed8\u8ba4\u67e5\u8be230\u6761\uff0c\u4e3b\u673a\u8bbe\u5907\u9ed8\u8ba4\u67e5\u8be220\u6761\uff0c\u53ef\u7ffb\u9875", None))
        ___qtablewidgetitem34 = self.zoomeye_tab.horizontalHeaderItem(0)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"IP", None));
        ___qtablewidgetitem35 = self.zoomeye_tab.horizontalHeaderItem(1)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Port", None));
        ___qtablewidgetitem36 = self.zoomeye_tab.horizontalHeaderItem(2)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Service", None));
        ___qtablewidgetitem37 = self.zoomeye_tab.horizontalHeaderItem(3)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"City", None));
        ___qtablewidgetitem38 = self.zoomeye_tab.horizontalHeaderItem(4)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"ISP", None));
        ___qtablewidgetitem39 = self.zoomeye_tab.horizontalHeaderItem(5)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"APP", None));
        ___qtablewidgetitem40 = self.zoomeye_tab.horizontalHeaderItem(6)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Org", None));
        ___qtablewidgetitem41 = self.zoomeye_tab.horizontalHeaderItem(7)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Timestamp", None));
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"\u65e5\u5fd7\uff1a", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u9875\u7801\uff1a", None))
        self.button_5.setText(QCoreApplication.translate("MainWindow", u"Zoomeye\u67e5\u8be2", None))
        self.num_6.setItemText(0, QCoreApplication.translate("MainWindow", u"\u4e3b\u673a\u8bbe\u5907", None))

        self.num_6.setCurrentText(QCoreApplication.translate("MainWindow", u"\u4e3b\u673a\u8bbe\u5907", None))
        self.zoomeye_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165Zoomeye\u8bed\u6cd5", None))
        self.zoomeye_page.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.zoomeye_page.setPlaceholderText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Zoomeye\u8bed\u6cd5\uff1a", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"0 \u6761", None))
        self.clear_4.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u7ed3\u679c", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22\u7ed3\u679c\uff1a", None))
        self.export_6.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u6570\u636e", None))
        self.clearrizi_4.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u65e5\u5fd7", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"Zoomeye", None))
        self.Censys_num.setItemText(0, QCoreApplication.translate("MainWindow", u"Hosts", None))
        self.Censys_num.setItemText(1, QCoreApplication.translate("MainWindow", u"IP", None))

        self.Censys_num.setCurrentText(QCoreApplication.translate("MainWindow", u"Hosts", None))
        ___qtablewidgetitem42 = self.Censys_tab.horizontalHeaderItem(0)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"IP", None));
        ___qtablewidgetitem43 = self.Censys_tab.horizontalHeaderItem(1)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"Domain", None));
        ___qtablewidgetitem44 = self.Censys_tab.horizontalHeaderItem(2)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"Port", None));
        ___qtablewidgetitem45 = self.Censys_tab.horizontalHeaderItem(3)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"Title", None));
        ___qtablewidgetitem46 = self.Censys_tab.horizontalHeaderItem(4)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"Protocol", None));
        ___qtablewidgetitem47 = self.Censys_tab.horizontalHeaderItem(5)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"Network", None));
        ___qtablewidgetitem48 = self.Censys_tab.horizontalHeaderItem(6)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"Country", None));
        ___qtablewidgetitem49 = self.Censys_tab.horizontalHeaderItem(7)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"Method", None));
        ___qtablewidgetitem50 = self.Censys_tab.horizontalHeaderItem(8)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"Status_Code", None));
        self.Censys_clearjieguo.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u7ed3\u679c", None))
        self.Censys_clearrizi.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u65e5\u5fd7", None))
        self.Censys_yufa.setText(QCoreApplication.translate("MainWindow", u"Censys\u8bed\u6cd5\uff1a", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22\u7ed3\u679c\uff1a", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"0 \u6761", None))
        self.Censys_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165Censys\u8bed\u6cd5", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u8d44\u4ea7\u7c7b\u578b\uff1a", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"\u65e5\u5fd7\uff1a", None))
        self.shuchu_5.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.shuchu_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u6ce8\u610f\uff1a                        1.\u4e00\u9875\u6700\u591a\u5c55\u793a100\u6761\u6570\u636e,\u53ef\u7ffb\u9875 2.\u6ce8\u610f\u8d44\u4ea7\u641c\u7d22\u7c7b\u578b", None))
        self.Censys_export.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u6570\u636e", None))
        self.Censys_search_1.setText(QCoreApplication.translate("MainWindow", u"Censys\u67e5\u8be2", None))
        self.Censys_next.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u9875", None))
        self.Censys_prev.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4e00\u9875", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_13), QCoreApplication.translate("MainWindow", u"Censys", None))
        self.save_config.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.shodan_config_2.setTitle(QCoreApplication.translate("MainWindow", u"Shodan\u914d\u7f6e", None))
        self.your_shodan_api.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u4f60\u7684SHODAN API", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"SHODAN_API\uff1a", None))
        self.shodan_xiugai.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539", None))
        self.hunter_config_2.setTitle(QCoreApplication.translate("MainWindow", u"Hunter\u914d\u7f6e", None))
        self.your_hunter_api.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u4f60\u7684\u9e70\u56feAPI", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"HUNTER_API\uff1a", None))
        self.hunter_xiugai.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"\u914d\u7f6e\u8bf4\u660e", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"\u6ce8\u610f\uff1a\n"
"\u7b2c\u4e00\u6b21\u4fdd\u5b58\u4e86API\u4e4b\u540e\uff0c\u518d\u60f3\u66ff\u6362\u65f6\uff0c\u8bf7\u70b9\u51fb\u4fee\u6539\uff0c\u8bf7\u4e0d\u8981\n"
"\u518d\u70b9\u51fb\u4fdd\u5b58\uff0c\u5982\u679c\u518d\u70b9\u51fb\u4fdd\u5b58\uff0c\u5176\u4ed6\u7684API\u5c06\u88ab\u8986\u76d6\uff0c\u5219\n"
"\u9700\u8981\u91cd\u65b0\u914d\u7f6e\n"
"\n"
"\n"
"\n"
"", None))
        self.fofa_config_3.setTitle(QCoreApplication.translate("MainWindow", u"Zoomeye\u914d\u7f6e", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Zoomeye_API\uff1a", None))
        self.your_zoomeye_api.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u4f60\u7684Zoomeye API", None))
        self.zoomeye_xiugai.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539", None))
        self.fofa_config_4.setTitle(QCoreApplication.translate("MainWindow", u"FOFA\u914d\u7f6e", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"FOFA_EMAIL\uff1a", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"FOFA_API\uff1a", None))
        self.your_fofa_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u4f60\u7684FOFA\u90ae\u7bb1", None))
        self.your_fofa_api.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u4f60\u7684FOFA API", None))
        self.fofa_xiugai.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539", None))
        self.shodan_config_4.setTitle(QCoreApplication.translate("MainWindow", u"Quake\u914d\u7f6e", None))
        self.your_quake_api.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u4f60\u7684QUAKE API", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"QUAKE_API\uff1a", None))
        self.quake_xiugai.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539", None))
        self.fofa_config_5.setTitle(QCoreApplication.translate("MainWindow", u"Censys\u914d\u7f6e", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"Censys_uid\uff1a", None))
        self.your_censys_uid.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u4f60\u7684Censys uid", None))
        self.censys_xiugai.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539", None))
        self.your_censys_secret.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u4f60\u7684Censys secret", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"Censys_secret\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u2b06\u2b06\u2b06\u7b2c\u4e00\u6b21\u914d\u7f6eAPI \u8bf7\u52a1\u5fc5\u70b9\u51fb\u4fdd\u5b58\u751f\u6548\u2b06\u2b06\u2b06", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_15), QCoreApplication.translate("MainWindow", u"Config", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Change Log", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"README", None))
        self.textBrowser_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u6ce8\uff1a</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u7b2c\u4e00\u6b21\u4f7f\u7528\u9009\u62e9\u4fdd\u5b58\uff0c\u4e4b\u540e\u9700\u8981\u4fee\u6539api\u70b9\u51fb\u4fee\u6539\u5373\u53ef\uff0c\u5982\u679c\u518d\u70b9\u51fb\u4fdd\u5b58\u5c06\u8986\u76d6\u6240\u6709\u5df2\u7ecf\u914d\u7f6e\u7684API\uff0c\u5219\u9700\u8981"
                        "\u91cd\u65b0\u518d\u914d\u7f6e</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">FOFA\uff1a</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.\u9ed8\u8ba4\u5c55\u793a10000\u6761\u6570\u636e</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:"
                        "0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2.\u652f\u6301iconhash\u67e5\u8be2\uff0c\u8f93\u51fa\u7684iconhash\u590d\u5236\u5230\u8f93\u5165\u6846\u70b9\u51fb\u67e5\u8be2\u5373\u53ef</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3.\u70b9\u51fb\u67e5\u8be2\u4f1a\u8986\u76d6\u5df2\u67e5\u8be2\u7684\u5185\u5bb9</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-b"
                        "lock-indent:0; text-indent:0px;\">\u9e70\u56fe\uff1a</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.\u9ed8\u8ba4\u5c55\u793a20\u6761\u6570\u636e\uff0c\u6700\u9ad8100\u6761 </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2.\u53ef\u4ee5\u81ea\u5df1\u8f93\u5165\u9875\u7801\uff0c\u9ed8\u8ba4\u7b2c\u4e00\u9875 </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0"
                        "px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3.\u6bcf\u6b21\u67e5\u8be2\u53ef\u4ee5\u770b\u5230\u6d88\u8017\u79ef\u5206\u548c\u5269\u4f59\u79ef\u5206</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4.\u5f53\u65e5\u91cd\u590d\u67e5\u8be2\u7684\u8bed\u53e5\uff0c\u4e0d\u4f1a\u7d2f\u8ba1\u6263\u79ef\u5206</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5.\u53ef\u4ee5\u81ea\u5df1\u9009\u62e9\u8d44\u4ea7\u7c7b\u578b\uff0c\u9ed8\u8ba4web\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px"
                        "; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">6.\u70b9\u51fb\u67e5\u8be2\u4f1a\u8986\u76d6\u5df2\u67e5\u8be2\u7684\u5185\u5bb9</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">7.\u6682\u4e0d\u652f\u6301\u67e5\u8be2iconhash\uff0c\u4e4b\u540e\u7248\u672c\u53ef\u80fd\u4f1a\u65b0\u589e</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p st"
                        "yle=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">shodan\uff1a</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.\u9ed8\u8ba4\u5c55\u793a100\u6761\uff0c\u53ef\u7ffb\u9875   </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2.shodan\u641c\u7d22\u901f\u5ea6\u53ef\u80fd\u6bd4\u5176\u4ed6\u7684\u7a7a\u95f4\u6d4b\u7ed8\u6162\u4e00\u4e9b\uff0c\u70b9\u51fb\u67e5\u8be2\u540e\u6ca1\u5fc5\u8981\u518d\u6b21\u70b9\u51fb\u67e5\u8be2\uff0c\u8bf7\u8010\u5fc3\u7b49\u5f85\u5373\u53ef   </"
                        "p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3.\u641c\u7d22\u65b9\u6cd5\uff1a\u5982\u679c\u9700\u8981\u641c\u7d22shodan\u8bed\u53e5\u9009\u62e9HOST\u65b9\u6cd5\uff0c\u5982\u679c\u9700\u8981\u641c\u7d22IP\u9009\u62e9IP\u5373\u53ef\uff0c\u9009\u9519\u53ef\u80fd\u4f1a\u5f71\u54cd\u5230\u641c\u7d22\u7ed3\u679c</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4.\u70b9\u51fb\u67e5\u8be2\u4e0d\u4f1a\u8986\u76d6\u5df2\u67e5\u8be2\u7684\u5185\u5bb9</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-i"
                        "ndent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5.\u53ea\u80fd\u5bfc\u51fa\u5df2\u67e5\u8be2\u51fa\u6765\u7684\u5185\u5bb9\uff0c\u53ef\u80fd\u4e4b\u540e\u7248\u672c\u4f1a\u89e3\u51b3</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">360 Quake</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-inde"
                        "nt:0; text-indent:0px;\">1.\u652f\u6301360 Quake\u8bed\u6cd5</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2.\u9ed8\u8ba4\u67e5\u8be220\u9875\uff0c\u6700\u5927\u67e5\u8be2499\u6761</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3.\u81ea\u52a8\u5c55\u793a\u53bb\u91cd</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                        "text-indent:0px;\">4.\u53ef\u67e5\u8be2\u672c\u6708\u5269\u4f59\u79ef\u5206</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5.\u6682\u65e0\u6cd5\u67e5\u8be2\u5230\u57df\u540d\u4fe1\u606f</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Zoomeye \u949f\u9997\u4e4b\u773c</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0p"
                        "x; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.\u63d0\u4f9b\u4e09\u4e2a\u8d44\u4ea7\u7c7b\u578b\uff0c\u5206\u522b\u662f\u4e3b\u673a\u8bbe\u5907\u3001\u5173\u8054\u57df\u540d\u3001\u5b50\u57df\u540d\uff0c\u9ed8\u8ba4\u5173\u8054\u57df\u540d\u67e5\u8be2</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2.\u5173\u8054\u57df\u540d\u3001\u5b50\u57df\u540d\u9ed8\u8ba4\u67e5\u8be230\u6761\uff0c\u4e3b\u673a\u8bbe\u5907\u9ed8\u8ba4\u67e5\u8be220\u6761\uff0c\u53ef\u7ffb\u9875</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" "
                        "margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3.\u5bfc\u51fa\u63d0\u4f9b\u4e24\u4e2a\u6309\u94ae\u5206\u522b\u6709\u201c\u5bfc\u51fa\u4e3b\u673a\u8bbe\u5907\u201d\u3001\u201c\u5bfc\u51fa\u5173\u8054\u57df\u540d/\u5b50\u57df\u540d\u201d\uff0c\u6ce8\u610f\uff1a\u9009\u62e9\u7684\u8d44\u4ea7\u7c7b\u578b\u6bd4\u5982\u662f\u201c\u4e3b\u673a\u8bbe\u5907\u201d\uff0c\u4f60\u5bfc\u51fa\u7684\u65f6\u5019\u4e5f\u5fc5\u987b\u9009\u62e9\u5bfc\u51fa\u201c\u4e3b\u673a\u8bbe\u5907\u201d \u5982\u679c\u9009\u4e86\u53e6\u4e00\u9879\u7cfb\u7edf\u7b2c\u4e00\u6b21\u5219\u4f1a\u81ea\u52a8\u63d0\u793a\uff0c\u7b2c\u4e8c\u6b21\u5219\u4e0d\u4f1a\u63d0\u793a\u76f4\u5230\u9000\u51fa\u540e\u91cd\u65b0\u8fdb\u5165</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-righ"
                        "t:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Censys</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.\u6700\u9ad8\u5c55\u793a100\u9875</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2.\u641c\u7d22\u7c7b\u578b\u5206\u522b\u6709host\u548cIP</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p"
                        ">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3.\u6839\u636e\u81ea\u5df1\u7684\u9700\u6c42\u9009\u62e9\u641c\u7d22\u65b9\u5f0f</p></body></html>", None))
        self.textBrowser_4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u7248\u672c\uff1av1.0 2022/11/12</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u00b7\u652f\u6301\u591a\u7ebf\u7a0b\u89e3\u51b3\u5927\u591a\u6570GUI\u5047\u6b7b\u72b6\u51b5</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\""
                        "><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u00b7\u652f\u6301fofa iconhash</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u00b7\u9e70\u56fe\u53ef\u67e5\u770b\u4e2a\u4eba\u79ef\u5206\u4fe1\u606f\u53ef\u9009\u62e9\u8d44\u4ea7\u7c7b\u578b\u67e5\u8be2</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u00b7shodan\u8bed\u6cd5\u548cIP\u5355\u72ec\u6a21\u5757</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:"
                        "0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u00b7\u652f\u6301\u4e00\u952e\u5bfc\u51fa </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u7248\u672c\uff1av2.0 2023/02/17</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u00b7\u4fee"
                        "\u590d\u5bfc\u51fa\u65f6\u95f4\u6233</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u00b7\u4fee\u590dHunter\u60c5\u51b5\u6062\u590d\u9875\u7801</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u00b7\u754c\u9762\u7a0d\u5fae\u8c03\u6574</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u00b7\u65b0\u589e"
                        "360 Quake</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u00b7\u65b0\u589eZoomeye \u949f\u9997\u4e4b\u773c</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u7248\u672c\uff1av3.0 2023/7/15</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-to"
                        "p:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u00b7\u65b0\u589eCensys</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u00b7quake\u548czoomeye\u4ee3\u7801\u4f18\u5316\u8c03\u6574</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u00b7\u754c\u9762\u6539\u52a8,\u65b0\u589e\u8bed\u6cd5\u53c2\u8003</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top"
                        ":0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u00b7\u4fee\u590d\u67e5\u8be2\u8fc7\u5927\u95ea\u9000\u95ee\u9898</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u00b7\u4fee\u590d\u5bfc\u51fa\u65f6\u95f4\u6233\u88ab\u8986\u76d6\u95ee\u9898</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u00b7\u4fee\u590d\u5df2\u77e5BUG</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
""
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Blog\uff1a</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">https://www.g3et.cn </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block"
                        "-indent:0; text-indent:0px;\">Github\uff1a</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">https://github.com/G3et/Search_Viewer </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">QQ\u7fa4\uff1a741069641</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

