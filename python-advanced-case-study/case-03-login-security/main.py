# Studi Kasus 3: Sistem Keamanan Akun & Audit Log Login
import re
from datetime import datetime
from functools import wraps


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not isinstance(value, str) or not re.fullmatch(r"[A-Za-z0-9]{5,}", value):
            raise ValueError("Username minimal 5 karakter dan hanya boleh berisi huruf/angka.")
        self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if not isinstance(value, str) or not re.fullmatch(r"(?=.*\d).{8,}", value):
            raise ValueError("Password minimal 8 karakter dan wajib mengandung angka.")
        self._password = value


def audit_log(func):
    @wraps(func)
    def wrapper(username, password):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            hasil = func(username, password)
            print(f"[{timestamp}] Username: {username} | Status: BERHASIL | Keterangan: Login berhasil.")
            return hasil
        except ValueError as error:
            print(f"[{timestamp}] Username: {username} | Status: DITOLAK | Alasan: {error}")
            return False
    return wrapper


@audit_log
def login(username, password):
    user = User(username, password)

    if user.username == "Mahasiswa01" and user.password == "Belajar123":
        return True
    raise ValueError("Username atau password tidak cocok.")


if __name__ == "__main__":
    print("=" * 65)
    print("               SISTEM KEAMANAN LOGIN")
    print("=" * 65)

    print("\nPengujian 1 - Username tidak valid")
    login("Av!n", "Belajar123")

    print("\nPengujian 2 - Password terlalu pendek")
    login("Mahasiswa01", "abc123")

    print("\nPengujian 3 - Password tidak mengandung angka")
    login("Mahasiswa01", "BelajarPython")

    print("\nPengujian 4 - Format valid tetapi kredensial salah")
    login("Mahasiswa02", "Rahasia123")

    print("\nPengujian 5 - Login berhasil")
    login("Mahasiswa01", "Belajar123")
