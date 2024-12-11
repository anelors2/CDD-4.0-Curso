package heranca;

public class Aluno extends Pessoa {
	double nota;	
	public Aluno(String nome, String telefone, String cpf) {
		super(nome, telefone, cpf);
		
	}
	public void sofrer() {
		System.out.println("Fazendo prova");
	}
}
