package fundamentos3;

import java.util.StringTokenizer;

public class Exercicio28 {
	public static void main(String[] args) {
		String str = " texto para retirar os espaços no inicio e fim ";
		String a = str.trim();
		System.out.println(a);
		StringTokenizer b = new StringTokenizer(" texto para retirar os espaços no inicio e fim ") ;
		System.out.println(b.countTokens());
}}
