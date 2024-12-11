package Fundamentos;
import java.util.Scanner;

public class Exercicio12 {

	public static void main(String[] args) {
		int num1;

		Scanner n1 = new Scanner(System.in);
		System.out.println("Digite um número: ");
		
		num1=n1.nextInt();
		
		if (num1==1) {
			System.out.println("Domingo");
		}
		else {
			if (num1==2) {
				System.out.println("Segunda");
			}
			else {
				if (num1==3) {
					System.out.println("Terça-Feira");
				}
				else {
					if (num1==4) {
						System.out.println("Quarta-Feira");
					}
					else {
						if (num1==5) {
							System.out.println("Quinta-Feira");
						}
						else {
							if (num1==5) {
								System.out.println("Sexta-Feira");
							}
							else {
								if (num1==5) {
									System.out.println("Sábado");
								}
								else {System.out.println("Valor Inválido.");
}}}}}}}}}