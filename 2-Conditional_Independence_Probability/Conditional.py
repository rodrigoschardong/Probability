from unittest import result
import unittest


class Conditional():
    def Conditional_Formula(self, probAandB, probB):
        if(probB > 0):
            return (probAandB / probB)
        return "Error"

    def Probability(self, conjunct, sampleUniverse):
        if(len(sampleUniverse) == 0):
            return "Error"
        probability = len(conjunct) / len(sampleUniverse)
        if(probability > 1):
            return "Error"
        return probability

    def Even_And_Odds_Conjunct(self, conjunct):
        even = []
        odd = []
        for i in range(len(conjunct)):
            if((conjunct[i] / 2) == int(conjunct[i] / 2)):
                even.append(conjunct[i])
            else:
                odd.append(conjunct[i])
        return even, odd

    def Less_Than_Conjunct(self, conjunct, value):
        out = []
        for i in range(len(conjunct)):
            if(conjunct[i] < value):
                out.append(conjunct[i])
        return out

    def Greater_Than_Conjunct(self, conjunct, value):
        out = []
        for i in range(len(conjunct)):
            if(conjunct[i] > value):
                out.append(conjunct[i])
        return out

    def And_OP_Conjunct(self, conjA, conjB, TEST = 0):
        if(not(any(isinstance(i, list) for i in conjA)) or not(any(isinstance(j, list) for j in conjB))):
            return list(set(conjA).intersection(conjB))
        elif(TEST == 1):
            conjAstr = []
            for a in range(len(conjA)):
                conjAstr.append(self.List_To_String(Conditional, conjA[a]))
            conjBstr = []
            for b in range(len(conjB)):
                conjBstr.append(self.List_To_String(Conditional, conjB[b]))

            andStr = list(set(conjAstr).intersection(conjBstr))
            out = []
            for s in range(len(andStr)):
                out.append(self.String_To_List(Conditional, andStr[s]))
            return out
        else:
            conjAstr = []
            for a in range(len(conjA)):
                conjAstr.append(self.List_To_String(conjA[a]))
            conjBstr = []
            for b in range(len(conjB)):
                conjBstr.append(self.List_To_String(conjB[b]))

            andStr = list(set(conjAstr).intersection(conjBstr))
            out = []
            for s in range(len(andStr)):
                out.append(self.String_To_List(andStr[s]))
            return out

    def Or_OP_Conjunct(self, conjA, conjB, TEST = 0):
        if(not(any(isinstance(i, list) for i in conjA)) or not(any(isinstance(j, list) for j in conjB))):
            out = list(conjA)
            out.extend(x for x in conjB if x not in out)
            out.sort()
            return out
        elif(TEST == 1):
            conjAstr = []
            for a in range(len(conjA)):
                conjAstr.append(self.List_To_String(Conditional, conjA[a]))
            conjBstr = []
            for b in range(len(conjB)):
                conjBstr.append(self.List_To_String(Conditional, conjB[b]))

            orStr = list(conjAstr)
            orStr.extend(x for x in conjBstr if x not in orStr)
            orStr.sort()
            
            out = []
            for s in range(len(orStr)):
                out.append(self.String_To_List(Conditional, orStr[s]))
            return out 
        else:
            conjAstr = []
            for a in range(len(conjA)):
                conjAstr.append(self.List_To_String(conjA[a]))
            conjBstr = []
            for b in range(len(conjB)):
                conjBstr.append(self.List_To_String(conjB[b]))

            orStr = list(conjAstr)
            orStr.extend(x for x in conjBstr if x not in orStr)
            orStr.sort()
            
            out = []
            for s in range(len(orStr)):
                out.append(self.String_To_List(orStr[s]))
            return out 

    def Not_OP_Conjunct(self, conj, sampleUniverse):
        return list(set(sampleUniverse) - set(conj))
    
    def Equal_To_Conjunct(self, conj, value):
        out = []
        for i in range(len(conj)):
            if(conj[i] == value):
                out.append(conj[i])
        return out

    def Sum_Of_Elements_Is_Equal(sel, conj, value):
        out = []
        for i in range(len(conj)):
            sum = 0
            for j in range(len(conj[i])):
                sum += conj[i][j]
            if(sum == value):
                out.append(conj[i])
        return out

    def An_Element_Is_Equal_To(self, conj, element, value):
        out = []
        for i in range(len(conj)):
            if(element <= len(conj[i])):
                if(value == conj[i][element]):
                    out.append(conj[i])
        return out

    def List_To_String(self, list):
        out = ""
        for i in range(len(list)):
            out += (str(list[i]) + " ")
        return out

    def String_To_List(self, string):
        list = string.split()
        out = []
        for i in range(len(list)):
            try:
                out.append(int(list[i]))
            except:
                out.append(float(list[i]))
        return out

