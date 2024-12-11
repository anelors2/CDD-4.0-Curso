package fundamentos3;

public class Exercicio26 {
	public static void main(String[] args) {
		String s = "Hello  ";		
		String res = s.replace("l","w");
		System.out.println(res); 		// Hewwo
		
		String str = "Oi "; String texto = str + "Mundo";
		System.out.println(texto);		// Oi Mundo
		
		int tres = 3;
		String resf = 3 + " palavra " + tres;
		System.out.println(resf);		// 3 palavra 3
		
		String str2 = "Hello World";
		String resu = str2.substring(6);
		System.out.println(resu);		// World
		
		resu = str2.substring(3,8);
		System.out.println(resu);		// lo Wo
		
		resu = str2.toUpperCase(); System.out.println(resu);		// HELLO WORLD
		
		resu = str2.toLowerCase(); System.out.println(resu);		// hello world
				
		res = s.trim(); System.out.println(s); System.out.println(res);		// Remove os espaços vazios "Hello  " - "Hello"
		
		char c = str2.charAt(1); System.out.println(c);		// Retorna o indice 1 da palavra - "e"	
		
		String s1 = "Hello";
		String s2 = "HELLO";
		boolean b1,b2,b3,b4;
		b1 = s1.equals("Hello"); if(b1==true) {
			System.out.println(b1 + " é Verdadeiro");
		}else {System.out.println(b1 + " é Falso");}
		
		b2 = s1.equals(s2);
		if(b2==true) {
			System.out.println("Verdadeiro");
		}else{ System.out.println("Falso");}
		
		b3 = s1.equalsIgnoreCase(s2);
		if(b3==true) {
			System.out.println("Verdadeiro");
		}else{ System.out.println("Falso");}
		
		b4 = s1.equalsIgnoreCase("azul");
		if(b4==true) {
			System.out.println("Verdadeiro");
		}else { System.out.println("Falso");}

		
		
}}