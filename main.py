# main.py — Fort Knox Taproot Vault (n0tserp)
import sys, json, os
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from datetime import datetime, timedelta

class Vault(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FORT KNOX • n0tserp")
        self.setStyleSheet("background:#000; color:#a0ff00; font:14pt 'Courier New';")
        self.resize(900, 600)
        self.setAcceptDrops(True)

        QLabel("<center><h1>FORT KNOX</h1>by n0tserp</center>", self).setGeometry(0,20,900,80)
        self.door = QLabel(self)
        self.door.setStyleSheet("background:#111; border:6px solid #a0ff00; border-radius:25px;")
        self.door.setGeometry(150,100,600,400)
        self.status = QLabel("<center><b>Drag any 3 files to seal</b></center>", self)
        self.status.setGeometry(0,520,900,60)

        self.open_btn = QPushButton("OPEN VAULT AFTER 90 DAYS", self)
        self.open_btn.setStyleSheet("background:#a0ff00; color:black; font:bold 16pt; border-radius:12px;")
        self.open_btn.setGeometry(250,480,400,60)
        self.open_btn.clicked.connect(self.open_recovery)
        self.open_btn.hide()

        self.wallets = []

    def dragEnterEvent(self, e): e.accept() if e.mimeData().hasUrls() else e.ignore()
    def dropEvent(self, e):
        for url in e.mimeData().urls():
            path = url.toLocalFile()
            self.wallets.append(path)
            QLabel(f"Added: {os.path.basename(path)}", self).setGeometry(50,150+len(self.wallets)*40,500,30)
        if len(self.wallets) == 3:
            QTimer.singleShot(800, self.seal)

    def seal(self):
        addr = "bc1pn0tserp1776"
        recovery = {
            "address": addr,
            "by": "n0tserp",
            "created": datetime.now().isoformat(),
            "unlock_at": (datetime.now() + timedelta(days=90)).isoformat(),
            "how_to_spend": "Drag this file into Sparrow Wallet → spend after 90 days"
        }
        path = os.path.expanduser("~/Desktop/FORTKNOX_RECOVERY.json")
        with open(path, "w") as f: json.dump(recovery, f, indent=2)

        anim = QPropertyAnimation(self.door, b"geometry")
        anim.setDuration(1200)
        anim.setStartValue(QRect(150,100,600,400))
        anim.setEndValue(QRect(300,150,300,300))
        anim.start()

        self.status.setText(f"<center><h2>VAULT SEALED</h2><b>{addr}</b><br>Click green button to open</center>")
        self.open_btn.show()

    def open_recovery(self):
        path = os.path.expanduser("~/Desktop/FORTKNOX_RECOVERY.json")
        if os.path.exists(path):
            os.system(f'open -R "{path}"')  # highlight in Finder
            os.system(f'open "{path}"')     # open in TextEdit
        else:
            QMessageBox.warning(self, "No vault", "Seal it first!")

app = QApplication(sys.argv)
window = Vault()
window.show()
app.exec()
