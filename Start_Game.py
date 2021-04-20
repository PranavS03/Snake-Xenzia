def main():
    def s():
        import Snake
    A=int(input("Enter 1 to open the snake game, 2 to view scores and 3 to exit: "))
    if A==1:
        print("snake game is opening")
        s()
        exit()
    elif A==2:
        import MySQLdb as a
        mycon=a.connect(host ="localhost" ,user ="root",passwd ="235489",database ="snakes")
        if mycon.is_connected ==False:
            print("error in connecting the database")
        cursor=mycon.cursor()
        cursor.execute("select  * from score")
        data=cursor.fetchall()
        count=cursor.rowcount
        print("Total number of rows retrieved: " , count)
        for row in data:
            print(row)
        main()

main()
