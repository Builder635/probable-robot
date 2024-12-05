import UI


if __name__ == '__main__':
    app = UI.QApplication(UI.sys.argv)
    ex = UI.YellowCircle()
    ex.show()
    UI.sys.exit(app.exec())
