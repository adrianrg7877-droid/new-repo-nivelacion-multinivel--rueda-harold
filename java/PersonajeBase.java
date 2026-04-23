import java.util.Scanner;

public class PersonajeBase {
  // Atributos del personaje
  String nombre = "Gandalf";
  int nivel = 5;
  double vida = 80.0;
  double vidaMaxima = 100.0;
  boolean estaVivo = true;
  String clase = "Mago";
  int puntosAtaque = 10;
  int puntosDefensa = 5;
  int mana = 120; // nuevo atributo

  public static void main(String[] args) {
    PersonajeBase p = new PersonajeBase();

    System.out.println(
      p.nombre + " [" + p.clase + "] Nv." + p.nivel +
      " | Vida: " + p.vida +
      " | Mana: " + p.mana
    );
  }
}