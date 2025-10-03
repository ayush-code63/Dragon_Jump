# 🐉 Dragon Jump - Web Game

A minimal 2D endless runner game where you control a dragon jumping over obstacles and collecting coins. Built with Python (Pyodide) running in the browser!

![Dragon Jump](https://img.shields.io/badge/Game-Dragon%20Jump-purple?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

## ✨ Features

- 🌓 **Dark & Light Mode** - Choose your preferred theme with persistent storage
- 📱 **Responsive Design** - Works seamlessly on desktop and mobile devices
- 🎮 **Simple Controls** - Tap, click, or use keyboard to jump
- 🚀 **Progressive Difficulty** - Speed increases over time
- 🎨 **Dynamic Contrast** - Background changes every 15 seconds for added challenge
- ✨ **Particle Effects** - Visual feedback for jumps and coin collection
- 🏆 **Score System** - Collect coins and survive as long as possible

## 🎮 Controls

- **Desktop**: Spacebar, Up Arrow, or Mouse Click
- **Mobile**: Tap anywhere on screen
- **Goal**: Jump over obstacles and collect coins!

## 🚀 Quick Start

### Option 1: Direct Browser (Simplest)
```bash
# Clone the repository
git clone https://github.com/ayush-code63/Dragon_Jump.git
cd Dragon_Jump

# Open index.html in your browser
open index.html  # macOS
start index.html # Windows
xdg-open index.html # Linux
```

### Option 2: Local Server (Recommended)
```bash
# Using Python's built-in server
python server.py

# Or use http.server
python -m http.server 8000

# Open http://localhost:8000 in your browser
```

## 🛠️ Technical Stack

- **Frontend**: HTML5 Canvas, CSS3, JavaScript
- **Game Logic**: Python 3.12 (via Pyodide)
- **Deployment**: Static files (no backend required)
- **Browser Support**: Chrome, Firefox, Safari, Edge (WebAssembly required)

## 📁 Project Structure

```
Dragon_Jump/
├── index.html      # Main game interface
├── game.py         # Python game logic and physics
├── main.js         # JavaScript bridge and UI management
├── style.css       # Responsive styling with themes
├── server.py       # Development server with CORS
├── test_game.py    # Unit tests for game mechanics
├── package.json    # Project metadata
└── README.md       # Documentation
```

## 🎯 Game Mechanics

- **Dragon**: Auto-runs and jumps with physics-based movement
- **Obstacles**: Randomly spawned with fair spacing
- **Coins**: Bonus points (50 pts each)
- **Score**: Increases with distance + coin collection
- **Difficulty**: Speed gradually increases over time
- **Contrast Mode**: Background inverts every 15 seconds

## 🧪 Testing

```bash
# Run unit tests
python test_game.py

# Expected output: ✅ All core mechanics tested!
```

## 🎨 Extending the Game

### Add New Power-ups
Edit `game.py` and extend the coin collection system:
```python
def spawn_powerup(self):
    self.powerups.append({
        'x': self.canvas.width,
        'y': random.randint(200, self.ground_y - 50),
        'type': 'shield'  # or 'speed', 'double_jump'
    })
```

### Modify Obstacle Patterns
Adjust spawning logic in `game.py`:
```python
def spawn_obstacle(self):
    # Add different obstacle types
    height = random.choice([60, 80, 100])
    self.obstacles.append({...})
```

### Add Sound Effects
Include audio in `index.html`:
```html
<audio id="jump-sound" src="sounds/jump.mp3"></audio>
<audio id="coin-sound" src="sounds/coin.mp3"></audio>
```

### Implement Leaderboard
Create a simple backend (optional):
```bash
pip install fastapi uvicorn
# Add WebSocket support for real-time features
```

## 🌐 Deployment

### GitHub Pages
```bash
# Push to GitHub
git add .
git commit -m "Initial commit"
git push origin main

# Enable GitHub Pages in repository settings
# Your game will be live at: https://ayush-code63.github.io/Dragon_Jump/
```

### Netlify
```bash
# Drag and drop the Dragon_Jump folder to Netlify
# Or connect your GitHub repository
```

### Vercel
```bash
vercel deploy
```

## 🔧 Browser Requirements

- WebAssembly support
- ES6+ JavaScript
- HTML5 Canvas
- LocalStorage for theme persistence

Tested on:
- ✅ Chrome 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Edge 90+
- ✅ Mobile browsers (iOS Safari, Chrome Mobile)

## 📝 License

MIT License - feel free to use this project for learning or building your own games!

## 👨‍💻 Developer

**Ayush Maurya**
- GitHub: [@ayush-code63](https://github.com/ayush-code63)
- Telegram: [@ayush_maurya_63](https://t.me/ayush_maurya_63)

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 🎮 Play Now!

[Live Demo](https://ayush-code63.github.io/Dragon_Jump/) (Once deployed)

---

Made with ❤️ using Python and Amazon Q Developer
