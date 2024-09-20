from widget import *
from speech2text import *
from fetchsuggestions import *
from setting import Ui_MainWindow as Ui_SettingsWindow
import webbrowser
import sys
import json


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.settings_window = QMainWindow()
        self.settings_ui = Ui_SettingsWindow()
        self.settings_ui.setupUi(self.settings_window)
        self.settings_window.setWindowFlags(Qt.FramelessWindowHint)
        self.settings_window.setAttribute(Qt.WA_TranslucentBackground)
        setting_flags = self.settings_window.windowFlags()
        self.settings_window.setWindowFlags(setting_flags | Qt.Tool |
                                            Qt.WindowStaysOnBottomHint)
        self.init_settings_window()

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        current_flags = self.windowFlags()
        self.setWindowFlags(current_flags | Qt.Tool |
                            Qt.WindowStaysOnBottomHint)
        self.loadState()
        self.show()
        self.ui.closeBtn.clicked.connect(self.exitWidget)
        self.ui.searchBtn.clicked.connect(self.start_voice_search)
        self.ui.settingBtn.clicked.connect(self.show_settings_window)
        self.settings_ui.settingCloseBtn.clicked.connect(
            self.hide_settings_window)
        self.edge_margin = 4
        self.edge_margin2 = 10
        self.resizing = False
        self.dragging = False
        self.resize_position = None
        self.drag_position = None

        self.suggestion_buttons = []
        self.current_thread = None
        self.focused_suggestion_index = -1

        self.debounce_timer = QTimer(self)
        self.debounce_timer.setSingleShot(True)
        self.debounce_timer.timeout.connect(self.fetchSuggestions)

        self.placeholder_timer = QTimer(self)
        self.placeholder_timer.setSingleShot(True)
        self.placeholder_timer.timeout.connect(
            lambda: self.ui.searchInputText.setPlaceholderText(u"Search on Google..."))

        self.ui.searchInputText.textChanged.connect(self.onTextChanged)
        self.settings_ui.autoVoiceSearchBomboBox.currentIndexChanged.connect(
            self.enable_voicesearch_redirects)
        self.settings_ui.opacityComboBox.currentIndexChanged.connect(
            self.parse_opacity)
        self.settings_ui.themeComboBox.currentIndexChanged.connect(
            self.change_theme)
        self.settings_ui.maxSuggestionComboBox.currentIndexChanged.connect(
            self.set_max_suggestions)
        self.settings_ui.languageComboBox.currentIndexChanged.connect(
            self.update_url)
        self.settings_ui.clientTypeComboBox.currentIndexChanged.connect(
            self.update_url)
        self.settings_ui.regionComboBox.currentIndexChanged.connect(
            self.update_url)
        self.base_url = "https://www.google.com/search"
        self.update_url()

    def enable_voicesearch_redirects(self):
        self.autoredirect = True if not self.settings_ui.autoVoiceSearchBomboBox.currentIndex() else False
        self.saveState()

    def change_theme(self):
        self.setStyleSheet(styles[self.settings_ui.themeComboBox.currentIndex()])
        self.saveState()

    def parse_opacity(self):
        opacity = int(self.settings_ui.opacityComboBox.currentText())/10
        self.setWindowOpacity(opacity)
        self.saveState()

    def set_max_suggestions(self):
        self.max_suggestion = int(
            self.settings_ui.maxSuggestionComboBox.currentText())
        self.saveState()

    def update_url(self):
        language_text = self.settings_ui.languageComboBox.currentText()
        client_type_text = self.settings_ui.clientTypeComboBox.currentText()
        region_text = self.settings_ui.regionComboBox.currentText()
        language = language_text.split(
            '(')[-1].split(')')[0].strip() if language_text else ''
        language = language.replace('hl=', '') if language else ''
        client_type = client_type_text.strip() if client_type_text else ''
        region = region_text.split(
            '(')[-1].split(')')[0].strip() if region_text else ''
        region = region.replace('region=', '') if region else ''
        params = []
        if language:
            params.append(f"hl={language}")
        if client_type:
            params.append(f"client={client_type}")
        if region:
            params.append(f"gl={region}")
        query_string = "&".join(params)
        if query_string:
            self.main_url = f"{self.base_url}?{query_string}"
        else:
            self.main_url = self.base_url
        self.saveState()
        # print(f"Updated URL: {self.main_url}")

    def show_settings_window(self):
        self.settings_window.show()

    def hide_settings_window(self):
        self.settings_window.hide()

    def start_voice_search(self):
        try:
            self.ui.searchBtn.setEnabled(False)
            self.voice_thread = VoiceSearchThread(self.ui)
            self.voice_thread.voice_recognized.connect(
                self.on_voice_recognized)
            self.voice_thread.start()
        except Exception as e:
            self.ui.searchBtn.setEnabled(True)
            self.ui.searchInputText.setPlaceholderText(
                u"Errors in Voice Search!")
            self.placeholder_timer.start(2000)

    def on_voice_recognized(self, query):
        self.ui.searchBtn.setEnabled(True)
        self.placeholder_timer.start(1000)
        if query != "":
            if self.autoredirect:
                self.perform_search(query)
            else:
                self.ui.searchInputText.setText(query)
        if self.voice_thread is not None and self.voice_thread.isRunning():
            self.voice_thread.quit()
            self.voice_thread.wait()

    def exitWidget(self):
        self.saveState()
        self.close()
        sys.exit()

    def onTextChanged(self):
        self.debounce_timer.start(40)
        # self.clear_suggestions()
        self.clear_focus()

    def fetchSuggestions(self):
        query = self.ui.searchInputText.text().strip()
        if query:
            if self.current_thread is not None and self.current_thread.isRunning():
                self.current_thread.quit()
                self.current_thread.wait()
            client_type_text = self.settings_ui.clientTypeComboBox.currentText().strip()
            region_text = self.settings_ui.regionComboBox.currentText()
            language_text = self.settings_ui.languageComboBox.currentText()
            language = language_text.split(
                '(')[-1].split(')')[0].strip() if language_text else ''
            language = language.replace('hl=', '') if language else ''
            region = region_text.split(
                '(')[-1].split(')')[0].strip() if region_text else ''
            region = region.replace('region=', '') if region else ''
            self.current_thread = FetchSuggestionsThread(
                query, self.max_suggestion, language=language, client_type=client_type_text, region=region
            )
            self.current_thread.suggestions_fetched.connect(
                self.update_suggestions)
            self.current_thread.start()
        else:
            self.clear_suggestions()

    def update_suggestions(self, suggestions):
        self.clear_suggestions()
        for suggestion in reversed(suggestions):
            self.add_suggestion_button(suggestion)
        self.focused_suggestion_index = -1

    def clear_suggestions(self):
        for button in self.suggestion_buttons:
            button.deleteLater()
        self.suggestion_buttons = []

    def add_suggestion_button(self, suggestion):
        if isinstance(suggestion, str):
            suggestion_text = suggestion
        elif isinstance(suggestion, list) and len(suggestion) > 0:
            suggestion_text = suggestion[0]
        else:
            suggestion_text = 'Unknown Format'
        button = QPushButton(suggestion_text, self.ui.centralwidget)
        button.setMinimumSize(QSize(0, 34))
        button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        button.clicked.connect(lambda: self.perform_search(suggestion))
        self.ui.verticalLayout.insertWidget(2, button)
        self.suggestion_buttons.append(button)

    def perform_search(self, query):
        url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
        webbrowser.open(url)

    def clear_focus(self):
        for button in self.suggestion_buttons:
            button.clearFocus()
        self.focused_suggestion_index = -1

    def update_focus(self):
        for i, button in enumerate(self.suggestion_buttons):
            if i == self.focused_suggestion_index:
                button.setFocus()
            else:
                button.clearFocus()

    def closeEvent(self, event):
        if self.current_thread is not None and self.current_thread.isRunning():
            self.current_thread.quit()
            self.current_thread.wait()
        event.accept()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Down:
            if self.suggestion_buttons:
                self.focused_suggestion_index = (
                    self.focused_suggestion_index + 1) % len(self.suggestion_buttons)
                self.update_focus()

        elif event.key() == Qt.Key_Up:
            if self.suggestion_buttons:
                self.focused_suggestion_index = (
                    self.focused_suggestion_index - 1) % len(self.suggestion_buttons)
                self.update_focus()

        elif event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            if 0 <= self.focused_suggestion_index < len(self.suggestion_buttons):
                self.perform_search(
                    self.suggestion_buttons[self.focused_suggestion_index].text())
            else:
                self.perform_search(self.ui.searchInputText.text().strip())

    def mousePressEvent(self, event):
        rect = self.rect()
        if (
                rect.topLeft().x() + self.edge_margin >= event.position().x()
                or rect.bottomRight().x() - self.edge_margin <= event.position().x()
                or rect.topLeft().y() + self.edge_margin >= event.position().y()
                or rect.bottomRight().y() - self.edge_margin <= event.position().y()
        ):
            self.resizing = True
            self.dragging = False
            self.resize_position = event.globalPosition().toPoint()
        else:
            self.resizing = False
            self.dragging = True
            self.drag_position = event.globalPosition().toPoint() - self.pos()

    def mouseMoveEvent(self, event):
        self.unsetCursor()
        if self.resizing:
            delta = event.globalPosition().toPoint() - self.resize_position
            new_width = max(self.width() + delta.x(), 100)
            new_height = max(self.height(), 100)
            self.resize(new_width, new_height)
            self.resize_position = event.globalPosition().toPoint()
            self.setCursor(Qt.SizeFDiagCursor)
        elif self.dragging:
            self.move(event.globalPosition().toPoint() - self.drag_position)
            self.setCursor(Qt.SizeAllCursor)

    def mouseReleaseEvent(self, event):
        self.resizing = False
        self.dragging = False
        self.unsetCursor()

    def init_settings_window(self):
        self.settings_window.mousePressEvent = self.settings_window_mousePressEvent
        self.settings_window.mouseMoveEvent = self.settings_window_mouseMoveEvent
        self.settings_window.mouseReleaseEvent = self.settings_window_mouseReleaseEvent

        self.settings_window.resizing = False
        self.settings_window.dragging = False
        self.settings_window.resize_position = None
        self.settings_window.drag_position = None

    def settings_window_mousePressEvent(self, event):
        rect = self.settings_window.rect()
        if (
                rect.topLeft().x() + self.edge_margin2 >= event.position().x()
                or rect.bottomRight().x() - self.edge_margin2 <= event.position().x()
                or rect.topLeft().y() + self.edge_margin2 >= event.position().y()
                or rect.bottomRight().y() - self.edge_margin2 <= event.position().y()
        ):
            self.settings_window.resizing = True
            self.settings_window.dragging = False
            self.settings_window.resize_position = event.globalPosition().toPoint()
        else:
            self.settings_window.resizing = False
            self.settings_window.dragging = True
            self.settings_window.drag_position = event.globalPosition().toPoint() - \
                self.settings_window.pos()

    def settings_window_mouseMoveEvent(self, event):
        self.settings_window.unsetCursor()
        if self.settings_window.resizing:
            delta = event.globalPosition().toPoint() - self.settings_window.resize_position
            new_width = max(self.settings_window.width() + delta.x(), 100)
            new_height = max(self.settings_window.height() + delta.y(), 100)
            self.settings_window.resize(new_width, new_height)
            self.settings_window.resize_position = event.globalPosition().toPoint()
            self.settings_window.setCursor(Qt.SizeFDiagCursor)
        elif self.settings_window.dragging:
            self.settings_window.move(event.globalPosition(
            ).toPoint() - self.settings_window.drag_position)
            self.settings_window.setCursor(Qt.SizeAllCursor)

    def settings_window_mouseReleaseEvent(self, event):
        self.settings_window.resizing = False
        self.settings_window.dragging = False
        self.settings_window.unsetCursor()

    def saveState(self):
        state = {
            'opacity': self.settings_ui.opacityComboBox.currentIndex(),
            'suggestion_count': self.settings_ui.maxSuggestionComboBox.currentIndex(),
            'language': self.settings_ui.languageComboBox.currentIndex(),
            'client_type': self.settings_ui.clientTypeComboBox.currentIndex(),
            'region': self.settings_ui.regionComboBox.currentIndex(),
            'autoredirect': self.settings_ui.autoVoiceSearchBomboBox.currentIndex(),
            'theme': self.settings_ui.themeComboBox.currentIndex(),
        }
        with open('.state.json', 'w') as f:
            json.dump(state, f)

    def loadState(self):
        default_opacity_index = 5
        default_suggestion_index = 4
        default_language_index = 0
        default_client_type_index = 1
        default_region_index = 4
        autoredirect_index = 0
        default_theme_index = 0
        try:
            with open('.state.json', 'r') as f:
                state = json.load(f)
                self.default_opacity_index = state.get(
                    'opacity', default_opacity_index)
                self.max_suggestion_index = state.get(
                    'suggestion_count', default_suggestion_index)
                self.language_index = state.get(
                    'language', default_language_index)
                self.client_type_index = state.get(
                    'client_type', default_client_type_index)
                self.region_index = state.get('region', default_region_index)
                self.autoredirect_index = state.get(
                    'autoredirect', autoredirect_index)
                self.default_theme_index = state.get(
                    'theme', default_theme_index)
        except FileNotFoundError:
            self.default_opacity_index = default_opacity_index
            self.max_suggestion_index = default_suggestion_index
            self.language_index = default_language_index
            self.client_type_index = default_client_type_index
            self.region_index = default_region_index
            self.autoredirect_index = autoredirect_index
            self.default_theme_index = default_theme_index


        self.settings_ui.maxSuggestionComboBox.setCurrentIndex(
            self.max_suggestion_index)
        self.settings_ui.opacityComboBox.setCurrentIndex(
            self.default_opacity_index)
        self.settings_ui.languageComboBox.setCurrentIndex(self.language_index)
        self.settings_ui.clientTypeComboBox.setCurrentIndex(
            self.client_type_index)
        self.settings_ui.regionComboBox.setCurrentIndex(self.region_index)
        self.settings_ui.autoVoiceSearchBomboBox.setCurrentIndex(
            self.autoredirect_index)
        self.settings_ui.themeComboBox.setCurrentIndex(
            self.default_theme_index)
        
        self.change_theme()
        self.enable_voicesearch_redirects()
        self.parse_opacity()
        self.set_max_suggestions()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    width, height = app.primaryScreen().size().toTuple()
    window = MainWindow()
    window_width = window.frameGeometry().width()
    window_height = window.frameGeometry().height()
    x = (width - window_width) // 2
    y = ((height-window_height) * 1) // 10
    window.move(x, y)
    window.show()
    window.lower()
    sys.exit(app.exec())
