import json

# Create a Controller class to connect the GUI and the model
class PyController:
    """PyCalc Controller class."""
    def __init__(self, view):
        """Controller initializer."""
        self._view = view
        # Connect signals and slots
        self._connectSignals()
        self._loadPlayers()

        print(self._view.search.text)

    def _loadPlayers(self):
        # Opening JSON file
        f = open('players.json')
        data = json.load(f)

        self.playersDB = {}
        for player in data['LegendsPlayers']:
            self.playersDB[player['id']] = (player['f'] + " " + player['l'], player['r'])
        for player in data['Players']:
            self.playersDB[player['id']] = (player['f'] + " " + player['l'], player['r'])
        
        # Closing file
        f.close()

    def _makeSearch(self):
        """Search for players."""
        print ('ahmed')

    def _connectSignals(self):
        """Connect signals and slots."""
        self._view.search.clicked.connect(self._makeSearch)
