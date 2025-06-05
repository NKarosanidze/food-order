import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout,
    QCheckBox, QLineEdit, QPushButton, QMessageBox
)


class FoodOrderApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("საჭმლის გამოძახება")
        self.setGeometry(200, 200, 450, 450)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()


        self.address_label = QLabel("ჩაწერე მისამართი:")
        self.address_input = QLineEdit()
        layout.addWidget(self.address_label)
        layout.addWidget(self.address_input)


        self.phone_label = QLabel("შეიყვანე ტელეფონის ნომერი:")
        self.phone_input = QLineEdit()
        self.phone_input.setPlaceholderText("მაგ: 555123456")
        layout.addWidget(self.phone_label)
        layout.addWidget(self.phone_input)


        layout.addWidget(QLabel("აირჩიე საკვები:"))

        self.items = {
            "დიეტური": [
                ("სალათი", 8),
                ("ბოსტნეულის წვნიანი", 6),
                ("სმუზი", 7),
                ("ხილის ასორტი", 15)
            ],
            "არადიეტური": [
                ("ხინკალი", 10),
                ("შაურმა", 9),
                ("მწვადი", 4),
                ("ბურგერი", 6)
            ],
            "სასმელები": [
                ("კოკა-კოლა", 3),
                ("წყალი", 1),
                ("ლიმონათი", 2.5),
                ("ბორჯომი", 2.9)
            ],
            "დესერტი": [
                ("ნამცხვარი", 6),
                ("ტირამისუ", 7.5),
                ("შოკოლადი", 4.5)
            ]
        }

        self.checkboxes = []

        for category, foods in self.items.items():
            layout.addWidget(QLabel(f"{category}:"))
            for name, price in foods:
                checkbox = QCheckBox(f"{name} - {price}₾")
                checkbox.setProperty("price", price)
                checkbox.setProperty("item", name)
                self.checkboxes.append(checkbox)
                layout.addWidget(checkbox)


        self.order_button = QPushButton("შეუკვეთე")
        self.order_button.clicked.connect(self.submit_order)
        layout.addWidget(self.order_button)

        self.setLayout(layout)

    def submit_order(self):
        address = self.address_input.text().strip()
        phone = self.phone_input.text().strip()

        if not address or not phone:
            QMessageBox.warning(self, "შეცდომა", "გთხოვთ მიუთითეთ მისამართი და ნომერი.")
            return

        if not (phone.isdigit() and len(phone) >= 9):
            QMessageBox.warning(self, "ნომერი არასწორია", "გთხოვთ შეიყვანეთ სწორი ნომერი (მაგ: 555123456).")
            return

        selected_items = []
        total_price = 0

        for checkbox in self.checkboxes:
            if checkbox.isChecked():
                name = checkbox.property("item")
                price = checkbox.property("price")
                selected_items.append(f"{name} - {price}₾")
                total_price += price

        if not selected_items:
            QMessageBox.warning(self, "შეცდომა", "გთხოვთ აირჩიოთ საკვები.")
            return

        summary = (
            f"შეკვეთა მიღებულია!\n"
            f"მისამართი: {address}\n"
            f"ტელეფონი: {phone}\n\n"
            f"შერჩეული პროდუქტები:\n" + "\n".join(selected_items) +
            f"\n\nჯამური ფასი: {total_price:.2f}₾"
        )

        QMessageBox.information(self, "შეკვეთა მიღებულია", summary)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FoodOrderApp()
    window.show()
    sys.exit(app.exec_())