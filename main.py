from PyQt6.QtWidgets import QWidget, QApplication

import sys

app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = QWidget()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.
window.setWindowTitle('PDF maker')

app.exec()