package Fundamentos;
import java.util.Scanner;
public class Exercicio16 {

	public static void main(String[] args) {
		
		int res;
		Scanner input = new Scanner(System.in);
		System.out.println("Telefonou para a vítima? ");
		res = input.nextInt();
		System.out.println("Esteve no local do crime? ");
		res += input.nextInt();
		System.out.println( "Mora perto da vítima? ");
		res += input.nextInt();
		System.out.println("Devia para a vítima? ");
		res += input.nextInt();
		System.out.println("Já trabalhou com a vítima? ");
		res += input.nextInt();
		
		if (res == 5) {
			System.out.println("Culpado!");
		}else if (res >= 3 && res <= 4) {
			System.out.println("Cúmplice!");
		}else if (res == 2) {
			System.out.println("Suspeito");
		}else {System.out.println("Inocente!");}
		
	}

}
