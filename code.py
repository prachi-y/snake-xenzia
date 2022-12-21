import time
import random
import os
import numpy as np
import msvcrt
import mysql.connector
import matplotlib.pyplot as pl

def turnR(base,sr,sc,x,y):
    os.system('cls')
    base[sr,sc+y]='_'
    if sr-x>=0 and sr-x<=34 and base[sr-x,sc]!='@':
        base[sr-x,sc]=' '
    if sr+x>=0 and sr+x<=34 and base[sr+x,sc]!='@':    
        base[sr+x,sc]=' '
    print(base)
        
def moveR(base,sr,sc,x):
    os.system('cls')
    base[sr,sc+1]='_'
    if sc-x>=0 and sc-x<=17 and base[sr,sc-x]!='@':
        base[sr,sc-x]=' '
    print(base)
    
def turnL(base,sr,sc,x,y):
    os.system('cls')
    base[sr,sc-y]='_'
    if sr-x>=0 and sr-x<=34 and base[sr-x,sc]!='@':
        base[sr-x,sc]=' '
    if sr+x>=0 and sr+x<=34 and base[sr+x,sc]!='@':
        base[sr+x,sc]=' '
    print(base)

def moveL(base,sr,sc,x):
    os.system('cls')
    base[sr,sc-1]='_'
    if sc+x>=0 and sc+x<=17 and base[sr,sc+x]!='@':
        base[sr,sc+x]=' '
    print(base)
   
def turnU(base,sr,sc,x,y):
    os.system('cls')
    base[sr-y,sc]='|'
    if sc-x>=0 and sc-x<=17 and base[sr,sc-x]!='@':
        base[sr,sc-x]=' '
    if sc+x>=0 and sc+x<=17 and base[sr,sc+x]!='@':
        base[sr,sc+x]=' '
    print(base)
    
def moveU(base,sr,sc,x):
    os.system('cls')
    base[sr-1,sc]='|'
    if sr+x>=0 and sr+x<=34 and base[sr+x,sc]!='@':
        base[sr+x,sc]=' '
    print(base)
    
def turnD(base,sr,sc,x,y):
    os.system('cls')
    base[sr+y,sc]='|'
    if sc-x>=0 and sc-x<=17 and base[sr,sc-x]!='@':
        base[sr,sc-x]=' '
    if sc+x>=0 and sc+x<=17 and base[sr,sc+x]!='@':
        base[sr,sc+x]=' '
    print(base)
    
def moveD(base,sr,sc,x):
    os.system('cls')
    base[sr+1,sc]='|'
    if sr-x>=0 and sr-x<=34 and base[sr-x,sc]!='@':
        base[sr-x,sc]=' '
    print(base)
    
db=mysql.connector.connect(host='localhost', user='root', passwd='tiger', database='project')
cursor=db.cursor()

