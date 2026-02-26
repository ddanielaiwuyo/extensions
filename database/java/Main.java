import utils.IO;

class Main {
	final static int LIST_ITEMS_CHOICE = 0;
	final static int CREATE_NEW_ITEM_CHOICE = 1;

	public static void main(String[] args) {
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
						sService.listAll();
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
				if (!choice.contains("y") || choice.contains("yes")) {
					System.out.println("  See you later");
					break;
				}
			}
		} catch (Exception e) {
			System.err.printf(" Unexpected error: %s", e);
		}
	}
}
