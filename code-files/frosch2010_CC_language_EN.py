class cc_language:

    cc_wrong_arguments = "[USER_ID] you must have forgotten the arguments?"
    cc_wrong_game_command = "[USER_ID] you must have mistyped?"
    cc_shutdown_bot = "Shut down bot..."



    cc_game_already_running = "[USER_ID] there is already a game running. Please wait until this one is over."
    cc_cards_per_player_set_to = "Each player gets [COUNTER] cards."
    cc_no_game_running = "[USER_ID] currently no game running!"
    cc_user_already_joined = "[USER_ID] you have already joined the game! Wait until it starts..."
    cc_user_joined_game = "[USER_ID] you have joined the game. [[PLAYER_JOINED_COUNT] player]"
    cc_more_players_needed = "[USER_ID] more players are needed for a start! At least [MIN_PLAYER_COUNT] players are needed for a start."
    cc_user_started_game = "[USER_NAME] has started a new game..."
    cc_user_not_part = "[USER_ID] you are not a player in the current round! Wait until this round is finished and then join a new round."
    cc_player_won = "#########################\n\n🏆 **[USER_NAME]** has won the game. 🏆"

    cc_user_leave_no_part = "[USER_ID] you are not a player in the current round!"
    cc_game_end_because_user_left = "The game was ended prematurely because [USER_NAME] left the game and now there are not enough players."
    cc_user_left = "[USER_NAME] has left the game."
    cc_user_cant_leave_his_turn = "[USER_ID] you can't leave the game right now! Place another card first. After that you can leave the game."

    cc_user_no_turn = "[USER_ID] please wait your turn."
    cc_card_not_exist = "[USER_ID] this card does not exist! Choose another one."
    cc_user_cant_lay_card = "[USER_ID] you can't lay this card! Choose another one."
    cc_user_your_turn = "[USER_ID] is now on the move."

    cc_wish_without_color = "[USER_ID] you forgot the color."
    cc_wish_unknown_color = "[USER_ID] the desired color does not exist."

    cc_input_only_numbers = "[USER_ID] you must use a card number and no letters or special characters!"
    cc_input_no_number_arg = "[USER_ID] please provide a card number."

    cc_game_stopped_by = "The game was terminated prematurely by [USER_NAME]!"
    cc_game_cant_stopped = "[USER_ID] you can't finish the game because you're not playing."
    cc_game_player_has_cc = "\n**[PLAYER_NAME]** has only one card left! **#CC**"
    cc_game_player_can_lay = " it's your turn to lay.\nLay one of your cards with '!card X'."
    cc_game_player_cant_lay = " it's your turn and you can't lay.\nPick up a new card with '!getnewcard'."



    cc_please_choose_wish_color_react = "[USER_ID] please select a color via the Reactions."
    cc_please_choose_card_color_react = "[USER_ID] please select a color via the Reactions. After that you will be able to choose one of the cards of that color from your hand."
    cc_please_choose_card_num_react = "[USER_ID] please select a card via the Reactions. Back to the color selection? Use the X"

    cc_false_choose_color_react = "[USER_ID] this color does not exist!"
    cc_false_choose_number_react = "[USER_ID] you have no card of this color with this number!"

    cc_no_kick_user = "[USER_ID] the player was not found."
    cc_kick_user_isnt_player = "[USER_ID] the user does not play at all."
    cc_cant_kick_current_player = "[USER_ID] the player cannot be removed right now because he has to explain terms. Try again when he doesn't have to explain any more terms."
    cc_user_kicked = "The player was successfully removed from the game."

    cc_suspend_player_cant_lay_direct_chat = " you'll have to sit this round out, unfortunately, since you can't counter. Wait a moment. We'll continue in a moment..."
    cc_suspend_player_cant_lay = "You'll have to sit this round out, unfortunately, since you can't counter. Wait a moment. We'll continue in a moment..."
    cc_suspend_player_false_card = "[USER_ID] you have laid the wrong card. Play a sitout card to counter or sit out with '!sitout'!"
    cc_suspend_player_must_counter = " Play a sitout card to counter or sit out with '!sitout'!"

    cc_suspend_player_counter_cant_get_new_cards = "[USER_ID] you can't pick up cards! Play a sitout card to counter or sit out with '!sitout'."
    cc_suspend_player_cant_get_new_cards = "[USER_ID] you can't pick up cards! Wait a moment. We'll be right back..."

    cc_suspend_player_want_sit_out = "[USER_ID] you are now sitting out."
    cc_suspend_player_cant_sit_out = "[USER_ID] you can't sit out!"
    cc_suspend_player_cant_skip = "[USER_ID] you're already sitting out! Wait a moment until it continues..."

    cc_plus_card_player_can_lay = " counter the plus card by also laying one, or take the [PLUS_AMOUNT] cards with '!take'."
    cc_plus_card_player_cant_lay = " you can't counter and pick up the [PLUS_AMOUNT] cards. Wait a moment. We'll continue in a moment..."
    cc_plus_card_player_lay_false_card = "[USER_ID] counter the plus card by also laying one, or take the [PLUS_AMOUNT] cards with '!take'."
    cc_plus_card_player_cant_lay_false_card = "[USER_ID] you can't counter and pick up the [PLUS_AMOUNT] cards. Wait a moment. We'll continue in a moment..."

    cc_plus_card_player_cant_take = "[USER_ID] there are no plus cards you can take!"
    cc_plus_card_player_take = "[USER_ID] you have recorded the plus cards."
    cc_plus_card_player_cant_skip = "[USER_ID] you have already automatically recorded the plus cards. Wait a moment until it goes further..."

    cc_plus_card_player_cant_get_new_cards = "[USER_ID] you cannot pick up any cards! Counter the plus card by laying one as well, or pick up the [PLUS_AMOUNT] cards with '!take'."
    cc_plus_card_player_counter_cant_get_new_cards = "[USER_ID] you cannot pick up any cards! Wait a moment. We'll be right back..."



    #Generate card-str
    cc_timer_action_sit_out = " had to sit out."
    cc_timer_action_take_plus_cards = " has picked up the cards."
    cc_your_cards = "Your cards"
    cc_current_mid_card = "Current deck of cards"
    cc_player_sequence = "Round sequence"
    cc_players_turn = " is now on the move."
    cc_player_laid_card = "put this card"
    cc_player_picked_up_card = "has picked up a card"



    #Voice
    cc_voice_players_turn = "[USER_NAME] is now on the move."
    cc_voice_player_won = "[USER_NAME] has won the game!"
    cc_voice_player_sit_out = "[USER_NAME] must sit out this round."