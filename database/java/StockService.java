import java.util.*;
import utils.IO;

public class StockService {
	List<Stock> allStocks = new ArrayList<>();

	private class Stock {
		String name;
		double price;
		int quantity;

		public Stock(String name, double price, int quantity) {
			this.name = name;
			this.price = price;
			this.quantity = quantity;
		}
	}

	private String[] stockItems = { "Maison Margiela", "Macbook Air", "Mercedes Pen" };

	public void listAll() {
		System.out.println("  DISPLAYING STOCK ITEMS ");
		for (int i = 0; i < stockItems.length; i++) {
			System.out.printf("  %d.   %s\n", i + 1, stockItems[i]);
		}
	}

	public void createStock() {
		while (true) {
			System.out.print(" stock name: ");
			String stockName = IO.readString();

			System.out.print(" unit price: ");
			double unitPrice = IO.readDouble(false);

			System.out.print("  quantity: ");
			int quantity = IO.readInt(false);

			System.out.printf("\n\n\n");
			Stock newStock = new Stock(stockName, unitPrice, quantity);
			allStocks.add(newStock);

			System.out.printf(
					"  stock_name: %s\n  unit_price: %f\n quantity: %d\n ",
					stockName, unitPrice, quantity);

			System.out.println("  stock added successfully");

			System.out.print("  Would you like to add another stock?[y/n] ");
			String userChoice = IO.readString();
			if (userChoice.toLowerCase().contains("no") || userChoice.toLowerCase().contains("n")) {
				break;
			}

		}
	}

}
