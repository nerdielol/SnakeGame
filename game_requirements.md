# Snake Game Requirements

## 1. Game Initialization

- **R1.1**: The game should create a window of size 800x600 pixels.
- **R1.2**: The game should initialize a clock object to manage the frame rate.

## 2. Snake

- **R2.1**: The snake's initial position should be at the center of the screen (400, 300).
- **R2.2**: The snake should start with a length of 1 segment.
- **R2.3**: The snake should move by 10 pixels per frame in the current direction.
- **R2.4**: The snake should grow by one segment when it eats food.
- **R2.5**: The game should end if the snake collides with the screen boundaries or itself.

## 3. Food

- **R3.1**: The food should spawn at a random position within the game window.
- **R3.2**: The food position should be updated when the snake eats it.
- **R3.3**: The score should increase by 1 point for each piece of food eaten.

## 4. Game Loop

- **R4.1**: The game loop should run until the player quits the game.
- **R4.2**: The game should handle input events, update the game state, and render the screen each frame.
- **R4.3**: The frame rate should be capped at 15 frames per second.

## 5. User Input

- **R5.1**: The player should be able to change the snake's direction using the arrow keys.
- **R5.2**: The game should quit when the player closes the window.

## 6. Game Over

- **R6.1**: A game over message should be displayed when the snake dies.
- **R6.2**: The player should be able to restart the game by pressing a key.
- **R6.3**: The player should be able to quit the game by closing the window.
