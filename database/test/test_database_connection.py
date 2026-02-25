from pytest import mark
# from lib.database_connection import connect_to_db
import lib.database_connection as database


@mark.it("Database is initilaised with seed")
def test_database_connection_initialisation():
    test_seed_path = "seeds/test_seed.sql"
    conn = database.connect()
    database.seed(conn, test_seed_path)

    actual_result = None
    with conn.cursor() as cursor:
        response = cursor.execute("select * from test_shows")
        actual_result = response.fetchall()


    expected_result = [
            {'id': 1, 'name':'Invincible', 'rating':9},
            {'id': 2, 'name':'Demolition', 'rating':10},
            {'id': 3, 'name':'Better Call Saul', 'rating':10},
    ]

    assert actual_result == expected_result
        


    
