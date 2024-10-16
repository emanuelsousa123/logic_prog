function alerta() {
    let peso = document.getElementById("peso").value;
    let altura = document.getElementById("altura").value;
    let imc = peso/(altura*altura)
    alert(imc);
}