self.menuBar = QMenuBar(self.centralwidget)
        self.menuBar.setEnabled(True)
        self.menuBar.setGeometry(QRect(0, 0, 980, 63))
        self.menuBar.setObjectName("menuBar")

        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuFile.setTitle("File")  # Set title for menu

        self.menuEdit = QMenu(self.menuBar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuEdit.setTitle("Edit")  # Set title for menu

        self.menuHelp = QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuHelp.setTitle("Help")  # Set title for menu

        MainWindow.setMenuBar(self.menuBar)

        self.actionNew = QAction("New", MainWindow)  # Create action for "New"
        self.actionNew.setObjectName("actionNew")

        self.actionPlain_Text_Document = QAction("Plain Text Document", MainWindow)
        self.actionPlain_Text_Document.setObjectName("actionPlain_Text_Document")

        self.actionRich_Text_Document = QAction("Rich Text Document", MainWindow)
        self.actionRich_Text_Document.setObjectName("actionRich_Text_Document")

        self.actionOpen = QAction("Open", MainWindow)
        self.actionOpen.setObjectName("actionOpen")

        self.actionSave = QAction("Save", MainWindow)
        self.actionSave.setEnabled(True)
        self.actionSave.setObjectName("actionSave")

        self.actionExit = QAction("Exit", MainWindow)
        self.actionExit.setObjectName("actionExit")

        self.actionUndo = QAction("Undo", MainWindow)
        self.actionUndo.setObjectName("actionUndo")

        self.actionCut = QAction("Cut", MainWindow)
        self.actionCut.setObjectName("actionCut")

        self.actionCopy = QAction("Copy", MainWindow)
        self.actionCopy.setObjectName("actionCopy")

        self.actionPaste = QAction("Paste", MainWindow)
        self.actionPaste.setObjectName("actionPaste")

        self.actionAbout = QAction("About", MainWindow)
        self.actionAbout.setEnabled(True)
        self.actionAbout.setObjectName("actionAbout")

        # Create submenu for New
        self.subMenuNew = QMenu("New", MainWindow)
        self.subMenuNew.addAction(self.actionPlain_Text_Document)
        self.subMenuNew.addAction(self.actionRich_Text_Document)

        self.menuFile.addAction(self.subMenuNew.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)

        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)

        self.menuHelp.addAction(self.actionAbout)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())