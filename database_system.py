import time

class User:
    def __init__(self, username, password):
        self.username = username
        self.time_created = time.time_ns() // 1000000
        self.password = self.encode(password, self.time_created)


    def encode(self, password, encoder):
        encoded_pass = ""
        for letter, number in zip(password, str(encoder)*5):
            encoded_pass += chr(ord(letter) + int(number))
        return encoded_pass


    def decode(self):
        password = self.password
        time_created = self.time_created
        decoded = ""

        for letter, number in zip(password, str(time_created)*5):
            decoded += chr(ord(letter) - int(number))

        return decoded



u1 = User("Pavlyuchenko", "Stepan_Je_Pepan")
print(u1.decode())
