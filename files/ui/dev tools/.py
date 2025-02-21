/*RADIOBUTTON*/
.QRadioButton {{
    min-height: 30px;
    max-height: 30px;
}}

.QRadioButton::indicator {{
    width: 22px;
    height: 22px;
    border-radius: 13px;
    border: 2px solid #999999;
    background-color: rgba(0, 0, 0, 5);
    margin-right: 5px;
}}

.QRadioButton::indicator:hover {{
    background-color: rgba(0, 0, 0, 0);
}}

.QRadioButton::indicator:pressed {{
    background-color: rgba(0, 0, 0, 5);
    border: 2px solid #bbbbbb;
    image: url(:/RadioButton/img light/RadioButton.png);
}}

.QRadioButton::indicator:checked {{
    background-color: {accent_color};
    border: 2px solid {accent_color};
    image: url(:/RadioButton/img light/RadioButton.png);
    color: rgb(255, 255, 255);
}}

.QRadioButton::indicator:checked:hover {{
    image: url(:/RadioButton/img light/RadioButtonHover.png);
}}

.QRadioButton::indicator:checked:pressed {{
    image: url(:/RadioButton/img light/RadioButtonPressed.png);
}}

.QRadioButton:disabled {{
    color: rgba(0, 0, 0, 110);
}}

.QRadioButton::indicator:disabled {{
    border: 2px solid #bbbbbb;
    background-color: rgba(0, 0, 0, 0);
}}
			
        /*CHECKBOX*/
        .QCheckBox {{
            min-height: 30px;
            max-height: 30px;
        }}

        .QCheckBox::indicator {{
            width: 22px;
            height: 22px;
            border-radius: 5px;
            border: 2px solid #999999;
            background-color: rgba(0, 0, 0, 0);
            margin-right: 5px;
        }}

        .QCheckBox::indicator:hover {{
            background-color: rgba(0, 0, 0, 15);
        }}

        .QCheckBox::indicator:pressed {{
            background-color: rgba(0, 0, 0, 24);
            border: 2px solid #bbbbbb;
        }}

        .QCheckBox::indicator:checked {{
            background-color: {accent_color};
            border: 2px solid {accent_color};
            image: url(:/CheckBox/img light/CheckBox.png);
            color: rgb(255, 255, 255);
        }}

        .QCheckBox::indicator:checked:pressed {{
            image: url(:/CheckBox/img light/CheckBoxPressed.png);
        }}

        .QCheckBox:disabled {{
            color: rgba(0, 0, 0, 110);
        }}

        .QCheckBox::indicator:disabled {{
            border: 2px solid #bbbbbb;
            background-color: rgba(0, 0, 0, 0);
        }}

