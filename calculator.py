from __future__ import division

class Module:
    def __init__(self, module_level, module_code, module_credits, module_grade, module_required=False):
        self.level = module_level
        self.code = module_code
        self.credits = module_credits
        self.grade = module_grade
        self.required = module_required


def get_required_modules(modules):
    req_mods = []
    for mod in modules:
        if mod.required:
            req_mods.append(mod.code)
    return req_mods

def get_permutations(modules, required_modules, max_creds = 100, max_creds_three = 100 , max_creds_two = 0, max_creds_one = 0):
    perms = []
    perm_bt(perms, modules, required_modules, max_creds, max_creds_three, max_creds_two, max_creds_one)
    return perms
    # Send to BT

def perm_bt(perms, modules, required_modules, max_creds, max_creds_three, max_creds_two, max_creds_one, partial = []):
    creds_one = 0
    creds_two = 0
    creds_three = 0
    creds_total = 0

    for mod in partial:
        if mod.level == 1:
            creds_one += mod.credits
        elif mod.level == 2:
            creds_two += mod.credits
        elif mod.level == 3:
            creds_three += mod.credits
        else:
            print("ERROR: INVALID MODULE LEVEL SPECIFIED")
        creds_total = creds_one + creds_two + creds_three
    
    if creds_one > max_creds_one or creds_two > max_creds_two or creds_three > max_creds_three or creds_total > max_creds:
        return

    if creds_total == max_creds:
        for mod_code in required_modules:
            acceptable = False
            for mod in partial:
                if mod.code == mod_code:
                    acceptable = True
            if not acceptable:
                return
        perms.append(partial)
    
    for i in range(len(modules)):
        module = modules[i]
        remaining = modules[i+1:]
        perm_bt(perms, remaining, required_modules, max_creds, max_creds_three, max_creds_two, max_creds_one, partial + [module])

def get_perm_grade(perm):
    total_credits = 0
    grade = 0
    for mod in perm:
        total_credits += mod.credits
    for mod in perm:
        weight = mod.credits / total_credits
        grade += mod.grade * weight
    return grade

def classification(modules, max_creds, max_creds_three, max_creds_two, max_creds_one):
    required_mods = get_required_modules(modules)
    permutations = get_permutations(modules, required_mods, max_creds, max_creds_three, max_creds_two, max_creds_one)
    best_perm = []
    best_grade = 0
    for perm in permutations:
        grade = get_perm_grade(perm)
        if grade > best_grade:
            best_grade = grade
            best_perm = perm
    return best_perm, round(best_grade, 2)
    

def print_grade(perm, grade):
    for mod in perm:
        print("\tModule: " + str(mod.code) + "\t-\t Grade: " + str(mod.grade) + "\t-\t Credits: " + str(mod.credits))
    print("\n\tGRADE:\t" + str(grade))
    print("\tCLASSIFICAION:\t" + get_classification_name(grade))
    print("\n")

def get_classification_name(grade):
    if (grade >=0 and grade < 40):
        return "Fail"
    elif(grade >=40 and grade < 50):
        return "Third Class"
    elif(grade >=50 and grade < 60):
        return "2:2 (Second Class, Second Division)"
    elif(grade >=60 and grade < 70):
        return "2:1 (Second Class, First Division)"
    elif(grade >=70 and grade <=100):
        return "1st Class"
    else:
        return "Either you entered some information incorrectly, or you cheated..."


if __name__ == "__main__":

    ##################################
    # INSERT GRADE INFORMATION BELOW #
    ##################################

    year_one_modules = [
        ## Year, Code, Credits, Grade, Required
        Module(1, "104KM", 20, 40), # Enterprise Information Systems
        Module(1, "106CR", 20, 40), # Designing for Usability 1
        Module(1, "120CT", 20, 40), # Computer Architecture and Networks
        Module(1, "121COM", 20, 40), # Introduction to Computing
        Module(1, "122COM", 10, 40), # Introduction to Algorithms
        Module(1, "124MS", 20, 40), # Logic and Sets
        Module(1, "Add+", 20, 40), # Add+Vantage
    ]

    year_two_modules = [
        ## Year, Code, Credits, Grade, Required
        Module(2, "250EC", 40, 40), # Placement
        Module(2, "206CDE", 20, 40), # Real World Project
        Module(2, "207SE", 20, 40), # Operating Systems, Security and Networks
        Module(2, "210CT", 20, 40), # Programming, Algorithms and Data Structures
        Module(2, "220CT", 20, 40), # Data and Information Retrieval
        Module(2, "260CT", 20, 40), # Software Engineering
        Module(2, "290COM", 10, 40), # Technology and its Social, Legal and Ethical Context
        Module(2, "Add+", 10, 40) # Add+Vantage
    ]

    year_three_modules = [
        ## Year, Code, Credits, Grade, Required
        Module(3, "303COM", 30, 40, True), # Individual Project
        Module(3, "340CT", 20, 40), # Software Quality and Process Management
        Module(3, "Add+", 10, 40), # Add+Vantage
        Module(3, "380CT", 20, 40), # Theoretical Aspects of Computer Science
        Module(3, "303CEM", 20, 40), # Optional Module 1
        Module(3, "370CT", 20, 40) # Optional Module 2
    ]

    ## CLASSIFICATION ONE ##
    # The average mark of the 100 credits worth of modules with the highest mark 
    # at level 6 or above
    c1_mods = year_three_modules
    c1_perm, c1_grade = classification(c1_mods, 100, 100, 0, 0)
    print_grade(c1_perm, c1_grade)

    ## CLASSIFICATION TWO ##
    # The average mark of the 220 credits worth of modules with the highest mark 
    # at level 5 and above (to include a maximum of 120 credits at Level 5)
    c2_mods = year_three_modules + year_two_modules
    c2_perm, c2_grade = classification(c2_mods, 220, 120, 120, 0)
    print_grade(c2_perm, c2_grade)

    ## CLASSIFICATION THREE ##
    # The average mark of the 300 credits worth of modules with the highest mark 
    # at levels 4 and above (to include a maximum of 120 credits at each of Levels 4 and 5)
    c3_mods = year_three_modules + year_two_modules + year_one_modules
    c3_perm, c3_grade = classification(c3_mods, 300, 120, 120, 120)
    print_grade(c3_perm, c3_grade)

    print("\t############################")
    print("\t#  HIGHEST CLASSIFICATION  #")
    print("\t############################\n")
    best_grade = max(c1_grade, c2_grade, c3_grade)
    print("\tGrade: " + str(best_grade))
    print("\tClassification: " + get_classification_name(best_grade))
    print("\n")
