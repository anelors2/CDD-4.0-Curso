package fundamentos2;
import java.util.Scanner;
public class Exercicio18 {

	public static void main(String[] args) {
		int alunos, fim;
		float nota, media;
		fim=0;
		nota=0;
		Scanner input = new Scanner(System.in);
		System.out.println("Quantos alunos tem na sala? ");
		alunos = input.nextInt();
		
		while(fim!=alunos) {
			Scanner notas = new Scanner(System.in);
			System.out.println("Qual a nota do aluno ");
			nota = nota+notas.nextFloat();
			fim++;
		}
		 media= nota/alunos;
		 System.out.println("Média dos alunos é: " + media);;
		
		
	}

}
