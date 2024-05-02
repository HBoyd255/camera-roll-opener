
# Harry Boyd - hboyd255@gmail.com - 02/05/2024

import os

# Path from the home folder to the camera roll
LOCAL_CAMERA_ROLL = "OneDrive\\01_personal\\Pictures\\Camera Roll"

# Absolute path to the camera roll
camera_roll = os.path.join(os.environ['USERPROFILE'], LOCAL_CAMERA_ROLL)

# Get the most recent year, by getting the folder with the highest number
current_year = max([x for x in os.listdir(camera_roll) if x.isdigit() ])

# The path of the current year's folder
current_year_path = os.path.join(camera_roll, current_year)

# Get the most recent month, by getting the folder with the highest number
current_month = max([x for x in os.listdir(current_year_path) if x.isdigit() ])

# The path of the current month's folder
current_month_path = os.path.join(current_year_path, current_month)

# Open the folder in the file explorer
os.startfile(current_month_path)



