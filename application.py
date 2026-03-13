def main():
    name=input("Enter your Name: ")
    exam=input("Enter the Exam you have taken up: ")
    if exam.upper()=="JEE MAINS":
        jee()
    elif exam.upper()=="NEET":
        neet()
    elif exam.upper()=="KCET":
        kcet()
    elif exam.upper()=="COMEDK":
        comedk()
    elif exam.upper()=="JEE ADVANCE":
        jee_advance()
    else:
        print("Invalid Entry")
def jee():
    score=int(input("Enter JEE Mains Score: "))
    if score==300:
        print("Percentile: 100")
        print("Rank: 1")
        print("Qualified to JEE Advance")
    elif score>=271 and score<=299:
        print("Percentile: 99.99")
        print("Rank: 2-56")
        print("Qualified to JEE Advance")
    elif score>=260 and score<=270:
        print("Percentile: 99.98")
        print("Rank: 55-115")
        print("Qualified to JEE Advanced")
    elif score>=241 and score<=259:
        print("Percentile: 99.95")
        print("Rank: 115-402")
        print("Qualified to JEE Advance")
    elif score>=222 and score<=240:
        print("Percenitle: 99.9")
        print("Rank: 402-978")
        print("Qualified to JEE Advance")
    elif score>=201 and score<=221:
        print("Percentile: 99.8")
        print("Rank: 978-2001")
        print("Qualified to JEE Advance")
    elif score>=180 and score<=200:
        print("Percentile: 99.7")
        print("Rank: 2001-3901")
        print("Qualified to JEE Advance")
    elif score>=161 and score>=179:
        print("Percentile: 99.3")
        print("Rank: 3901-7003")
        print("Qualified to JEE Advance")
    elif score>=141 and score<=160:
        print("Percentile: 99.2")
        print("Rank: 7003-12200")
        print("Qulified to JEE Advance")
    elif score>=119 and score<=140:
        print("Percentile: 98.7")
        print("Rank: 12200-21010")
        print("Qualified to JEE Advance")
    elif score>=100 and score<=119:
        print("Percentile: 96.9")
        print("Rank: 21010-35000")
        print("Qualified to JEE Advance")
    elif score>=-24 and score<=99:
        print("Percentile: 0.843-96.89")
        print("Rank: 35000-300000")
        print("Failed to qualify to JEE Advance")
    else:
        print("Invalid Entry")
def neet():
    score=int(input("Enter NEET Marks: "))
    if score>=686:
        print("Rank: 1")
        print("Top College to this rank: AIIMS, New Delhi")
    elif score>=662 and score<=685:
        print("Rank: 2-33")
        print("Top College to this rank: AIIMS, New Delhi")
    elif score>=625 and score<=661:
        print("Rank: 34-158")
        print("Top college to this rank: Maulana Azad Medical College, New Delhi")
    elif score>=607 and score<=624:
        print("Rank: 159-1022")
        print("Top college to this rank: Christian Medical College, Bangalore")
    elif score>=606 and score<=605:
        print("Rank: 1023-1047")
        print("Top College to this rank: Institute of Medical Education and Research, Chandigarh")
    elif score>=600 and score<=604:
        print("Rank: 1048-1386")
        print("Top College to this rank: Jawaharlal Institute of Medical Education and Research, Puducherry")
    elif score>=599 and score<=582:
        print("Rank: 1386-3200")
        print("Top College to this rank: Sanjay Gandhi Institute of Medical Science, Lucknow")
    elif score>=581 and score<=563:
        print("Rank: 3201-7497")
        print("Top college to this rank: Banaras Hindu University, Varansi")