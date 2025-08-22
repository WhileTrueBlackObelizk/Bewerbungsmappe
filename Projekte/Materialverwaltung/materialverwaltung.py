from app import app
app.secret_key = 'very secret, change to something random'

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')