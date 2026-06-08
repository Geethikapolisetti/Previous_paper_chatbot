from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load paper data from JSON
with open('data/papers.json', 'r', encoding='utf-8') as f:
    content = f.read()
    print("DEBUG - File Content:", repr(content))  # This shows exactly what's in the file
    paper_data = json.loads(content)

# 1. Home Page
@app.route('/')
def index():
    return render_template('index.html')

# 2. Return all unique subjects
@app.route('/get_subjects', methods=['GET'])
def get_subjects():
    subjects = sorted(set(p['subject'] for p in paper_data))
    return jsonify(subjects)

# 3. Return years for selected subject
@app.route('/get_years', methods=['POST'])
def get_years():
    subject = request.json['subject']
    years = sorted(set(p['year'] for p in paper_data if p['subject'] == subject))
    return jsonify(years)

# 4. Return semesters for subject + year
@app.route('/get_semesters', methods=['POST'])
def get_semesters():
    subject = request.json['subject']
    year = request.json['year']
    semesters = sorted(set(p['semester'] for p in paper_data if p['subject'] == subject and p['year'] == year))
    return jsonify(semesters)

# 5. Return papers matching subject, year, and semester
@app.route('/get_papers', methods=['POST'])
def get_papers():
    data = request.json
    filtered = [p for p in paper_data if p['subject'] == data['subject'] and p['year'] == data['year'] and p['semester'] == data['semester']]
    return jsonify(filtered)

if __name__ == '__main__':
    app.run(debug=True)