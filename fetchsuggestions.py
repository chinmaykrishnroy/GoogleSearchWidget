from PySide6.QtCore import QThread, Signal
import requests


class FetchSuggestionsThread(QThread):
    suggestions_fetched = Signal(list)

    def __init__(self, query, max_suggestion=5, language='en', client_type='chrome', region='IN'):
        super().__init__()
        self.query = query
        self.max_suggestion = max_suggestion
        self.language = language
        self.client_type = client_type
        self.region = region

    def run(self):
        try:
            url = (f"https://suggestqueries.google.com/complete/search?client={self.client_type}&hl={self.language}&gl={self.region}&q={requests.utils.quote(self.query)}")
            # print(f"Fetching suggestions from URL: {url}")

            response = requests.get(url)
            # print(f"Response Status Code: {response.status_code}")

            if response.status_code == 200:
                # print(f"Response Content: {response.text}")
                try:
                    suggestions = response.json()[1]
                    # print(f"Suggestions: {suggestions}")
                    self.suggestions_fetched.emit(
                        suggestions[:self.max_suggestion])
                except (IndexError, ValueError) as parse_error:
                    # print(f"Error parsing response: {parse_error}")
                    self.suggestions_fetched.emit([])
            else:
                # print(f"Unexpected response status: {response.status_code}")
                self.suggestions_fetched.emit([])
        except requests.exceptions.RequestException as e:
            # print(f"Network Error fetching suggestions: {e}")
            self.suggestions_fetched.emit([])
        except Exception as e:
            # print(f"General Error fetching suggestions: {e}")
            self.suggestions_fetched.emit([])
