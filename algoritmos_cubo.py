class Cube:
    def __init__(self, string: str) -> None:
        self.string = string

    def filter_algorithm(self) -> tuple:
        """Create a list based on a string by taking the apostrophe"""
        list1 = self.string.replace("´", "").split(" ")
        """Create a list based on a string without stripping the apostrophe"""
        list2 = self.string.split(" ")
        return list1, list2

    def invert_alg(self) -> str:
        """Create a string from a list"""
        list3 = self.list4[::-1]
        return " ".join(list3)

    def put_line(self) -> list:
        list4 = []
        for elem in range(len(self.list2)):
            if "´" in self.list2[elem]:
                list4.append(self.list1[elem])
            else:
                string3 = self.list1[elem] + "´"
                list4.append(string3)
        return list4
    
    def user_interaction(self) -> None:
        print("Returns a resolution of the Rubik's Cube given rolls")
        x = input("Enter the algorithms: ")
        cube1 = Cube(x)
        lists = cube1.filter_algorithm()
        print(lists)
        list2 = cube1.put_line()
        print(list2)
        string = cube1.invert_alg()
        print(string)