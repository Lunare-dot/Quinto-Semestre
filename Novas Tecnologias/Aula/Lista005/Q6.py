from datetime import *

def dateComparison(date1, date2):
    
    d1 = datetime.strptime(date1, "%d/%m/%Y")
    d2 = datetime.strptime(date2, "%d/%m/%Y")
    
    gDate = max(d1, d2)
    mDate = min(d1, d2)
    
    total_days = abs((gDate - mDate).days)
    
    weeks = total_days // 7
    remaining_days =  total_days % 7
    
    print(f"Maior data: {gDate}")
    print(f"Diferença de dias: {total_days}")
    print(f"Diferença de semanas + dias: {weeks} e {remaining_days}")
    
u_entry1 = input("Digite a primeira data: ")
u_entry2 = input("Digite a segunda data: ")
dateComparison(u_entry1, u_entry2)