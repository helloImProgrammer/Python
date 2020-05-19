def black_board(board):
    print('   |   |     ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' ')
    print('-----------')
    print('   |   |     ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' ')
    print('-----------')
    print('   |   |     ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' ')

#--------------------------------------------------------------------------------------------
def input_user():
    user=' '
    
    while not (user == 'X' or user == 'O') :
        
        user = input('Lütfen bir değer girin : ').upper()
        
        if user == 'X':
            
            return ('X','O')
        
        else:
            
            return ('O','X')
#--------------------------------------------------------------------------------------------
def mark_position(user,position,board):
    
    board[position]=user
#--------------------------------------------------------------------------------------------
def winning_check(board,mark):
    
    
    return((board[1]==mark and board[2]==mark and board[3]==mark) or       #HORIZONTAL
    (board[4]==mark and board[5]==mark and board[6]==mark) or               #HORIZONTAL
    (board[7]==mark and board[8]==mark and board[9]==mark) or                #HORIZONTAL
    (board[1]==mark and board[4]==mark and board[7]==mark) or                 #VERTICAL
    (board[2]==mark and board[5]==mark and board[8]==mark) or                  #VERTICAL
    (board[3]==mark and board[6]==mark and board[9]==mark) or                   #VERTICAL
    (board[1]==mark and board[5]==mark and board[9]==mark) or                    #CROSS
    (board[3]==mark and board[5]==mark and board[7]==mark))                       #CROSS
#--------------------------------------------------------------------------------------------

from random import randint

def first_user():
    
    user1=randint(0,10)
    
    user2=randint(0,10)
    
    if user1> user2:
        
        return 'USER 1'
    
    else:
        
        return 'USER 2'
#--------------------------------------------------------------------------------------------
def space_control(board,position):
    
    return board[position] == ' '
#--------------------------------------------------------------------------------------------
def full_control(board):
    
    for i in range(1,10):
        
        if space_control (board,i):
           
            return False
    
    return True
#--------------------------------------------------------------------------------------------
def board_marking(board):
    
    position=0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_control(board,position):
        
        position=int(input('Lütfen (1-9) sayı aralığında bir işaretleme yapın : '))
    
    return position
#--------------------------------------------------------------------------------------------

def retry():
    
    retry1=int(input('Eğer oynamaya devam etmek stiyorsanız (1) çıkış yapmak istiyorsanız (0) basın : '))
    
    if retry1==1:
        
        return True
    
    else :
        
        return False 
#--------------------------------------------------------------------------------------------


###################################################################### GAMEEEEEEEEEEEEEEEEE -- -------  - - -- - - - -

on_game=True

while True :

    board1=[' ']*10

    user1_marker , user2_marker=input_user()

    return1=first_user()

    print(return1,'İlk başlıyor !!!!!')

    start=int(input('Hazır iseniz (1) e basın : '))

    if start==1 :
        
        on_game=True
    
    else:
        
        on_game=False

    while on_game==True:
        
        if return1== 'USER 1':
            
            black_board(board1)

            position=board_marking(board1)

            mark_position(user1_marker,position,board1)

            if winning_check(board1,user1_marker ):
                
                black_board(board1)
                
                print('USER 1 kazandı :):)):))):)))):))))')
                
                on_game=False
            
            else:
                
                if full_control(board1):
                    
                    black_board(board1)
                    
                    print('Oyun berabere bitti !!!!!')

                    on_game=False
                
                else:
                    
                    return1= 'USER 2'


        if return1== 'USER 2':
            
            black_board(board1)

            position=board_marking(board1)

            mark_position(user2_marker,position,board1)

            if winning_check(board1,user2_marker ):
                
                black_board(board1)
                
                print('USER 2 kazandı :):)):))):)))):))))')
                
                on_game=False
            else:
                
                if full_control(board1):
                    
                    black_board(board1)
                    
                    print('Oyun berabere bitti !!!!!')

                    on_game=False
                
                else:
                    
                    return1= 'USER 1'

    if not retry():
        
        break