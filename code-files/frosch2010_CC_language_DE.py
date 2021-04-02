class cc_language:

    cc_wrong_arguments = "[USER_ID] du hast wohl die Argumente vergessen?"
    cc_wrong_game_command = "[USER_ID] du hast dich wohl vertippt?"
    cc_shutdown_bot = "Der Bot fährt herunter..."



    cc_game_already_running = "[USER_ID] es läuft bereits ein Spiel. Bitte warte bis dieses zu Ende ist."
    cc_cards_per_player_set_to = "Jeder Spieler bekommt [COUNTER] Karten."
    cc_no_game_running = "[USER_ID] derzeit läuft kein Spiel!"
    cc_user_already_joined = "[USER_ID] du bist dem Spiel bereits beigetreten! Warte bis es los geht..."
    cc_user_joined_game = "[USER_ID] du bist dem Spiel beigetreten. [[PLAYER_JOINED_COUNT] Spieler]"
    cc_more_players_needed = "[USER_ID] es werden mehr Spieler für einen Start benötigt! Mindestens [MIN_PLAYER_COUNT] Spieler sind für einen Start nötig."
    cc_user_started_game = "[USER_NAME] hat ein neues Spiel gestartet..."
    cc_user_not_part = "[USER_ID] du bist kein Spieler in der aktuellen Runde! Warte bis diese Runde zu Ende gespielt ist und tritt dann einer neuen Runde bei."
    cc_player_won = "#########################\n\n🏆 **[USER_NAME]** hat das Spiel gewonnen. 🏆"

    cc_user_leave_no_part = "[USER_ID] du bist kein Spieler in der aktuellen Runde!"
    cc_game_end_because_user_left = "Das Spiel wurde vorzeitig beendet, weil [USER_NAME] das Spiel verlassen hat und nun nicht mehr genügend Spieler mitspielen."
    cc_user_left = "[USER_NAME] hat das Spiel verlassen."
    cc_user_cant_leave_his_turn = "[USER_ID] du kannst gerade das Spiel nicht verlassen! Lege erst noch eine Karte. Danach kannst du das Spiel verlassen."

    cc_user_no_turn = "[USER_ID] warte bitte bis du dran bist."
    cc_card_not_exist = "[USER_ID] diese Karte gibt es nicht! Wähle eine andere."
    cc_user_cant_lay_card = "[USER_ID] du kannst diese Karte nicht legen! Wähle eine andere aus."
    cc_user_your_turn = "[USER_ID] du bist dran."

    cc_wish_without_color = "[USER_ID] du hast die Farbe vergessen."
    cc_wish_unknown_color = "[USER_ID] die gewünschte Farbe gibt es nicht."

    cc_input_only_numbers = "[USER_ID] du musst eine Kartennummer verwenden und keine Buchstaben oder Sonderzeichen!"
    cc_input_no_number_arg = "[USER_ID] bitte gebe eine Kartennummer an."

    cc_game_stopped_by = "Das Spiel wurde vorzeitig von [USER_NAME] beendet!"
    cc_game_cant_stopped = "[USER_ID] du kannst das Spiel nicht beenden, weil du nicht mitspielst."
    cc_game_player_has_cc = "\n**[PLAYER_NAME]** hat nur noch eine Karte! **#CC**"
    cc_game_player_can_lay = " du bist dran und kannst legen.\nLege eine deiner Karten mit '!card X'"
    cc_game_player_cant_lay = " du bist dran und kannst nicht legen.\nNehme mit '!getnewcard' eine neue Karte auf."



    cc_please_choose_wish_color_react = "[USER_ID] bitte wähle über die Reactions eine Farbe aus."
    cc_please_choose_card_color_react = "[USER_ID] bitte wähle über die Reactions eine Farbe aus. Im Anschluss wirst du eine der Karte von der Farbe aus deiner Hand auswählen können."
    cc_please_choose_card_num_react = "[USER_ID] bitte wähle über die Reactions eine Karte aus. Zurück zur Farbwahl? Nutze das X"

    cc_false_choose_color_react = "[USER_ID] diese Farbe gibt es nicht!"
    cc_false_choose_number_react = "[USER_ID] du hast keine Karte dieser Farbe mit dieser Zahl!"

    cc_no_kick_user = "[USER_ID] der Spieler wurde nicht gefunden."
    cc_kick_user_isnt_player = "[USER_ID] der User spielt gar nicht mit."
    cc_cant_kick_current_player = "[USER_ID] der Spieler kann gerade nicht entfernt werden, weil er Begriffe erklären muss. Versuche es nochmal, wenn er keine Begriffe mehr erklären muss."
    cc_user_kicked = "Der Spieler wurde erfolgreich vom Spiel entfernt."

    cc_suspend_player_cant_lay_direct_chat = " du musst diese Runde leider aussetzen, da du nicht kontern kannst. Warte einen Moment. Gleich geht's weiter..."
    cc_suspend_player_cant_lay = "Du musst diese Runde leider aussetzen, da du nicht kontern kannst. Warte einen Moment. Gleich geht's weiter..."
    cc_suspend_player_false_card = "[USER_ID] du hast die falsche Karte gelegt. Lege eine Aussetzenkarte, um zu kontern oder setze mit '!sitout' aus!"
    cc_suspend_player_must_counter = " lege eine Aussetzenkarte, um zu kontern oder setze mit '!sitout' aus!"

    cc_suspend_player_counter_cant_get_new_cards = "[USER_ID] du kannst keine Karten aufnehmen! Lege eine Aussetzenkarte, um zu kontern oder setze mit '!sitout' aus."
    cc_suspend_player_cant_get_new_cards = "[USER_ID] du kannst keine Karten aufnehmen! Warte einen Moment. Gleich geht's weiter..."

    cc_suspend_player_want_sit_out = "[USER_ID] du setzt nun aus."
    cc_suspend_player_cant_sit_out = "[USER_ID] du kannst nicht aussetzen!"
    cc_suspend_player_cant_skip = "[USER_ID] du setzt bereits aus! Warte einen Moment, bis es weiter geht..."

    cc_plus_card_player_can_lay = " kontere die Plus-Karte, indem du ebenfalls eine legst oder nehme mit '!take' die [PLUS_AMOUNT] Karten auf."
    cc_plus_card_player_cant_lay = " du kannst nicht kontern und nimmst die [PLUS_AMOUNT] Karten auf. Warte einen Moment. Gleich geht's weiter..."
    cc_plus_card_player_lay_false_card = "[USER_ID] kontere die Plus-Karte, indem du ebenfalls eine legst oder nehme mit '!take' die [PLUS_AMOUNT] Karten auf."
    cc_plus_card_player_cant_lay_false_card = "[USER_ID] du kannst nicht kontern und nimmst die [PLUS_AMOUNT] Karten auf. Warte einen Moment. Gleich geht's weiter..."

    cc_plus_card_player_cant_take = "[USER_ID] es gibt keine Plus-Karten, die du nehmen kannst!"
    cc_plus_card_player_take = "[USER_ID] du hast die Plus-Karten aufgenommen."
    cc_plus_card_player_cant_skip = "[USER_ID] du hast die Plus-Karten bereits automatisch aufgenommen. Warte einen Moment, bis es weiter geht..."

    cc_plus_card_player_cant_get_new_cards = "[USER_ID] du kannst keine Karten aufnehmen! Kontere die Plus-Karte, indem du ebenfalls eine legst oder nehme mit '!take' die [PLUS_AMOUNT] Karten auf."
    cc_plus_card_player_counter_cant_get_new_cards = "[USER_ID] du kannst keine Karten aufnehmen! Warte einen Moment. Gleich geht's weiter..."



    #Generate card-str
    cc_timer_action_sit_out = " musste aussetzen."
    cc_timer_action_take_plus_cards = " hat die Karten aufgenommen."
    cc_your_cards = "Deine Karten"
    cc_current_mid_card = "Aktueller Kartenstapel"
    cc_player_sequence = "Rundenfolge"
    cc_players_turn = "ist an der Reihe"
    cc_player_laid_card = "legte diese Karte"
    cc_player_picked_up_card = "hat eine Karte aufgenommen"



    #Voice
    cc_voice_players_turn = "[USER_NAME] ist jetzt am Zug."
    cc_voice_player_won = "[USER_NAME] hat das Spiel gewonnen!"
    cc_voice_player_sit_out = "[USER_NAME] muss diese Runde aussetzen."