while True:
    end=False
    while True:
        os.system('cls')
        print('\t\t\t\t\t\tSNAKE XENZIA','\t\t\t\t\t\t^^^^^^^^^^^^',sep='\n')
        print('\t\t\t\t\t\t\tBy Prachi Yadav','\t\t\t\t\t\t\t^^^^^^^^^^^^^^^',sep='\n')
        print("1. Play","2. Top 5 Scores","3. User's Performance","4. Quit\n",sep="\n")
        choice1=input('Enter your choice(1 or 2 or 3 or 4):')
        
        if choice1=='1':  
            break
                
        elif choice1=='2':
            qry="SELECT * FROM records ORDER BY score DESC"
            cursor.execute(qry)
            data=cursor.fetchall()
            
            print('','Username\tScore\t   Date\t\t   Time','-'*49,sep='\n')
            for i in data[:5]:
                print(i[0].upper(),'\t\t',i[1],'\t',i[2],'\t',i[3])
            
            input('\nPress Enter to continue...')
        
        elif choice1=='3':
            while True:
                os.system('cls')
                print('\t\t\t\t\t\tSNAKE XENZIA','\t\t\t\t\t\t^^^^^^^^^^^^',sep='\n')
                print('\t\t\t\t\t\t\tBy Prachi Yadav','\t\t\t\t\t\t\t^^^^^^^^^^^^^^^',sep='\n')
                print("1.Today's Performance(Last 10 games)","2. Daily High Score(Last 10 active days)","3. Back\n",sep='\n')
                choice2=input('Enter your choice(1 or 2 or 3):')
                
                if choice2=='3':
                    break
                
                elif choice2 not in ['1','2']:
                    print('Invalid choice')
                    input('\nPress Enter to continue...')

                else:
                    name=input('Enter username:')                    
                    qry="SELECT COUNT(*) FROM records WHERE Username='%s'"%(name)
                    cursor.execute(qry)
                    count=cursor.fetchone()
                        
                    if count[0]==0:
                        print('User not found')
                        input('\nPress Enter to continue...')
                        
                    else:
                        if choice2=='1':
                            qry="SELECT Score,Time FROM records WHERE Username='%s' AND Date=CURDATE() ORDER BY Time"%(name)
                            cursor.execute(qry)                               
                            data=cursor.fetchall()
                            xaxis=[]
                            yaxis=[]
                            
                            for i in data:
                                xaxis+=[str(i[1])]
                                yaxis+=[i[0]]
                                
                            pl.xlabel('Time')
                            pl.ylabel('Score')
                            pl.title("TODAY's PERFORMANCE")
                            pl.bar(xaxis[-10:],yaxis[-10:])    
                                              
                        else:
                            qry="SELECT MAX(Score),Date FROM records WHERE Username='%s' GROUP BY Date ORDER BY Date"%(name)
                            cursor.execute(qry)                              
                            data=cursor.fetchall()
                            xaxis=[]
                            yaxis=[]
                            
                            for i in data:
                                xaxis+=[str(i[1])]
                                yaxis+=[i[0]]
                                
                            pl.xlabel('Date')
                            pl.ylabel('Score')
                            pl.title("DAILY HIGH SCORE")
                            pl.bar(xaxis[-10:],yaxis[-10:])
                        
                        manager = pl.get_current_fig_manager()
                        manager.window.showMaximized()
                        pl.show()
                        input('\nPress Enter to continue...')
            
        elif choice1=='4':
            end=True
            break
        
        else:
            print('Invalid choice')
            input('\nPress Enter to continue...')
    
    if end:
        db.close()
        break  
        
    os.system('cls')
    
    while True:
        print('One word username. No spaces, digits or special characters.')
        name=input('Enter username:')
        if name.isalpha():
            os.system('cls')
            break
        else:
            print('Invalid entry')
            input('\nPress Enter to continue...')
            os.system('cls')
        
    print('\t\t\t\t\t\tSNAKE XENZIA','\t\t\t\t\t\t^^^^^^^^^^^^',sep='\n')
    print('\t\t\t\t\t\t\tBy Prachi Yadav','\t\t\t\t\t\t\t^^^^^^^^^^^^^^^',sep='\n')
    print('INSTRUCTIONS:-','~~~~~~~~~~~~','','8-->Up','2-->Down','6-->Right','4-->Left','','',sep='\n')
    print('RULES','~~~~~',sep='\n')
    print('1. If the snake hits the boundary you would lose.')
    print('2. Don\'t turn the snake until it becomes straight.','','',sep='\n')
    input('Press Enter to Start!!')
    os.system('cls')
    
    length=3
    frow=random.randint(5,34)
    fcol=random.randint(3,17)
    base=np.full([35,18],' ')
    base[frow,fcol]='@'
    base[0,0]=base[0,1]=base[0,2]='_'
    print(base)
    tr,tc=0,2
    row,col=tr,tc
    score=0
    flag='r'
    x=length-1
    y=1
    
    try:
        while True:
            if score<3:
                tym=0.6
            elif score<6:
                tym=0.45
            else:
                tym=0.3
                
            if row==frow and col==fcol:
                score+=1
                length+=1
                x+=1
                
                if score==10:
                    os.system('cls')
                    print('Your score is 10','You won :)',sep='\n')
                    input('\nPress Enter to continue...')
                    break
                
                while True:
                    frow=random.randint(0,34)
                    fcol=random.randint(0,17)
                    if base[frow,fcol] not in ['_','|']:
                        base[frow,fcol]='@'
                        break
            
            if row<0 or col<0:
                os.system('cls')
                print('OUT!!!')
                print('Your score is',score)
                input('\nPress Enter to continue...')
                break
                        
            time.sleep(tym)
            press=msvcrt.kbhit()

            if press:
                
                if tr==row and tc==col:
                                
                    key=ord(msvcrt.getch())
                    
                    if key==54:     #right (6)
                        if flag!='r':
                            turnR(base,row,col,x,y)
                            col+=1
                            flag='r'
                        
                    elif key==52:   #left (4) 
                        if flag!='l':
                            turnL(base,row,col,x,y)
                            col-=1
                            flag='l'
                    
                    elif key==56:   #up (8)
                        if flag!='u':
                            turnU(base,row,col,x,y)
                            row-=1
                            flag='u'
                                    
                    elif key==50:  #down (2) 
                        if flag!='d':
                            turnD(base,row,col,x,y)
                            row+=1
                            flag='d'

                    extra=msvcrt.getch()
                    
                else:
                    for i in range(2):                        
                        extra=msvcrt.getch()
                    
                                
            else:
                if flag=='r':
                    if base[row,tc]=='|':
                        x-=1
                        y+=1
                        turnR(base,row,tc,x,y)
                        
                        if base[row,tc]!='|':
                            x=length-1
                            y=1
                            tr=row
                            tc=col+1
                        
                    else:
                        x=length-1
                        y=1
                        tr,tc=row,col                        
                        moveR(base,tr,tc,x)
                        tc+=1

                    col+=1
                    
                elif flag=='l':
                    if base[row,tc]=='|':
                        x-=1
                        y+=1
                        turnL(base,row,tc,x,y)                        
                        
                        if base[row,tc]!='|':
                            x=length-1
                            y=1
                            tr=row
                            tc=col-1
                        
                    else:
                        x=length-1
                        y=1
                        tr,tc=row,col                        
                        moveL(base,tr,tc,x)
                        tc-=1

                    col-=1
                        
                elif flag=='u':
                    if base[tr,col]=='_':
                        x-=1
                        y+=1
                        turnU(base,tr,col,x,y)
                        
                        if base[tr,col]!='_':
                            x=length-1
                            y=1
                            tc=col
                            tr=row-1
                        
                    else:
                        x=length-1
                        y=1
                        tr,tc=row,col                        
                        moveU(base,tr,tc,x)
                        tr-=1

                    row-=1
                
                elif flag=='d':
                    if base[tr,col]=='_':
                        x-=1
                        y+=1
                        turnD(base,tr,col,x,y)
                        
                        if base[tr,col]!='_':
                            x=length-1
                            y=1
                            tc=col
                            tr=row+1                            
                        
                    else:
                        x=length-1
                        y=1
                        tr,tc=row,col
                        moveD(base,tr,tc,x)
                        tr+=1

                    row+=1
    
    except:
        os.system('cls')
        print('OUT!!!')
        print('Your score is',score)
        input('\nPress Enter to continue...')
        
    qry="insert into records values('%s',%s,CURDATE(),CURRENT_TIME())"%(name,score)
    cursor.execute(qry)
    db.commit()

