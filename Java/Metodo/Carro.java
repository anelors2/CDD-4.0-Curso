package Metodo;

public class Carro {
	String modelo,cor;
	double preco;
	boolean estado=false;
	
	public Carro() {
		
	}
	public Carro(String modelo) {
		this.modelo=modelo;
	}
	public Carro(String modelo,String cor){
		this.modelo=modelo;
		this.cor=cor;
	}
	public Carro(String modelo,String cor,double preco){
		this.modelo=modelo;
		this.cor=cor;
		this.preco=preco;
	}

	public void ligar(){
		if (estado == false) {
			System.out.println("Carro ligou.");
			estado = true;}
		else {
			System.out.println("Carro já está ligado");}}
	
	public void desligar(){
		if(estado == true) {
			System.out.println("Carro desligou.");
			estado = false;}
		else {System.out.println("Carro já está desligado");}}
	
	public void acelerar(){
		if(estado == true) {
			System.out.println("Vrumm Vrummm, Acelerou.");}
		else {System.out.println("Carro Desligado.");}
	}
	
	public void frear(){
		if(estado == true) {
			System.out.println("Freando...");}
		else {System.out.println("Carro Desligado.");}
	}

}
