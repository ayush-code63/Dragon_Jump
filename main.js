let pyodide;
let gameRunning = false;

// Settings management
function loadSettings() {
    const theme = localStorage.getItem('theme');
    
    setTimeout(() => {
        document.getElementById('loading-screen').classList.add('hidden');
        
        if (!theme) {
            document.getElementById('theme-modal').classList.remove('hidden');
        } else {
            document.documentElement.setAttribute('data-theme', theme);
        }
    }, 2000);
}

function selectTheme(theme) {
    localStorage.setItem('theme', theme);
    document.documentElement.setAttribute('data-theme', theme);
    document.getElementById('theme-modal').classList.add('hidden');
}

// Game initialization
async function initPyodide() {
    pyodide = await loadPyodide();
    await pyodide.loadPackage(['numpy']);
    
    const response = await fetch('game.py');
    const pythonCode = await response.text();
    pyodide.runPython(pythonCode);
    
    pyodide.runPython('game = DragonJump()');
    pyodide.runPython('game.start()');
    gameRunning = true;
    gameLoop();
}

function gameLoop() {
    if (gameRunning && !pyodide.runPython('game.game_over_state')) {
        pyodide.runPython('game.update()');
        pyodide.runPython('game.draw()');
        requestAnimationFrame(gameLoop);
    }
}

// Event listeners
document.addEventListener('DOMContentLoaded', () => {
    loadSettings();
    initPyodide();
    
    // Keyboard controls
    document.addEventListener('keydown', (e) => {
        if ((e.code === 'Space' || e.code === 'ArrowUp') && gameRunning) {
            e.preventDefault();
            pyodide.runPython('game.jump()');
        }
    });
    
    // Touch controls
    document.getElementById('game-canvas').addEventListener('touchstart', (e) => {
        if (gameRunning) {
            e.preventDefault();
            pyodide.runPython('game.jump()');
        }
    });
    
    // Mouse/Click controls
    document.getElementById('game-canvas').addEventListener('click', (e) => {
        if (gameRunning) {
            pyodide.runPython('game.jump()');
        }
    });
});

// Expose functions to Python
window.updateScore = (score) => {
    document.getElementById('score').textContent = `Score: ${score}`;
};

window.getTheme = () => {
    return document.documentElement.getAttribute('data-theme');
};

window.showGameOver = (score) => {
    document.getElementById('final-score').textContent = score;
    document.getElementById('game-over-modal').classList.remove('hidden');
};

window.setContrast = (enabled) => {
    document.documentElement.setAttribute('data-contrast', enabled);
};

function restartGame() {
    document.getElementById('game-over-modal').classList.add('hidden');
    pyodide.runPython('game.restart()');
    gameRunning = true;
    gameLoop();
}

function goHome() {
    document.getElementById('game-over-modal').classList.add('hidden');
    document.getElementById('theme-modal').classList.remove('hidden');
}