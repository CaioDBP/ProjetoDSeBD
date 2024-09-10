const form = document.getElementById('form');

form.addEventListener('submit', (e) => {
	e.preventDefault();
	
	const cpf = document.getElementById('cpf').value;
	const nome = document.getElementById('nome').value;
	const senha = document.getElementById('senha').value;
	const sexo = document.getElementById('sexo').value;
	const idade = document.getElementById('idade').value;
	const endereco = document.getElementById('endereco').value;
	const email = document.getElementById('email').value;
	const telefone = document.getElementById('telefone').value;
	
	// You can add your logic here to handle the form data
	console.log(`CPF: ${cpf}, Nome: ${nome}, Senha: ${senha}, Sexo: ${sexo}, Idade: ${idade}, Endereço: ${endereco}, Email: ${email}, Telefone: ${telefone}`);
});