package Fundamentos;

import java.util.Scanner;

public class Exercicio10 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner entrada = new Scanner(System.in);
		System.out.println("Digite um número: ");
		
		int n = entrada.nextInt();
		if (n > 0) {
		System.out.println("Número Positivo.");
		}
		else {
			System.out.println("Número Negativo.");
		}

	}

}
