package Fundamentos;
import java.util.Scanner;
public class Exercicio15 {
	public static void main(String[] args) {		 
		Scanner MF = new Scanner(System.in);
		System.out.println("Qual seu gênero: ");		
		char gen = MF.next().charAt(0);
		if (gen =='F' || gen == 'f') {System.out.println("Feminino");}			
		else { if (gen == 'M' || gen == 'm') {System.out.println("Masculino");} else {System.out.println("Valor Incorreto.");}}}}
			
			

