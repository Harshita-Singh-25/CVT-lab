from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Docker Flask</title>
            <style>
                body {
                    font-family: 'Helvetica Neue', Arial, sans-serif;
                    background: #f8f9fa;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    color: #333;
                }
                .container {
                    text-align: center;
                    padding: 2rem;
                    background: white;
                    border-radius: 8px;
                    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                    max-width: 600px;
                }
                h1 {
                    font-weight: 300;
                    margin-bottom: 1rem;
                }
                .docker {
                    color: #2496ed;
                    font-weight: 400;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Hello from <span class="docker">Container</span></h1>
                <p>A Python Flask app running inside Docker</p>
            </div>
        </body>
        </html>
    ''')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)