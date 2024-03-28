from flask import Flask, request, jsonify , Blueprint
import sqlite3

app = Flask(__name__)

paragraphs_bp = Blueprint('try', __name__)

def get_paragraph_from_database(age_group, level):
    complexity = 'Easy' if level in [1, 2] else 'Difficult' if level in [3, 4] else None
    if complexity is None:
        return None

    query = """
    SELECT paragraph, word_count, theme
    FROM paragraphs
    WHERE age_group = ? AND complexity = ?
    ORDER BY RANDOM()
    LIMIT 1
    """
    
    try:
        # Open a new connection to the SQLite database
        conn = sqlite3.connect('dyslexiadetect.db')  # Update this with the actual database path
        cursor = conn.cursor()
        cursor.execute(query, (age_group, complexity))
        result = cursor.fetchone()
        cursor.close()
        conn.close()

        if result:
            return result
        else:
            return None
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None

@paragraphs_bp.route('/get_paragraph', methods=['POST'])
def get_paragraph():
    data = request.json
    age = data.get('age')
    level = data.get('level')

    if not level or level not in [1, 2, 3, 4]:
        return jsonify({'error': 'Invalid or missing level'}), 400

    if age:
        age_group = ''
        if 4 <= age <= 6:
            age_group = '4-6'
        elif 7 <= age <= 9:
            age_group = '7-9'
        elif 10 <= age <= 12:
            age_group = '10-12'
        else:
            return jsonify({'error': 'Age not in valid range'}), 400

        paragraph_data = get_paragraph_from_database(age_group, level)
        if paragraph_data:
            paragraph, word_count, theme = paragraph_data
            return jsonify({'paragraph': paragraph, 'word_count': word_count, 'theme': theme})
        else:
            return jsonify({'error': 'No paragraph found for this age group and level'}), 404
    else:
        return jsonify({'error': 'Age is required'}), 400

