package Metodo;

public class usoCalc {

	public static void main(String[] args) {
		calculadora c1 = new calculadora();
		c1.somar(2, 3, 10);
		c1.somar(8, 7);
		
		c1.subtrair(7, 9, 5);
		c1.subtrair(7, 3);
		
		c1.multiplicar(7, 9, 5);
		c1.multiplicar(7, 3);
		
		c1.dividir(7, 9, 3);
		c1.dividir(7, 5);
		
		Carro c2 = new Carro();
		c2.desligar();
		c2.ligar();
		c2.ligar();
		c2.desligar();
		System.out.println(c2.modelo);
		
		Carro uno = new Carro(null);
		uno.ligar();
		uno.acelerar();
		uno.frear();
		uno.desligar();
		
		Carro onix = new Carro(null, null);
		onix.ligar();
		onix.acelerar();
		onix.frear();
		onix.desligar();
		
		Carro gol = new Carro(null,null, 120000);
		gol.ligar();
		gol.acelerar();
		gol.frear();
		gol.desligar();		
		
	}

}
