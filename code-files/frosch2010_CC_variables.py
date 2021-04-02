class cc_variables:

    cc_carddeck_template = ["r:1","r:1","r:2","r:2","r:3","r:3","r:4","r:4","r:5","r:5","r:6","r:6","r:7","r:7","r:8","r:8","r:9","r:9", "r:🔄", "r:🔄", "r:🔂", "r:🚫", "r:🚫", "r:❌", "r:⏫", "r:⏫",
                      "g:1","g:1","g:2","g:2","g:3","g:3","g:4","g:4","g:5","g:5","g:6","g:6","g:7","g:7","g:8","g:8","g:9","g:9", "g:🔄", "g:🔄", "g:🔂", "g:🚫", "g:🚫", "g:❌", "g:⏫", "g:⏫",
                      "b:1","b:1","b:2","b:2","b:3","b:3","b:4","b:4","b:5","b:5","b:6","b:6","b:7","b:7","b:8","b:8","b:9","b:9", "b:🔄", "b:🔄", "b:🔂", "b:🚫", "b:🚫", "b:❌", "b:⏫", "b:⏫",
                      "y:1","y:1","y:2","y:2","y:3","y:3","y:4","y:4","y:5","y:5","y:6","y:6","y:7","y:7","y:8","y:8","y:9","y:9", "y:🔄", "y:🔄", "y:🔂", "y:🚫", "y:🚫", "y:❌", "y:⏫", "y:⏫",
                      "wi:🔳", "wi:🔳", "wi:🔳", "wi:🔳", "wi:❓", "wi:❓", "wi:👨‍👨‍👧‍👦", "wi:👨‍👨‍👧‍👦"]

    cc_current_carddeck = ["r:1","r:1","r:2","r:2","r:3","r:3","r:4","r:4","r:5","r:5","r:6","r:6","r:7","r:7","r:8","r:8","r:9","r:9", "r:🔄", "r:🔄", "r:🔂", "r:🚫", "r:🚫", "r:❌", "r:⏫", "r:⏫",
                      "g:1","g:1","g:2","g:2","g:3","g:3","g:4","g:4","g:5","g:5","g:6","g:6","g:7","g:7","g:8","g:8","g:9","g:9", "g:🔄", "g:🔄", "g:🔂", "g:🚫", "g:🚫", "g:❌", "g:⏫", "g:⏫",
                      "b:1","b:1","b:2","b:2","b:3","b:3","b:4","b:4","b:5","b:5","b:6","b:6","b:7","b:7","b:8","b:8","b:9","b:9", "b:🔄", "b:🔄", "b:🔂", "b:🚫", "b:🚫", "b:❌", "b:⏫", "b:⏫",
                      "y:1","y:1","y:2","y:2","y:3","y:3","y:4","y:4","y:5","y:5","y:6","y:6","y:7","y:7","y:8","y:8","y:9","y:9", "y:🔄", "y:🔄", "y:🔂", "y:🚫", "y:🚫", "y:❌", "y:⏫", "y:⏫",
                      "wi:🔳", "wi:🔳", "wi:🔳", "wi:🔳", "wi:❓", "wi:❓", "wi:👨‍👨‍👧‍👦", "wi:👨‍👨‍👧‍👦"]

    cc_red_card_template = "🟥🟥🟥|🟥  **NUM**  🟥    COUNT|🟥🟥🟥"
    cc_blue_card_template = "🟦🟦🟦|🟦  **NUM**  🟦    COUNT|🟦🟦🟦"
    cc_green_card_template = "🟩🟩🟩|🟩  **NUM**  🟩    COUNT|🟩🟩🟩"
    cc_yellow_card_template = "🟨🟨🟨|🟨  **NUM**  🟨    COUNT|🟨🟨🟨"
    cc_wish_card_template = "🔳🟥🔳|🟦  **NUM**  🟩    COUNT|🔳🟨🔳"


    cc_current_mid_card = ""

    cc_current_wish_color = ""

    cc_player_list = []
    cc_player_display_list = ""
    cc_player_hand = []
    cc_player_str_hand = []
    

    cc_current_player = 0


    cc_is_running = False
    cc_is_reversed = False


    cc_is_lay_card_reacting = False
    cc_next_react_is_number = False
    cc_player_lay_card_reacting = None
    cc_lay_card_react_message = None
    cc_lay_card_possible_colors = []
    cc_lay_card_possible_numbers = []
    cc_lay_card_react_choosed_color = ""


    cc_is_wish_reacting = False
    cc_player_wish_reacting = None
    cc_wish_react_message = None
    cc_wish_react_card_num = None


    cc_card_messages = []
    cc_player_card_str = []


    cc_rotate_player_hands = False

    cc_player_is_suspend = False
    cc_suspended_player_can_lay = False


    cc_plus_card_amount = 0
    cc_plus_player_can_lay = False
    cc_plus_print = False


    cc_wish_next_player_get_cards = False