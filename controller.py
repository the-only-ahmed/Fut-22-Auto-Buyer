import json
import unidecode
# from interface import PyUi

# Create a Controller class to connect the GUI and the model
class PyController:
    """PyCalc Controller class."""
    def __init__(self, view):
        """Controller initializer."""
        if (view != None):
            self._view = view
            # Connect signals and slots
            self._loadPlayers()
            self._connectSignals()

    def _loadPlayers(self):
        # Opening JSON file
        f = open('players.json')
        data = json.load(f)

        self.playersDB = []
        for player in data['LegendsPlayers']:
            if 'c' in player:
                pseudo = player['c']
            else:
                pseudo = None
            p = (player['id'], pseudo, player['f'], player['l'], player['r'], "LEGEND")
            self.playersDB.append(p)
        for player in data['Players']:
            if 'c' in player:
                pseudo = player['c']
            else:
                pseudo = None
            p = (player['id'], pseudo, player['f'], player['l'], player['r'], "CURRENT")
            self.playersDB.append(p)
        
        self.playersDB.sort(key=lambda x:x[4], reverse=True)
        # Closing file
        f.close()

    def _nameSearch(self, item, name):
        if item[1] != None:
            cName = unidecode.unidecode(item[1])
            if cName.lower().startswith(name):
                return True

        firstName = unidecode.unidecode(item[2])
        lastName = unidecode.unidecode(item[3])
        if firstName.lower().startswith(name) or lastName.lower().startswith(name):
            return True

        fullName = firstName + " " + lastName
        return fullName.lower().startswith(name)

    def _makeSearchByName(self):
        """Search for players."""
        name = self._view.playerName.text().lower()
        name = unidecode.unidecode(name)
        result = []
        if name:
            self._view.choice.show()
            result = list(filter(lambda x: self._nameSearch(x, name), self.playersDB))
        else:
            self._view.choice.hide()
        self._view.AddCompleter(result[:3])

    def _makeSearchById(self, id):
        """Search for players."""
        result = list(filter(lambda x: x[0] == int(id), self.playersDB))
        return result[:3]

    def _makeSearchByRate(self, rate):
        """Search for players."""
        result = list(filter(lambda x: x[4] == int(rate), self.playersDB))
        return result[:3]

    def _playerSelected(self):
        selectedItems = self._view.choice.selectedItems()
        for item in selectedItems:
            print (item.data(1))
            print (item.text())
            self._view.playerName.setText(item.text())
            self._view.choice.hide()

    def _playerQualitySelected(self, pos):
        self._view.rarity.clear()
        if pos == 0:
            self._view.rarity.addItems(self._view.rarityItems)
        elif pos in range(1, 4):
            self._view.rarity.addItems(self._view.rarityItems[:4])
        else:
            self._view.rarity.addItem(self._view.rarityItems[0])
            self._view.rarity.addItems(self._view.rarityItems[3:])

    def _connectSignals(self):
        """Connect signals and slots."""
        self._view.playerName.textChanged.connect(self._makeSearchByName)
        self._view.choice.itemSelectionChanged.connect(self._playerSelected)
        self._view.quality.currentIndexChanged.connect(self._playerQualitySelected)
