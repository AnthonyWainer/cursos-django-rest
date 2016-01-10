function suma(){
    s = $("#formulario").serialize();
    $.get("/suma",s,function(data){
        $("#resultado").html(data);
    });
}

function sumar(){
    n = prompt("ingrese la cantidad de números a sumar: ");
    texto = '';
    for (var i = 1; i <= parseInt(n); i++) {        
        texto += '<input type="number" class="form-control" name="suma[]" placeholder="número '+i+' "/>';
    }
    texto += "<input type='button' class='btn btn-default' onclick= 'suma()' value='sumar'>";
    $("#mostrar").html(texto);
}

function division(){
    d = $("#formulario").serialize();
    $.post("/div",d,function(data){
        $("#resultado").html(data);
    });
}

function divi(){
    texto = '';
    texto += '<input type="number" class="form-control" name="dividendo" placeholder="ingrese dividendo"/>';
    texto += '<input type="number" class="form-control" name="divisor" placeholder="ingrese divisor"/>';
    texto += "<input type='button' class='btn btn-default' onclick= 'division()' value='Dividir'>";
    $("#mostrar").html(texto);    
}