package fundamentos2;

import java.util.Scanner;

public class Exercicio24 {

	public static void main(String[] args) {
		int alunos;
		float nota, media;
		nota=0;
		alunos=2;
		Scanner input = new Scanner(System.in);
		System.out.println("Quantos alunos tem na sala? ");
		alunos = input.nextInt();
		
		for(int i = 0;i!=alunos; i++) {
			Scanner notas = new Scanner(System.in);
			System.out.println("Qual a nota do aluno ");
			nota = nota+notas.nextFloat();
			
		}
		 media= nota/alunos;
		 System.out.println("Média dos alunos é: " + media);;

	}

}
