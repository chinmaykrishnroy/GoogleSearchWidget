styles = """
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
	background-color: #3A606E;
	border-radius: 4px;
}

#scrollAreaWidgetContents QPushButton {
	background-color: #3A606E;
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

#mediaButtonsFrame QComboBox:pressed {
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
