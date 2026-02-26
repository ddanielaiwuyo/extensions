package repos;

import java.util.*;
import java.sql.*;
import entity.*;

public class StockRepo {

	private static Connection db_conn;

	public void connect() {
		String connUrl = "jdbc:postgresql://localhost:5432/extension_db";
		String user = "postgres";
		String password = "password";
		try {
			Connection conn = DriverManager.getConnection(connUrl, user, password);
			System.out.printf(" connecting to  database with version: %d\n", conn.getMetaData().getDatabaseMajorVersion());

			db_conn = conn;

			System.out.println(conn.getMetaData().getDatabaseMajorVersion());
		} catch (Exception err) {
			System.out.println(" could not connnect to database");
			System.out.println(err);
		}
	}

	public List<StockEntity> getAllOrders() throws Exception {

		List<StockEntity> all_stocks = new ArrayList<>();

		if (db_conn == null){
			System.out.println(" db connection is null!!");
		}
		try {
			Statement st = db_conn.createStatement();
			ResultSet rs = st.executeQuery("select * from stock_items;");

			while (rs.next()) {
				String name = rs.getString("name");
				int price = rs.getInt("price");
				int quantity = rs.getInt("quantity");
				StockEntity new_stock = new StockEntity(name, price, quantity);
				all_stocks.add(new_stock);
			}

		} catch (SQLException err) {
			System.err.println(" sql_exception occured, %s\n");
			err.printStackTrace();

		} catch (Exception err) {
			throw new Exception(err);
		}

		return all_stocks;
	}

	public void addStock(StockEntity stock) {
		System.out.println(" adding to stock");
		try {
			String query = "insert into stock_items (name, price, quantity) values (?, ?, ?)";
			PreparedStatement st = db_conn.prepareStatement(query);
			st.setString(1, stock.name);
			st.setInt(2, stock.price);
			st.setInt(3, stock.quantity);

			st.executeUpdate();
			System.out.println(" successfully added to database");
		} catch(SQLException err) {
			err.printStackTrace();
		}
	}

	public List<StockEntity> getAll(){
		String query = "select * from stock_items;";
		List<StockEntity> parsedStocks = new ArrayList<>();
		try {
			Statement st = db_conn.createStatement();
			ResultSet rs = st.executeQuery(query);

			while(rs.next()){
				String stockName = rs.getString("name");
				int price = rs.getInt("price");
				int quantity = rs.getInt("quantity");

				StockEntity newStock = new StockEntity(stockName, price, quantity);
				parsedStocks.add(newStock);
			}

		} catch(SQLException err) {
			System.err.println(" sql error in getting all stocks");
			err.printStackTrace();
		}
	
		return parsedStocks;
	}

}
