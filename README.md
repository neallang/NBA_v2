# NBA Player Analysis

## Overview

NBA Player Analysis is a web application that allows users to compare the statistics, awards, and personal information of NBA players. Users can view career statistics, career progression graphs, player awards and information, and a featured comparison of the day.


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


## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/nba-player-comparison.git
    cd nba-player-comparison
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up your environment variables:**
    Create a `.env` file in the root directory and add the following:
    ```plaintext
    SECRET_KEY=your_secret_key
    DEBUG=True
    ALLOWED_HOSTS=localhost,127.0.0.1
    ```


## Usage

1. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

2. **Open your browser and navigate to:**
    ```
    http://127.0.0.1:8000
    ```

3. **Compare NBA Players:**
    - Use the autocomplete search bars to select two players.
    - Click the "Compare" button to see their stats, awards, and personal information.

4. **Toggle Dark Mode:**
    - Click the "Toggle Dark Mode" button to switch between light and dark themes.


## Acknowledgements

- **Icons**:
    - Basketball jersey icons created by Nikita Golubev - [Flaticon](https://www.flaticon.com/free-icons/basketball-jersey).

