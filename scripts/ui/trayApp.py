import os
import sys
from PySide2 import QtWidgets
from PySide2 import QtGui


# TODO !Add multithreading to fix UI being blocked when bot is running
class BotTray(QtWidgets.QSystemTrayIcon):
    def __init__(self, icon, bot, tokken, parent=None):
        super(BotTray, self).__init__(icon=icon, parent=parent)

        self.setToolTip("KanaBot")
        self.bot = bot
        self.tokken = tokken

        self.createActions()
        self.createWidgets()
        self.createConnections()

    def createActions(self):
        self.startBotAction = QtWidgets.QAction("Activate bot")
        self.stopBotAction = QtWidgets.QAction("Stop bot")

    def createWidgets(self):
        self.mainMenu = QtWidgets.QMenu(self.parent())
        self.mainMenu.addAction(self.startBotAction)
        self.mainMenu.addAction(self.stopBotAction)

        self.setContextMenu(self.mainMenu)

    def createConnections(self):
        # Actions
        self.startBotAction.triggered.connect(self.startBot)
        self.startBotAction.triggered.connect(self.bot.logout)
        # Tray
        self.activated.connect(self.onTrayIconActivated)

    def onTrayIconActivated(self, reason):
        pass

    def startBot(self):
        try:
            self.bot.run(self.tokken)
            self.showMessage("KanaBot", "Running...")
        except Exception as e:
            print("Failed to start Kana Bot")
            e.with_traceback()


def runTray(bot, tokken):
    app = QtWidgets.QApplication(sys.argv)
    mainWidget = QtWidgets.QWidget()
    tray = BotTray(QtGui.QIcon("images/trayIcon.jpg"), bot, tokken, mainWidget)
    tray.show()
    sys.exit(app.exec_())
