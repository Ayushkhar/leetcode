# Last updated: 6/6/2026, 10:24:41 PM
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count_sq_sand = 0
        count_cir_sand = 0
        for s in sandwiches:

            if s == 0:
                count_cir_sand += 1
            else:
                count_sq_sand += 1
                

        count_sq_stud = 0
        count_cir_stud = 0
        for st in students:
            if st == 0:
                count_cir_stud += 1
            else:
                count_sq_stud += 1

        for s in sandwiches:

            if s == 0:

                if count_cir_stud == 0:  
                    break

                count_cir_stud -= 1
            else:
                if count_sq_stud == 0: 
                    break
                count_sq_stud -= 1

        return count_cir_stud + count_sq_stud
