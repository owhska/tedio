package main

import rl "vendor:raylib"
import "core:fmt"
import "core:math/rand"

main :: proc() {

    contador := 0;
    v1 := rand.int31_max(10)
    v2 := rand.int31_max(10)
    v3 := rand.int31_max(10)

    rl.InitWindow(800, 450, "Exemplo de Botão")
    defer rl.CloseWindow()

    rl.SetTargetFPS(60)

    botao_rect := rl.Rectangle{300, 200, 200, 50}

    for !rl.WindowShouldClose() {
        if rl.IsMouseButtonPressed(.LEFT) {
            mouse_pos := rl.GetMousePosition()
            if rl.CheckCollisionPointRec(mouse_pos, botao_rect) {
                contador = contador + 1
                v1 = rand.int31_max(10)
                v2 = rand.int31_max(10)
                v3 = rand.int31_max(10)

                if v1 == 7 || v2 == 7 || v3 == 7 { fmt.println("vitoria na tentativa:", contador,"|", v1, v2, v3, "|"); break }
                fmt.println("tentativa:",contador, "|", v1, v2, v3, "|")
            }
        }
        
        rl.BeginDrawing()
        rl.ClearBackground(rl.RAYWHITE)
        
        //rl.DrawText(rl.TextFormat("Cliques: %d", contador), 350, 300, 20, rl.DARKGRAY)
        if v1 == 7 || v2 == 7 || v3 == 7 { 
            rl.DrawText(rl.TextFormat("vitoria na tentativa: %d | %d %d %d |",contador, v1, v2, v3), 350, 300, 20, rl.DARKGRAY)
        } else {
            rl.DrawText(rl.TextFormat("tentaiva: %d | %d %d %d |",contador, v1, v2, v3), 350, 300, 20, rl.DARKGRAY)
        }

        rl.DrawRectangleRec(botao_rect, rl.LIGHTGRAY)
        rl.DrawText("Clique Aqui", i32(botao_rect.x + 50), i32(botao_rect.y + 15), 20, rl.BLACK)

        rl.EndDrawing()
    }
}
