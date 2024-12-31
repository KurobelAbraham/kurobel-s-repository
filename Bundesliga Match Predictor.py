# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder

# Bundesliga 2024/25 teams
teams = [
    "Bayern Munich", "Borussia Dortmund", "RB Leipzig", "Bayer Leverkusen", 
    "Union Berlin", "Freiburg", "VfL Wolfsburg", "Eintracht Frankfurt", 
    "Mainz 05", "Borussia Mönchengladbach", "VfB Stuttgart", 
    "Augsburg", "Hoffenheim", "Werder Bremen", "FC Köln", 
    "Heidenheim", "Darmstadt", "VfL Bochum"
]

# Load historical Bundesliga data (replace with actual path to the dataset)
# Example dataset columns: ['home_team', 'away_team', 'home_goals', 'away_goals', 'shots_home', 'shots_away', 'possession_home', 'possession_away', 'result']
df = pd.read_csv('bundesliga_matches.csv')

# Inspect the first few rows of the dataset
print(df.head())

# Preprocessing
# Encoding categorical variables (home_team and away_team)
label_encoder = LabelEncoder()
df['home_team'] = label_encoder.fit_transform(df['home_team'])
df['away_team'] = label_encoder.fit_transform(df['away_team'])

# Encode result as 1 for home win, 0 for draw, and -1 for away win
result_mapping = {'Home Win': 1, 'Draw': 0, 'Away Win': -1}
df['result'] = df['result'].map(result_mapping)

# Feature selection: Choose relevant features for model training
features = ['home_team', 'away_team', 'home_goals', 'away_goals', 'shots_home', 'shots_away', 'possession_home', 'possession_away']

# Split data into features (X) and target (y)
X = df[features]
y = df['result']

# Train-test split (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model selection: Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
print("Classification Report:")
print(classification_report(y_test, y_pred))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Prediction for a future match
# Example: Bayern Munich (home) vs Borussia Dortmund (away)
home_team = "Bayern Munich"
away_team = "Borussia Dortmund"

# Encode teams
home_team_encoded = label_encoder.transform([home_team])[0]
away_team_encoded = label_encoder.transform([away_team])[0]

# Example stats for prediction (these would come from current data, so we'll mock them for now)
home_goals = 2
away_goals = 1
shots_home = 15
shots_away = 10
possession_home = 60
possession_away = 40

# Create the input for prediction
match_features = np.array([[home_team_encoded, away_team_encoded, home_goals, away_goals, shots_home, shots_away, possession_home, possession_away]])

# Predict the outcome
predicted_result = model.predict(match_features)[0]

# Map the result back to human-readable form
result_mapping_reverse = {1: 'Home Win', 0: 'Draw', -1: 'Away Win'}
predicted_outcome = result_mapping_reverse[predicted_result]

print(f"Predicted Outcome: {predicted_outcome}")
