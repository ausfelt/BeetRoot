class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []

    def __repr__(self):
        return f"Id: {self.id}, Name: {self.name}, Company: {self.company}"

    @property
    def workers(self):
        return self._workers

    def add_worker(self, worker):
        if isinstance(worker, Worker):
            self._workers.append(worker)
        else:
            raise TypeError("You can only add an instance of the class Worker.")


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self.boss = boss

    def __repr__(self):
        return f"Id: {self.id}, Name: {self.name}, Company: {self.company}, Boss: {self.boss.name}"

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, boss):
        if isinstance(boss, Boss):
            self._boss = boss
        else:
            raise TypeError("Boss must be an instance of the class Boss.")


boss1 = Boss(112, "Joel", "Spotify")
worker1 = Worker(12345, "Billy", "Spotify", boss1)
boss1.add_worker(worker1)
print(boss1.workers)
print(worker1.boss)