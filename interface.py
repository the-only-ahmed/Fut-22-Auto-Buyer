# Import QApplication and the required widgets from PyQt5.QtWidgets
from PyQt5.QtWidgets import QComboBox, QMainWindow
from PyQt5.QtWidgets import QWidget

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout

# Create a subclass of QMainWindow to setup the calculator's GUI
class PyUi(QMainWindow):
    qualityItems = ["Quality", "Bronze", "Silver", "Gold", "Special"]
    rarityItems = ["Rarity", "Common", "Rare", "Adidas", "Conmebol", "Heroes", "Headliners", "Icons",
                    "Ones To Watch" , "Record Breaker", "Rule Breaker", "Signature Signings", 
                    "Squad Foundations", "TOTW", "UCL Road to the knockouts", "UECL Road to the knockouts",
                    "UEL Road to the knockouts", "UECL Road team of the tournament", 
                    "UCL Road team of the tournament", "UEL Road team of the tournament", 
                    "Wildcard token", "Winter Wildcards"]

    """PyCalc's View (GUI)."""
    def __init__(self):
        """View initializer."""
        super().__init__()
        # Set some main window's properties
        self.setWindowTitle('FIFA ULTIMATE TEAM')
        self.setFixedSize(500, 250)
        # Set the central widget and the general layout
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        # Create the display and the buttons
        self._createPlayerNameBox()
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
        # Add the display to the general layout
        self.generalLayout.addWidget(self.playerName)

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