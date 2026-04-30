public class simulacion{
    public static void main(String[] args) {

        
        String heroe = "Guerrero";
        int nivel = 2;
        int vidaMax = 80;
        int vida = 80;
        int ataque = 18;
        int defensa = 8;
        String[] enemigos = {"Goblin", "Orco", "Dragon"};
        int[] vidasEnemigos = {40, 70, 120};
        int[] ataquesEnemigos = {8, 14, 25};
        System.out.println("Héroe: " + heroe);
        System.out.println("Nivel: " + nivel);
        System.out.println("Vida: " + vida);
        System.out.println("\nEnemigos:");
        for (int i = 0; i < enemigos.length; i++) {
            System.out.println(enemigos[i] + " - Vida: " + vidasEnemigos[i] + " - Ataque: " + ataquesEnemigos[i]);
        }
    }
}