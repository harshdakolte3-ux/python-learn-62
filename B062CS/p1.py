def countlistelements(1st):
    output = {}
    for val in 1st:
        if val in output:
            output[val] =  output[val] + 1
        else:
            output[val] = 1
        return output
    def calculateaverage(marks):
        return round(sum(marks)/len(marks),2)
    
147691