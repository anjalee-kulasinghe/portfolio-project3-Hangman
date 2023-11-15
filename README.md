# Hangman

## Code Institute - Thired Milestone Project: Python Essentials Portfolio Project

## Overview
This program is a computerized version of the original hangman game, based inside a mock terminal deployed via Heroku.

As a child, I enjoyed the Hangman game a lot during my school days. It is popular as an educational tool to reinforce vocabulary and spelling skills.

Hangman is a classic word-guessing game in which one player thinks of a word and the other player tries to guess it by suggesting letters. The word is represented by dashes, with each dash representing a letter in the word. The player guessing the word suggests letters one at a time, and if the guessed letter is in the word, the other player reveals all occurrences of that letter in the word. If the guessed letter is not in the word, a part of a stick figure (traditionally a gallows) is drawn as a tally of incorrect guesses.

The game continues until the guessing player successfully guesses the word or the stick figure is completely drawn (indicating too many incorrect guesses), resulting in a loss. The stick figure drawing often resembles a hanging person, which is why the game is called "Hangman."


# Table of Contents
- [Hangman](#hangman)
  - [Code Institute - Second Milestone Project: JavaScript Essentials Portfolio Project.](#code-institute---third-milestone-project-python-essentials-portfolio-project)
- [Table of Contents](#table-of-contents)
  - [Demo](#demo)
    - [A live demo to the website can be found here](#a-live-demo-to-the-website-can-be-found-here)
  - [UX](#ux)
  - [User stories](#user-stories)
    - [Strategy](#strategy)
    - [Scope](#scope)
    - [Structure](#structure)
    - [Skeleton](#skeleton)
    - [Surface](#surface)
  - [Technologies](#technologies)
  - [Features](#features)
    - [Existing Features](#existing-features)
    - [Features Left to Implement](#features-left-to-implement)
  - [Testing](#testing)
    - [Validator Testing](#validator-testing)
    - [Bugs](#bugs)
  - [Deployment](#deployment)
  - [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Acknowledgements](#acknowledgements)

## Demo

![Start of the game](assets/readme-assets/device_look.PNG)

### A live demo to the website can be found [here](https://anjalee-kulasinghe.github.io/portfolio-project2-quiz-saga/)


## How to Play:
- The system will provide a random word, reflecting the number of letters of the word by dash marks.
- Click on the letter buttons to guess the word.
- If the guessed letter is correct, the system will reveal all occurrences of that letter in the word.
- Each wrong guess will add a part for the hangman.
- Six incorrect guesses will end the game. 
- Try to guess the word and increase your score!


## Planning Phase
### User stories
- As a player, I want to start a new game so that I can begin guessing a new word.
- As a player, I want to see the number of letters in the word represented by dashes, so that I know how many letters I need to guess.
- As a player, I want to be able to guess a letter and see if it is in the word, so that I can progress in solving the puzzle.
- As a player, I want a visual representation of the Hangman figure to track my progress and avoid making too many incorrect guesses.
- As a player, I want to see the letters I have already guessed, so that I don't accidentally repeat guesses.
- As a player, I want the option to quit the game and start a new one at any time.
- As a player, I want to be notified when I win the game by correctly guessing the word.
- As a player, I want to be notified when I lose the game by making too many incorrect guesses.
- As a player, I want a variety of words to guess to keep the game interesting and challenging.
- As a player, I want to be able to see my score or progress in the game.
- As a player, I want the game to be visually appealing and user-friendly.
- As a player, I want to play an enjoyable game of the classic hangman game by myself.

### Site Aims:
1. Entertainment:
  - Provide a fun and engaging experience for users who enjoy playing word games.
  - Offer a casual and entertaining way for users to spend their leisure time.
2. Education:
  - Reinforce vocabulary and spelling skills by incorporating a variety of words for players to guess.
3. User Engagement:
  - Encourage users to return by providing a user-friendly and enjoyable game environment.
4. Learning and Improvement:
  - Offer a positive learning experience by providing feedback on correct and incorrect guesses.
  - Motivate players to improve their word-guessing skills over time.

### How Will This Be Achieved:
1. Entertainment:
  - Diverse Word Database: Include a wide range of words from different categories to keep the game interesting.
  - Engaging User Interface: Design an attractive and intuitive interface to enhance the overall gaming experience.
2. Education:
  - Word Categories: Categorize words based on difficulty levels or themes (e.g., science, geography, history) to cater to different learning objectives.
  - Progress Tracking: Allow players to track their progress in terms of the words they have successfully guessed, promoting a sense of accomplishment.
3. User Engagement:
  - Regular Updates: Keep the game content fresh by regularly updating the word database, introducing new features, or hosting events.
4. Learning and Improvement:
  - Feedback Mechanism: Provide immediate feedback on each guessed letter, indicating whether it is correct or incorrect.
  - Score Tracking: Implement a scoring system to track and display players' scores, encouraging healthy competition.
5. Motivation for Improvement:
  - Achievements and Rewards: Introduce achievements or rewards for reaching milestones, encouraging players to strive for continuous improvement.
6. Accessibility:
  - User-Friendly Controls: Design intuitive controls and interfaces to make the game accessible to users of all ages and skill levels.

### Game Flow Chart:
To understand the steps required in order to program the game, I created the below flowchart using lucid charts.
![flow_chart](assets/readme-assets/Flowchart.PNG)

## Features
### Welcome Screen:
From the welcome screen, the user will get the guidance 'How to Play the Game'.
![welcome](assets/readme-assets/welcome.PNG)

### Once Play Game is Started:
* The player can see the dash lines for the secret word.
![strat_page](assets/readme-assets/start.PNG)
 
* If the player guesses the letter correctly, it will replace the dash line.
![correct_guess](assets/readme-assets/correct_guess.PNG)

![correct_guess_multiple](assets/readme-assets/multiple.PNG)

* If the player guesses the wrong letter, it will start to draw the hangman.
![wrong_guess1](assets/readme-assets/wrong_guess1.PNG)

![wrong_guess2](assets/readme-assets/wrong_guess2.PNG)

![wrong_guess3](assets/readme-assets/wrong_guess3.PNG)

![wrong_guess4](assets/readme-assets/wrong_guess4.PNG)

![wrong_guess5](assets/readme-assets/wrong_guess5.PNG)

* If the player guesses wrong six times, the hangman will be completed, and the player will lose the game.
![lost](assets/readme-assets/lost.PNG)

* If the player guesses the word correctly, the player will win the game.
![Win](assets/readme-assets/Win.PNG)

* If the player wins the game, a score will be added.
![score](assets/readme-assets/score.PNG)

* Whether the player wins or loses the game, the player has the option to continue the game.
![play_again](assets/readme-assets/play_again.PNG)

* If the player wants, the player has a chance to exit the game.
![exit](assets/readme-assets/exit.PNG)

### Error Handling:
During the development process, error handling is done to make sure the player will have a smoother user experience and to make the code more robust.
1. File Not Found:
  - If the 'words.txt' file is not found, the code prints an error message and exits the program.
2. File Reading Error:
  - If there is an error while reading the file, an exception is caught, and an error message is printed before exiting.
3. Resource Loading Error:
  - If there is an error while loading image resources (hangman images), an exception is caught, and an error message is printed before exiting.
4. Tkinter Window Creation Error:
  - If there is an error during the creation of the Tkinter window, an exception is caught, and an error message is printed before exiting.
  
### Future-Enhancements
Below are the things that would take my current MVP to the next level:
1. Multiple Difficulty Levels:
    - Implement different difficulty levels with varying word complexities. Allow users to choose their preferred difficulty before starting the game.
2. Word Categories:
   - Introduce word categories or themes (e.g., animals, countries, sports) and allow users to select a category before playing.
3. User Profiles:
   - Implement user profiles to track individual scores and progress over time. Users can log in and see their game history.
4. Hint System:
   - Add a hint system that provides players with a clue about the selected word. This can be optional and may cost the player in terms of points.
5. Multiplayer Mode:
   - Develop a multiplayer mode where users can play against each other. This could involve taking turns guessing words or competing in real-time.
6. Achievements and Badges:
   - Introduce achievements or badges for completing specific challenges, reaching high scores, or mastering certain categories.
7. Customizable Hangman Images:
   - Allow users to choose from a selection of hangman images or upload their own custom images to personalize the game.
8. Sound Effects and Music:
   - Incorporate sound effects for correct and incorrect guesses, as well as background music to enhance the gaming experience.
9. Leaderboards:
   - Create online leaderboards to showcase top scores globally or within specific categories. This encourages friendly competition among players.
10. Responsive Design:
   - Ensure the game is fully responsive to different screen sizes, making it accessible and enjoyable on various devices.

## Data Model
### Overview of Classes:
### Logic Flow:
* Setup Phase:
* Firing Round:
## Testing Phase
## Libraries
### random:
## Deployment
### Playing on a Local machine or via Gitpod Terminal:
### Final Deployment to Heroku:
## Honorable Mentions
## Credits