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
        MainWindow.resize(1434, 836)
        MainWindow.setMaximumSize(QSize(1434, 836))
        icon = QIcon()
        icon.addFile(u"C:/Users/code/.designer/backup/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actionfofa = QAction(MainWindow)
        self.actionfofa.setObjectName(u"actionfofa")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QRect(0, 0, 1531, 891))
        self.tabWidget.setMaximumSize(QSize(10800, 1000))
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
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 27, 60, 31))
        self.button = QPushButton(self.tab)
        self.button.setObjectName(u"button")
        self.button.setGeometry(QRect(1060, 20, 141, 41))
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
        self.fofa_search.setGeometry(QRect(160, 27, 641, 31))
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
        self.num.setGeometry(QRect(880, 30, 131, 31))
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
        self.clear.setGeometry(QRect(1060, 100, 141, 41))
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
        self.export_2.setGeometry(QRect(1210, 740, 201, 41))
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
        self.label_2.setGeometry(QRect(100, 140, 271, 31))
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
        self.label_10.setGeometry(QRect(90, 90, 60, 31))
        self.ico_hash = QLineEdit(self.tab)
        self.ico_hash.setObjectName(u"ico_hash")
        self.ico_hash.setGeometry(QRect(160, 90, 311, 31))
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
        self.button_4.setGeometry(QRect(880, 100, 131, 41))
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
        self.textBrowser.setGeometry(QRect(510, 90, 291, 31))
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
        self.shuchu.setGeometry(QRect(1210, 180, 201, 461))
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
        self.label_31.setGeometry(QRect(1210, 140, 60, 31))
        self.label_32 = QLabel(self.tab)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setEnabled(True)
        self.label_32.setGeometry(QRect(30, 140, 60, 31))
        self.clearrizi = QPushButton(self.tab)
        self.clearrizi.setObjectName(u"clearrizi")
        self.clearrizi.setGeometry(QRect(1210, 670, 201, 41))
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
        self.fofa.setGeometry(QRect(30, 180, 1161, 601))
        self.fofa.horizontalHeader().setDefaultSectionSize(138)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QRect(100, 140, 231, 31))
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
        self.label_5.setGeometry(QRect(90, 27, 60, 31))
        self.button_2 = QPushButton(self.tab_2)
        self.button_2.setObjectName(u"button_2")
        self.button_2.setGeometry(QRect(870, 20, 141, 41))
        self.button_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.clear_2 = QPushButton(self.tab_2)
        self.clear_2.setObjectName(u"clear_2")
        self.clear_2.setGeometry(QRect(1080, 20, 141, 41))
        self.clear_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.hunter_search = QLineEdit(self.tab_2)
        self.hunter_search.setObjectName(u"hunter_search")
        self.hunter_search.setGeometry(QRect(160, 27, 521, 31))
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
        self.export_3.setGeometry(QRect(1210, 740, 201, 41))
        self.export_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.num_2 = QComboBox(self.tab_2)
        self.num_2.addItem("")
        self.num_2.addItem("")
        self.num_2.addItem("")
        self.num_2.addItem("")
        self.num_2.setObjectName(u"num_2")
        self.num_2.setGeometry(QRect(720, 30, 91, 31))
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
        self.hunter_tab.setGeometry(QRect(30, 180, 1161, 601))
        self.hunter_tab.horizontalHeader().setDefaultSectionSize(101)
        self.xiaohao = QLabel(self.tab_2)
        self.xiaohao.setObjectName(u"xiaohao")
        self.xiaohao.setEnabled(False)
        self.xiaohao.setGeometry(QRect(510, 140, 191, 31))
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
        self.shengyu.setGeometry(QRect(990, 140, 191, 31))
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
        self.hunter_page.setGeometry(QRect(580, 90, 101, 31))
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
        self.clearrizi_2.setGeometry(QRect(1210, 670, 201, 41))
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
        self.shuchu_2.setGeometry(QRect(1210, 180, 201, 461))
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
        self.label_33.setGeometry(QRect(1210, 140, 60, 31))
        self.label_34 = QLabel(self.tab_2)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setEnabled(True)
        self.label_34.setGeometry(QRect(30, 140, 60, 31))
        self.num_3 = QComboBox(self.tab_2)
        self.num_3.addItem("")
        self.num_3.addItem("")
        self.num_3.addItem("")
        self.num_3.setObjectName(u"num_3")
        self.num_3.setGeometry(QRect(160, 90, 111, 31))
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
        self.label_6.setGeometry(QRect(90, 90, 60, 31))
        self.label_15 = QLabel(self.tab_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(530, 90, 60, 31))
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.shodan_search1 = QLineEdit(self.tab_3)
        self.shodan_search1.setObjectName(u"shodan_search1")
        self.shodan_search1.setGeometry(QRect(160, 27, 521, 31))
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
        self.export_4.setGeometry(QRect(1210, 740, 201, 41))
        self.export_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_8 = QLabel(self.tab_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setEnabled(True)
        self.label_8.setGeometry(QRect(100, 140, 231, 31))
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
        self.shodan_tab.setGeometry(QRect(30, 180, 1161, 601))
        self.shodan_tab.horizontalHeader().setDefaultSectionSize(139)
        self.clear_3 = QPushButton(self.tab_3)
        self.clear_3.setObjectName(u"clear_3")
        self.clear_3.setGeometry(QRect(990, 20, 131, 41))
        self.clear_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_3 = QPushButton(self.tab_3)
        self.button_3.setObjectName(u"button_3")
        self.button_3.setGeometry(QRect(780, 20, 131, 41))
        self.button_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.shodan_page = QLineEdit(self.tab_3)
        self.shodan_page.setObjectName(u"shodan_page")
        self.shodan_page.setGeometry(QRect(580, 90, 101, 31))
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
        self.clearrizi_3.setGeometry(QRect(1210, 670, 201, 41))
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
        self.label_35.setGeometry(QRect(1210, 140, 60, 31))
        self.shuchu_3 = QTextBrowser(self.tab_3)
        self.shuchu_3.setObjectName(u"shuchu_3")
        self.shuchu_3.setGeometry(QRect(1210, 180, 201, 461))
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
        self.label_36.setGeometry(QRect(30, 140, 60, 31))
        self.num_4 = QComboBox(self.tab_3)
        self.num_4.addItem("")
        self.num_4.addItem("")
        self.num_4.setObjectName(u"num_4")
        self.num_4.setGeometry(QRect(160, 90, 111, 31))
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
        self.label_7.setGeometry(QRect(80, 20, 71, 41))
        self.label_9 = QLabel(self.tab_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(90, 90, 60, 31))
        self.label_16 = QLabel(self.tab_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(530, 90, 60, 31))
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.clearrizi_7 = QPushButton(self.tab_6)
        self.clearrizi_7.setObjectName(u"clearrizi_7")
        self.clearrizi_7.setGeometry(QRect(1210, 670, 201, 41))
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
        self.shuchu_7.setGeometry(QRect(1210, 180, 201, 461))
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
        self.quake_search.setGeometry(QRect(160, 27, 521, 31))
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
        self.label_45.setGeometry(QRect(30, 140, 60, 31))
        self.quake_tab = QTableWidget(self.tab_6)
        if (self.quake_tab.columnCount() < 6):
            self.quake_tab.setColumnCount(6)
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
        self.quake_tab.setObjectName(u"quake_tab")
        self.quake_tab.setGeometry(QRect(30, 180, 1161, 601))
        self.quake_tab.horizontalHeader().setMinimumSectionSize(25)
        self.quake_tab.horizontalHeader().setDefaultSectionSize(187)
        self.quake_tab.horizontalHeader().setHighlightSections(True)
        self.label_46 = QLabel(self.tab_6)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(1210, 140, 60, 31))
        self.label_48 = QLabel(self.tab_6)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(80, 20, 71, 41))
        self.button_9 = QPushButton(self.tab_6)
        self.button_9.setObjectName(u"button_9")
        self.button_9.setGeometry(QRect(780, 20, 131, 41))
        self.button_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.clear_7 = QPushButton(self.tab_6)
        self.clear_7.setObjectName(u"clear_7")
        self.clear_7.setGeometry(QRect(990, 20, 131, 41))
        self.clear_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_50 = QLabel(self.tab_6)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setEnabled(True)
        self.label_50.setGeometry(QRect(100, 140, 231, 31))
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
        self.export_8.setGeometry(QRect(1210, 740, 201, 41))
        self.export_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.num_10 = QComboBox(self.tab_6)
        self.num_10.addItem("")
        self.num_10.addItem("")
        self.num_10.addItem("")
        self.num_10.addItem("")
        self.num_10.addItem("")
        self.num_10.addItem("")
        self.num_10.setObjectName(u"num_10")
        self.num_10.setGeometry(QRect(160, 90, 111, 31))
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
        self.xiaohao_3 = QLabel(self.tab_6)
        self.xiaohao_3.setObjectName(u"xiaohao_3")
        self.xiaohao_3.setEnabled(False)
        self.xiaohao_3.setGeometry(QRect(510, 140, 191, 31))
        self.xiaohao_3.setFont(font1)
        self.xiaohao_3.setFocusPolicy(Qt.NoFocus)
        self.xiaohao_3.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.xiaohao_3.setLayoutDirection(Qt.LeftToRight)
        self.xiaohao_3.setAutoFillBackground(False)
        self.xiaohao_3.setFrameShadow(QFrame.Plain)
        self.xiaohao_3.setLineWidth(1)
        self.xiaohao_3.setTextFormat(Qt.AutoText)
        self.xiaohao_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.xiaohao_3.setTextInteractionFlags(Qt.LinksAccessibleByMouse)
        self.xiaohao_4 = QLabel(self.tab_6)
        self.xiaohao_4.setObjectName(u"xiaohao_4")
        self.xiaohao_4.setEnabled(False)
        self.xiaohao_4.setGeometry(QRect(990, 140, 191, 31))
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
        self.label_49.setGeometry(QRect(89, 90, 81, 31))
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.shengyu_2 = QLabel(self.tab_7)
        self.shengyu_2.setObjectName(u"shengyu_2")
        self.shengyu_2.setEnabled(False)
        self.shengyu_2.setGeometry(QRect(990, 140, 191, 31))
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
        self.label_18.setGeometry(QRect(90, 90, 60, 31))
        self.shuchu_4 = QTextBrowser(self.tab_7)
        self.shuchu_4.setObjectName(u"shuchu_4")
        self.shuchu_4.setGeometry(QRect(1210, 180, 201, 461))
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
        if (self.zoomeye_tab.columnCount() < 9):
            self.zoomeye_tab.setColumnCount(9)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.zoomeye_tab.setHorizontalHeaderItem(0, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.zoomeye_tab.setHorizontalHeaderItem(1, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.zoomeye_tab.setHorizontalHeaderItem(2, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.zoomeye_tab.setHorizontalHeaderItem(3, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.zoomeye_tab.setHorizontalHeaderItem(4, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.zoomeye_tab.setHorizontalHeaderItem(5, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.zoomeye_tab.setHorizontalHeaderItem(6, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.zoomeye_tab.setHorizontalHeaderItem(7, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.zoomeye_tab.setHorizontalHeaderItem(8, __qtablewidgetitem41)
        self.zoomeye_tab.setObjectName(u"zoomeye_tab")
        self.zoomeye_tab.setGeometry(QRect(30, 180, 1161, 601))
        self.zoomeye_tab.horizontalHeader().setDefaultSectionSize(125)
        self.label_37 = QLabel(self.tab_7)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(1210, 140, 60, 31))
        self.label_19 = QLabel(self.tab_7)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(530, 90, 60, 31))
        self.button_5 = QPushButton(self.tab_7)
        self.button_5.setObjectName(u"button_5")
        self.button_5.setGeometry(QRect(780, 20, 131, 41))
        self.button_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.num_6 = QComboBox(self.tab_7)
        self.num_6.addItem("")
        self.num_6.addItem("")
        self.num_6.addItem("")
        self.num_6.setObjectName(u"num_6")
        self.num_6.setGeometry(QRect(160, 90, 111, 31))
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
        self.zoomeye_search.setGeometry(QRect(160, 27, 521, 31))
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
        self.zoomeye_page.setGeometry(QRect(580, 90, 101, 31))
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
        self.label_20.setGeometry(QRect(69, 27, 81, 31))
        self.label_21 = QLabel(self.tab_7)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setEnabled(True)
        self.label_21.setGeometry(QRect(100, 140, 231, 31))
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
        self.export_5 = QPushButton(self.tab_7)
        self.export_5.setObjectName(u"export_5")
        self.export_5.setGeometry(QRect(1210, 750, 201, 41))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setBold(True)
        font2.setItalic(False)
        font2.setWeight(75)
        self.export_5.setFont(font2)
        self.export_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.clear_4 = QPushButton(self.tab_7)
        self.clear_4.setObjectName(u"clear_4")
        self.clear_4.setGeometry(QRect(990, 20, 131, 41))
        self.clear_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_38 = QLabel(self.tab_7)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setEnabled(True)
        self.label_38.setGeometry(QRect(30, 140, 60, 31))
        self.export_6 = QPushButton(self.tab_7)
        self.export_6.setObjectName(u"export_6")
        self.export_6.setGeometry(QRect(1210, 700, 201, 41))
        self.export_6.setFont(font2)
        self.export_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.clearrizi_4 = QPushButton(self.tab_7)
        self.clearrizi_4.setObjectName(u"clearrizi_4")
        self.clearrizi_4.setGeometry(QRect(1210, 650, 201, 41))
        self.clearrizi_4.setFont(font2)
        self.clearrizi_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.fofa_config = QGroupBox(self.tab_4)
        self.fofa_config.setObjectName(u"fofa_config")
        self.fofa_config.setGeometry(QRect(20, 10, 801, 161))
        self.fofa_config.setFont(font)
        self.label_11 = QLabel(self.fofa_config)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(40, 40, 81, 31))
        self.label_12 = QLabel(self.fofa_config)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(50, 90, 81, 41))
        self.your_fofa_email = QLineEdit(self.fofa_config)
        self.your_fofa_email.setObjectName(u"your_fofa_email")
        self.your_fofa_email.setGeometry(QRect(130, 40, 411, 31))
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
        self.your_fofa_api = QLineEdit(self.fofa_config)
        self.your_fofa_api.setObjectName(u"your_fofa_api")
        self.your_fofa_api.setGeometry(QRect(130, 100, 411, 31))
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
        self.fofa_xiugai = QPushButton(self.fofa_config)
        self.fofa_xiugai.setObjectName(u"fofa_xiugai")
        self.fofa_xiugai.setGeometry(QRect(620, 70, 111, 41))
        self.fofa_xiugai.setCursor(QCursor(Qt.PointingHandCursor))
        self.hunter_config = QGroupBox(self.tab_4)
        self.hunter_config.setObjectName(u"hunter_config")
        self.hunter_config.setGeometry(QRect(20, 200, 801, 111))
        self.your_hunter_api = QLineEdit(self.hunter_config)
        self.your_hunter_api.setObjectName(u"your_hunter_api")
        self.your_hunter_api.setGeometry(QRect(130, 40, 411, 31))
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
        self.label_13 = QLabel(self.hunter_config)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(40, 30, 81, 41))
        self.hunter_xiugai = QPushButton(self.hunter_config)
        self.hunter_xiugai.setObjectName(u"hunter_xiugai")
        self.hunter_xiugai.setGeometry(QRect(620, 40, 111, 41))
        self.hunter_xiugai.setCursor(QCursor(Qt.PointingHandCursor))
        self.shodan_config = QGroupBox(self.tab_4)
        self.shodan_config.setObjectName(u"shodan_config")
        self.shodan_config.setGeometry(QRect(20, 340, 801, 111))
        self.your_shodan_api = QLineEdit(self.shodan_config)
        self.your_shodan_api.setObjectName(u"your_shodan_api")
        self.your_shodan_api.setGeometry(QRect(130, 40, 411, 31))
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
        self.label_14 = QLabel(self.shodan_config)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(40, 30, 81, 41))
        self.shodan_xiugai = QPushButton(self.shodan_config)
        self.shodan_xiugai.setObjectName(u"shodan_xiugai")
        self.shodan_xiugai.setGeometry(QRect(620, 30, 111, 41))
        self.shodan_xiugai.setCursor(QCursor(Qt.PointingHandCursor))
        self.save_config = QPushButton(self.tab_4)
        self.save_config.setObjectName(u"save_config")
        self.save_config.setGeometry(QRect(1000, 720, 111, 41))
        self.save_config.setCursor(QCursor(Qt.PointingHandCursor))
        self.groupBox = QGroupBox(self.tab_4)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(850, 50, 421, 621))
        font3 = QFont()
        font3.setPointSize(13)
        self.groupBox.setFont(font3)
        self.groupBox.setLayoutDirection(Qt.LeftToRight)
        self.label_17 = QLabel(self.groupBox)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(20, 20, 391, 171))
        font4 = QFont()
        font4.setFamily(u"\u9ed1\u4f53")
        font4.setPointSize(12)
        self.label_17.setFont(font4)
        self.label_17.setLayoutDirection(Qt.LeftToRight)
        self.label_17.setFrameShadow(QFrame.Plain)
        self.shodan_config_3 = QGroupBox(self.tab_4)
        self.shodan_config_3.setObjectName(u"shodan_config_3")
        self.shodan_config_3.setGeometry(QRect(20, 480, 801, 111))
        self.your_quake_api = QLineEdit(self.shodan_config_3)
        self.your_quake_api.setObjectName(u"your_quake_api")
        self.your_quake_api.setGeometry(QRect(130, 40, 411, 31))
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
        self.label_56 = QLabel(self.shodan_config_3)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setGeometry(QRect(40, 30, 81, 41))
        self.quake_xiugai = QPushButton(self.shodan_config_3)
        self.quake_xiugai.setObjectName(u"quake_xiugai")
        self.quake_xiugai.setGeometry(QRect(620, 30, 111, 41))
        self.quake_xiugai.setCursor(QCursor(Qt.PointingHandCursor))
        self.fofa_config_2 = QGroupBox(self.tab_4)
        self.fofa_config_2.setObjectName(u"fofa_config_2")
        self.fofa_config_2.setGeometry(QRect(20, 620, 801, 111))
        self.fofa_config_2.setFont(font)
        self.label_26 = QLabel(self.fofa_config_2)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(20, 40, 101, 31))
        self.your_zoomeye_api = QLineEdit(self.fofa_config_2)
        self.your_zoomeye_api.setObjectName(u"your_zoomeye_api")
        self.your_zoomeye_api.setGeometry(QRect(130, 40, 411, 31))
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
        self.zoomeye_xiugai = QPushButton(self.fofa_config_2)
        self.zoomeye_xiugai.setObjectName(u"zoomeye_xiugai")
        self.zoomeye_xiugai.setGeometry(QRect(620, 30, 111, 41))
        self.zoomeye_xiugai.setCursor(QCursor(Qt.PointingHandCursor))
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.groupBox_2 = QGroupBox(self.tab_5)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(20, 10, 571, 761))
        self.groupBox_2.setFont(font)
        self.groupBox_3 = QGroupBox(self.tab_5)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(690, 10, 571, 761))
        self.groupBox_3.setFont(font)
        self.textBrowser_3 = QTextBrowser(self.groupBox_3)
        self.textBrowser_3.setObjectName(u"textBrowser_3")
        self.textBrowser_3.setGeometry(QRect(30, 30, 501, 701))
        self.textBrowser_4 = QTextBrowser(self.tab_5)
        self.textBrowser_4.setObjectName(u"textBrowser_4")
        self.textBrowser_4.setGeometry(QRect(40, 40, 521, 701))
        self.tabWidget.addTab(self.tab_5, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.num_2.setCurrentIndex(1)
        self.num_3.setCurrentIndex(0)
        self.num_4.setCurrentIndex(0)
        self.num_10.setCurrentIndex(0)
        self.num_6.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Search_Viewer     Author\uff1aG3et     v2.0", None))
        self.actionfofa.setText(QCoreApplication.translate("MainWindow", u"fofa", None))
#if QT_CONFIG(shortcut)
        self.actionfofa.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+A", None))
#endif // QT_CONFIG(shortcut)
        self.label.setText(QCoreApplication.translate("MainWindow", u"FOFA\u8bed\u6cd5\uff1a", None))
        self.button.setText(QCoreApplication.translate("MainWindow", u"FOFA\u67e5\u8be2", None))
        self.fofa_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165FOFA\u8bed\u6cd5", None))
        self.num.setItemText(0, QCoreApplication.translate("MainWindow", u"10000", None))
        self.num.setItemText(1, QCoreApplication.translate("MainWindow", u"5000", None))
        self.num.setItemText(2, QCoreApplication.translate("MainWindow", u"2000", None))
        self.num.setItemText(3, QCoreApplication.translate("MainWindow", u"1000", None))
        self.num.setItemText(4, QCoreApplication.translate("MainWindow", u"100", None))

        self.clear.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a", None))
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
        self.button_2.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2", None))
        self.clear_2.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a", None))
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
        self.clear_3.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a", None))
        self.button_3.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2", None))
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
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Location", None));
        ___qtablewidgetitem31 = self.quake_tab.horizontalHeaderItem(4)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"isp", None));
        ___qtablewidgetitem32 = self.quake_tab.horizontalHeaderItem(5)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Time", None));
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"\u65e5\u5fd7\uff1a", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Quake\u8bed\u6cd5\uff1a", None))
        self.button_9.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2", None))
        self.clear_7.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"0 \u6761", None))
        self.export_8.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u6570\u636e", None))
        self.num_10.setItemText(0, QCoreApplication.translate("MainWindow", u"20", None))
        self.num_10.setItemText(1, QCoreApplication.translate("MainWindow", u"10", None))
        self.num_10.setItemText(2, QCoreApplication.translate("MainWindow", u"50", None))
        self.num_10.setItemText(3, QCoreApplication.translate("MainWindow", u"100", None))
        self.num_10.setItemText(4, QCoreApplication.translate("MainWindow", u"200", None))
        self.num_10.setItemText(5, QCoreApplication.translate("MainWindow", u"499", None))

        self.num_10.setCurrentText(QCoreApplication.translate("MainWindow", u"20", None))
        self.xiaohao_3.setText(QCoreApplication.translate("MainWindow", u"\u53bb\u91cd\u540e\uff1a", None))
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
        ___qtablewidgetitem33 = self.zoomeye_tab.horizontalHeaderItem(0)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"IP", None));
        ___qtablewidgetitem34 = self.zoomeye_tab.horizontalHeaderItem(1)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Port", None));
        ___qtablewidgetitem35 = self.zoomeye_tab.horizontalHeaderItem(2)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Title", None));
        ___qtablewidgetitem36 = self.zoomeye_tab.horizontalHeaderItem(3)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Service", None));
        ___qtablewidgetitem37 = self.zoomeye_tab.horizontalHeaderItem(4)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"City", None));
        ___qtablewidgetitem38 = self.zoomeye_tab.horizontalHeaderItem(5)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"ISP", None));
        ___qtablewidgetitem39 = self.zoomeye_tab.horizontalHeaderItem(6)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"APP", None));
        ___qtablewidgetitem40 = self.zoomeye_tab.horizontalHeaderItem(7)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Timestamp", None));
        ___qtablewidgetitem41 = self.zoomeye_tab.horizontalHeaderItem(8)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Domain", None));
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"\u65e5\u5fd7\uff1a", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u9875\u7801\uff1a", None))
        self.button_5.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2", None))
        self.num_6.setItemText(0, QCoreApplication.translate("MainWindow", u"\u5173\u8054\u57df\u540d", None))
        self.num_6.setItemText(1, QCoreApplication.translate("MainWindow", u"\u5b50\u57df\u540d", None))
        self.num_6.setItemText(2, QCoreApplication.translate("MainWindow", u"\u4e3b\u673a\u8bbe\u5907", None))

        self.num_6.setCurrentText(QCoreApplication.translate("MainWindow", u"\u5173\u8054\u57df\u540d", None))
        self.zoomeye_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165Zoomeye\u8bed\u6cd5", None))
        self.zoomeye_page.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.zoomeye_page.setPlaceholderText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Zoomeye\u8bed\u6cd5\uff1a", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"0 \u6761", None))
        self.export_5.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u5173\u8054\u57df\u540d/\u5b50\u57df\u540d", None))
        self.clear_4.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22\u7ed3\u679c\uff1a", None))
        self.export_6.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u4e3b\u673a\u8bbe\u5907", None))
        self.clearrizi_4.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u65e5\u5fd7", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"Zoomeye", None))
        self.fofa_config.setTitle(QCoreApplication.translate("MainWindow", u"FOFA\u914d\u7f6e", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"FOFA_EMAIL\uff1a", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"FOFA_API\uff1a", None))
        self.your_fofa_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u4f60\u7684FOFA\u90ae\u7bb1", None))
        self.your_fofa_api.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u4f60\u7684FOFA API", None))
        self.fofa_xiugai.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539", None))
        self.hunter_config.setTitle(QCoreApplication.translate("MainWindow", u"Hunter\u914d\u7f6e", None))
        self.your_hunter_api.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u4f60\u7684\u9e70\u56feAPI", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"HUNTER_API\uff1a", None))
        self.hunter_xiugai.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539", None))
        self.shodan_config.setTitle(QCoreApplication.translate("MainWindow", u"Shodan\u914d\u7f6e", None))
        self.your_shodan_api.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u4f60\u7684SHODAN API", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"SHODAN_API\uff1a", None))
        self.shodan_xiugai.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539", None))
        self.save_config.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u914d\u7f6e\u8bf4\u660e", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u6ce8\u610f\uff1a\n"
