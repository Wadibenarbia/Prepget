import sqlite3

conn = sqlite3.connect('Prepget.db')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS Paquets(ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, Nom TEXT NOT NULL, Logiciel TEXT NOT NULL, Version TEXT NOT NULL, Path TEXT NOT NULL)')
c.execute('CREATE TABLE IF NOT EXISTS User(ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, Login TEXT NOT NULL, Password TEXT NOT NULL, Email TEXT NOT NULL)')
c.execute("INSERT INTO Paquets VALUES(NULL, 'python2.7', 'Python' , '2.7', '/Python/Python-2.7.tgz')")
c.execute("INSERT INTO Paquets VALUES(NULL, 'python2.72', 'Python' , '2.72', '/Python/Python-2.72.tgz')")
c.execute("INSERT INTO Paquets VALUES(NULL, 'oppenssl1.0.2', 'openssl' , '1.0.2', '/openssl-1.0.2n.tar.gz')")
c.execute("INSERT INTO Paquets VALUES(NULL, 'Php7', 'php' , '7.2.2', 'php-7.2.2.tar.gz')")
c.execute("INSERT INTO Paquets VALUES(NULL, 'openvpn2.4.4', 'openvpn' , '2.4.4', '/openvpn-2.4.4.tar.gz')")
c.execute("INSERT INTO Paquets VALUES(NULL, 'Php5.6.33', 'php' , '5.6.33', '/php-5.6.33.tar.gz')")
conn.commit()
c.close()
conn.close()

