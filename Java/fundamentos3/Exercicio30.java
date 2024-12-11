package fundamentos3;

public class Exercicio30 {

	public static void main(String[] args) {
		String texto[] = {"a","vida","é","bela"};
		
 		for (int i=0; i < texto.length;i++) {
			System.out.print(texto[i].toUpperCase()+' ');
		}

		for (int i=texto.length-2; i>0 ;i--) {
			System.out.print(texto[i].toUpperCase()+' ');
		}
	}

}