"\u7b2c\u4e00\u6b21\u4fdd\u5b58\u4e86API\u4e4b\u540e\uff0c\u518d\u60f3\u66ff\u6362\u65f6\uff0c\u8bf7\u70b9\u51fb\u4fee\u6539\uff0c\u8bf7\u4e0d\u8981\n"
"\u518d\u70b9\u51fb\u4fdd\u5b58\uff0c\u5982\u679c\u518d\u70b9\u51fb\u4fdd\u5b58\uff0c\u5176\u4ed6\u7684API\u5c06\u88ab\u8986\u76d6\uff0c\u5219\n"
"\u9700\u8981\u91cd\u65b0\u914d\u7f6e\n"
"\n"
"\n"
"\n"
"", None))
        self.shodan_config_3.setTitle(QCoreApplication.translate("MainWindow", u"Quake\u914d\u7f6e", None))
        self.your_quake_api.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u4f60\u7684QUAKE API", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"QUAKE_API\uff1a", None))
        self.quake_xiugai.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539", None))
        self.fofa_config_2.setTitle(QCoreApplication.translate("MainWindow", u"Zoomeye\u914d\u7f6e", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Zoomeye_API\uff1a", None))
        self.your_zoomeye_api.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u4f60\u7684Zoomeye API", None))
        self.zoomeye_xiugai.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Config", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Change Log", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"README", None))
        self.textBrowser_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u6ce8\uff1a</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u7b2c\u4e00\u6b21\u4f7f\u7528\u9009\u62e9\u4fdd\u5b58\uff0c\u4e4b\u540e\u9700\u8981\u4fee\u6539api\u70b9\u51fb\u4fee\u6539\u5373\u53ef\uff0c\u5982\u679c\u518d\u70b9\u51fb\u4fdd\u5b58\u5c06\u8986\u76d6\u6240\u6709\u5df2\u7ecf\u914d\u7f6e\u7684API\uff0c\u5219\u9700\u8981\u91cd\u65b0\u518d\u914d\u7f6e</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-blo"
                        "ck-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">FOFA\uff1a</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.\u9ed8\u8ba4\u5c55\u793a10000\u6761\u6570\u636e<br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2.\u652f\u6301iconhash\u67e5\u8be2\uff0c\u8f93\u51fa\u7684iconhash\u590d\u5236\u5230\u8f93\u5165\u6846\u70b9\u51fb\u67e5\u8be2\u5373\u53ef<br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3.\u70b9\u51fb\u67e5\u8be2\u4f1a\u8986\u76d6\u5df2\u67e5\u8be2\u7684\u5185\u5bb9</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
