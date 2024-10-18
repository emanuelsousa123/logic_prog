
function alerta(){
    let peso = document.getElementById('peso').value;
    let altura = document.getElementById('altura').value;
    let imc = peso/(altura*altura);
    document.getElementById('imc').innerHTML= imc.toFixed(1);
    if (imc<18.5) {
        document.getElementById('class').innerHTML= 'Abaixo do peso.';
    } else if (18.5<imc && imc<24.9) {
        document.getElementById('class').innerHTML= 'Peso normal.';
    } else if (25<imc && imc<29.9) {
        document.getElementById('class').innerHTML= 'Excesso de peso.';
    } else {
        document.getElementById('class').innerHTML= 'Obesidade.'
    }
}
