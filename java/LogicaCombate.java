import java.util.Scanner;
public class LogicaCombate {
  public static void main(String[] args) {

    // Datos del combate
    int vida_enemigo = 40;
    int ataque = 35;
    int nivel_jugador = 6;

    // Clase del jugador
    String clase = "Mago";
    int nivelHabilidad = 3;

    // Tipo de ataque (switch moderno)
    String tipoAtaque = switch (clase) {
      case "Guerrero" -> "Espada";
      case "Mago"     -> "Hechizo";
      case "Arquero"  -> "Flecha";
      default         -> "Puño";
    };

    // Puede usar magia
    boolean puedeUsarMagia =
      clase.equals("Mago") && nivelHabilidad >= 3;

    // Bonificación
    int bonificacion = (nivel_jugador >= 5) ? 10 : 0;

    // Cálculos
    int dano_total = ataque + bonificacion;
    int vida_restante = vida_enemigo - dano_total;

    // Acción del jugador
    if (puedeUsarMagia) {
      System.out.println("Bola de fuego!");
    } else {
      System.out.println(tipoAtaque + " basico");
    }

    // Resultado del combate
    if (vida_restante <= 0) {
      System.out.println("Enemigo derrotado! +50 XP");
    } else if (vida_restante <= 20) {
      System.out.println("Enemigo en estado critico");
    } else {
      System.out.println("Enemigo resiste. Vida restante: " + vida_restante);
    }
  }
}