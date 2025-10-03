"""
Simple tests for Dragon Jump game mechanics
Run with: python test_game.py
"""

class MockCanvas:
    def __init__(self):
        self.width = 800
        self.height = 600

class MockContext:
    def __init__(self):
        self.fillStyle = None
    def fillRect(self, x, y, w, h): pass
    def beginPath(self): pass
    def arc(self, x, y, r, start, end): pass
    def fill(self): pass

class MockDocument:
    def getElementById(self, id):
        canvas = MockCanvas()
        canvas.getContext = lambda x: MockContext()
        return canvas

class MockWindow:
    innerWidth = 800
    innerHeight = 600
    def updateScore(self, score): pass
    def getTheme(self): return 'light'
    def showGameOver(self, score): pass
    def setContrast(self, enabled): pass

# Mock the JS imports
import sys
sys.modules['js'] = type('MockJS', (), {
    'document': MockDocument(),
    'window': MockWindow(),
    'requestAnimationFrame': lambda x: None
})()

# Now import and test the game
from game import DragonJump

def test_dragon_jump():
    game = DragonJump()
    
    # Test initial state
    assert game.dragon['x'] == 100
    assert game.dragon['on_ground'] == True
    assert game.score == 0
    
    # Test jump
    game.jump()
    assert game.dragon['vel_y'] < 0
    assert game.dragon['on_ground'] == False
    
    # Test physics
    game.update()
    assert game.dragon['vel_y'] > -18
    
    # Test spawning
    game.spawn_obstacle()
    game.spawn_coin()
    assert len(game.obstacles) > 0
    assert len(game.coins) > 0
    
    # Test collision detection
    game.dragon['x'] = game.obstacles[0]['x']
    game.dragon['y'] = game.obstacles[0]['y']
    game.check_collisions()
    assert game.game_over_state == True
    
    print("✅ All core mechanics tested!")

if __name__ == "__main__":
    test_dragon_jump()