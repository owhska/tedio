program ler;

var
numero: integer;

begin
    writeln('Digite sua idade: ');
    readln(numero);

    if(numero < 18)then
    begin
        writeln('menor de idade');
    end
    else
    begin
        writeln('maior de idade');
    end
end.

