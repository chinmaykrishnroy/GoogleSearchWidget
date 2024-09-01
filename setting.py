from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
                               QLabel, QLineEdit, QMainWindow, QPushButton,
                               QScrollArea, QSizePolicy, QToolButton, QVBoxLayout,
                               QWidget)
import res_rc
from styles import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(250, 250)
        MainWindow.setMaximumSize(QSize(275, 325))
        MainWindow.setWindowOpacity(0.6)
        MainWindow.setStyleSheet(styles)
        self.centerwidget = QWidget(MainWindow)
        self.centerwidget.setObjectName(u"centerwidget")
        self.verticalLayout = QVBoxLayout(self.centerwidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.headerWidget = QWidget(self.centerwidget)
        self.headerWidget.setObjectName(u"headerWidget")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.headerWidget.sizePolicy().hasHeightForWidth())
        self.headerWidget.setSizePolicy(sizePolicy)
        self.headerWidget.setMinimumSize(QSize(0, 36))
        self.headerWidget.setMaximumSize(QSize(16777215, 28))
        self.horizontalLayout_8 = QHBoxLayout(self.headerWidget)
        self.horizontalLayout_8.setSpacing(12)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 6, 0)
        self.titleLabel = QLabel(self.headerWidget)
        self.titleLabel.setObjectName(u"titleLabel")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.titleLabel.sizePolicy().hasHeightForWidth())
        self.titleLabel.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setBold(True)
        self.titleLabel.setFont(font)

        self.horizontalLayout_8.addWidget(
            self.titleLabel, 0, Qt.AlignmentFlag.AlignVCenter)

        self.settingCloseBtn = QToolButton(self.headerWidget)
        self.settingCloseBtn.setObjectName(u"settingCloseBtn")
        self.settingCloseBtn.setMinimumSize(QSize(24, 24))
        self.settingCloseBtn.setMaximumSize(QSize(24, 24))
        icon = QIcon()
        icon.addFile(u":/icons/cil-x.png", QSize(),
                     QIcon.Mode.Normal, QIcon.State.Off)
        self.settingCloseBtn.setIcon(icon)

        self.horizontalLayout_8.addWidget(
            self.settingCloseBtn, 0, Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout.addWidget(self.headerWidget)

        self.settingWidgets = QWidget(self.centerwidget)
        self.settingWidgets.setObjectName(u"settingWidgets")
        self.verticalLayout_2 = QVBoxLayout(self.settingWidgets)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.settingWidgets)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(
            u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -37, 246, 270))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.opacityFrame = QFrame(self.scrollAreaWidgetContents)
        self.opacityFrame.setObjectName(u"opacityFrame")
        self.opacityFrame.setMinimumSize(QSize(0, 28))
        self.opacityFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.opacityFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.opacityFrame)
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(12, 0, 12, 0)
        self.opacityBtn = QPushButton(self.opacityFrame)
        self.opacityBtn.setObjectName(u"opacityBtn")

        self.horizontalLayout.addWidget(
            self.opacityBtn, 0, Qt.AlignmentFlag.AlignLeft)

        self.opacityComboBox = QComboBox(self.opacityFrame)
        self.opacityComboBox.setObjectName(u"opacityComboBox")
        self.opacityComboBox.setMaximumSize(QSize(84, 24))
        self.opacityComboBox.addItems([str(i) for i in range(1, 11)])
        self.opacityComboBox.setCurrentIndex(5)
        self.horizontalLayout.addWidget(self.opacityComboBox)

        self.verticalLayout_3.addWidget(self.opacityFrame)

        self.maxSuggestionFrame = QFrame(self.scrollAreaWidgetContents)
        self.maxSuggestionFrame.setObjectName(u"maxSuggestionFrame")
        self.maxSuggestionFrame.setMinimumSize(QSize(0, 28))
        self.maxSuggestionFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.maxSuggestionFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.maxSuggestionFrame)
        self.horizontalLayout_3.setSpacing(12)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(12, 0, 12, 0)
        self.maxSuggestionBtn = QPushButton(self.maxSuggestionFrame)
        self.maxSuggestionBtn.setObjectName(u"maxSuggestionBtn")

        self.horizontalLayout_3.addWidget(
            self.maxSuggestionBtn, 0, Qt.AlignmentFlag.AlignLeft)

        self.maxSuggestionComboBox = QComboBox(self.maxSuggestionFrame)
        self.maxSuggestionComboBox.addItem("")
        self.maxSuggestionComboBox.addItem("")
        self.maxSuggestionComboBox.addItem("")
        self.maxSuggestionComboBox.addItem("")
        self.maxSuggestionComboBox.addItem("")
        self.maxSuggestionComboBox.addItem("")
        self.maxSuggestionComboBox.addItem("")
        self.maxSuggestionComboBox.addItem("")
        self.maxSuggestionComboBox.addItem("")
        self.maxSuggestionComboBox.addItem("")
        self.maxSuggestionComboBox.setObjectName(u"maxSuggestionComboBox")
        self.maxSuggestionComboBox.setMaximumSize(QSize(84, 24))
        self.maxSuggestionComboBox.setCurrentIndex(4)

        self.horizontalLayout_3.addWidget(self.maxSuggestionComboBox)

        self.verticalLayout_3.addWidget(self.maxSuggestionFrame)

        self.languageFrame = QFrame(self.scrollAreaWidgetContents)
        self.languageFrame.setObjectName(u"languageFrame")
        self.languageFrame.setMinimumSize(QSize(0, 28))
        self.languageFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.languageFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.languageFrame)
        self.horizontalLayout_4.setSpacing(12)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(12, 0, 12, 0)
        self.languageBtn = QPushButton(self.languageFrame)
        self.languageBtn.setObjectName(u"languageBtn")

        self.horizontalLayout_4.addWidget(
            self.languageBtn, 0, Qt.AlignmentFlag.AlignLeft)

        self.languageComboBox = QComboBox(self.languageFrame)
        self.languageComboBox.setObjectName(u"languageComboBox")
        self.languageComboBox.setMaximumSize(QSize(84, 24))
        self.languageComboBox.addItems([
            'English (en)',
            'Spanish (es)',
            'French (fr)',
            'German (de)',
            'Italian (it)',
            'Portuguese (pt)',
            'Russian (ru)',
            'Chinese (zh)',
            'Japanese (ja)',
            'Korean (ko)',
            'Hindi (hi)',
            'Arabic (ar)',
            'Dutch (nl)',
            'Turkish (tr)',
            'Swedish (sv)',
            'Norwegian (no)'
        ])
        self.languageComboBox.setCurrentIndex(0)

        self.horizontalLayout_4.addWidget(self.languageComboBox)

        self.verticalLayout_3.addWidget(self.languageFrame)

        self.clienTypeFrame = QFrame(self.scrollAreaWidgetContents)
        self.clienTypeFrame.setObjectName(u"clienTypeFrame")
        self.clienTypeFrame.setMinimumSize(QSize(0, 28))
        self.clienTypeFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.clienTypeFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.clienTypeFrame)
        self.horizontalLayout_5.setSpacing(12)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(12, 0, 12, 0)
        self.clientTypeBtn = QPushButton(self.clienTypeFrame)
        self.clientTypeBtn.setObjectName(u"clientTypeBtn")

        self.horizontalLayout_5.addWidget(
            self.clientTypeBtn, 0, Qt.AlignmentFlag.AlignLeft)

        self.clientTypeComboBox = QComboBox(self.clienTypeFrame)
        self.clientTypeComboBox.setObjectName(u"clientTypeComboBox")
        self.clientTypeComboBox.setMaximumSize(QSize(84, 24))
        self.clientTypeComboBox.addItems([
            'firefox',
            'chrome',
            'safari',
            'edge',
            'opera',
            'android',
            'ios',
            'desktop',
            'mobile',
            'tablet'
        ])
        self.clientTypeComboBox.setCurrentIndex(1)

        self.horizontalLayout_5.addWidget(self.clientTypeComboBox)

        self.verticalLayout_3.addWidget(self.clienTypeFrame)

        self.regionFrame = QFrame(self.scrollAreaWidgetContents)
        self.regionFrame.setObjectName(u"regionFrame")
        self.regionFrame.setMinimumSize(QSize(0, 28))
        self.regionFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.regionFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.regionFrame)
        self.horizontalLayout_6.setSpacing(12)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(12, 0, 12, 0)
        self.regionBtn = QPushButton(self.regionFrame)
        self.regionBtn.setObjectName(u"regionBtn")

        self.horizontalLayout_6.addWidget(
            self.regionBtn, 0, Qt.AlignmentFlag.AlignLeft)

        self.regionComboBox = QComboBox(self.regionFrame)
        self.regionComboBox.setObjectName(u"regionComboBox")
        self.regionComboBox.setMaximumSize(QSize(84, 24))
        self.regionComboBox.addItems([
            'United States (region=US)',
            'United Kingdom (region=GB)',
            'Canada (region=CA)',
            'Australia (region=AU)',
            'India (region=IN)',
            'Japan (region=JP)',
            'Germany (region=DE)',
            'France (region=FR)',
            'Brazil (region=BR)',
            'South Africa (region=ZA)',
            'Mexico (region=MX)',
            'Russia (region=RU)',
            'China (region=CN)',
            'South Korea (region=KR)',
            'Italy (region=IT)',
            'Spain (region=ES)'
        ])
        self.regionComboBox.setCurrentIndex(4)

        self.horizontalLayout_6.addWidget(self.regionComboBox)

        self.verticalLayout_3.addWidget(self.regionFrame)

        self.autoVoiceSearch = QFrame(self.scrollAreaWidgetContents)
        self.autoVoiceSearch.setObjectName(u"autoVoiceSearch")
        self.autoVoiceSearch.setMinimumSize(QSize(0, 28))
        self.autoVoiceSearch.setFrameShape(QFrame.Shape.StyledPanel)
        self.autoVoiceSearch.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.autoVoiceSearch)
        self.horizontalLayout_7.setSpacing(12)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(12, 0, 12, 0)
        self.autoVoiceSearchBtn = QPushButton(self.autoVoiceSearch)
        self.autoVoiceSearchBtn.setObjectName(u"autoVoiceSearchBtn")

        self.horizontalLayout_7.addWidget(
            self.autoVoiceSearchBtn, 0, Qt.AlignmentFlag.AlignLeft)

        self.autoVoiceSearchBomboBox = QComboBox(self.autoVoiceSearch)
        self.autoVoiceSearchBomboBox.addItem("")
        self.autoVoiceSearchBomboBox.addItem("")
        self.autoVoiceSearchBomboBox.setObjectName(u"autoVoiceSearchBomboBox")
        self.autoVoiceSearchBomboBox.setMaximumSize(QSize(84, 24))
        self.autoVoiceSearchBomboBox.setCurrentIndex(1)

        self.horizontalLayout_7.addWidget(self.autoVoiceSearchBomboBox)

        self.verticalLayout_3.addWidget(self.autoVoiceSearch)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.verticalLayout.addWidget(self.settingWidgets)

        MainWindow.setCentralWidget(self.centerwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.titleLabel.setText(QCoreApplication.translate(
            "MainWindow", u"Settings", None))
        self.settingCloseBtn.setText(
            QCoreApplication.translate("MainWindow", u"...", None))
        self.opacityBtn.setText(QCoreApplication.translate(
            "MainWindow", u"Opacity", None))
        self.maxSuggestionBtn.setText(QCoreApplication.translate(
            "MainWindow", u"Max Suggestions", None))
        self.maxSuggestionComboBox.setItemText(
            0, QCoreApplication.translate("MainWindow", u"1", None))
        self.maxSuggestionComboBox.setItemText(
            1, QCoreApplication.translate("MainWindow", u"2", None))
        self.maxSuggestionComboBox.setItemText(
            2, QCoreApplication.translate("MainWindow", u"3", None))
        self.maxSuggestionComboBox.setItemText(
            3, QCoreApplication.translate("MainWindow", u"4", None))
        self.maxSuggestionComboBox.setItemText(
            4, QCoreApplication.translate("MainWindow", u"5", None))
        self.maxSuggestionComboBox.setItemText(
            5, QCoreApplication.translate("MainWindow", u"6", None))
        self.maxSuggestionComboBox.setItemText(
            6, QCoreApplication.translate("MainWindow", u"7", None))
        self.maxSuggestionComboBox.setItemText(
            7, QCoreApplication.translate("MainWindow", u"8", None))
        self.maxSuggestionComboBox.setItemText(
            8, QCoreApplication.translate("MainWindow", u"9", None))
        self.maxSuggestionComboBox.setItemText(
            9, QCoreApplication.translate("MainWindow", u"10", None))

        self.languageBtn.setText(QCoreApplication.translate(
            "MainWindow", u"Language", None))
        self.clientTypeBtn.setText(QCoreApplication.translate(
            "MainWindow", u"Client Type", None))
        self.regionBtn.setText(QCoreApplication.translate(
            "MainWindow", u"Region", None))
        self.autoVoiceSearchBtn.setText(QCoreApplication.translate(
            "MainWindow", u"Auto Voice Search", None))
        self.autoVoiceSearchBomboBox.setItemText(
            0, QCoreApplication.translate("MainWindow", u"Yes", None))
        self.autoVoiceSearchBomboBox.setItemText(
            1, QCoreApplication.translate("MainWindow", u"No", None))

    # retranslateUi
