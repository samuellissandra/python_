from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet

# Gerar um par de chaves RSA (assimétrico)
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
public_key = private_key.public_key()

# Gerar uma chave simétrica para criptografia dos dados
symmetric_key = Fernet.generate_key()
cipher_suite = Fernet(symmetric_key)

class Person:
    def __init__(self, nome, cpf, rg, telefone, email, estado_civil):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.telefone = telefone
        self.email = email
        self.estado_civil = estado_civil
    
    def cifrar_dados(self):
        # Criptografar os dados sensíveis com chave simétrica
        self.cpf = cipher_suite.encrypt(self.cpf.encode()).decode()
        self.rg = cipher_suite.encrypt(self.rg.encode()).decode()
        
        # Criptografar a chave simétrica com chave pública
        self.encrypted_symmetric_key = public_key.encrypt(
            symmetric_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

    def decifrar_dados(self):
        # Decifrar a chave simétrica com chave privada
        symmetric_key = private_key.decrypt(
            self.encrypted_symmetric_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        # Decifrar os dados sensíveis com a chave simétrica
        self.cpf = cipher_suite.decrypt(self.cpf.encode()).decode()
        self.rg = cipher_suite.decrypt(self.rg.encode()).decode()

# Exemplo de uso:
if __name__ == "__main__":
    # Criando uma instância de Person
    pessoa = Person(
        nome="Fulano de Tal",
        cpf="123.456.789-00",
        rg="123456789",
        telefone="(12) 3456-7890",
        email="fulano@example.com",
        estado_civil="solteiro(a)"
    )

    # Cifrar os dados sensíveis (CPF e RG)
    pessoa.cifrar_dados()

    # Mostrar os dados cifrados
    print("Dados cifrados:")
    print(f"CPF cifrado: {pessoa.cpf}")
    print(f"RG cifrado: {pessoa.rg}")

    # Decifrar os dados
    pessoa.decifrar_dados()

    # Mostrar os dados decifrados
    print("\nDados decifrados:")
    print(f"CPF decifrado: {pessoa.cpf}")
    print(f"RG decifrado: {pessoa.rg}")
