# Load the uploaded Jupyter Notebook to inspect its contents
from nbformat import read

# Path to the uploaded file
file_path = '/mnt/data/Customer_data.ipynb'

# Read the contents of the Jupyter Notebook
with open(file_path, 'r', encoding='utf-8') as file:
    notebook_content = read(file, as_version=4)

# Extracting the structure and first few cells to understand its content
notebook_content.cells[:5]  # Show the first few cells to understand the notebook's purpose and data structure
