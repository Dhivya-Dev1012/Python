class EligibilityForMarriage():
    def eligibilityForMarriage(gender,age):
        if(gender=="Male"):
            if(age>20):
                message="ELIGIBLE"
            else:
                message="NOT ELIGIBLE"
        if(gender=="Female"):
            if(age>17):
                message="ELIGIBLE"
            else:
                message="NOT ELIGIBLE"
        return message