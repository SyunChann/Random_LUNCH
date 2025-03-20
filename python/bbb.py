from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from base64 import b64encode

# C#에서 추출한 키와 IV 값
key = bytes([
    220, 166, 28, 230, 161, 196, 166, 41, 
    77, 136, 152, 135, 51, 66, 143, 93, 
    155, 136, 118, 221, 221, 208, 84, 80, 
    21, 228, 39, 178, 153, 87, 50, 85
])

iv = bytes([
    77, 136, 152, 135, 51, 66, 143, 93, 
    78, 68, 60, 93, 199, 125, 188, 9
])

# 암호화할 OrderId (예: "E24110702025")
order_id = "E24110702025"

def encrypt_aes256_cbc(data, key, iv):
    # AES 암호화 설정 (CBC 모드)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    
    # 데이터에 UTF-16 인코딩 및 PKCS7 패딩 추가
    data_bytes = data.encode("utf-16")[2:]  # UTF-16 BOM 제거
    padding_len = 16 - (len(data_bytes) % 16)
    padded_data = data_bytes + bytes([padding_len] * padding_len)
    
    # 암호화 수행
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    
    # 암호화된 데이터를 Base64 인코딩하여 반환
    return b64encode(encrypted_data).decode()

# AES256-CBC 암호화 수행하여 EncryptionOrderId 생성
encryption_order_id = encrypt_aes256_cbc(order_id, key, iv)

# 결과 출력
print("암호화된 OrderId (EncryptionOrderId):", encryption_order_id)