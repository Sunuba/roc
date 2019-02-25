from classes.Commands import IsVerifyOn, CheckAntibot, GoOutside, ClickSearchTargetButton, ClickWoodButton
from classes.Commands import ClickResetLevelButton, ClickSetLevelButton, ClickSearchWoodButton, ClickGatherButton
from classes.Commands import ClickNewTroopButtonForGathering, ClickMarch, IsQueueAvailable
from time import sleep

is_verify_on = IsVerifyOn()
check_antibot = CheckAntibot()
get_out = GoOutside()
click_search_target = ClickSearchTargetButton()
click_wood_button = ClickWoodButton()
reset_level = ClickResetLevelButton()
set_level = ClickSetLevelButton()
level = set_level.set_level(6)
search_button = ClickSearchWoodButton()
click_gather = ClickGatherButton()
click_new_troop_gather = ClickNewTroopButtonForGathering()
is_queue_available = IsQueueAvailable()
click_march = ClickMarch()

sleep(2)
# construct chain here
is_verify_on.set_successor(check_antibot)
check_antibot.set_successor(get_out)
get_out.set_successor(click_search_target)
click_search_target.set_successor(click_wood_button)
click_wood_button.set_successor(reset_level)
reset_level.set_successor(set_level)
set_level.set_successor(search_button)
search_button.set_successor(click_gather)
click_gather.set_successor(click_new_troop_gather)
click_new_troop_gather.set_successor(is_queue_available)
is_queue_available.set_successor(click_march)

is_verify_on.do_work()




