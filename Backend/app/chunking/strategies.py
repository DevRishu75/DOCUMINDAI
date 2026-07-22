from app.chunking.splitter import CharacterSplitter

class SplitterFactory:

    @staticmethod
    def get_splitter(stratergy:str = "character"):
        if stratergy == "character":
            return CharacterSplitter()
        raise ValueError(f"Unknown split stratergy used {stratergy}")