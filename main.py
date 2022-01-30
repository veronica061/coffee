import sys
import sqlite3

from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import *
from PyQt5 import uic


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('coffee.sqlite')
        db.open()

        view = QTableView(self)
        model = QSqlTableModel(self, db)
        model.setTable('coffee')
        model.select()

        view.setModel(model)
        view.move(10, 10)
        view.resize(1480, 315)

        self.setGeometry(300, 100, 1500, 450)
        self.setWindowTitle('Эспрессо')

        self.pushButton = QPushButton(self)
        self.pushButton.move(10, 340)
        self.pushButton.setText('Добавить')
        self.pushButton.clicked.connect(self.add)
        self.show()

    def add(self):
        self.addcoffee = AddCoffee()
        self.addcoffee.show()


class AddCoffee(QMainWindow):
    def __init__(self):
        super(AddCoffee, self).__init__()
        self.setGeometry(300, 100, 500, 500)
        self.label = QLabel(self)
        self.label1 = QLabel(self)
        self.label2 = QLabel(self)
        self.label3 = QLabel(self)
        self.label4 = QLabel(self)
        self.label5 = QLabel(self)
        self.label6 = QLabel(self)
        self.label.move(10, 10)
        self.label1.move(10, 60)
        self.label2.move(10, 110)
        self.label3.move(10, 160)
        self.label4.move(10, 210)
        self.label5.move(10, 260)
        self.label6.move(10, 310)
        self.label.resize(200, 100)
        self.label1.resize(200, 100)
        self.label2.resize(200, 100)
        self.label3.resize(200, 100)
        self.label4.resize(200, 100)
        self.label5.resize(200, 100)
        self.label6.resize(200, 100)
        self.label.setText('ID')
        self.label1.setText('Название сорта')
        self.label2.setText('Степень обжарки')
        self.label3.setText('Молотый/в зернах')
        self.label4.setText('Описание вкуса')
        self.label5.setText('Цена')
        self.label6.setText('Объем упаковки')
        self.ID = QLineEdit(self)
        self.sort = QLineEdit(self)
        self.degree = QLineEdit(self)
        self.type = QLineEdit(self)
        self.taste = QLineEdit(self)
        self.cost = QLineEdit(self)
        self.v = QLineEdit(self)
        self.ID.move(210, 50)
        self.sort.move(210, 100)
        self.degree.move(210, 150)
        self.type.move(210, 200)
        self.taste.move(210, 250)
        self.cost.move(210, 300)
        self.v.move(210, 350)
        self.ID.resize(250, 30)
        self.sort.resize(250, 30)
        self.degree.resize(250, 30)
        self.type.resize(250, 30)
        self.taste.resize(250, 30)
        self.cost.resize(250, 30)
        self.v.resize(250, 30)
        self.ok = QPushButton('Добавить', self)
        self.ok.move(10, 400)
        self.ok.clicked.connect(self.run)

    def run(self):
        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        coff = int(self.ID.text()), str(self.sort.text()), int(self.degree.text()), str(self.type.text()), str(
            self.taste.text()), int(self.cost.text()), int(self.v.text())
        cur.execute("""INSERT INTO coffee VALUES(?, ?, ?, ?, ?, ?, ?);""", coff)
        con.commit()
        con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())
