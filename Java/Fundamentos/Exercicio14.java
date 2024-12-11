package Fundamentos;
import java.util.Scanner;
public class Exercicio14 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		float n1,n2,nf;
		
		Scanner nota1 = new Scanner(System.in);
		System.out.println("Digite a primeira nota: ");
		
		Scanner nota2 = new Scanner(System.in);
		System.out.println("Digite a segunda nota: ");
		
		n1= nota1.nextFloat();
		n2 = nota2.nextFloat();
		
		nf = (n1+n2)/2;
		
		System.out.println("Sua nota é: " + nf);

	}

}
