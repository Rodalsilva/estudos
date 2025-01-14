package calculo_circunferencia;

import java.util.Locale;
import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		Locale.setDefault(Locale.US);
		Scanner sc = new Scanner(System.in);
		System.out.print("Digite um valor para o raio da circunferência: ");
		double R = sc.nextDouble();
		if (R < 10) {
			double C, P;
			P = Math.PI;
			C = 2*P*R;
			System.out.printf("O comprimento da circunferência é: %.2f%n", C);
		}		
		else {
			int n = 10;
			int i = 0;
			int j = i;
			while (i < n) {
				R = R/Math.pow(10, i);
				j = j + i;
				if (R < 10) {
					double C, P;
					P = Math.PI;
					C = 2*P*R*Math.pow(10, i);
					System.out.printf("O comprimento da circunferência em km é: %.4f%n", C);
					System.out.print("A ordem de grandeza da circunferência é dada por 10 elevado a: ");
					System.out.print(j);
					break;
				}
				i = i + 1;
			}
		}		
		sc.close();
	}
}


