from arguments import Arguments
from state import State
from run import Run
from features import Features
from settings import Settings

class Network:
    def __init__(self):
        self.arguments = Arguments()
        self.state = State()
        self.run = Run()
        self.features = Features()
        self.settings = Settings()
