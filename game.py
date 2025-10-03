import random
import math
import time
from js import document, window, requestAnimationFrame

class DragonJump:
    def __init__(self):
        self.canvas = document.getElementById('game-canvas')
        self.ctx = self.canvas.getContext('2d')
        self.setup_canvas()
        
        # Game state
        self.score = 0
        self.speed = 3
        self.gravity = 0.8
        self.jump_power = -18
        self.game_over_state = False
        self.contrast_mode = False
        self.contrast_timer = 0
        
        # Dragon
        self.dragon = {
            'x': 100,
            'y': 300,
            'width': 40,
            'height': 40,
            'vel_y': 0,
            'on_ground': True
        }
        
        # Obstacles and coins
        self.obstacles = []
        self.coins = []
        self.particles = []
        
        # Ground
        self.ground_y = 400
        
        # Timing
        self.last_obstacle = 0
        self.last_coin = 0
        self.last_time = time.time()
        
    def setup_canvas(self):
        self.canvas.width = window.innerWidth
        self.canvas.height = window.innerHeight
        self.ground_y = self.canvas.height - 100
        
    def start(self):
        self.spawn_obstacle()
        self.spawn_coin()
        
    def jump(self):
        if self.dragon['on_ground']:
            self.dragon['vel_y'] = self.jump_power
            self.dragon['on_ground'] = False
            self.create_particles(self.dragon['x'], self.dragon['y'] + self.dragon['height'])
            window.playSound('jump-sound')
            
    def update(self):
        current_time = time.time()
        dt = current_time - self.last_time
        self.last_time = current_time
        
        # Update dragon physics
        self.dragon['vel_y'] += self.gravity
        self.dragon['y'] += self.dragon['vel_y']
        
        # Ground collision
        if self.dragon['y'] + self.dragon['height'] >= self.ground_y:
            self.dragon['y'] = self.ground_y - self.dragon['height']
            self.dragon['vel_y'] = 0
            self.dragon['on_ground'] = True
            
        # Update obstacles
        for obstacle in self.obstacles[:]:
            obstacle['x'] -= self.speed
            if obstacle['x'] + obstacle['width'] < 0:
                self.obstacles.remove(obstacle)
                self.score += 10
                
        # Update coins
        for coin in self.coins[:]:
            coin['x'] -= self.speed
            if coin['x'] + coin['size'] < 0:
                self.coins.remove(coin)
                
        # Update particles
        for particle in self.particles[:]:
            particle['x'] += particle['vel_x']
            particle['y'] += particle['vel_y']
            particle['vel_y'] += 0.2
            particle['life'] -= dt
            if particle['life'] <= 0:
                self.particles.remove(particle)
                
        # Spawn new obstacles and coins
        if len(self.obstacles) == 0 or self.obstacles[-1]['x'] < self.canvas.width - 300:
            self.spawn_obstacle()
            
        if len(self.coins) == 0 or self.coins[-1]['x'] < self.canvas.width - 200:
            self.spawn_coin()
            
        # Check collisions
        self.check_collisions()
        
        # Increase speed over time
        self.speed += 0.001
        self.score += 0.1
        
        # Toggle contrast mode every 15 seconds
        self.contrast_timer += dt
        if self.contrast_timer >= 15:
            self.contrast_mode = not self.contrast_mode
            window.setContrast('true' if self.contrast_mode else 'false')
            self.contrast_timer = 0
        
        # Update UI
        window.updateScore(int(self.score))
        
    def spawn_obstacle(self):
        self.obstacles.append({
            'x': self.canvas.width,
            'y': self.ground_y - 60,
            'width': 30,
            'height': 60
        })
        
    def spawn_coin(self):
        self.coins.append({
            'x': self.canvas.width + random.randint(50, 200),
            'y': random.randint(200, self.ground_y - 50),
            'size': 20,
            'collected': False
        })
        
    def check_collisions(self):
        dragon_rect = self.dragon
        
        # Obstacle collision
        for obstacle in self.obstacles:
            if (dragon_rect['x'] < obstacle['x'] + obstacle['width'] and
                dragon_rect['x'] + dragon_rect['width'] > obstacle['x'] and
                dragon_rect['y'] < obstacle['y'] + obstacle['height'] and
                dragon_rect['y'] + dragon_rect['height'] > obstacle['y']):
                self.game_over()
                
        # Coin collection
        for coin in self.coins[:]:
            if not coin['collected']:
                if (dragon_rect['x'] < coin['x'] + coin['size'] and
                    dragon_rect['x'] + dragon_rect['width'] > coin['x'] and
                    dragon_rect['y'] < coin['y'] + coin['size'] and
                    dragon_rect['y'] + dragon_rect['height'] > coin['y']):
                    coin['collected'] = True
                    self.coins.remove(coin)
                    self.score += 50
                    self.create_particles(coin['x'], coin['y'], color='gold')
                    window.playSound('coin-sound')
                    
    def create_particles(self, x, y, color='white'):
        for _ in range(5):
            self.particles.append({
                'x': x,
                'y': y,
                'vel_x': random.uniform(-3, 3),
                'vel_y': random.uniform(-5, -1),
                'life': 1.0,
                'color': color
            })
            
    def game_over(self):
        self.game_over_state = True
        window.showGameOver(int(self.score))
        
    def restart(self):
        self.__init__()
        self.start()
        
    def draw(self):
        theme = window.getTheme()
        
        # Clear canvas
        if theme == 'dark':
            self.ctx.fillStyle = '#1a1a2e'
        else:
            self.ctx.fillStyle = '#87CEEB'
        self.ctx.fillRect(0, 0, self.canvas.width, self.canvas.height)
        
        # Draw ground
        if theme == 'dark':
            self.ctx.fillStyle = '#16213e'
        else:
            self.ctx.fillStyle = '#8B4513'
        self.ctx.fillRect(0, self.ground_y, self.canvas.width, self.canvas.height - self.ground_y)
        
        # Draw dragon
        self.ctx.fillStyle = '#ff6b6b'
        self.ctx.fillRect(self.dragon['x'], self.dragon['y'], self.dragon['width'], self.dragon['height'])
        
        # Draw obstacles
        self.ctx.fillStyle = '#333' if theme == 'dark' else '#654321'
        for obstacle in self.obstacles:
            self.ctx.fillRect(obstacle['x'], obstacle['y'], obstacle['width'], obstacle['height'])
            
        # Draw coins
        self.ctx.fillStyle = '#ffd700'
        for coin in self.coins:
            if not coin['collected']:
                self.ctx.beginPath()
                self.ctx.arc(coin['x'] + coin['size']//2, coin['y'] + coin['size']//2, coin['size']//2, 0, 2 * math.pi)
                self.ctx.fill()
                
        # Draw particles
        for particle in self.particles:
            alpha = particle['life']
            if particle['color'] == 'gold':
                self.ctx.fillStyle = f'rgba(255, 215, 0, {alpha})'
            else:
                self.ctx.fillStyle = f'rgba(255, 255, 255, {alpha})'
            self.ctx.fillRect(particle['x'], particle['y'], 3, 3)