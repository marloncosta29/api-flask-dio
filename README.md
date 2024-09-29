# Projeto de Estudo em Flask - DIO

Este repositório contém um projeto desenvolvido com **Flask**, parte do curso de Formação Python da plataforma [Digital Innovation One (DIO)](https://www.dio.me). O objetivo principal é explorar os fundamentos da construção de APIs em Python, incluindo a integração com bancos de dados e a migração de esquemas. O foco deste projeto é permitir que quem estuda Python por hobby ou paixão possa aprender e experimentar recursos práticos em um ambiente controlado.

## Descrição

Este projeto tem como finalidade apresentar uma API simples utilizando o framework **Flask**, um dos mais populares frameworks de desenvolvimento web em Python. Ele inclui suporte para autenticação JWT e migrações de banco de dados utilizando Flask-Migrate e SQLAlchemy para persistência de dados.

O projeto é ideal para quem já tem familiaridade básica com Python e quer aprofundar seus conhecimentos no desenvolvimento de APIs utilizando tecnologias amplamente usadas no mercado. Todos os pacotes utilizados foram gerenciados com o **Poetry**, permitindo um gerenciamento eficaz de dependências e ambientes.

## Principais Tecnologias Utilizadas

Aqui estão listados os pacotes mais importantes e seus papéis no projeto:

- **[Flask](https://flask.palletsprojects.com/)** (v3.0.3): Framework principal para a construção da API. Ele fornece uma base leve e flexível para o desenvolvimento de APIs robustas e escaláveis.
- **[Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)** (v3.1.1): Extensão para integrar o ORM SQLAlchemy ao Flask, facilitando a manipulação de dados em bancos de dados relacionais.
- **[Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/)** (v4.6.0): Extensão que permite implementar autenticação baseada em tokens JWT, garantindo uma segurança robusta para a API.
- **[Flask-Migrate](https://flask-migrate.readthedocs.io/)** (v4.0.7): Ferramenta para gerenciar migrações de banco de dados em uma aplicação Flask utilizando SQLAlchemy.
- **[SQLAlchemy](https://www.sqlalchemy.org/)** (v2.0.34): Biblioteca de abstração de banco de dados que facilita o trabalho com diferentes bancos relacionais em Python.
- **[PyJWT](https://pyjwt.readthedocs.io/)** (v2.9.0): Implementação de JSON Web Tokens (JWT) em Python, usada para autenticação e autorização de usuários.

## Requisitos

- **Python 3.10 ou superior**
- **Poetry** para gerenciar as dependências
- Um banco de dados (PostgreSQL, MySQL, ou SQLite)

## Como Executar o Projeto

1. Clone este repositório:
   ```bash
    git clone https://github.com/seuusuario/seuprojeto.git
    cd seuprojeto
   ```
2. Instale as dependências do projeto:
   ```bash 
   poetry install
   ```
3. Execute as migrações do banco de dados:
    ```bash
    poetry run flask db upgrade
    ```
4. Inicie a aplicação:
    ```bash
    poetry run flask db upgrade
    ```
## Conclusão
Este projeto foi desenvolvido com o intuito de proporcionar uma experiência prática no uso do Flask, SQLAlchemy e outras bibliotecas relevantes. É ideal para quem quer aprender desenvolvimento de APIs em Python de maneira estruturada, mas também flexível o suficiente para explorar novas funcionalidades e conceitos.