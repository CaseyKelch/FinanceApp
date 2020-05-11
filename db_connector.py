import mysql.connector
import keyring
import datetime


def database_query(ip, user, password, db, sql, val):
    fin_db = mysql.connector.connect(
        host=ip,
        user=user,
        passwd=password,
        database=db,
    )
    my_cursor = fin_db.cursor()
    sql_insert = sql
    insert_val = val
    my_cursor.execute(sql_insert, insert_val)
    fin_db.commit()
    return 0


if __name__ == "__main__":
    now_time = datetime.datetime.now()
    timestamp = now_time.strftime("%Y-%m-%d %H:%M:%S")
    workbench_pwd = keyring.get_password("mysql", "workbench")
    sql_query = "INSERT INTO financeapp (ticker, price, outstanding, teps, fep, bv, fpe, pbv, valuation, datetime) " \
        "VALUES (%s, %s, %s, %s, %s,%s,%s,%s,%s,%s)"
    values = ("AAPL", 1, 2, 3, 4, 5, 6, 7, 8, timestamp)

    database_query("192.168.1.7", "workbench", workbench_pwd, "fin", sql_query, values)





