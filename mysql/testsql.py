import mysqlhelper


if __name__ == "__main__":
    mysql_helper = mysqlhelper.MysqlHelper(host="localhost", db="log_5", user="root", passwd="123456", port=3306, pool_size=2, pool_name="mysql", commit_size=2)

    print 1, mysql_helper.select("show tables;")