class Tests(unittest.TestCase):
    def test_Conditional_Formula_Error(self):
        self.assertEqual(Conditional.Conditional_Formula(Conditional, 10, 0),  "Error", "Should be Error")
    def test_Conditional_Formula_Zero(self):
        self.assertEqual(Conditional.Conditional_Formula(Conditional, 0, 10),  0, "Should be 0")
    def test_Conditional_Formula_One(self):
        self.assertEqual(Conditional.Conditional_Formula(Conditional, 10, 10),  1, "Should be 1")
    def test_Conditional_Formula_Half(self):
        self.assertEqual(Conditional.Conditional_Formula(Conditional, 0.5, 2),  0.25, "Should be 0.25")

    def test_Probability_Half(self):
        self.assertEqual(Conditional.Probability(Conditional, [0,1], [0,1,2,3]),  0.5, "Should be 0.5")
    def test_Probability_One(self):
        self.assertEqual(Conditional.Probability(Conditional, [0,1], [0,1]),  1, "Should be 1")
    def test_Probability_Zero(self):
        self.assertEqual(Conditional.Probability(Conditional, [], [0,1,2,3]),  0, "Should be 0")
    def test_Probability_Divided_By_Zero(self):
        self.assertEqual(Conditional.Probability(Conditional, [0,1], []),  "Error", "Should be Error")
    def test_Probability_Conjunct_Bigger_Than_Universe(self):
        self.assertEqual(Conditional.Probability(Conditional, [0,1], [0]),  "Error", "Should be Error")

    def test_Probability_Even(self):
        even, odd = Conditional.Even_And_Odds_Conjunct(Conditional, [1,2,3,4,5])
        self.assertEqual(even,  [2,4], "Should be [2,4]")
    def test_Probability_Odd(self):
        even, odd = Conditional.Even_And_Odds_Conjunct(Conditional, [1,2,3,4,5])
        self.assertEqual(odd,  [1,3,5], "Should be [1,3,5]")

    def test_Less_Than_Conjunct(self):
        self.assertEqual(Conditional.Less_Than_Conjunct(Conditional, [0,1], 1),  [0], "Should be [0]")
    def test_Less_Than_Conjunct_Return_All(self):
        self.assertEqual(Conditional.Less_Than_Conjunct(Conditional, [0,1], 10),  [0,1], "Should be [0,1]")
    def test_Less_Than_Conjunct_Return_Nothing(self):
        self.assertEqual(Conditional.Less_Than_Conjunct(Conditional, [0,1], 0),  [], "Should be []")
    def test_Less_Than_Conjunct_Enter_Emply(self):
        self.assertEqual(Conditional.Less_Than_Conjunct(Conditional, [], 1),  [], "Should be []")

    def test_More_Than_Conjunct(self):
        self.assertEqual(Conditional.Greater_Than_Conjunct(Conditional, [0,1], 0),  [1], "Should be [1]")
    def test_More_Than_Conjunct_Return_All(self):
        self.assertEqual(Conditional.Greater_Than_Conjunct(Conditional, [0,1], 10),  [], "Should be []")
    def test_More_Than_Conjunct_Return_Nothing(self):
        self.assertEqual(Conditional.Greater_Than_Conjunct(Conditional, [2,1], 0),  [2,1], "Should be [2,1]")
    def test_More_Than_Conjunct_Enter_Emply(self):
        self.assertEqual(Conditional.Greater_Than_Conjunct(Conditional, [], 1),  [], "Should be []")

    def test_And_OP_Conjunct(self):
        self.assertEqual(Conditional.And_OP_Conjunct(Conditional, [1,2], [0,1], 1),  [1], "Should be [1]")
    def test_And_OP_Conjunct_All_Elements(self):
        self.assertEqual(Conditional.And_OP_Conjunct(Conditional, [1,2], [2,1], 1),  [1,2], "Should be [1]")
    def test_And_OP_Conjunct_Emply(self):
        self.assertEqual(Conditional.And_OP_Conjunct(Conditional, [1,2], [0,10], 1),  [], "Should be []")
    def test_And_OP_Conjunct_Repeated_Numbers(self):
        self.assertEqual(Conditional.And_OP_Conjunct(Conditional, [0,0,2], [0,1], 1),  [0], "Should be [0]")
    def test_And_OP_Conjunct_String(self):
        self.assertEqual(Conditional.And_OP_Conjunct(Conditional, ["1","2"], ["0","1"], 1),  ["1"], "Should be ['1']")
    def test_And_OP_Conjunct_list(self):
        self.assertEqual(Conditional.And_OP_Conjunct(Conditional, [[1,2],[1,3]], [[2,1], [1,2]], 1),  [[1,2]], "Should be [[1,2]]")

    def test_Or_OP_Conjunct(self):
        self.assertEqual(Conditional.Or_OP_Conjunct(Conditional, [1,2], [0,5,7], 1),  [0,1,2,5,7], "Should be [0,1,2,5,7]")
    def test_Or_OP_Conjunct_Excluding(self):
        self.assertEqual(Conditional.Or_OP_Conjunct(Conditional, [1,2], [0,1], 1),  [0,1,2], "Should be [0,1,2]")
    def test_Or_OP_Conjunct_A_Emply(self):
        self.assertEqual(Conditional.Or_OP_Conjunct(Conditional, [], [0,1], 1),  [0,1], "Should be [0,1]")
    def test_Or_OP_Conjunct_B_Emply(self):
        self.assertEqual(Conditional.Or_OP_Conjunct(Conditional, [0,1], [], 1),  [0,1], "Should be [0,1]")
    def test_Or_OP_Conjunct_AB_Emply(self):
        self.assertEqual(Conditional.Or_OP_Conjunct(Conditional, [], [], 1),  [], "Should be []")
    def test_Or_OP_Conjunct_AB_String(self):
        self.assertEqual(Conditional.Or_OP_Conjunct(Conditional, ["0","1","2"], ["1","-2", "3"], 1), ["-2","0","1","2","3"], "Should be ['-2','0','1','2','3']")
    def test_Or_OP_Conjunct_list(self):
        self.assertEqual(Conditional.Or_OP_Conjunct(Conditional, [[1,2],[1,3]], [[2,1], [1,2]], 1),  [[1,2], [1,3], [2,1]], "Should be [[1,2], [1,3], [2,1]]")

    def test_Not_OP_Conjunct(self):
        self.assertEqual(Conditional.Not_OP_Conjunct(Conditional, [0], [0,1]),  [1], "Should be [1]")
    def test_Not_OP_Conjunct_Erase_All(self):
        self.assertEqual(Conditional.Not_OP_Conjunct(Conditional, [0,1], [0,1]),  [], "Should be []")
    def test_Not_OP_Conjunct_Erase_Nothing(self):
        self.assertEqual(Conditional.Not_OP_Conjunct(Conditional, [], [0,1]),  [0,1], "Should be [0,1]")
    def test_Not_OP_Conjunct_Erase_Not_Found(self):
        self.assertEqual(Conditional.Not_OP_Conjunct(Conditional, [3], [0,1]),  [0,1], "Should be [0,1]")
    def test_Not_OP_Conjunct_Erase_More_Than_All(self):
        self.assertEqual(Conditional.Not_OP_Conjunct(Conditional, [0,1,2], [0,1]),  [], "Should be []")

    def test_Equal_To_Conjunct(self):
        self.assertEqual(Conditional.Equal_To_Conjunct(Conditional, [0,1,2], 1),  [1], "Should be [1]")
    def test_Equal_To_Conjunct_None(self):
        self.assertEqual(Conditional.Equal_To_Conjunct(Conditional, [0,1,2], 3),  [], "Should be []")
    def test_Equal_To_Conjunct_More_than_One(self):
        self.assertEqual(Conditional.Equal_To_Conjunct(Conditional, [0,1,1,2], 1),  [1,1], "Should be [1,1]")

    def test_Sum_Of_Elements_Is_Equal(self):
        self.assertEqual(Conditional.Sum_Of_Elements_Is_Equal(Conditional, [[0,1],[2,2],[1]], 1), [[0,1],[1]], "Should be [[0,1],[1]]")
    def test_Sum_Of_Elements_Is_Equal_None(self):
        self.assertEqual(Conditional.Sum_Of_Elements_Is_Equal(Conditional, [[0,1],[2,2],[1]], 6), [], "Should be []")

    def test_An_Element_Is_Equal_To(self):
        self.assertEqual(Conditional.An_Element_Is_Equal_To(Conditional, [[0,1],[2,2],[1]], 0, 0), [[0,1]], "Should be [[0,1]]")
    def test_An_Element_Is_Equal_To_None(self):
        self.assertEqual(Conditional.An_Element_Is_Equal_To(Conditional, [[0,1],[2,2],[1]], 0, 5), [], "Should be []")
    def test_An_Element_Is_Equal_To_No_Element(self):
        self.assertEqual(Conditional.An_Element_Is_Equal_To(Conditional, [[0,1],[2,2],[1]], 10, 0), [], "Should be []")

    def test_List_To_String(self):
        self.assertEqual(Conditional.List_To_String(Conditional, [0,1,2,3]), "0 1 2 3 ", "Should be '0 1 2 3 '")
    def test_List_To_String_Neg(self):
        self.assertEqual(Conditional.List_To_String(Conditional, [0,-1,2,3]), "0 -1 2 3 ", "Should be '0 -1 2 3 '")
    def test_List_To_String_Emply(self):
        self.assertEqual(Conditional.List_To_String(Conditional, []), "", "Should be ''")
    def test_List_To_String_Broken(self):
        self.assertEqual(Conditional.List_To_String(Conditional, [0.1,-1.7,2,3]), "0.1 -1.7 2 3 ", "Should be '0.1 -1.7 2 3 '")

    def test_String_To_List(self):
        self.assertEqual(Conditional.String_To_List(Conditional, "0 1 2 3 "), [0,1,2,3], "Should be [0,1,2,3]")
    def test_String_To_List_Neg(self):
        self.assertEqual(Conditional.String_To_List(Conditional, "0 -1 2 3 "), [0,-1,2,3], "Should be [0,-1,2,3]")
    def test_String_To_List_broken(self):
        self.assertEqual(Conditional.String_To_List(Conditional, "0 1.7 2 3.2 "), [0,1.7,2,3.2], "Should be [0,1.7,2,3.2]")
    
    
if __name__ == '__main__':
    unittest.main()