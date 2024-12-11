package Poli;

public abstract class Animal {
	String nome;
	public Animal(String nome) {
		this.nome=nome;
		
	}public void Comer(){
		System.out.println("Animal foi Comer.");
	}public void Locomover() {
		System.out.println("O animal se locomoveu.");
	}

}
