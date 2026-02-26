import utils.IO;
import service.StockService;

public class Main {

	public static void main(String[] args) {
		final int LIST_ITEMS_CHOICE = 0;
		final int CREATE_NEW_ITEM_CHOICE = 1;
		System.out.println("hello, world");
		String[] menu = {
				"List all shop items", "Create a new item",
				"List all orders", "Create new order", "Quit"
		};
		StockService sService = new StockService();

		try {
			while (true) {
				UI ui = new UI(menu);
				int userChoice = ui.getUserChoice();

				switch (userChoice) {

					case LIST_ITEMS_CHOICE:
						sService.listAllStocks();
						break;

					case CREATE_NEW_ITEM_CHOICE:
						sService.createStock();
						break;

					default:
						System.out.println("  Unidentified value passed");
						break;
				}

				System.out.print("  Go to main menu or quit?[y/n]: ");
				String choice = IO.readString();
				if (!choice.contains("y")) {
					System.out.println("  See you later");
					IO.close();
					return;
				}
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