""
                        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Hunter\uff1a</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.\u9ed8\u8ba4\u5c55\u793a20\u6761\u6570\u636e\uff0c\u6700\u9ad8100\u6761 <br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2.\u53ef\u4ee5\u81ea\u5df1\u8f93\u5165\u9875\u7801\uff0c\u9ed8\u8ba4\u7b2c\u4e00\u9875 <br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3.\u6bcf\u6b21\u67e5\u8be2\u53ef\u4ee5\u770b\u5230\u6d88\u8017\u79ef\u5206\u548c\u5269\u4f59\u79ef\u5206<br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4.\u5f53\u65e5\u91cd\u590d\u67e5\u8be2\u7684\u8bed\u53e5\uff0c\u4e0d\u4f1a\u7d2f"
                        "\u8ba1\u6263\u79ef\u5206<br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5.\u53ef\u4ee5\u81ea\u5df1\u9009\u62e9\u8d44\u4ea7\u7c7b\u578b\uff0c\u9ed8\u8ba4web\u8d44\u4ea7<br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">6.\u70b9\u51fb\u67e5\u8be2\u4f1a\u8986\u76d6\u5df2\u67e5\u8be2\u7684\u5185\u5bb9<br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">7.\u6682\u4e0d\u652f\u6301\u67e5\u8be2iconhash\uff0c\u4e4b\u540e\u7248\u672c\u53ef\u80fd\u4f1a\u65b0\u589e<br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">shodan\uff1a</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.\u9ed8\u8ba4\u5c55\u793a"
                        "100\u6761\uff0c\u53ef\u7ffb\u9875 <br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2.shodan\u641c\u7d22\u901f\u5ea6\u53ef\u80fd\u6bd4\u5176\u4ed6\u7684\u7a7a\u95f4\u6d4b\u7ed8\u6162\u4e00\u4e9b\uff0c\u70b9\u51fb\u67e5\u8be2\u540e\u6ca1\u5fc5\u8981\u518d\u6b21\u70b9\u51fb\u67e5\u8be2\uff0c\u8bf7\u8010\u5fc3\u7b49\u5f85\u5373\u53ef </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3.\u641c\u7d22\u65b9\u6cd5\uff1a\u5982\u679c\u9700\u8981\u641c\u7d22shodan\u8bed\u53e5\u9009\u62e9HOST\u65b9\u6cd5\uff0c\u5982\u679c\u9700\u8981\u641c\u7d22IP\u9009\u62e9IP\u5373\u53ef\uff0c\u9009\u9519\u53ef\u80fd\u4f1a\u5f71\u54cd\u5230\u641c\u7d22\u7ed3\u679c<br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4.\u70b9\u51fb\u67e5\u8be2\u4e0d\u4f1a\u8986\u76d6\u5df2\u67e5\u8be2\u7684"
                        "\u5185\u5bb9</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5.\u53ea\u80fd\u5bfc\u51fa\u5df2\u67e5\u8be2\u51fa\u6765\u7684\u5185\u5bb9\uff0c\u53ef\u80fd\u4e4b\u540e\u7248\u672c\u4f1a\u89e3\u51b3</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">360 Quake\uff1a</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.\u652f\u6301360 Quake\u8bed\u6cd5</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-"
                        "right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2.\u9ed8\u8ba4\u67e5\u8be220\u9875\uff0c\u6700\u5927\u67e5\u8be2499\u6761</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3.\u81ea\u52a8\u5c55\u793a\u53bb\u91cd</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4.\u53ef\u67e5\u8be2\u672c\u6708\u5269\u4f59\u79ef\u5206</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12p"
                        "x; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5.\u6682\u65e0\u6cd5\u67e5\u8be2\u5230\u57df\u540d\u4fe1\u606f</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Zoomeye \u949f\u9997\u4e4b\u773c\uff1a</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.\u63d0\u4f9b\u4e09\u4e2a\u8d44\u4ea7\u7c7b\u578b\uff0c\u5206\u522b\u662f\u4e3b\u673a\u8bbe\u5907\u3001\u5173\u8054\u57df\u540d\u3001\u5b50\u57df\u540d\uff0c\u9ed8\u8ba4\u5173\u8054\u57df\u540d\u67e5\u8be2</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:"
                        "12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2.\u5173\u8054\u57df\u540d\u3001\u5b50\u57df\u540d\u9ed8\u8ba4\u67e5\u8be230\u6761\uff0c\u4e3b\u673a\u8bbe\u5907\u9ed8\u8ba4\u67e5\u8be220\u6761\uff0c\u53ef\u7ffb\u9875</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3.\u5bfc\u51fa\u63d0\u4f9b\u4e24\u4e2a\u6309\u94ae\u5206\u522b\u6709&quot;\u5bfc\u51fa\u4e3b\u673a\u8bbe\u5907&quot;\u3001&quot;\u5bfc\u51fa\u5173\u8054\u57df\u540d/\u5b50\u57df\u540d&quot;\uff0c\u6ce8\u610f\uff1a\u9009\u62e9\u7684\u8d44\u4ea7\u7c7b\u578b\u6bd4\u5982\u662f&quot;\u4e3b\u673a\u8bbe\u5907&quot;\uff0c\u4f60\u5bfc\u51fa\u7684\u65f6"
                        "\u5019\u4e5f\u5fc5\u987b\u9009\u62e9\u5bfc\u51fa&quot;\u4e3b\u673a\u8bbe\u5907&quot;\u5982\u679c\u9009\u4e86\u53e6\u4e00\u9879\u7cfb\u7edf\u7b2c\u4e00\u6b21\u5219\u4f1a\u81ea\u52a8\u63d0\u793a\uff0c\u7b2c\u4e8c\u6b21\u5219\u4e0d\u4f1a\u63d0\u793a\u76f4\u5230\u9000\u51fa\u540e\u91cd\u65b0\u8fdb\u5165</p></body></html>", None))
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
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Blog\uff1a</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin"
                        "-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">https://www.g3et.cn </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Github\uff1a</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">https://github.com/G3et/Search_Viewer </p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

