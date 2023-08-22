class TestScreen():
    def __init__(self, screenVar):
        self.screen = screenVar

    def handle_events(self):
        pass

    def update(self):
        pass

    def draw(self):
        self.screen.fill((255, 255, 255))
