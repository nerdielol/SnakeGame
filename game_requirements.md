# Game Requirements Document

## Overview

This document outlines the requirements for the enhanced snake game, which now includes new features such as speed boosts, projectiles, and additional advantage items.

## Functional Requirements

### 1. Gameplay Modes

- **Single Player Mode**: Player vs. Bot.
- **Two Player Mode**: Player vs. Player on the same screen.

### 2. Players

- Players are represented by a textured snake, which grows when collecting items.
- Players can move in four directions: **UP**, **DOWN**, **LEFT**, and **RIGHT**.
- Players can collect items, use speed boosts, and fire projectiles.

### 3. Items

- **Regular Items (Green)**: Increase the snake's length by one segment.
- **Speed Boost Items (Yellow)**: Double the speed of the player for a set duration (10 seconds). Effects are stackable.
- **Projectile Items (Orange)**: Allow players to fire projectiles from the snake's head.

### 4. Projectiles

- **Firing Mechanism**: Players with projectile ability can fire using a specific key (**SPACE** for player 1).
- **Projectile Behavior**: If a projectile hits an opposing player, the opposing player's snake loses one segment.

### 5. Collisions

- If a player's snake head collides with another player, the colliding player resets.
- Projectiles fired by players can also reduce the size of the opposing player's snake upon impact.

### 6. Particle Effects

- Particle effects are displayed when a player collects an item, enhancing the visual experience.

## Non-Functional Requirements

### 1. Performance

- The game should run at **60 FPS** for a smooth user experience.
- The movement and projectile speeds should be consistent across different devices.

### 2. Compatibility

- The game requires **pygame version 2.1.0 or higher** for compatibility with the new features.

### 3. User Interface

- The game should display player scores and speed levels in a verbose manner, indicating if the player has a speed boost and the current multiplier (e.g., "Fast (x2)").
- The game should provide clear visual cues for the different types of items (e.g., colors for regular, speed, and projectile items).

## Controls

### Player 1

- **W, A, S, D**: Movement.
- **SPACE**: Fire projectile (if available).

### Player 2

- **Arrow Keys**: Movement.

## Assets

- **Textures**: Textures for the snakes must be provided (`red_texture.png`, `blue_texture.png`).
- **Background**: A background image (`background.png`) is used to enhance the game's visual appeal.

## Future Enhancements

- **Additional Power-ups**: Introduce more power-ups that could affect the game in various ways, such as invisibility or teleportation.
- **Multiplayer Over Network**: Enable multiplayer gameplay over a network connection.
