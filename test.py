import pprint
import pyodbc


def login():
    # インスタンス
    instance = "sqlserver-2.ctaunxocvdmg.ap-northeast-1.rds.amazonaws.com,1433"

    # ユーザー
    user = "ユーザー"

    #パスワード
    pasword = "パスワード"

    #DB
    db = "TutorialDB"
    msg = "DRIVER={ODBC Driver 18 for SQL Server};SERVER=" + instance + ";uid=" + user + \
                 ";pwd=" + pasword + ";DATABASE=" + db + ";TrustServerCertificate=Yes"
    print(msg)
    connect = pyodbc.connect(msg)
    cursor = connect.cursor()
    cursor.execute( "SELECT * FROM dbo.Customers;" )
    rows = cursor.fetchall()
    pprint.pprint( rows )

    cursor.close()
    connect.close()

if __name__ == '__main__':login()
