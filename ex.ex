IO.puts("salve")
v1 = IO.gets("> ") |> String.trim() |> String.to_integer()
v2 = IO.gets("> ") |> String.trim() |> String.to_integer()

IO.puts("Resultado = #{v1 + v2}")
