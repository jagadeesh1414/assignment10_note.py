def up_low(s):      
    u = sum(1 for i in s if i.isupper())
    l = sum(1 for i in s if i.islower())
    print( "No. of Upper case characters : %s", u) 
    print ("No. of Lower case characters : %s", l) 
 
up_low("The GITAM UniVersity Is in BanGalore ")