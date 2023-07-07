import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from matplotlib import backend_bases

# Load the Excel file with 83 sheets
excel_file = 'Animato Analysis.xlsx'
data_frames = pd.read_excel(excel_file, sheet_name=None)

# Define the video count categories
categories = ['1-5 Videos', '6-15 Videos', '15+ Videos']

# Iterate over each category and plot the data if it exists
for i, category in enumerate(categories):
    # Filter the data based on the video count category
    if i == 0:
        filtered_data = {
            sheet_name: df for sheet_name, df in data_frames.items() if 0 <= len(df) <= 5
        }
    elif i == 1:
        filtered_data = {
            sheet_name: df for sheet_name, df in data_frames.items() if 6 <= len(df) <= 15 and len(df) >= 6
        }
    elif i == 2:
        filtered_data = {
            sheet_name: df for sheet_name, df in data_frames.items() if len(df) > 15
        }
    else:
        filtered_data = {}

    # Check if there is data available for the category
    if filtered_data:
        # Exclude line graphs from other categories
        if i == 0:
            filtered_data = {
                sheet_name: df for sheet_name, df in filtered_data.items() if len(df) <= 5
            }
        elif i == 2:
            filtered_data = {
                sheet_name: df for sheet_name, df in filtered_data.items() if len(df) > 15
            }

        # Create a new figure and axis for each category
        fig, ax = plt.subplots(figsize=(12, 8))

        # Iterate over each sheet in the filtered data and plot the data
        for sheet_name, df in filtered_data.items():
            video_number = [0] + list(range(1, len(df) + 1))  # Add 0 to the beginning of the list
            view_count = [0] + df.iloc[:, 1].tolist()  # Add 0 to the beginning of the list
            ax.plot(video_number, view_count, label=sheet_name)

        # Set the labels and title for the current plot
        ax.set_xlabel('Video Number')
        ax.set_ylabel('View Count')
        ax.set_title(category)
        ax.legend()

        # Format the y-axis labels
        ax.yaxis.set_major_formatter(FuncFormatter(lambda x, pos: f'{int(x):,}'))

        # Adjust the x-axis limits for the first plot
        if i == 0:
            ax.set_xlim(0, 5)
        elif i == 1:
            ax.set_xlim(0, 15)

        # Display the plot
        plt.show()
