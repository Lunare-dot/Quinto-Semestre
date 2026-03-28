import java.util.Random;

public class Singleton {
    private static Singleton instance;
    private static int valor;

    private Singleton() {
        Random rn = new Random(System.currentTimeMillis());
        valor = rn.nextInt(1000);
    }

    public static Singleton getInstance() {
        if(instance == null) {
            instance = new Singleton();
        }
        return instance;
    }

    public void showMessage() { System.out.println("Singleton: " + valor); }
}
