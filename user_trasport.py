from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QDate
from functions import table_style, tab_style

class PublicTransportBooking(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)


        header = QLabel("Public Transport Booking")
        header.setAlignment(Qt.AlignCenter)
        header.setStyleSheet("font-size: 24px; font-weight: bold; color: white;")
        layout.addWidget(header)

        self.tab_widget = QTabWidget()
        self.tab_widget.setStyleSheet(tab_style())
        
        self.init_route_search_tab()
        self.init_booking_history_tab()

        layout.addWidget(self.tab_widget)
        self.setLayout(layout)

    def init_route_search_tab(self):
        search_tab = QWidget()
        layout = QVBoxLayout(search_tab)


        search_layout = QHBoxLayout()


        source_label = QLabel("Source:")
        source_label.setStyleSheet("font-size: 14px; font-weight: bold; color: white;")
        search_layout.addWidget(source_label)

        self.source_input = QLineEdit()
        self.source_input.setPlaceholderText("Enter source location")
        search_layout.addWidget(self.source_input)

        dest_label = QLabel("Destination:")
        dest_label.setStyleSheet("font-size: 14px; font-weight: bold; color: white;")
        search_layout.addWidget(dest_label)

        self.dest_input = QLineEdit()
        self.dest_input.setPlaceholderText("Enter destination location")
        search_layout.addWidget(self.dest_input)

        # Date Picker
        date_label = QLabel("Travel Date:")
        date_label.setStyleSheet("font-size: 14px; font-weight: bold; color: white;")
        search_layout.addWidget(date_label)

        self.date_picker = QDateEdit()
        self.date_picker.setCalendarPopup(True)
        self.date_picker.setDate(QDate.currentDate())
        search_layout.addWidget(self.date_picker)

        # Search Button
        search_button = QPushButton("Search Routes")
        search_button.setStyleSheet("""
            QPushButton {
                background-color: #3498DB;
                color: white;
                padding: 10px;
                border-radius: 5px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #2980B9;
            }
        """)
        search_button.clicked.connect(self.search_routes)
        search_layout.addWidget(search_button)

        layout.addLayout(search_layout)

        self.route_table = QTableWidget()
        self.route_table.setColumnCount(5)
        self.route_table.setHorizontalHeaderLabels(["Route", "Date", "Time", "Fare", "Actions"])
        self.route_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.route_table.setStyleSheet(table_style())
        layout.addWidget(self.route_table)

        self.tab_widget.addTab(search_tab, "Route Search")  

    def init_booking_history_tab(self):
        history_tab = QWidget()
        layout = QVBoxLayout(history_tab)


        history_label = QLabel("Booking History")
        history_label.setAlignment(Qt.AlignCenter)
        history_label.setStyleSheet("font-size: 18px; font-weight: bold; color: white;")
        layout.addWidget(history_label)

        self.history_table = QTableWidget()
        self.history_table.setColumnCount(6)
        self.history_table.setHorizontalHeaderLabels(["Route", "Date", "Time", "Fare", "Status", "Actions"])
        self.history_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.history_table.setStyleSheet(table_style())
        layout.addWidget(self.history_table)


        refresh_button = QPushButton("Refresh Bookings")
        refresh_button.setStyleSheet("""
            QPushButton {
                background-color: #27AE60;
                color: white;
                padding: 10px;
                font-size: 14px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #229954;
            }
        """)
        refresh_button.clicked.connect(self.refresh_bookings)
        layout.addWidget(refresh_button)

        self.tab_widget.addTab(history_tab, "Booking History") 

    def search_routes(self):
        """Search for available routes."""
        source = self.source_input.text()
        destination = self.dest_input.text()
        travel_date = self.date_picker.date().toString("yyyy-MM-dd")

        if not source or not destination:
            QMessageBox.warning(self, "Input Error", "Please provide both source and destination.")
            return

        routes = [
            {"route": f"{source} to {destination}", "date": travel_date, "time": "10:00 AM", "fare": ""},
            {"route": f"{source} to {destination}", "date": travel_date, "time": "3:00 PM", "fare": ""},
        ]

        self.populate_table(self.route_table, routes, "Book")

    def refresh_bookings(self):
        bookings = [
            {"route": "City A to City B", "date": "2025-01-10", "time": "10:00 AM", "fare": "$15", "status": "Confirmed"},
            {"route": "City B to City A", "date": "2025-01-15", "time": "3:00 PM", "fare": "$20", "status": "Cancelled"},
        ]

        self.populate_table(self.history_table, bookings, "Cancel/Reschedule")

    def populate_table(self, table, data, action_text):
        table.setRowCount(len(data))
        for row, item in enumerate(data):
            for col, key in enumerate(["route", "date", "time", "fare", "status"]):
                table.setItem(row, col, QTableWidgetItem(item.get(key, "")))

            action_button = QPushButton(action_text)
            action_button.setStyleSheet("""
                QPushButton {
                    background-color: #E74C3C;
                    color: white;
                    padding: 5px;
                    border-radius: 5px;
                    font-size: 12px;
                }
                QPushButton:hover {
                    background-color: #C0392B;
                }
            """)
            action_button.clicked.connect(lambda _, r=row: self.handle_action(r))
            table.setCellWidget(row, len(data[0]), action_button)

    def handle_action(self, row):
        QMessageBox.information(self, "Action", f"Action triggered for row {row}.")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = PublicTransportBooking()
    window.setStyleSheet("background-color: #2C3E50; color: white;")
    window.show()
    sys.exit(app.exec_())
