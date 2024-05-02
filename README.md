# NBA Champion Prediction Model

## Project Overview
This project aims to predict the NBA champion of a season based on historical data using machine learning techniques. The model leverages detailed team performance metrics from regular season games to identify patterns and predictors of championship success.

## Dataset Description
The dataset comprises team performance statistics from the NBA regular season. Each row in the dataset represents aggregated team statistics for one season.

## Features Explanation
Here's a breakdown of the columns present in the dataset:

- **Team**: The name of the NBA team.
- **Year**: The season year.
- **W%**: Win percentage of the team during the regular season.
- **G**: Total games played in the regular season.
- **FG**: Average field goals made per game.
- **FGA**: Average field goal attempts per game.
- **3P**: Average three-point field goals made per game.
- **3PA**: Average three-point field goal attempts per game.
- **2P**: Average two-point field goals made per game.
- **2PA**: Average two-point field goal attempts per game.
- **FT**: Average free throws made per game.
- **FTA**: Average free throw attempts per game.
- **ORB**: Average offensive rebounds per game.
- **DRB**: Average defensive rebounds per game.
- **AST**: Average assists per game.
- **STL**: Average steals per game.
- **BLK**: Average blocks per game.
- **TOV**: Average turnovers per game.
- **PF**: Average personal fouls per game.
- **PPG**: Average points per game by the team.
- **Opponent Metrics** (Prefixed with 'O'): Similar metrics for opponents.
- **Age**: Average age of the players on the team.
- **SOS**: Strength of schedule.
- **SRS**: Simple Rating System score.
- **ORtg**: Offensive rating.
- **DRtg**: Defensive rating.
- **Pace**: Number of possessions per 48 minutes.
- **FTr**: Free throw attempt rate.
- **3PAr**: Three-point attempt rate.
- **TS%**: True shooting percentage.
- **eFG%**: Effective field goal percentage.
- **TOV%**: Turnover percentage.
- **ORB%**: Offensive rebound percentage.
- **FT/FGA**: Ratio of free throws to field goal attempts.
- **Opponent Efficiencies** (Prefixed with 'O'): Similar metrics for opponents.
- **Arena**: Home arena of the team.
- **Attend./G**: Average home game attendance.
- **Champion**: 1 if the team won the NBA championship, 0 otherwise.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.
