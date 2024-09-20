# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'widget.ui'
##
# Created by: Qt User Interface Compiler version 6.7.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale, QEvent,
                            QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QTimer)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QGradient,
                           QIcon, QImage, QKeySequence, QLinearGradient, QPainter, QPalette, QPixmap, QRadialGradient, QTransform,)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLineEdit, QMainWindow,
                               QPushButton, QSizePolicy, QSpacerItem, QToolButton, QVBoxLayout, QWidget,)
from PySide6.QtConcurrent import QtConcurrent
import res_rc
from styles import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(415, 108)
        MainWindow.setWindowOpacity(0.6)
        MainWindow.setStyleSheet(styles[2])
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(415, 0))
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.footer = QFrame(self.centralwidget)
        self.footer.setObjectName(u"footer")
        self.footer.setMinimumSize(QSize(0, 12))
        self.footer.setMaximumSize(QSize(16777215, 14))
        self.footer.setFrameShape(QFrame.Shape.StyledPanel)
        self.footer.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.footer)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.resizeFrame = QFrame(self.footer)
        self.resizeFrame.setObjectName(u"resizeFrame")
        self.resizeFrame.setMinimumSize(QSize(12, 6))
        self.resizeFrame.setMaximumSize(QSize(24, 12))
        self.resizeFrame.setCursor(QCursor(Qt.CursorShape.UpArrowCursor))
        self.resizeFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.resizeFrame.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout.addWidget(self.resizeFrame)

        self.settingBtn = QToolButton(self.footer)
        self.settingBtn.setObjectName(u"settingBtn")
        self.settingBtn.setMinimumSize(QSize(6, 6))
        self.settingBtn.setMaximumSize(QSize(12, 12))
        self.settingBtn.setCursor(QCursor(Qt.CursorShape.UpArrowCursor))
        icon = QIcon()
        icon.addFile(u":/icons/icon_settings.png", QSize(),
                     QIcon.Mode.Normal, QIcon.State.Off)
        self.settingBtn.setIcon(icon)
        self.settingBtn.setIconSize(QSize(18, 18))

        self.horizontalLayout.addWidget(self.settingBtn)

        self.closeBtn = QToolButton(self.footer)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setMinimumSize(QSize(6, 6))
        self.closeBtn.setMaximumSize(QSize(12, 12))
        self.closeBtn.setCursor(QCursor(Qt.CursorShape.UpArrowCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/cil-x.png", QSize(),
                      QIcon.Mode.Normal, QIcon.State.Off)
        self.closeBtn.setIcon(icon1)

        self.horizontalLayout.addWidget(self.closeBtn)

        self.verticalLayout.addWidget(
            self.footer, 0, Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

        self.searchArea = QWidget(self.centralwidget)
        self.searchArea.setObjectName(u"searchArea")
        self.searchArea.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_12 = QHBoxLayout(self.searchArea)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.searchInputText = QLineEdit(self.searchArea)
        self.searchInputText.setObjectName(u"searchInputText")
        self.searchInputText.setMinimumSize(QSize(0, 28))

        self.horizontalLayout_12.addWidget(self.searchInputText)

        self.searchBtn = QToolButton(self.searchArea)
        self.searchBtn.setObjectName(u"searchBtn")
        self.searchBtn.setMinimumSize(QSize(80, 28))
        self.searchBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/cil-microphone.png", QSize(),
                      QIcon.Mode.Normal, QIcon.State.Off)
        self.searchBtn.setIcon(icon2)
        self.searchBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_12.addWidget(self.searchBtn)

        self.verticalLayout.addWidget(
            self.searchArea, 0, Qt.AlignmentFlag.AlignTop)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.settingBtn.setText(
            QCoreApplication.translate("MainWindow", u"...", None))
        self.closeBtn.setText(
            QCoreApplication.translate("MainWindow", u"...", None))
        self.searchInputText.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", u"Search on Google...", None))
        self.searchBtn.setText("")
    # retranslateUi
