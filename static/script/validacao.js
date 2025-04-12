const btnLogin = document.querySelector('.carrinho-form__btn');

const validarInput = () =>{
    inputUser = document.querySelector('#usuario').value;
    inputSenha = document.querySelector('#senha').value;
    if (inputUser.length < 8 || inputSenha.length < 8){
        alert("Mínimo 8 dígitos!");
        input.value = '';
        return false;
    }
    else{
        return true;
    }
}

btnLogin.addEventListener('click', validarInput)