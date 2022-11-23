# Importar arquivo Pessoa.py no diretório model
from model.Pessoa import Pessoa

# Exemplo de uso
poyatos = Pessoa(1, "Henrique Poyatos")
print(poyatos)

# Mostrar só o nome
print(poyatos.nome)