package br.com.RestauranteMaven.domain;

public class Estoque {
	public String NomeProduto;
	public String TipoEstoque;
	public Produto produto;
	public String getNomeProduto() {
		return NomeProduto;
	}
	public void setNomeProduto(String nomeProduto) {
		NomeProduto = nomeProduto;
	}
	public String getTipoEstoque() {
		return TipoEstoque;
	}
	public void setTipoEstoque(String tipoEstoque) {
		TipoEstoque = tipoEstoque;
	}
	public Produto getProduto() {
		return produto;
	}
	public void setProduto(Produto produto) {
		this.produto = produto;
	}
}
