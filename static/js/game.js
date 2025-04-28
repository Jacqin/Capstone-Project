document.addEventListener('DOMContentLoaded', () => {
    const board = document.getElementById('board');
    const cells = document.querySelectorAll('.cell');
    const status = document.getElementById('status');
    const resetButton = document.getElementById('reset');
    
    let gameActive = true;
    
    const updateStatus = (message) => {
        status.textContent = message;
    };
    
    const updateCell = (index, value) => {
        cells[index].textContent = value;
        cells[index].classList.add(value);
    };
    
    const handleMove = async (index) => {
        if (!gameActive) return;
        
        try {
            const response = await fetch('/make_move', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ position: index }),
            });
            
            const result = await response.json();
            
            if (result.status === 'invalid') return;
            
            // Update the board with all moves
            if (result.board) {
                for (let i = 0; i < 9; i++) {
                    cells[i].textContent = result.board[i] || '';
                    cells[i].classList.remove('X', 'O');
                    if (result.board[i]) {
                        cells[i].classList.add(result.board[i]);
                    }
                }
            }
            
            if (result.game_over) {
                gameActive = false;
                if (result.winner === 'draw') {
                    updateStatus("It's a draw!");
                } else {
                    updateStatus(`Player ${result.winner} wins!`);
                }
            } else {
                updateStatus("Player X's turn");
            }
            
        } catch (error) {
            console.error('Error:', error);
            updateStatus('An error occurred. Please try again.');
        }
    };
    
    const resetGame = async () => {
        try {
            await fetch('/reset_game', {
                method: 'POST',
            });
            
            cells.forEach(cell => {
                cell.textContent = '';
                cell.classList.remove('X', 'O');
            });
            
            gameActive = true;
            updateStatus("Player X's turn");
            
        } catch (error) {
            console.error('Error:', error);
            updateStatus('An error occurred while resetting the game.');
        }
    };
    
    cells.forEach(cell => {
        cell.addEventListener('click', () => {
            const index = parseInt(cell.dataset.index);
            handleMove(index);
        });
    });
    
    resetButton.addEventListener('click', resetGame);
}); 