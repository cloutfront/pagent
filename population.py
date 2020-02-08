import agent

class Population:

    def __init__(self):
        self.population = []

    def get_population(self):
        return self.population

    def init_population(self, size, printing=False):
        self.population = []
        for i in range(size):
            x = agent.Agent()
            if printing:
                print(i, ": ", x.name, x.uid)
            self.population.append(x)

    def iterative_runout(self, key, val):
        inc = 0 
        res = []
        while self.howMany(key, val) > 0:
            for a in self.population:
                if a.props[key] == val:
                    a.recheck_prop(key)
            
            res.append([inc, self.howMany(key, val)])
            inc += 1
        return res

    def howMany(self, key, value):
        return len([1 for a in self.population if a.props[key] == value ])
