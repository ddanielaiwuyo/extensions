package utils;

import java.util.*;

/*
 * IO is used to read from stdin. All reading from stdin
 * should be done here, to centralise IO processess
 * and easy implementation
**/
public class IO {
	private static final Scanner stdin = new Scanner(System.in);

	public static int readInt(boolean allowNegative) {
		while (true) {
			try {
				int userInput = stdin.nextInt();
				if (userInput <= 0 && !allowNegative) {
					stdin.next();
					System.out.println(" Please provide a non zero postive value");
					System.out.print(" Enter: ");
				}
				return userInput;
			} catch (InputMismatchException err) {
				stdin.next();
				System.out.println("  Please provide a valid number");
			}
		}
	}

	public static String readString() {
		while (true) {
			try {
				String userInput = stdin.next();
				if (userInput.isBlank()) {
					stdin.next();
					System.out.println("  Input must not be empty");
					System.out.print(" Enter: ");
					continue;
				}
				return userInput;
			} catch (InputMismatchException err) {
				stdin.next();
				System.out.println("  Please provide a valid string");
			}
		}
	}

	public static double readDouble(boolean allowNegative) {
		while (true) {
			try {
				double userInput = stdin.nextDouble();
				if (userInput <= 0 && !allowNegative) {
					stdin.next();
					System.out.println(" Please provide a non zero postive value");
					System.out.print(" Enter: ");
					continue;
				}
				return userInput;
			} catch (InputMismatchException err) {
				stdin.next();
				System.out.println("  Please provid a valid string");
			}
		}

	}

}
