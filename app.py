# ============================================================
# PART 4 — STREAMLIT INTERFACE AND USER EXPERIENCE
# Assigned to:
# ============================================================


# 4.1 IMPORT LIBRARIES AND LOAD SAVED FILES
# Import Streamlit and the recommendation function.
# Load the saved model and beer catalog.
# Keep data preparation and model training in BeerModel.ipynb.


# 4.2 APP TITLE AND INSTRUCTIONS
# Display the DiscoverBeer title and a short description.
# Explain how to select three to five beers and rate them 1–5.
# Explain that recommendations are estimates, not guarantees.


# 4.3 BEER SELECTION AND RATING CONTROLS
# Let users search for beers in the catalog.
# Add a rating control for each selected beer.
# Add a "Get Recommendations" button.


# 4.4 INPUT VALIDATION AND MODEL CONNECTION
# Require three to five different beers.
# Check for missing ratings and duplicate selections.
# Show helpful messages when something needs fixing.
# Pass valid beer IDs and ratings to the recommendation function.


# 4.5 RESULTS AND RESET CONTROLS
# Show a loading message while recommendations are generated.
# Display up to five recommendations.
# Include each beer's name, style, and ABV when available.
# Exclude beers the user already selected.
# Let users change their ratings or reset their selections.
# Handle missing model files or recommendation errors clearly.


# 4.6 HCI PRINCIPLES
# Visibility: Make instructions and buttons easy to find.
# Feedback: Show loading, success, and error messages.
# Error prevention: Check inputs before generating results.
# User control: Allow changes, retries, and resets.
# Transparency: Explain recommendations and their limitations.
# Accessibility: Use clear labels and readable text.


# 4.7 USABILITY TESTING
# Have at least three participants try the app, where feasible.
# Record feedback and improvements in the report.
# Keep participant notes out of the public-facing interface.