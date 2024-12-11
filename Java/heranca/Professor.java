package heranca;

public class Professor extends Pessoa {
	double salario;
	
	
	public Professor(String nome, String telefone, String cpf) {
		super(nome, telefone, cpf);
		
	}
	public void diversao() {
		System.out.println("Aplicando prova.");
	}
	public void certificar() {
		System.out.println("Se ferrou.");
	}

}
