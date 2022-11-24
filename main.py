# Importar arquivo Pessoa.py no diretório model
from model.Pessoa import Pessoa
from database.Database import Database
from dao.PessoaDAO import PessoaDAO

# Exemplo de uso
poyatos = Pessoa(1, "Henrique Poyatos")
print(poyatos)

# Mostrar só o nome
print(poyatos.nome)
print("\nAcesso ao banco...\n")

# Chamar objeto de banco de dados
db = Database()

# Instancia o objeto
pessoaDAO = PessoaDAO(db.conexao, db.cursor)

# Carregar uma lista com o que veio do banco de dados
pessoas = pessoaDAO.getAll(orderBy = True)
for pessoa in pessoas:
  print(pessoa)


# Criar um objeto com qualquer ator/atriz/diretor
novo = Pessoa(0, "Denzel Washington")

novo = pessoaDAO.save(novo)

print(" ")

# Consultar banco novamente
pessoas = pessoaDAO.getAll(orderBy = True)
for pessoa in pessoas:
  print(pessoa)