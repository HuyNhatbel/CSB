import csv

def process_csv(file_path):
    unique_emails = set()
    company_counts = dict()
    
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        # cat tung dong
        for row in reader:
            # ktra so luong cot(3)
            if len(row) != 3:
                continue
            name, comp, email = row
            # xoa khoang trang
            email = email.strip()
            comp = comp.strip()
            # kiem tra email da ton tai
            if email not in unique_emails:
                unique_emails.add(email)
                # cap nhat so luong dai biet cua cty
                if comp in company_counts:
                    company_counts[comp] += 1
                else:
                    company_counts[comp] = 1
                    
        sorted_companies = sorted(
            company_counts.items(), key=(lambda item: item[1]), reverse=True
            )
        
        
    #in kq
    print(f"Dai bieu: {len(unique_emails)}")
    print("Danh sách công ty và số lượng đại biểu:")
    for company, count in sorted_companies:
        print(f"{company}: {count}")
        
process_csv("B10/L10/data.csv")
            