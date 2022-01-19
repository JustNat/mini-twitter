# PROJETO MINI-TWITTER

by b2bit


	Bem-vindo(a) ao projeto de seleção para backend developers da b2bit! Neste projeto, vamos abordar algumas técnicas e tecnologias  que você utilizará no seu dia-a-dia aqui na empresa 😉. Abaixo, segue um índice sobre este documento. 

🏁 DESCRIÇÃO

	Implementar uma API REST em que um usuário possa realizar um cadastro, publicar Posts e ver as publicações de outros usuários.


📄 REQUISITOS TÉCNICOS

    Criar a aplicação em formato REST;
    Python 3;
    Django REST Framework (preferencialmente). Mas pode utilizar qualquer framework em Python. Queremos avaliar se você conhece os conceitos da web;
    Banco de dados: relacional. Preferencialmente PostgreSQL;


Diferencial

    Diagrama entidade relacional do banco de dados utilizado no projeto;


👨🏼‍🏫 CASOS DE USO
CASO 1: Cadastro de usuário

	O ator faz o cadastro no sistema através da API. Como usuário, ele deve poder fazer o cadastro, para que ele tenha acesso ao Login. Use os campos que achar necessário para a definição do modelo do usuário.


CASO 2: Autenticação (Login)

	O ator deve ser autenticado no sistema através de um Token. Como usuário, ele deve poder fazer login, para que ele tenha acesso ao sistema. Este token deve ter uma data de expiração.


CASO 3: Fazer uma publicação

	O ator cria um post. Esta publicação é persistida no sistema. Como usuário, ele deve poder criar uma publicação, para que possa ser vista por outros usuários do sistema.


CASO 4: Feed geral

    O ator deve receber, no formato JSON, o feed dos últimos 10 posts.


CASO 5: Feed personalizado

    Como usuário, ele deve ter um feed com apenas as publicações de usuários selecionados, para que ele possa ter mais controle do seu feed


Este caso de uso é semelhante a uma funcionalidade de feed de pessoas que você segue.



📜 Regras de negócio

    No feed, usuário não deve ver as próprias publicações;



💯 EXTRAS

Entregas extras que serão muito bem vistas.

    Testes automatizados;
    Deploy do projeto (colocar em produção);
    Upload de arquivos estáticos;
    Servir arquivos estáticos. Preferencialmente por uma CDN. Indicamos o AWS S3;


