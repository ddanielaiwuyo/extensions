package entity;

public class StockEntity {
	public String name;
	public int price;
	public int quantity;

	public StockEntity(String name, int price, int quantity) {
		this.name = name;
		this.price = price;
		this.quantity = quantity;
	}
}
