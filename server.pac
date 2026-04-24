program SimpleHTTPServer;

uses
  sockets, sysutils;

var
  serverSocket, clientSocket: longint;
  addr: TInetSockAddr;
  buffer: array[0..1023] of char;
  response: string;
  len: longint;

begin
  serverSocket := fpsocket(AF_INET, SOCK_STREAM, 0);

  addr.sin_family := AF_INET;
  addr.sin_port := htons(8080);
  addr.sin_addr.s_addr := htonl(INADDR_ANY);

  if fpbind(serverSocket, @addr, sizeof(addr)) <> 0 then
  begin
    writeln('Erro ao fazer bind');
    halt;
  end;

  if fplisten(serverSocket, 1) <> 0 then
  begin
    writeln('Erro ao iniciar listen');
    halt;
  end;

  writeln('Servidor rodando em http://localhost:8080');

  clientSocket := fpaccept(serverSocket, nil, nil);

  len := fprecv(clientSocket, @buffer, sizeof(buffer), 0);

  response :=
    'HTTP/1.1 200 OK'#13#10 +
    'Content-Type: text/html'#13#10 +
    'Connection: close'#13#10 +
    #13#10 +
    '<html><body><h1>Hello World em Pascal</h1></body></html>';

  fpsend(clientSocket, @response[1], length(response), 0);

  CloseSocket(clientSocket);
  CloseSocket(serverSocket);
end.
