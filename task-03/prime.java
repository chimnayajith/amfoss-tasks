import java.util.Scanner;

public class Main {
    public static Boolean isPrime(int num){
        if (num <= 1) return false;
        if (num <= 3) return true;
        if (num % 2 == 0 || num % 3 == 0) return false;

        int i = 5;
        while (i * i <= num) {
            if (num % i == 0 || num % (i + 2) == 0) return false;
            i += 6;
        }
        return true;
    }

    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        scanner.close();

        for (int i =2 ; i<=n ; i++){
            if(isPrime(i)){
                System.out.print(i + " ");
            }
        }

    }
}


// run java prime.java