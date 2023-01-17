from hashlib import sha256
from cryptography.hazmat.primitives import serialization, asymmetric


def generate_key_pair() -> tuple[str, str]:
    private_key = asymmetric.rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    return private_pem.decode(), public_pem.decode()


def encrypt_256(string: str) -> str:
    return sha256(string.encode()).hexdigest()


if __name__ == "__main__":
    private, public = generate_key_pair()
    print(private)
    print(public)


