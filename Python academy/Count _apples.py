class Apple:
    count = 0
    total_weight = 0

    def __init__(self, weight):
        self.weight = weight
        Apple.count += 1
        Apple.total_weight += weight


apples = []

for i in range(1000):

    if Apple.count > 300:
        break

    apples.append(Apple(random.uniform(0.2, 0.5)))