🤖 ProjectMind AI Dashboard

ProjectMind AI is a Smart Portfolio Monitoring & Risk Insight System built with Streamlit, Pandas, Matplotlib, and WordCloud. This dashboard helps monitor project status, analyze trends, and generate AI-driven insights from your project data.

🛠 Key Features

Dashboard Overview
Displays total projects, project status counts (On Track, Warning, At Risk), and visual charts of project status and top risks.

Trend Analysis
Analyze project trends per month using interactive line charts based on the selected month column.

Project Data Table
View all project data in an interactive table and filter by status (green, orange, red).

AI Insights
Generates a lessons learned word cloud and provides automatic insights: projects running smoothly, needing attention, high risk projects, and most common risks.

Project File Upload
Supports CSV file upload (PDF is currently a placeholder for future enhancement).

⚡ Installation

Clone the repository:

git clone https://github.com/Priskaaitn/projectmind-ai.git
cd projectmind-ai


Create a virtual environment (optional):

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows


Install dependencies:

pip install -r requirements.txt


Required Python Packages:

streamlit

pandas

matplotlib

wordcloud

Example requirements.txt:

streamlit
pandas
matplotlib
wordcloud

🚀 How to Run

Start the Streamlit app:

streamlit run app.py

Navigation Menu

🏠 Dashboard – Overview of project metrics and charts for status and risks.

📈 Trend Analysis – Track monthly project trends.

📊 Project Data – Interactive table to view and filter projects.

🧠 AI Insights – Lessons learned word cloud and AI-generated portfolio insights.

Upload your project CSV file at the top of the page or use the default project_reports.csv.

🎨 Customization

CSS Styling
Modify style/style.css to customize the dashboard appearance.

Data Columns
Ensure your CSV contains at least the following columns:

name,status,risk,lesson,<month_column>


Project Status
Use values: green, orange, red

Lessons Learned
Text from the lesson column is used to generate the word cloud.

📝 Notes

PDF upload is currently a placeholder; CSV is recommended for full functionality.

Ensure month column values match January, February, ..., December for trend analysis.

📂 Project Structure
projectmind-ai/
│
├─ app.py               # Main Streamlit file
├─ project_reports.csv   # Sample project data
├─ style/
│   └─ style.css        # Custom CSS
├─ requirements.txt     # Python dependencies
└─ README.md            # This README file

👨‍💻 Author
Priska Intan, Mellisa Rizki, Renata Reika, Elifele Dyra– AI & Data Enthusiast
