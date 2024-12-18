from flask import Flask, render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required
import openai

app = Flask(__name__)

# Configure your OpenAI API key
openai.api_key = 'your-openai-api-key'

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Generate a dynamic story using LLM
@app.route('/generate_story', methods=['POST'])
@login_required
def generate_story():
    if request.method == 'POST':
        genre = request.form.get('genre')
        prompt = f"Create a story in the genre {genre}"
        response = openai.Completion.create(
          engine="davinci",
          prompt=prompt,
          max_tokens=150
        )
        story_text = response.choices[0].text.strip()
        # Save story_text to database, associated with the user
        return render_template('story.html', story=story_text)

if __name__ == '__main__':
    app.run(debug=True)
