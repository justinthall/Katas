"""problem: with the integer value of a month in a year, return what quarter of the year it is in.
    solution: create a switch statement using a dictionary to directly pull the month's quarter"""
def quarter_of(month):
    def quarter1():
        return 1
    def quarter2():
        return 2
    def quarter3():
        return 3
    def quarter4():
        return 4
    map={
        1:quarter1(),
        2:quarter1(),
        3:quarter1(),
        4:quarter2(),
        5:quarter2(),
        6:quarter2(),
        7:quarter3(),
        8:quarter3(),
        9:quarter3(),
        10:quarter4(),
        11:quarter4(),
        12:quarter4()
    }
    func=map.get(month, "month not found")
    return func

