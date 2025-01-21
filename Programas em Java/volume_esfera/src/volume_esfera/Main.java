package volume_esfera;

import java.util.Locale;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Locale.setDefault(Locale.US);
		Scanner sc = new Scanner(System.in);
		System.out.println("Digite o valor do raio da esfera: ");
		double R = sc.nextDouble();
		System.out.println(R);
		if (R < 10) {
			double V = (4/3)*Math.PI*R*Math.pow(R, 3);
			System.out.printf("A área da superfície da esfera em quilômetros quadrados é: %.4f%n", V);
		}		
		else {
			int n = 10;
			int i = 0;
			int j =  i;
			while (i < n) {
				R = R/Math.pow(10, i);
				j = j + i;
				if (R < 10) {
					double V = (4*Math.PI*Math.pow(R*Math.pow(10, i), 3))/3;
					System.out.printf("A área da superfície da esfera em quilômetros quadrados é: %.4f%n", V);
					System.out.print("A ordem de grandeza da medida da área da superfície da esfera é superior a 10 elevado a: ");
					System.out.print(3*j);
					break;
				}
				i = i + 1;
			}
		}	
		
		sc.close();
	}

}
