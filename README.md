
# E-commerce API

Bem-vindo à E-commerce API! Este é um projeto de exemplo desenvolvido para fins de estudo, focado em demonstrar a criação de uma API RESTful para gerenciar um e-commerce. A API oferece recursos para manipulação de produtos, usuários, login e carrinhos de compras.


## Tecnologias Utilizadas

- **Python** (Flask)
- **SQLAlchemy** (ORM)
- **SQLite** (Banco de dados para teste)
- **Flask Login Manager** (Para fazer login e logout na API e controlar as rotas que não podem ser chamadas sem usuário logado)



## Funcionalidades

- Login e logout de usuário 
- Criação de novos usuários
- CRUD de produtos (criar, listar, atualizar, consultar e excluir produtos)
- CRUD de carrinhos de compras (criar, atualizar, consultar e checkout excluindo o carrinho) validando usuário logado

## Como Executar o Projeto

**Pré-requisitos**
- Python 3.x
- Virtualenv (recomendado)


**Passos para rodar a aplicação**

 1 - Clone este repositório:
 ```bash
  git clone https://github.com/brunosenadev/api-ecommerce.git
  cd api-ecommerce
```
2 - Crie um ambiente virtual e ative-o::
 ```bash
  python -m venv venv
  source venv/bin/activate   # Linux/macOS
  venv\Scripts\activate      # Windows 
```
 3 - Instale as dependências:
 ```bash
  pip install -r requirements.txte
```
4 - Execute a aplicação:
```bash
  python src/main.python
```
## Rotas disponíveis

**Usuários**

- **POST** `/login` - Login de usuários 
- **POST** `/logout` - Logout de usuários
- **POST** `/api/users/add` - Criar um novo usuário

**Produtos**
- **GET** `/api/producs` - Listar todos os produtos
- **GET** `/api/products/{product_id}` - Visualizar detalhes de um produto específico
- **POST** `/api/products/add` - Adicionar um novo produto
- **PUT** `/api/products/update/{product_id}` - Atualizar um produto
- **DELETE** `/api/products/delete/{product_id}` - Excluir um produto

**Carrinho**
- **POST** `/api/cart/add/{product_id}` - Adicionar um item ao carrinho
- **DELETE** `/api/cart/remove/{product_id}` - Remover um item do carrinho
- **GET** `/api/cart` - Visualizar o carrinho do usuário logado
- **POST** `/api/cart/checkout` - Checkout e limpar o carrinho
