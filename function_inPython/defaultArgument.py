def calculate_marks(maths,eng,hindi,history=100):
    print(f"Maths={maths}")
    print(f"English ={eng}")
    print(f"Hindi ={hindi}")
    print(f"History ={history}")

    total=maths+eng+hindi+history
    print(f"Total marks scored = {total}")


calculate_marks(80,79,90,20)