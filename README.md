# Google Search Widget with Voice Search

This project is a **Google Search Widget** built with **PySide6** that provides a streamlined, always-accessible user interface for performing Google searches. It supports voice search, customizable settings, and dynamic search suggestions. The widget integrates seamlessly with the default web browser to display search results and offers an aesthetically pleasing, modern interface.

## Description

The Google Search Widget allows you to perform Google searches directly from your desktop without opening a full browser. With a lightweight design, the widget features voice search, dynamic suggestions, customizable opacity, and other settings for enhanced usability. This application is highly customizable, enabling users to adjust the number of search suggestions, search language, and region preferences.

## Technology Used

- **PySide6**: Used for creating the graphical user interface (GUI).
- **Python**: The core programming language.
- **SpeechRecognition**: Used for voice search functionality (converting speech to text).
- **Multithreading**: For dynamically fetching search suggestions without blocking the user interface.
- **Web Browser Integration**: To open search results in the user's default browser.

## Use Case

This widget is perfect for users who want a lightweight, always-on-bottom search bar for quick searches on Google. The voice search feature makes it particularly useful for those who prefer hands-free operation, and the customizable UI can adapt to different work environments.

### Example Use Cases:
- Quickly perform searches while multitasking without opening a full web browser.
- Use voice commands to search for information without typing.
- Customize the widget to fit your desktop environment (e.g., setting transparency or adjusting the number of search suggestions).

## Features

- **Google Search Integration**: Perform searches directly from the widget using Google.
- **Dynamic Search Suggestions**: Provides real-time search suggestions as you type.
- **Voice Search**: Allows you to perform searches using voice commands.
- **Customizable Settings**:
  - Adjust the number of search suggestions (default is 5).
  - Change the opacity for a semi-transparent look.
  - Set Google search parameters like language (`hl`), region (`gl`), and client type.
- **Always-On-Bottom**: The widget stays on the bottom of all windows, ensuring no interference to the full-screen app.
- **Resizable & Draggable**: Easily move or resize the widget on your screen.
- **Lightweight & Frameless Design**: Offers a clean, minimalistic UI with no window borders.
- **Persistent Settings**: Saves user preferences (e.g., opacity, suggestions limit) for future sessions.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/chinmaykrishnroy/GoogleSearchWidget.git
   cd GoogleSearchWidget

2. Run the run.bat script for the first time:

   ```bash
   run.bat

3. Run the createshortcut.bat to generate a shortcut for the widget:

   ```bash
   createshortcut.bat

4. Use the shortcut file 'GoogleSearch' to open the widget for the next time.
5. For adding the widget to start during Windows start-up, follow:
   ```bash
   Press Win+R
   Type shell:startup
   Paste the shortcut created in the GoogleSearchWidget folder by running createshort.bat to this startup folder

## Customization

The widget offers several customization options to improve user experience and adapt to individual preferences:

- **Opacity**: 
  - You can adjust the transparency level of the widget using a slider in the settings menu. This allows the widget to blend seamlessly with your desktop background.
  
- **Search Suggestion Count**:
  - You can set the maximum number of search suggestions to be displayed when typing in the search bar. The default is set to 5 but can be customized to any number based on user preference.

- **Positioning**:
  - The widget can be freely dragged and placed anywhere on your screen. The settings state is stored and maintained even after closing the app or restarting the system.

---

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## Screenshots
![image](https://github.com/user-attachments/assets/ca2b08bb-2c9d-4477-a40f-add89e4e2efb)
![image](https://github.com/user-attachments/assets/85a0c1bc-0cc3-4e57-86f7-ec119b23a0b0)
![image](https://github.com/user-attachments/assets/e3acb12c-705d-43c4-af5e-3ad3b2f332b1)
![image](https://github.com/user-attachments/assets/4590fef2-fb4a-4b0c-b714-263f2dc64355)
