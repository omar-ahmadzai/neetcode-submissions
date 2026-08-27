class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        generate = [[0, 0, ""]]  # [open, close, parentheses]

        while True:
            generate = Solution.generate_next_parnethesis(generate, n)
            # n number of opening parentheses and n number of closing.
            if len(generate[0][2]) == n*2:
                break

        return [array[2] for array in generate]
    
    def generate_next_parnethesis(current, number_of_parentheses):
        new = []

        for array in current:
            opening = array[0]
            closing = array[1]
            parentheses = array[2]
            if opening > closing:
                if opening == number_of_parentheses: 
                    # just have to add a closing
                    new.append([opening, closing + 1, parentheses + ")"])
                else:
                    # Have to add both opening and closing
                    new.append([opening + 1, closing, parentheses + "("])
                    new.append([opening, closing + 1, parentheses + ")"])
            elif opening == closing:
                if opening == number_of_parentheses:
                    # Done
                    new.append(array)
                else:
                    # just have to add an opening
                    new.append([opening + 1, closing, parentheses + "("])
        
        return new