import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPalette, QFont
from user_signup import User_SignUpPage
from admin_signup import Admin_SignUpPage
from user_dashboard import user_MainWindow

class LoginPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Smart City Management - Login")
        self.setGeometry(300, 100, 1400, 900)  # Adjusted window size for a laptop-like experience
        self.setFixedSize(1400, 900)  # Fixed window size
        self.setStyleSheet("background-color: #2C3E50;")  # Set background color

        # Apply custom theme and font
        self.setTheme()
        
        # Create UI elements
        self.create_widgets()

    def setTheme(self):
        # Set palette for modern dark theme
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#2C3E50"))
        palette.setColor(QPalette.Button, QColor("#3498DB"))
        palette.setColor(QPalette.Highlight, QColor("#1ABC9C"))
        palette.setColor(QPalette.ButtonText, QColor("#FFFFFF"))
        self.setPalette(palette)

        # Set font for the whole window
        font = QFont("Arial", 12)
        self.setFont(font)
        
    def create_widgets(self):
        # Main layout
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignCenter)

        # Title Label
        title_label = QLabel("Welcome to the Smart City Management System")
        title_label.setStyleSheet("font-size: 20px; font-weight: bold; color: white;")
        main_layout.addWidget(title_label)

        # Create form layout for input fields
        form_layout = QVBoxLayout()
        
        # Username field
        username_label = QLabel("Cnic:")
        username_label.setStyleSheet("color: white; font-size: 14px;")
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter your Cnic")
        self.username_input.setStyleSheet(self.input_style())
        
        # Password field
        password_label = QLabel("Password:")
        password_label.setStyleSheet("color: white; font-size: 14px;")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter your password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setStyleSheet(self.input_style())
        
        # User type selection (ComboBox)
        user_type_label = QLabel("Select User Type:")
        user_type_label.setStyleSheet("color: white; font-size: 14px;")
        self.user_type_combo = QComboBox()
        self.user_type_combo.addItems(["Citizen", "Admin"])
        self.user_type_combo.setStyleSheet(self.input_style())

        # Login Button
        self.login_button = QPushButton("Login")
        self.login_button.setStyleSheet(self.button_style())
        self.login_button.clicked.connect(self.check_credentials)

        # Sign Up Button
        self.signup_button = QPushButton("Sign Up")
        self.signup_button.setStyleSheet(self.button_style())
        self.signup_button.clicked.connect(self.go_to_signup)

        # Add widgets to form layout
        form_layout.addWidget(username_label)
        form_layout.addWidget(self.username_input)
        form_layout.addWidget(password_label)
        form_layout.addWidget(self.password_input)
        form_layout.addWidget(user_type_label)
        form_layout.addWidget(self.user_type_combo)
        form_layout.addWidget(self.login_button)
        form_layout.addWidget(self.signup_button)

        main_layout.addLayout(form_layout)
        
        # Set the main layout for the window
        self.setLayout(main_layout)

    def input_style(self):
        return """
            background-color: #34495E;
            color: white;
            border-radius: 10px;
            padding: 10px;
            font-size: 14px;
            margin-bottom: 15px;
        """

    def button_style(self):
        return """
            background-color: #3498DB;
            color: white;
            border-radius: 10px;
            padding: 15px;
            font-size: 16px;
            font-weight: bold;
            transition: background-color 0.3s ease;
        """
    
    def check_credentials(self):
        username = self.username_input.text()
        password = self.password_input.text()
        user_type = self.user_type_combo.currentText()

        if not username or not password:
            self.show_error_message("Please enter both username and password.")
            return

        if user_type == 'Citizen':
            self.varify_citizen(username, password)
        else:
            self.varify_admin(username, password)

    def varify_citizen(self, username, password):
        # Check if the user exists in the database

        self.go_to_user_dashboard()

    def varify_admin(self, username, password):
        # Check if the admin exists in the database
        self.go_to_admin_dashboard()

    def show_error_message(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle("Login Error")
        msg.setStyleSheet("background-color: #E74C3C; color: white; font-size: 14px;")
        msg.exec_()

    def show_success_message(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.setWindowTitle("Login Successful")
        msg.setStyleSheet("background-color: #2ECC71; color: white; font-size: 14px;")
        msg.exec_()
    
    def go_to_signup(self):
        # Create a custom QMessageBox
        message_box = QMessageBox(self)
        message_box.setWindowTitle("Sign Up")
        message_box.setText("Are you an Admin or User?")
        
        # Add custom buttons
        admin_button = message_box.addButton("Admin", QMessageBox.ActionRole)
        user_button = message_box.addButton("User", QMessageBox.ActionRole)
        
        # Display the message box
        message_box.exec_()
        self.signup_page = User_SignUpPage()

        # Check which button was clicked
        if message_box.clickedButton() == admin_button:
            print("Admin selected.")
            self.signup_page = Admin_SignUpPage()  # Navigate to AdminSignUpPage
        elif message_box.clickedButton() == user_button:
            print("User selected.")
            self.signup_page = User_SignUpPage()  # Navigate to UserSignUpPage

        # Show the signup page
        self.signup_page.show()
        self.close()

    def go_to_user_dashboard(self):
        self.dashboard = user_MainWindow()
        self.dashboard.show()
        self.close()
    
    def go_to_admin_dashboard(self):
        pass