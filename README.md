# Teste Técnico Ivjur

Este é um teste técnico proposto pela Ivjur para avaliar suas habilidades em diversas áreas da programação, desde fundamentos de Python até integrações com APIs externas e manipulação de dados.

## Questões:

1. **Fundamentos de Python:** Nesta questão, você será desafiado a escrever uma função em Python que receba uma lista de números e retorne uma nova lista contendo apenas os números pares da lista original, multiplicados por 2.

2. **FastAPI:** Aqui, sua tarefa é criar um pequeno aplicativo FastAPI. Você deve implementar um endpoint POST `/create-user`, que aceite um "username" e "email" no corpo da solicitação, e um endpoint GET `/get-user/{user_id}`, que retorne os dados de um usuário com base em um ID fornecido.

3. **Integrações com APIs Externas:** Nesta questão, você irá utilizar Python para fazer uma requisição à API pública JSONPlaceholder (https://jsonplaceholder.typicode.com/) para obter posts de usuários. Em seguida, você deve expor esses dados através de um endpoint FastAPI. Além disso, descreva como você faria a autenticação se a API exigisse um token de acesso.

4. **Manipulação de Dados e Lógica de Negócios:** Nesta tarefa prática, você receberá um arquivo JSON contendo dados de vendas de produtos (produto, quantidade, preço). Sua missão é escrever um script Python que calcule o total de vendas (quantidade * preço) para cada produto e retorne o nome do produto mais vendido.

## Guia de Utilização:

1. Abra uma pasta no seu editor de código preferido, como o Visual Studio Code.
2. Crie uma nova pasta com o nome que preferir para este teste técnico.
3. Abra o terminal na pasta recém-criada.
4. Inicie o git no terminal com o seguinte comando:
   ```
   git init
   ```
5. Clone este repositório utilizando o seguinte comando:
   ```
   git clone https://github.com/Jozincanela/Teste-tec-ivjur.git
   ```
   (Substitua "link" pelo link fornecido para clonagem do repositório)
6. Após clonar o repositório, execute o arquivo `.cmd` para configurar o ambiente virtual e instalar as bibliotecas necessárias com o seguinte comando:
   ```
   ./run.cmd
   ```
7. Aguarde até que a configuração e instalação sejam concluídas.
8. Agora você está pronto para começar a testar as soluções propostas. Cada questão pode ter suas próprias instruções específicas para teste.
9. Para testar a API da questão 2 e 3, será necessário abrir outro terminal dentro de uma das pastas e executar os seguintes comandos:
   ```
   cd env
   ./scripts/activate
   cd ..
   uvicorn main:app --reload
   ```
10. Após executar esses comandos, um link HTTPS será gerado. Copie este link e cole-o na barra de endereços do seu navegador. Adicione "/docs" ao final do link para visualizar o Swagger da aplicação em FastAPI.
