class Cube:
     def __init__(self,string):
          self.string=string
     
     def filter_algorithm(self):
          # Create a list based on a string by taking the apostrophe
          string2=self.string.replace('´', '')
          list1=string2.split(' ')
          self.list1=list1
          # Create a list based on a string without stripping the apostrophe
          list2=self.string.split(' ')
          self.list2=list2
          return (list1,list2)

     def invert_alg(self):
          # Create a string from a list
          list3=self.list4[::-1]
          new_string = " ".join(list3)
          # print(new_string)
          return (new_string)

     def Put_line(self):
          list4=[]
          for elem in range(len(self.list2)):
               if( '´' in self.list2[elem])==True:
                    lista4.append(self.list1[elem])
               if ('´' in self.list2[elem])==False:
                    string3=self.list1[elem] + '´'
                    list4.append(string3)
          self.list4=list4
          return list4
                    
     def User_interaction(self):
          print("Returns a resolution of the Rubik's Cube given rolls")
          x=str(input('Enter the algorithms: '))
          Cube1=Cubo(x)
          L=Cube1.filter_algorithm()
          print(L)
          L2=Cube1.Put_line()
          print(L2)
          S=Cube1.invert_alg()
          print(S)