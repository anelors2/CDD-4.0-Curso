package Aula01;

import java.util.Scanner;

public class Exemplo09 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner entrada = new Scanner(System.in);
		System.out.println("Digite um número: ");
		double resp = entrada.nextDouble();
		System.out.println(resp);
		
		Scanner entrada = new Scanner(System.in);
		System.out.println("Digite um número: ");
		Scanner mult = new Scanner(System.in);
		System.out.println("Digite outro número: ");
		double resp = entrada.nextDouble() + mult.nextDouble();

	}

}
