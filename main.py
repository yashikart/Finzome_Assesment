import pandas as pd
from flask import Flask, request, render_template, jsonify

from calculations import calculations_daily_volatility, calculations_annualized_volatility

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_calculation():
    try:
        # Check if CSV file is uploaded
        print('Entered into calculations part')
        file = request.files['file']
        if file and file.filename.endswith('.csv'):
            # Process the CSV file using Pandas
            df = pd.read_csv(file, encoding='unicode_escape')
            # Calculate daily volatility
            daily_volatility = calculations_daily_volatility(df)
            # Calculate annualized volatility
            annualized_volatility = calculations_annualized_volatility(daily_volatility, df)
            # Return the results in JSON format
            return jsonify({"daily_volatility": daily_volatility,
                            "annualized_volatility": annualized_volatility})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
