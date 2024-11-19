# Feedback Analysis Project

## Description
This project is a simple application for analyzing customer feedback from product pages (e.g., Amazon or eBay). It extracts text content from the given URL, analyzes its sentiment (positive, negative, or neutral), and stores the results in a MySQL database. The application features a graphical interface where users can input a URL and view the analysis results.

---

## Features
- Extracts and processes text from product feedback pages using **Goose3**.
- Performs sentiment analysis using **TextBlob**.
- Stores feedback content and sentiment in a **MySQL database**.
- Graphical User Interface (GUI) built with **Tkinter**.

---

## Requirements
### Software:
- Python 3.7 or higher
- MySQL Server

### Python Libraries:
The required libraries can be installed with:
```bash
pip install goose3 textblob mysql-connector-python
```

### Additional Data:
- **NLTK corpora**: The project requires `punkt` and `brown` corpora for TextBlob to function correctly. Install them using the following commands:
```python
import nltk
nltk.download('punkt')
nltk.download('brown')
```

---

## Installation

1. **Clone the Repository** (or download the project files):
   ```bash
   git clone <repository-url>
   cd feedback_analysis_project
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up the MySQL Database**:
   - Ensure your MySQL server is running.
   - Execute the following script (via MySQL Workbench, MySQL CLI, or included in the project):
     ```sql
     CREATE DATABASE feedback_analysis;
     USE feedback_analysis;

     CREATE TABLE feedback (
         id INT AUTO_INCREMENT PRIMARY KEY,
         url TEXT,
         content TEXT,
         sentiment FLOAT
     );
     ```
   - Alternatively, you can let the project script create the database and table automatically during runtime.

4. **Run the Application**:
   ```bash
   python main.py
   ```

---

## Usage
1. **Launch the Application**: Run the `main.py` script. A GUI window will appear.
2. **Input the URL**: Paste the URL of a product feedback page into the input field.
3. **Analyze Feedback**: Click the "Analyze" button to:
   - Extract text from the page.
   - Perform sentiment analysis.
   - View the results in the output field.
   - Automatically save the feedback and sentiment into the MySQL database.

---

## Project Structure
```
feedback_analysis_project/
├── main.py                  # Main application file with GUI, analysis, and MySQL integration
├── db_setup.py              # Optional script for initializing the MySQL database and table
├── requirements.txt         # List of required Python libraries
├── README.md                # Project documentation
└── nltk_data/               # Folder for storing NLTK corpora (created automatically)
```

---

## Troubleshooting
- **MySQL Connection Error**: Ensure MySQL is running and the credentials in the script match your MySQL setup.
- **Missing NLTK Data**: Run `nltk.download('punkt')` and `nltk.download('brown')` to resolve missing corpus issues.
- **Goose3 Extraction Issue**: Ensure the URL provided contains extractable text (some dynamic pages may not work).

---

## Future Improvements
- Add support for other languages in sentiment analysis.
- Enhance the GUI for a better user experience.
- Add functionality to visualize feedback sentiment trends.

---


 
