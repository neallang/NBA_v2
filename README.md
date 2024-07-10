# NBA Player Analysis

## Overview

NBA Player Analysis is a web application that allows users to compare the statistics, awards, and personal information of NBA players. Users can view career statistics, career progression graphs, player awards and information, and a featured comparison of the day.

## How to Use

1. **Access the Web Application**:
    Open your web browser and navigate to the provided URL (e.g., `https://www.yourdomain.com/`).

2. **Compare Players**:
    - Enter the names of any two NBA players (don't have to be currently playing) in the input fields.
    - Click on the "Compare" button to view the comparison.

## Features

- **Featured Comparison**: Display a random featured comparison of the day.
- **Smart (Ajax) Search**: Implemented an intuitive search functionality using Ajax, allowing users to quickly and efficiently find players as they type. This feature provides real-time search results, enhancing the user experience by minimizing the need for page reloads and offering instant feedback.
- **Career Progression Graphs**: View the career progression of players in various stats.
- **Dark Mode**: Toggle between light and dark mode for a better viewing experience.
- **Error Handling**: Provides error messages for invalid player inputs.

## Technologies Used

- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript
- **Data**: `nba_api` package for fetching player statistics and information
- **Graphing**: Matplotlib, Seaborn, Pandas
- **Caching**: Redis
- **Web Scraping**: Beautiful Soup for fetching additional player information

## Acknowledgements

- **Icons**:
    - Basketball jersey icons created by Nikita Golubev - [Flaticon](https://www.flaticon.com/free-icons/basketball-jersey).

