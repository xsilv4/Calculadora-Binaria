function convert() {
    var choice = document.getElementById("choice").value;
    var input = document.getElementById("input").value;

    if (choice == '1') {
        document.getElementById("binary").innerHTML = parseInt(input, 10).toString(2);
        document.getElementById("hexadecimal").innerHTML = parseInt(input, 10).toString(16);
        document.getElementById("octal").innerHTML = parseInt(input, 10).toString(8);
    } else if (choice == '2') {
        document.getElementById("decimal").innerHTML = parseInt(input, 2).toString(10);
        document.getElementById("decimal2").innerHTML = parseInt(input, 8).toString(10);
        document.getElementById("decimal3").innerHTML = parseInt(input, 16).toString(10);
    } else {
        alert("Opção inválida.");
    }
}