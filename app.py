from flask import Flask, jsonify

app = Flask(_name_)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify(status="UP", message="Application is running successfully!"), 200

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)