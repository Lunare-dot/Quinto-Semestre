//trazer o formulário
const form = document.getElementById('user-form')
const userList = document.getElementById('user-list')

cadastrarUsuario();

//evento para capturar os dados do formulário
form.addEventListener('submit', e=>{
    e.preventDefault(); //evitar que o formulário recarregue a página
    const nome = document.getElementById('nome').value;
    const email = document.getElementById('email').value;
    console.log(nome, email)
    
    //chamar uma função para cadastrar usuários
    cadastrarUsuario(nome, email);
});

//carregar usuários
function carregarUsuario(){
    fetch('/api/users', {
        method: 'GET'
    }) //requisição ao servidor
    .then(res => res.json()) //retornando as requisições no formato JSON
    .then(data => {
        //criar os itens do HTML
        userList.innerHTML = ''; //limpar o conteúdo
        data.users.forEach(user => {
            const li = document.createElement('li');
            li.innerHTML = `${user.nome} - ${user.email}
            <button onclick="excluirUsuario(${user.id})">Excluir</button>
            <button onclick="editarUsuario(${user.id})">Editar</button>`
            userList.appendChild(li);
        })
    })
}

//cadastrar usuários
function cadastrarUsuario(nome, email) {
    fetch('/api/users', { //rota disponível no servidor
        method: 'POST', //método HTTP
        headers: {'Content-Type': 'application/json'}, //o corpo da mensagem é no formato JSON
        body: JSON.stringify({nome, email}) //convertendo o objeto em uma string JSON
    })
    .then(() => { //usado para tratar a rota de requisição
        form.reset(); //limpar o formulário
        carregarUsuario(); //chamar a função de carregar usuários
        editarUsuario();
    })
}

//função excluir usuários
function excluirUsuario(id) {
    const confirmacao = confirm("Tem certeza?");
    if(!confirmacao) {
        return
    }
    fetch(`api/users/${id}`, { //definindo rota para excluir
        method: 'DELETE'
    }) //requisição para o servidor
    .then(() => {
        carregarUsuario();
    })
}

//função editar usuário
function editarUsuario(id) {
    fetch(`api/users/${id}`, {
        method: 'PUT',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({nome, email})
    })
    .then(() => {
        form.reset();
        carregarUsuario();
    })
}