def get_all_movements(board):
    all_movements = []
    for row in board:
        for col in row:
            all_movements.append(col)
    return all_movements

def assign_player_choices(player_choice, player1, player2, choices, player1_choice):
    for _choice in choices:
        if _choice == player1_choice:
            player_choice[player1] = _choice
        else:
            player_choice[player2] = _choice
    return player_choice

def print_game_board(board):
    vertical_separator = ' '
    # horizontal_separator = '-'
    # lines = 1
    for row in board:
        # if lines > 1 and lines <= len(board):
        #     print(horizontal_separator*(len(row)*2-1))
        # lines += 1
        columns = 1
        for cell in row:
            if columns > 1 and columns <= len(row):
                print(vertical_separator, end="")
            print(cell, end="")
            columns += 1
        print()

def get_user_input(message, acceptable_input, error_message=''):
    user_input = ''
    while True:
        user_input = input(message)
        if user_input in acceptable_input:
            break
        if error_message != '':
            print(error_message)
    return user_input

def get_index(movement, board):
    _row = 0
    _col = 0
    for row in board:
        for col in row:
            if col == movement:
                return _row, _col
            _col += 1
        _row += 1
        _col = 0
    return _row, _col

def make_move(row, col, player_char, board):
    board[row][col] = player_char
    return board

def check_victory(row, col, board):
    # check horizontal
    if len(set(board[row])) == 1:
        # return 'horizontal'
        return True

    # check vertical
    vertical = []
    for _row in board:
        vertical.append(_row[col])
    if len(set(vertical)) == 1:
        # return 'vertical'
        return True

    # check diagonal 1
    diagonal = []
    if row == col:
        diagonal.append(board[0][0])
        diagonal.append(board[1][1])
        diagonal.append(board[2][2])
    if len(set(diagonal)) == 1:
        # return 'diagonal 1'
        return True

    # check diagonal 2
    diagonal = []
    if (row == 0 and col == 2) or (row == 2 and col == 0):
        diagonal.append(board[0][2])
        diagonal.append(board[1][1])
        diagonal.append(board[2][0])
    if len(set(diagonal)) == 1:
        # return 'diagonal 2'
        return True

    return False

def start_game():
    game_board_help = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    _empty = '\u2591'
    game_board = [[_empty, _empty, _empty], [_empty, _empty, _empty], [_empty, _empty, _empty]]
    player1 = '1'
    player2 = '2'
    player_choice = {player1: '', player2: ''}
    choices = ['x', 'o']
    continue_playing = 'y'
    exit_playing = 'n'
    play_again_input = ''
    play_again_choices = [continue_playing, exit_playing]
    pending_movements = get_all_movements(game_board_help)
    current_player = player1
    print('Tic tac toe: use this for input positions:')
    print_game_board(game_board_help)
    player_choice_input = get_user_input("Player {} chose your character: {}: ".format(current_player, choices), choices, "Only allowed: {}".format(choices))
    player_choice = assign_player_choices(player_choice, player1, player2, choices, player_choice_input)

    while True:
        player_movement = get_user_input("Player {} chose your movement: {}: ".format(current_player, pending_movements), pending_movements, "Only allowed: {}".format(pending_movements))
        pending_movements.remove(player_movement)
        row, col = get_index(player_movement, game_board_help)
        game_board = make_move(row, col, player_choice[current_player], game_board)
        if check_victory(row, col, game_board):
            print_game_board(game_board)
            print('Player {} wins!'.format(current_player))
            play_again_input = get_user_input("Do you want to play again?: {}: ".format(play_again_choices), play_again_choices, "Only allowed: {}".format(play_again_choices))
            break
        if player1 == current_player:
            current_player = player2
        else:
            current_player = player1
        print_game_board(game_board)

    if play_again_input == continue_playing:
        start_game()
    else:
        print('Thanks for playing!')

start_game()