package Fundamentos;

import java.util.Scanner;

public class Exercicio11 {
	public static void main(String[] args) {
		
		Scanner n1 = new Scanner(System.in);
		System.out.println("Digite o primeiro número: ");
		
		Scanner n2 = new Scanner(System.in);
		System.out.println("Digite o segundo número: ");
		
		Scanner n3 = new Scanner(System.in);
		System.out.println("Digite o terceiro número: ");
		
		int num1, num2, num3;
		
		num1 = n1.nextInt();
		num2 = n2.nextInt();
		num3 = n3.nextInt();
		
		if (num1>num2 && num1>num3) {
			System.out.println(num1 + " é o maior.");
		}
		else {}
		if (num2>num1 && num2>num3) {
			System.out.println(num2 + " é o maior.");
			}
		else {
			if (num3>num1 && num3>num2) {
			System.out.println(num3 + " é o maior número");
				}	}	
	}
}
