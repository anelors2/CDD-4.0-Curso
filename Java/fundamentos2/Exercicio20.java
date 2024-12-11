package fundamentos2;

public class Exercicio20 {

	public static void main(String[] args) {
		for(int i=1; i<100;i++) {
			if(i%3==0) {
				System.out.println(i);
				break;
			}
		}
		
		for(int i=0;i<100;i++) {
			if(i>50 && i<60) {
				continue;
			}
			System.out.println(i);
		}
			

	}

}
