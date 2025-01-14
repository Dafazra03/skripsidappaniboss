from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

app = Flask(__name__)

# Memuat model
model = pickle.load(open('models/model.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prediksi', methods=['POST'])
def prediction():
    try:
        # Mengambil data dari request
        data = request.get_json()

        # Validasi data input
        if not data:
            return jsonify({'error': 'No data provided'}), 400

        # Mengonversi data menjadi DataFrame
        data_df = pd.DataFrame([data])

        # Pastikan data numerik
        data_df = data_df.astype('float64')

        # Prediksi menggunakan model
        prediction = model.predict(data_df)
        prediction = int(prediction[0])

        # Menentukan hasil
        result = "Loan Failed" if prediction == 0 else "Loan Approved"

        return jsonify({'result': result})

    except Exception as e:
        # Menangkap error dan mengembalikan respons
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)