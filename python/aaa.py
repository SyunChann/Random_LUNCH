from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from base64 import b64encode, b64decode
import requests

# API 키와 Client ID
client_id = "HunSYLjIcoL5PeO3krEuzg=="  # 정확한 Client ID인지 확인 필요
api_key = "390797e1f0b8f216b8ec90293637ad63f2c66da4f6a90d0ce4d22c7596205af3"  # 정확한 ApiKey인지 확인 필요

# 고정된 암호화 키와 IV (C#의 encryptionKey와 initialisationVector와 동일하게 설정)
encryption_key = b64decode("TIy5wflhXD6JrQshQFVcG+mMK0jEn8qqqjVYfXDUVtY=")  # Base64 디코딩된 키
initialisation_vector = "wm00001218166458".encode("utf-8")  # IV를 UTF-8 바이트 문자열로 변환

# 암호화할 OrderId (예: "E24110702025")
order_id = "E24110702025"

def encrypt_aes256_cbc(data, key, iv):
    # AES 암호화 설정 (CBC 모드)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    # 데이터에 PKCS7 패딩 추가 (PKCS5와 동일)
    padding_len = 16 - (len(data) % 16)
    padded_data = data + bytes([padding_len] * padding_len)
    
    # 암호화 수행
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    print(encrypted_data)
    
    # 암호화된 데이터를 Base64 인코딩하여 반환
    return b64encode(encrypted_data).decode().rstrip("=")

# 1. OrderId를 먼저 Base64 인코딩
base64_encoded_order_id = b64encode(order_id.encode("utf-8")).decode("utf-8")

# 2. AES256-CBC 암호화 수행하여 EncryptionOrderId 생성
encryption_order_id = encrypt_aes256_cbc(base64_encoded_order_id.encode("utf-8"), encryption_key, initialisation_vector)

# 3. 암호화된 결과를 URL에 추가
api_url = f"https://wapi.wifidosirak.com/api/v1/order/{encryption_order_id}"

# 헤더 설정
headers = {
    "ClientID": client_id,
    "ApiKey": api_key
}

# API 요청 전송
response = requests.get(api_url, headers=headers)

# 응답 출력
print("Base64 인코딩된 OrderId:", base64_encoded_order_id)
print("암호화된 OrderId (EncryptionOrderId):", encryption_order_id)
print("API 호출 URL:", api_url)
print("응답 상태 코드:", response.status_code)
print("응답 본문:", response.text)
