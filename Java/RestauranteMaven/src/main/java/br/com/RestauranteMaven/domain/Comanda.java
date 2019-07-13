package br.com.RestauranteMaven.domain;

public class Comanda {
	public int mesa;
	public double valorItens;
	public double Resultado;
	public double ValorPago;
	public double Troco;
	public int getMesa() {
		return mesa;
	}
	public void setMesa(int mesa) {
		this.mesa = mesa;
	}
	public double getValorItens() {
		return valorItens;
	}
	public void setValorItens(double valorItens) {
		this.valorItens = valorItens;
	}
	public double getResultado() {
		return Resultado;
	}
	public void setResultado(double resultado) {
		Resultado = resultado;
	}
	public double getValorPago() {
		return ValorPago;
	}
	public void setValorPago(double valorPago) {
		ValorPago = valorPago;
	}
	public double getTroco() {
		return Troco;
	}
	public void setTroco(double troco) {
		Troco = troco;
	}
	
	
}
