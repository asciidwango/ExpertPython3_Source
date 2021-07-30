class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    def __repr__(self):
        return "と".join(self.toppings) + "がトッピングされたピザ"

    @classmethod
    def recommend(cls):
        """さまざまなトッピングが入ったおすすめのピザ"""
        return cls(['スパム', 'ハム', '卵'])


class VikingPizza(Pizza):
    @classmethod
    def recommend(cls):
        """基本のおすすめトッピングにスパムを追加"""
        recommended = super(VikingPizza, cls).recommend()
        recommended.toppings += ['スパム'] * 5
        return recommended


if __name__ == "__main__":
    print("一般的なピザのおすすめ:", Pizza.recommend())
    print("海賊ピザのおすすめ:", VikingPizza.recommend())
