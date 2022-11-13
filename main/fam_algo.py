pmem = {
    "name" : "Aditya",
    "age" : 22,
    "gender" : 'M',
    "mid_name" : "Anil",
    "epic" : "1234"
}

pmem1 = {
    "name" : "Anil",
    "age" : 48,
    "gender" : 'M',
    "mid_name" : "Lilaram",
    "epic" : "1234"
}

pmem2 = {
    "name" : "Mansi",
    "age" : 45,
    "gender" : 'F',
    "mid_name" : "Anil",
    "epic" : "1234"
}

pmem3 = {
    "name" : "Tanusha",
    "age" : 16,
    "gender" : 'F',
    "mid_name" : "Anil",
    "epic" : "1234"
} 

pers = [pmem, pmem1, pmem2, pmem3]

class Person(object):

    def __init__(self, mem_json):
        self.name = mem_json['name']
        self.age = mem_json['age']
        self.gender = mem_json['gender']
        self.mid_name = mem_json['mid_name']
        self.epic = mem_json['epic']

        self.mother = None
        self.sister = []
        self.father = None
        self.daughter = []
        self.brother = []
        self.son = []
        self.dist_rel = []
        self.fam = dict()
        
    def add_mem(self, mem):
        # if self.gender == 'M':
        if mem.gender == 'M':
            if mem.mid_name == self.mid_name:
                self.brother.append(mem)
                # mem.brother.append(mem)
            else:
                if self.mid_name == mem.name:
                    self.father = mem
                    # mem.son.append(self)

                else:
                    self.dist_rel.append(mem)
                    # mem.dist_rel.append(self)
        else:
            if self.mid_name == mem.mid_name:
                if(abs(self.age - mem.age) <= 12):
                    self.sister.append(mem)
                else:
                    self.mother = mem
            
            else:
                self.dist_rel.append(mem)

    def add_mem2(self, mem):
        try:
            if (self.father.father != None):
                if self.father.name == mem.son.name:
                    self.gfather = mem
        except AttributeError:
            return self

        try:
            if (self.father.mother != None):
                if self.father.mother.name == mem.name:
                    self.gmother = mem

        except AttributeError:
            return self

    def give_dict(self):

        # self.fam['parent'] = dict()
        # if self.father:
        #     print("here")
        #     self.fam['parent']['father'] = to_dict(self.father)
        #     # self.fam['parent']['rel'] = 'father'

        # if self.mother:
        #     self.fam['parent']['mother'] = to_dict(self.mother)
        #     # self.fam['parent']['rel'] = 'mother'

        self.fam = []

        if self.father:
            self.fam.append((self.father.name, 'parent'))
        
        if self.mother:
            self.fam.append((self.mother.name, 'parent'))
        
        if len(self.brother) != 0:
            for bro in self.brother:
                self.fam.append((bro.name, 'brother'))

        if len(self.sister) != 0:
            for sis in self.sister:
                self.fam.append((sis.name, 'sister'))

        if len(self.son) != 0:
            for s in self.son:
                self.fam.append((s.name, 'son'))

        if len(self.daughter) != 0:
            for d in self.daughter:
                self.fam.append((d.name, 'daughter'))

        return self.fam

    def to_dict(self):
        per_dict = dict()
        per_dict['name'] = self.name
        per_dict['age'] = self.age
        per_dict['gender'] = self.gender
        per_dict['epic'] = self.epic
        per_dict['mid_name'] = self.mid_name

        return per_dict    

        # if not 

def to_dict(mem: Person):
    per_dict = dict()
    per_dict['name'] = mem.name
    per_dict['age'] = mem.age
    per_dict['gender'] = mem.gender
    per_dict['epic'] = mem.epic
    per_dict['mid_name'] = mem.mid_name

    return per_dict
    # per_dict['father']
    
def main():
    tu = Person(pmem)

    for per in pers[1:]:
        tu.add_mem(Person(per))

    # print(tu.to_dict())
    # print(tu.father.to_dict())
    # print(tu.mother.to_dict())

    print(tu.give_dict())
if __name__ == '__main__':
    main()
