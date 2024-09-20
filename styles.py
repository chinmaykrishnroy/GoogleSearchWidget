styles1 = """
* {
	border: none;
    padding: 0px;
    margin: 0px;
    background-color: none;
    font-family: "Segoe UI";
    font-size: 16px;
}

#centralwidget {
    background: transparent;
}

#centerwidget {
    background: transparent;
}

#searchArea {
    background: transparent;
}

#footer {
    background: transparent;
}

QWidget {
	background: #111111;
}


QScrollBar:vertical {
    width: 4px;
    margin: 10px 0px 10px 0px;
}

QScrollBar:horizontal {
    height: 4px;
    margin: 0px 40px 0px 40px;
}

QScrollBar:vertical, QScrollBar:horizontal {
    background: #dddddd;
    border-radius: 2px;
}

QScrollBar::handle:vertical, QScrollBar::handle:horizontal {
    background: #424242;
    border-radius: 2px;
    min-height: 20px;
    min-width: 20px;
}

QScrollBar::handle:vertical:hover, QScrollBar::handle:horizontal:hover {
    background: #a7b308;
    border-radius: 2px;
}

QScrollBar::add-line, QScrollBar::sub-line {
    background: transparent;
}


#searchInputText {
	background: #050505;
	border: 1px solid #000000;
	color: #ffffff;
	padding: 0px 12px;
	border-top-left-radius: 6px;
    border-bottom-left-radius: 6px;
}

#footer QToolButton {
	background: #050505;
	margin: 1px 1px;
	border: 1px solid #000000;
	border-radius: 4px;
}

#searchBtn {
	background-color: #477300;
	border-top-right-radius: 6px;
    border-bottom-right-radius: 6px;
}

#searchBtn:hover {
	background-color: #779300;
}

#searchBtn:pressed {
	background-color: #444444;
	border-right: 1px solid #779300;
	border-top: 1px solid #779300;
	border-bottom: 1px solid #779300;
}

#centralwidget QPushButton {
	text-align: left;
	background: #050505;
	border: 1px solid #000000;
	color: #ffffff;
	padding: 0px 12px;
	border-top-left-radius: 6px;
    border-bottom-left-radius: 6px;
	border-top-right-radius: 6px;
    border-bottom-right-radius: 6px;
	margin-top: 6px
}

#centralwidget QPushButton:hover {
	background: #111111;
}

#centralwidget QPushButton:focus {
    border: 1px solid #000000;
}

#closeBtn:hover {
	background: #ff0000;
}

#closeBtn:pressed {
	background: #880000;
}

#settingBtn:hover {
	background: #ff00ff;
}

#settingBtn:pressed {
	background: #0000ff;
}

#resizeFrame {
	background: #237d13;
	margin: 1px 1px;
	border: 1px solid #222222;
	border-radius: 4px;
}

#resizeFrame:hover {
	background: #00ff00;
	margin: 1px 1px;
	border: 1px solid #222222;
	border-radius: 4px;
}

#scrollAreaWidgetContents QFrame {
	background-color: #ff0000;
	border-radius: 4px;
}

#scrollAreaWidgetContents QPushButton {
	background-color: #ff0000;
	color: #ffffff;
	padding: 2px 4px;
}

#scrollAreaWidgetContents QLineEdit {
	background-color: #eeeeee;
	color: #111111;
	padding: 2px 4px;
	border-radius: 4px;
}

#headerWidget QLabel {
	padding: 2px 4px;
	font-size: 20px;
    border-radius: 6px;
	color: #dddddd;
}

#headerWidget QToolButton {
	border-radius: 12px;
	border: 1px solid #111111;
}

#headerWidget QToolButton:hover {
	border-radius: 12px;
	border: 1px solid #ff0000;
	background: #bb0000;
}

#headerWidget QToolButton:pressed {
	border-radius: 12px;
	border: 1px solid #ff0000;
	background: #ff2200;
}

#headerWidget {
	border-radius: 6px;
	background: #111111;
}

#settingWidgets {
	border-radius: 6px;
	background: #111111;
}

#scrollAreaWidgetContents {
	border-radius: 6px;
	background: #111111;
}

#scrollAreaWidgetContents QComboBox {
	padding-left: 4px;
    color: #000000;
	background: #dddddd;
	font-family: "Segoe UI";
	font-size: 12px;
	border: 2px solid #dddddd; 
	border-radius: 6px;
}

#scrollAreaWidgetContents QComboBox:hover {
	border-style: solid; 
	border-radius: 6px; 
}

#scrollAreaWidgetContents QComboBox:pressed {
	border-style: solid; 
	border-radius: 6px;
}

#scrollAreaWidgetContents QComboBox QAbstractItemView {
    color: white;
    background-color: #474349;
    selection-background-color: #105758; 
    border: none;
}

#scrollAreaWidgetContents QComboBox:focus {
}

#scrollAreaWidgetContents QComboBox::drop-down:button
{
    border: none;
    padding: 0;
    width: 0;
}
"""
styles2 = """
* {
	border: none;
    padding: 0px;
    margin: 0px;
    background-color: none;
	font-family: 'Times New Roman', serif;
    font-size: 17px;
}

#centralwidget {
    background: transparent;
}

#centerwidget {
    background: transparent;
}

#searchArea {
    background: transparent;
}

#footer {
    background: transparent;
}

QWidget {
	background: #111111;
}


QScrollBar:vertical {
    width: 4px;
    margin: 10px 0px 10px 0px;
}

QScrollBar:horizontal {
    height: 4px;
    margin: 0px 40px 0px 40px;
}

QScrollBar:vertical, QScrollBar:horizontal {
    background: #dddddd;
    border-radius: 2px;
}

QScrollBar::handle:vertical, QScrollBar::handle:horizontal {
    background: #424242;
    border-radius: 2px;
    min-height: 20px;
    min-width: 20px;
}

QScrollBar::handle:vertical:hover, QScrollBar::handle:horizontal:hover {
    background: #a7b308;
    border-radius: 2px;
}

QScrollBar::add-line, QScrollBar::sub-line {
    background: transparent;
}


#searchInputText {
	background: #FFECD1;
	border: 1px solid #FFCCB1;
	color: #111111;
	padding: 0px 12px;
	border-top-left-radius: 14px;
    border-bottom-left-radius: 14px;
}

#footer QToolButton {
	background: #050505;
	margin: 1px 1px;
	border: 1px solid #000000;
	border-radius: 4px;
}

#searchBtn {
	background-color: #DD290F;
	border-top-right-radius: 14px;
    border-bottom-right-radius: 14px;
}

#searchBtn:hover {
	background-color: #CC0000;
}

#searchBtn:pressed {
	background-color: #444444;
	border-right: 1px solid #779300;
	border-top: 1px solid #779300;
	border-bottom: 1px solid #779300;
}

#centralwidget QPushButton {
	text-align: left;
	background: #FFECD1;
	border: 1px solid #FF7D00;
	color: #111111;
	padding: 0px 12px;
	border-top-left-radius: 14px;
    border-bottom-left-radius: 14px;
	border-top-right-radius: 14px;
    border-bottom-right-radius: 14px;
	margin-top: 6px
}

#centralwidget QPushButton:hover {
	background: #FFFDFB;
}

#centralwidget QPushButton:focus {
    border: 1px solid #000000;
}

#closeBtn:hover {
	background: #ff0000;
}

#closeBtn:pressed {
	background: #880000;
}

#settingBtn:hover {
	background: #FF7D00;
}

#settingBtn:pressed {
	background: #0000ff;
}

#resizeFrame {
	background: #FF7D00;
	margin: 1px 1px;
	border: 1px solid #222222;
	border-radius: 4px;
}

#resizeFrame:hover {
	background: #ffff00;
	margin: 1px 1px;
	border: 1px solid #222222;
	border-radius: 4px;
}

#scrollAreaWidgetContents QFrame {
	background-color: #ff0000;
	border-radius: 4px;
}

#scrollAreaWidgetContents QPushButton {
	background-color: #ff0000;
	color: #ffffff;
	padding: 2px 4px;
}

#scrollAreaWidgetContents QLineEdit {
	background-color: #eeeeee;
	color: #111111;
	padding: 2px 4px;
	border-radius: 4px;
}

#headerWidget QLabel {
	padding: 2px 4px;
	font-size: 20px;
    border-radius: 6px;
	color: #dddddd;
}

#headerWidget QToolButton {
	border-radius: 12px;
	border: 1px solid #111111;
}

#headerWidget QToolButton:hover {
	border-radius: 12px;
	border: 1px solid #ff0000;
	background: #bb0000;
}

#headerWidget QToolButton:pressed {
	border-radius: 12px;
	border: 1px solid #ff0000;
	background: #ff2200;
}

#headerWidget {
	border-radius: 6px;
	background: #111111;
}

#settingWidgets {
	border-radius: 6px;
	background: #111111;
}

#scrollAreaWidgetContents {
	border-radius: 6px;
	background: #111111;
}

#scrollAreaWidgetContents QComboBox {
	padding-left: 4px;
    color: #000000;
	background: #dddddd;
	font-family: "Segoe UI";
	font-size: 12px;
	border: 2px solid #dddddd; 
	border-radius: 6px;
}

#scrollAreaWidgetContents QComboBox:hover {
	border-style: solid; 
	border-radius: 6px; 
}

#scrollAreaWidgetContents QComboBox:pressed {
	border-style: solid; 
	border-radius: 6px;
}

#scrollAreaWidgetContents QComboBox QAbstractItemView {
    color: white;
    background-color: #474349;
    selection-background-color: #105758; 
    border: none;
}

#scrollAreaWidgetContents QComboBox:focus {
}

#scrollAreaWidgetContents QComboBox::drop-down:button
{
    border: none;
    padding: 0;
    width: 0;
}
"""
styles3 = """
* {
	border: none;
    padding: 0px;
    margin: 0px;
    background-color: none;
    font-family: "Segoe UI";
    font-size: 16px;
}

#centralwidget {
    background: transparent;
}

#centerwidget {
    background: transparent;
}

#searchArea {
    background: transparent;
}

#footer {
    background: transparent;
}

QWidget {
	background: #111111;
}


QScrollBar:vertical {
    width: 4px;
    margin: 10px 0px 10px 0px;
}

QScrollBar:horizontal {
    height: 4px;
    margin: 0px 40px 0px 40px;
}

QScrollBar:vertical, QScrollBar:horizontal {
    background: #dddddd;
    border-radius: 2px;
}

QScrollBar::handle:vertical, QScrollBar::handle:horizontal {
    background: #424242;
    border-radius: 2px;
    min-height: 20px;
    min-width: 20px;
}

QScrollBar::handle:vertical:hover, QScrollBar::handle:horizontal:hover {
    background: #a7b308;
    border-radius: 2px;
}

QScrollBar::add-line, QScrollBar::sub-line {
    background: transparent;
}


#searchInputText {
	background: #15616D;
	border: 1px solid #15616D;
	color: #FFECD1;
	padding: 0px 12px;
	border-top-left-radius: 2px;
    border-bottom-left-radius: 2px;
}

#footer QToolButton {
	background: #001524;
	margin: 1px 1px;
	border: 1px solid #223746;
	border-radius: 4px;
}

#searchBtn {
	background-color: #001524;
	border-top-right-radius: 2px;
    border-bottom-right-radius: 2px;
}

#searchBtn:hover {
	background-color: #112645;
}

#searchBtn:pressed {
	background-color: #111111;
	border-right: 1px solid #000000;
	border-top: 1px solid #000000;
	border-bottom: 1px solid #000000;
}

#centralwidget QPushButton {
	text-align: left;
	background: #15616D;
	border: 1px solid #15616D;
	color: #FFECD1;
	padding: 0px 12px;
	border-top-left-radius: 2px;
    border-bottom-left-radius: 2px;
	border-top-right-radius: 2px;
    border-bottom-right-radius: 2px;
	margin-top: 6px
}

#centralwidget QPushButton:hover {
	background: #05515D;
}

#centralwidget QPushButton:focus {
    border: 1px solid #000000;
}

#closeBtn:hover {
	background: #ff0000;
}

#closeBtn:pressed {
	background: #880000;
}

#settingBtn:hover {
	background: #15616D;
}

#settingBtn:pressed {
	background: #0000ff;
}

#resizeFrame {
	background: #112635;
	margin: 1px 1px;
	border: 1px solid #223746;
	border-radius: 4px;
}

#resizeFrame:hover {
	background: #001524;
	margin: 1px 1px;
	border: 1px solid #223746;
	border-radius: 4px;
}

#scrollAreaWidgetContents QFrame {
	background-color: #ff0000;
	border-radius: 4px;
}

#scrollAreaWidgetContents QPushButton {
	background-color: #ff0000;
	color: #ffffff;
	padding: 2px 4px;
}

#scrollAreaWidgetContents QLineEdit {
	background-color: #eeeeee;
	color: #111111;
	padding: 2px 4px;
	border-radius: 4px;
}

#headerWidget QLabel {
	padding: 2px 4px;
	font-size: 20px;
    border-radius: 6px;
	color: #dddddd;
}

#headerWidget QToolButton {
	border-radius: 12px;
	border: 1px solid #111111;
}

#headerWidget QToolButton:hover {
	border-radius: 12px;
	border: 1px solid #ff0000;
	background: #bb0000;
}

#headerWidget QToolButton:pressed {
	border-radius: 12px;
	border: 1px solid #ff0000;
	background: #ff2200;
}

#headerWidget {
	border-radius: 6px;
	background: #111111;
}

#settingWidgets {
	border-radius: 6px;
	background: #111111;
}

#scrollAreaWidgetContents {
	border-radius: 6px;
	background: #111111;
}

#scrollAreaWidgetContents QComboBox {
	padding-left: 4px;
    color: #000000;
	background: #dddddd;
	font-family: "Segoe UI";
	font-size: 12px;
	border: 2px solid #dddddd; 
	border-radius: 6px;
}

#scrollAreaWidgetContents QComboBox:hover {
	border-style: solid; 
	border-radius: 6px; 
}

#scrollAreaWidgetContents QComboBox:pressed {
	border-style: solid; 
	border-radius: 6px;
}

#scrollAreaWidgetContents QComboBox QAbstractItemView {
    color: white;
    background-color: #474349;
    selection-background-color: #105758; 
    border: none;
}

#scrollAreaWidgetContents QComboBox:focus {
}

#scrollAreaWidgetContents QComboBox::drop-down:button
{
    border: none;
    padding: 0;
    width: 0;
}
"""
styles4 = """
* {
	border: none;
    padding: 0px;
    margin: 0px;
    background-color: none;
	font-family: "Segoe UI";
    font-size: 16px;
}

#centralwidget {
    background: transparent;
}

#centerwidget {
    background: transparent;
}

#searchArea {
    background: transparent;
}

#footer {
    background: transparent;
}

QWidget {
	background: #111111;
}


QScrollBar:vertical {
    width: 4px;
    margin: 10px 0px 10px 0px;
}

QScrollBar:horizontal {
    height: 4px;
    margin: 0px 40px 0px 40px;
}

QScrollBar:vertical, QScrollBar:horizontal {
    background: #dddddd;
    border-radius: 2px;
}

QScrollBar::handle:vertical, QScrollBar::handle:horizontal {
    background: #424242;
    border-radius: 2px;
    min-height: 20px;
    min-width: 20px;
}

QScrollBar::handle:vertical:hover, QScrollBar::handle:horizontal:hover {
    background: #a7b308;
    border-radius: 2px;
}

QScrollBar::add-line, QScrollBar::sub-line {
    background: transparent;
}


#searchInputText {
	background: #D7C0D0;
	border: 1px solid #D7C0D0;
	color: #000000;
	padding: 0px 12px;
	border-top-left-radius: 4px;
    border-bottom-left-radius: 4px;
}

#footer QToolButton {
	background: #333333;
	margin: 1px 1px;
	border: 1px solid #444444;
	border-radius: 4px;
}

#searchBtn {
	background-color: #C6AEBE;
	border-top-right-radius: 4px;
    border-bottom-right-radius: 4px;
}

#searchBtn:hover {
	background-color: #978090;
}

#searchBtn:pressed {
	background-color: #888888;
	border-right: 1px solid #888888;
	border-top: 1px solid #888888;
	border-bottom: 1px solid #888888;
}

#centralwidget QPushButton {
	text-align: left;
	background: #D7C0D0;
	border: 1px solid #D7C0D0;
	color: #111111;
	padding: 0px 12px;
	border-top-left-radius: 4px;
    border-bottom-left-radius: 4px;
	border-top-right-radius: 4px;
    border-bottom-right-radius: 4px;
	margin-top: 6px
}

#centralwidget QPushButton:hover {
	background: #FFFDFB;
}

#centralwidget QPushButton:focus {
    border: 1px solid #000000;
}

#closeBtn:hover {
	background: #ff0000;
}

#closeBtn:pressed {
	background: #880000;
}

#settingBtn:hover {
	background: #555500;
}

#settingBtn:pressed {
	background: #000000;
}

#resizeFrame {
	background: #333333;
	margin: 1px 1px;
	border: 1px solid #444444;
	border-radius: 4px;
}

#resizeFrame:hover {
	background: #888888;
	margin: 1px 1px;
	border: 1px solid #222222;
	border-radius: 4px;
}

#scrollAreaWidgetContents QFrame {
	background-color: #ff0000;
	border-radius: 4px;
}

#scrollAreaWidgetContents QPushButton {
	background-color: #ff0000;
	color: #ffffff;
	padding: 2px 4px;
}

#scrollAreaWidgetContents QLineEdit {
	background-color: #eeeeee;
	color: #111111;
	padding: 2px 4px;
	border-radius: 4px;
}

#headerWidget QLabel {
	padding: 2px 4px;
	font-size: 20px;
    border-radius: 6px;
	color: #dddddd;
}

#headerWidget QToolButton {
	border-radius: 12px;
	border: 1px solid #111111;
}

#headerWidget QToolButton:hover {
	border-radius: 12px;
	border: 1px solid #ff0000;
	background: #bb0000;
}

#headerWidget QToolButton:pressed {
	border-radius: 12px;
	border: 1px solid #ff0000;
	background: #ff2200;
}

#headerWidget {
	border-radius: 6px;
	background: #111111;
}

#settingWidgets {
	border-radius: 6px;
	background: #111111;
}

#scrollAreaWidgetContents {
	border-radius: 6px;
	background: #111111;
}

#scrollAreaWidgetContents QComboBox {
	padding-left: 4px;
    color: #000000;
	background: #dddddd;
	font-family: "Segoe UI";
	font-size: 12px;
	border: 2px solid #dddddd; 
	border-radius: 6px;
}

#scrollAreaWidgetContents QComboBox:hover {
	border-style: solid; 
	border-radius: 6px; 
}

#scrollAreaWidgetContents QComboBox:pressed {
	border-style: solid; 
	border-radius: 6px;
}

#scrollAreaWidgetContents QComboBox QAbstractItemView {
    color: white;
    background-color: #474349;
    selection-background-color: #105758; 
    border: none;
}

#scrollAreaWidgetContents QComboBox:focus {
}

#scrollAreaWidgetContents QComboBox::drop-down:button
{
    border: none;
    padding: 0;
    width: 0;
}
"""
styles5 = """
* {
	border: none;
    padding: 0px;
    margin: 0px;
    background-color: none;
	font-family: "Segoe UI";
    font-size: 16px;
}

#centralwidget {
    background: transparent;
}

#centerwidget {
    background: transparent;
}

#searchArea {
    background: transparent;
}

#footer {
    background: transparent;
}

QWidget {
	background: #111111;
}


QScrollBar:vertical {
    width: 4px;
    margin: 10px 0px 10px 0px;
}

QScrollBar:horizontal {
    height: 4px;
    margin: 0px 40px 0px 40px;
}

QScrollBar:vertical, QScrollBar:horizontal {
    background: #dddddd;
    border-radius: 2px;
}

QScrollBar::handle:vertical, QScrollBar::handle:horizontal {
    background: #424242;
    border-radius: 2px;
    min-height: 20px;
    min-width: 20px;
}

QScrollBar::handle:vertical:hover, QScrollBar::handle:horizontal:hover {
    background: #a7b308;
    border-radius: 2px;
}

QScrollBar::add-line, QScrollBar::sub-line {
    background: transparent;
}


#searchInputText {
	background: #000000;
	border: 1px solid #060606;
	color: #ffffff;
	padding: 0px 12px;
	border-top-left-radius: 0px;
    border-bottom-left-radius: 0px;
}

#footer QToolButton {
	background: #070707;
	margin: 1px 1px;
	border: 1px solid #000000;
	border-radius: 4px;
}

#searchBtn {
	background-color: #060606;
	border-top-right-radius: 0px;
    border-bottom-right-radius: 0px;
}

#searchBtn:hover {
	background-color: #222222;
}

#searchBtn:pressed {
	background-color: #000000;
	border-right: 1px solid #000000;
	border-top: 1px solid #000000;
	border-bottom: 1px solid #000000;
}

#centralwidget QPushButton {
	text-align: left;
	background: #000000;
	border: 1px solid #060606;
	color: #ffffff;
	padding: 0px 12px;
	border-top-left-radius: 0px;
    border-bottom-left-radius: 0px;
	border-top-right-radius: 0px;
    border-bottom-right-radius: 0px;
	margin-top: 6px
}

#centralwidget QPushButton:hover {
	background: #090909;
    border: 1px solid #171717;
}

#centralwidget QPushButton:focus {
    border: 1px solid #000000;
}

#closeBtn:hover {
	background: #ff0000;
}

#closeBtn:pressed {
	background: #880000;
}

#settingBtn:hover {
	background: #555500;
}

#settingBtn:pressed {
	background: #000000;
}

#resizeFrame {
	background: #070707;
	margin: 1px 1px;
	border: 1px solid #000000;
	border-radius: 4px;
}

#resizeFrame:hover {
	background: #888888;
	margin: 1px 1px;
	border: 1px solid #222222;
	border-radius: 4px;
}

#scrollAreaWidgetContents QFrame {
	background-color: #ff0000;
	border-radius: 4px;
}

#scrollAreaWidgetContents QPushButton {
	background-color: #ff0000;
	color: #ffffff;
	padding: 2px 4px;
}

#scrollAreaWidgetContents QLineEdit {
	background-color: #eeeeee;
	color: #111111;
	padding: 2px 4px;
	border-radius: 4px;
}

#headerWidget QLabel {
	padding: 2px 4px;
	font-size: 20px;
    border-radius: 6px;
	color: #dddddd;
}

#headerWidget QToolButton {
	border-radius: 12px;
	border: 1px solid #111111;
}

#headerWidget QToolButton:hover {
	border-radius: 12px;
	border: 1px solid #ff0000;
	background: #bb0000;
}

#headerWidget QToolButton:pressed {
	border-radius: 12px;
	border: 1px solid #ff0000;
	background: #ff2200;
}

#headerWidget {
	border-radius: 6px;
	background: #111111;
}

#settingWidgets {
	border-radius: 6px;
	background: #111111;
}

#scrollAreaWidgetContents {
	border-radius: 6px;
	background: #111111;
}

#scrollAreaWidgetContents QComboBox {
	padding-left: 4px;
    color: #000000;
	background: #dddddd;
	font-family: "Segoe UI";
	font-size: 12px;
	border: 2px solid #dddddd; 
	border-radius: 6px;
}

#scrollAreaWidgetContents QComboBox:hover {
	border-style: solid; 
	border-radius: 6px; 
}

#scrollAreaWidgetContents QComboBox:pressed {
	border-style: solid; 
	border-radius: 6px;
}

#scrollAreaWidgetContents QComboBox QAbstractItemView {
    color: white;
    background-color: #474349;
    selection-background-color: #105758; 
    border: none;
}

#scrollAreaWidgetContents QComboBox:focus {
}

#scrollAreaWidgetContents QComboBox::drop-down:button
{
    border: none;
    padding: 0;
    width: 0;
}
"""

styles = [styles1, styles2, styles3, styles4, styles5]