package fundamentos3;

import java.util.Scanner;

public class Exercicio29 {

	public static void main(String[] args) {
		String texto01 = "Será que são iguais?";
		String texto02 = "Será que são iguais?";
		boolean res = texto01.equals(texto02);
		System.out.println(res);
		
		Scanner n1 = new Scanner(System.in);
		System.out.println("Digite um texto: ");
		String tex = n1.next();
		String m = tex.toUpperCase();
		System.out.println(m);
	}

}
