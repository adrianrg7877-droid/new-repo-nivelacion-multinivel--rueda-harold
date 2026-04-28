public class FuncionesRPG {

    // Retorna el daño real (min 1)
    public static int calcularDano(int ataque, int defensa) {
        int dano = ataque - defensa;
        return dano > 0 ? dano : 1;
    }

    // Cura sin pasar del máximo
    public static double aplicarCuracion(double vida, double cur, double max) {
        double nueva = vida + cur;
        return nueva > max ? max : nueva;
    }

    // Sin retorno: solo imprime
    public static void mostrarEstado(String n, double vida, int niv) {
        System.out.printf("%s [Nv%d] HP: %.0f%n", n, niv, vida);
    }

    // Sube de nivel si tiene suficiente XP
    public static int subirNivel(int xpActual, int xpNecesario, int nivelActual) {
        if (xpActual >= xpNecesario) {
            nivelActual++;
            xpActual = 0;
            System.out.println("¡Subiste al nivel " + nivelActual + "!");
        }
        return nivelActual;
    }

    public static void main(String[] args) {

        // Prueba calcularDano
        int d = calcularDano(20, 8);
        System.out.println("Dano: " + d);

        // Prueba aplicarCuracion y mostrarEstado
        double v = aplicarCuracion(40, 80, 100);
        mostrarEstado("Frodo", v, 3);

        // Prueba subirNivel: xp=110, xpNecesario=100, nivel=3 → retorna 4
        int resultado1 = subirNivel(110, 100, 3);
        System.out.println("Nivel resultante: " + resultado1);

        // Prueba subirNivel: xp=80, xpNecesario=100, nivel=3 → retorna 3
        int resultado2 = subirNivel(80, 100, 3);
        System.out.println("Nivel resultante: " + resultado2);
    }
}