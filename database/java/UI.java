import java.util.*;

import utils.IO;

public class UI {
	static String welcome_msg = "Welcome to the shop program";
	private String[] iterable;

	public UI(String[] iterable) {
		this.iterable = iterable;
	}

	public int getUserChoice() throws Exception {
		if (this.iterable.length < 1) {
			throw new Exception("  Main this.iterable must have at least one item!");
		}

		for (int i = 0; i < this.iterable.length; i++) {
			System.out.printf("  %d.   %s\n", i + 1, this.iterable[i]);
		}

		int maxChoice = this.iterable.length - 1;
		while (true) {
			try {

				System.out.print("  Please select a number: ");
				int userInput = IO.readInt(false);
				userInput = userInput - 1;

				if (userInput < 0 || userInput > maxChoice) {
					System.out.printf("  Please provide a number between 1 and %d\n", this.iterable.length);
					continue;
				}

				return userInput;
			} catch (InputMismatchException e) {
				System.out.println("  Please enter a valid number");
				continue;

			}
		}

	}

}
