# Import QApplication and the required widgets from PyQt5.QtWidgets
from PyQt5.QtWidgets import QComboBox, QListWidget, QListWidgetItem, QMainWindow, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtWidgets import QWidget, QCompleter

from PyQt5.QtCore import Qt, QStringListModel


# Create a subclass of QMainWindow to setup the calculator's GUI
class PyUi(QMainWindow):
    qualityItems = ["Quality", "Bronze", "Silver", "Gold", "Special"]
    rarityItems = ["Rarity", "Common", "Rare", "TOTW", "Adidas", "Conmebol", "Heroes", "Headliners",
                    "Ones To Watch" , "Record Breaker", "Rule Breaker", "Signature Signings", "Icons",
                    "Squad Foundations", "UCL Road to the knockouts", "UECL Road to the knockouts",
                    "UEL Road to the knockouts", "UECL Road team of the tournament", 
                    "UCL Road team of the tournament", "UEL Road team of the tournament", 
                    "Wildcard token", "Winter Wildcards"]

    """PyCalc's View (GUI)."""
    def __init__(self):
        """View initializer."""
        super().__init__()
        # Set some main window's properties
        self.setWindowTitle('FIFA ULTIMATE TEAM')
        self.setFixedSize(500, 300)
        # Set the central widget and the general layout
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        # Create the display and the buttons
        self._createPlayerNameBox()
        self._playerChoiceBox()
        self._createQualityMenu()
        self._createRarityMenu()
        self._createMaxPriceBox()
        self._createSearchBtn()

    def _createPlayerNameBox(self):
        """Create the Edit Box for player name."""
        self.playerName = QLineEdit()
        self.playerName.setFixedHeight(35)
        self.playerName.setAlignment(Qt.AlignLeft)
        self.playerName.setPlaceholderText("Type player name")
        
        self.completer = QCompleter()
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.playerName.setCompleter(self.completer)

        self.model = QStringListModel()
        self.completer.setModel(self.model)
        self.completer.setCompletionPrefix("")

        # Add the display to the general layout
        self.generalLayout.addWidget(self.playerName)

    def _playerChoiceBox(self):
        self.choice = QListWidget()
        self.choice.setFixedSize(475, 82)
        self.choice.hide()
        self.setStyleSheet("QListWidget {margin: 10px;}")

        self.generalLayout.addWidget(self.choice)

    def _createQualityMenu(self):
        """Create the Player Quality drop down menu."""
        self.quality = QComboBox()
        self.quality.addItems(self.qualityItems)
        self.generalLayout.addWidget(self.quality)

    def _createRarityMenu(self):
        """Create the Player Card Rarity drop down menu."""
        self.rarity = QComboBox()
        self.rarity.addItems(self.rarityItems)
        self.generalLayout.addWidget(self.rarity)

    def _createMaxPriceBox(self):
        """Create the Edit Box for max price."""
        self.maxPrice = QLineEdit()
        self.maxPrice.setFixedHeight(35)
        self.maxPrice.setAlignment(Qt.AlignLeft)
        self.maxPrice.setPlaceholderText("ANY")
        # Add the display to the general layout
        self.generalLayout.addWidget(self.maxPrice)

    def _createSearchBtn(self):
        """Create the Search button."""
        self.search = QPushButton('Search')
        self.search.setFixedSize(150, 42)
        self.generalLayout.addWidget(self.search, alignment=Qt.AlignCenter)

    def AddCompleter(self, players):
        self.choice.clear()

        for p in players:
            item = QListWidgetItem()
            item.setText(p[1] + " " + str(p[4]) if p[1] != None else p[2] + " " + p[3] + " " + str(p[4]))
            item.setData(1, p[0])
            self.choice.addItem(item)       
