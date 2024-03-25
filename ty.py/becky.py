Back-end (Python)
Python (app.py):
python
Copy code
from flask import Flask, request, jsonify

app = Flask(_name_)

@app.route('/notifyBank', methods=['POST'])
def notify_bank():
    try:
        data = request.get_json()
        debtor_id = data['id']

        # Perform necessary checks and notifications to the bank
        # In a real-world scenario, you would interact with a database and external services

        # Return a response message
        return jsonify({'message': f'Notification sent for debtor with ID: {debtor_id}'})
    except Exception as e:
        return jsonify({'error': str(e)})

if _name_ == '_main_':
    app.run(debug=True)