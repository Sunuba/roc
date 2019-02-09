from classes.ImageCoordinate import ImageCoordinate


class Troops:
    @staticmethod
    def check():
        if ImageCoordinate.is_on_screen('images/troop_returns'):
            return 'home'
        else:
            return 'war'