from app.chunking.splitter import CharacterSplitter

class SplitterFactorty:
    '''creates the appropriate splitter'''

    @staticmethod
    def getSplitter(stratergy:str = "character"):
        if stratergy == "character":
            return CharacterSplitter()
        raise ValueError( {f"Unknown splitting stratergy{stratergy}"})

