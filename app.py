from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# 접속한 IP 주소를 저장할 리스트
ip_addresses = []

@app.route('/')
def index():
    # 접속자의 IP를 저장
    user_ip = request.remote_addr
    if user_ip not in ip_addresses:
        ip_addresses.append(user_ip)  # 중복되지 않게 저장
    return render_template('index.html')

@app.route('/get_ips', methods=['GET'])
def get_ips():
    # 저장된 IP 리스트를 JSON으로 반환
    return jsonify(ip_addresses)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
