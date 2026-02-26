package service;

import java.util.*;

import entity.*;
import utils.IO;
import repos.StockRepo;

public class StockService {
	private final StockRepo stockRepo = new StockRepo();
	public void createStock() {
		stockRepo.connect();

		List<StockEntity> allStocks = new ArrayList<>();

		while (true) {
			System.out.println("  CREATING A STOCK ");
			System.out.print("  Stock Name: ");
			String stockName = IO.readString();

			System.out.print("  Unit Price: ");
			int unitPrice = IO.readInt(false);

			System.out.print("  Quantity: ");
			int quantity = IO.readInt(false);


			StockEntity newStock = new StockEntity(stockName, unitPrice, quantity);
			allStocks.add(newStock);

			System.out.println("  Would you like to add another stock?[y/n]: ");
			String choice = IO.readString();

			if (choice.isBlank() || choice.toLowerCase().contains("n")){
				break;
			}
		}


		for (StockEntity stock : allStocks) {
			stockRepo.addStock(stock);
		}
	}

	public void listAllStocks() {
		stockRepo.connect();
		System.out.println("  retrieving all stocks from db...\n");
		List<StockEntity> allStocks = stockRepo.getAll();

		int counter = 1;
		for (StockEntity stock: allStocks) {
			System.out.printf(
				"  %d. Name: %s  Price: %d Qty: %d\n",
				counter, stock.name, stock.price, stock.quantity
			);

			counter+=1;
		}

	}

}
