

def calculate_marks(maths,eng,hindi,history=0):
    print(f"Maths={maths}")
    print(f"English ={eng}")
    print(f"Hindi ={hindi}")
    print(f"History ={history}")

    total=maths+eng+hindi+history
    print(f"Total marks scored = {total}")


calculate_marks(maths=79,hindi=45,history=60,eng=70)