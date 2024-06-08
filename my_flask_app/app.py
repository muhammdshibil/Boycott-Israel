from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Load the dataset
df = pd.read_csv('data.csv')

# Drop the specified columns
df = df.drop(columns=['id', 'description', 'categories', 'website', 'alternatives', 'alternatives_text', 'allOf', 'reasons', 'status'])

# Save the modified DataFrame to a new CSV file
df.to_csv('modified_data.csv', index=False)

@app.route('/')
def index():
    # Convert the DataFrame to HTML, including the logo column as images
    df_html = df.copy()
    df_html['logo'] = df_html['logo'].apply(lambda x: f'<img src="{x}" width="150" height="150">' if pd.notnull(x) else '')
    data = df_html.to_html(classes='table table-hover table-bordered table-sm', escape=False, index=False)
    return render_template('index.html', tables=[data], titles=df.columns.values)

if __name__ == '__main__':
    app.run(debug=True)
