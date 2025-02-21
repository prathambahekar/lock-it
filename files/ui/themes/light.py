from main import *
# module to edit/read registory
from winreg import *

# setting light theme
class UILight(MainWindow):
    # get default accent color
    def GetAccentColor(self):
        # Connect to the registry and retrieve the accent color
        registry = ConnectRegistry(None, HKEY_CURRENT_USER)
        key = OpenKey(registry, r'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Accent')
        key_value = QueryValueEx(key, 'AccentColorMenu')
        accent_int = key_value[0]
        accent = accent_int - 4278190080
        accent = str(hex(accent)).split('x')[1]
        accent = accent[4:6] + accent[2:4] + accent[0:2]  # Reorder to RGB
        return 'rgb' + str(tuple(int(accent[i:i + 2], 16) for i in (0, 2, 4)))

    # set light stylesheet
    def SetStyleSheetLight(self):
        # Define color variables
        background_color = "#f0f0f0"
        primary_color = "#ffffff"  # Light background
        secondary_color = "#f0f0f0"  # Slightly darker for contrast
        border_color = "#f0f0f0"  # Lighter border
        hover_color = "#e0e0e0"  # Hover effect color
        pressed_color = "#c0c0c0"  # Pressed effect color
        text_color = "#000000"  # Text color
        button_text_color = "#000000"  # Button text color
        header_font = "700 24pt 'Segoe UI Variable Small'"
        button_font = "600 14pt 'Segoe UI Variable Small'"
        accent_color = UILight.GetAccentColor(self)  # Use self to call the method

        # Use the accent color in the stylesheet
        self.ui.centralwidget.setStyleSheet(f"""
        /* General Styles */
        * {{
            background: transparent;
            color: rgb(0, 0, 0);
            font-size: 17px;
            font-family: "Segoe UI Variable Small", serif;
            font-weight: 400;
        }}
        
        /* Left Menu Button Styles */
        #leftMenu .QPushButton {{
            background-color: transparent;
            border-radius: 7px;
            padding: 7px;
            image-position: left center;
            font: {button_font};
            color: {button_text_color};
        }}

        #leftMenu .QPushButton:hover {{
            background-color: {hover_color};
        }}

        #leftMenu .QPushButton:pressed {{
            background-color: {pressed_color};
        }}

        /* Main Frame Styles */
        #mainFrame {{
            border: 2px solid {border_color};    
            border-radius: 7px;
        }}

        #mainFrame .QFrame, 
        #mainFrame .QLabel {{
            background-color: {primary_color};
        }}


        /* Button Icons */
        #settings_btn {{
            image: url(:/light/light/settings_48_regular.svg);
        }}

        #home_btn {{
            image: url(:/light/light/home_48_regular.svg);
        }}

        #theme_btn {{
            image: url(:/light/light/weather_sunny_48_regular.svg);
        }}

        #menu_btn {{
            image: url(:/light/light/panel_left_text_48_regular.svg);
        }}

        /* Section Header Styles */
        #stg_lbl_main {{
            padding-left: 4px;
            font: {header_font};
        }}

        /* Stack Settings */
        #stack_stg .QWidget {{
            border-radius: 8px;
            background-color: {secondary_color}; /* Updated for better contrast  */
        }}

        /* Home App Button Styles */
        #stg_home_app_bt_lbl, 
        #stg_home_info_bt_lbl {{
            font: 600 13pt "Segoe UI Variable Small";
            padding-left: 16px;
        }}

        #stg_home_app_img_lbl, 
        #stg_home_info_img_lbl {{
            padding: 17px;
        }}

        #stg_home_app_hd_lbl, 
        #stg_home_info_hd_lbl {{
            font: 900 16pt "Segoe UI Variable Small";
            padding-left: 2px;
        }}

        #stg_home_app_img_btn, 
        #stg_home_info_img_btn {{
            font: 600 14pt "Segoe UI Variable Small";
            padding-left: 4px;
            border:  0px;
        }}

        /* Page Background Colors */
        #home_page, 
        #setting_page, 
        #info_page, 
        #stg_abt_pg, 
        #stg_home_pg, 
        #stg_app_pg {{
            background-color: {primary_color};
        }}

        /* Additional styles for light theme */
        #leftMenu .QPushButton {{
            padding: 7px;
            image-position: left center;
            font: 13pt "Segoe UI Variable Small";
            color: rgb(0, 0, 0);
        }}

        


        
        """)  # End of light theme styles