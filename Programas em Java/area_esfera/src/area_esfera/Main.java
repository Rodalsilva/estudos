package area_esfera;

import java.util.Locale;
import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		Locale.setDefault(Locale.US);
		Scanner sc = new Scanner(System.in);
		System.out.print("Digite um valor para o raio da circunferência: ");
		double R = sc.nextDouble();
		if (R < 10) {
			double A = 4*Math.PI*R*Math.pow(R, 2);
			System.out.printf("A área da superfície da esfera em quilômetros quadrados é: %.4f%n", A);
		}		
		else {
			int n = 10;
			int i = 0;
			int j =  i;
			while (i < n) {
				R = R/Math.pow(10, i);
				j = j + i;
				if (R < 10) {
					double A = 4*Math.PI*Math.pow(R*Math.pow(10, i), 2);
					System.out.printf("A área da superfície da esfera em quilômetros quadrados é: %.4f%n", A);
					System.out.print("A ordem de grandeza da medida da área da superfície da esfera é superior a 10 elevado a: ");
					System.out.print(2*j);
					break;
				}
				i = i + 1;
			}
		}		
		sc.close();
	}
}

