package br.com.RestauranteMaven.domain;

public class Produto {
	public String NomeProduto;
	public double ValorCompra;
	public double ValorVenda;
	public Data DataValidade;
	public String Lote;
	public String TipoProduto;
	public String getNomeProduto() {
		return NomeProduto;
	}
	public void setNomeProduto(String nomeProduto) {
		NomeProduto = nomeProduto;
	}
	public double getValorCompra() {
		return ValorCompra;
	}
	public void setValorCompra(double valorCompra) {
		ValorCompra = valorCompra;
	}
	public double getValorVenda() {
		return ValorVenda;
	}
	public void setValorVenda(double valorVenda) {
		ValorVenda = valorVenda;
	}
	public Data getDataValidade() {
		return DataValidade;
	}
	public void setDataValidade(Data dataValidade) {
		DataValidade = dataValidade;
	}
	public String getLote() {
		return Lote;
	}
	public void setLote(String lote) {
		Lote = lote;
	}
	public String getTipoProduto() {
		return TipoProduto;
	}
	public void setTipoProduto(String tipoProduto) {
		TipoProduto = tipoProduto;
	}

}

