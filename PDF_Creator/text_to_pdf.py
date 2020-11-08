def Print_PDF(train, name, age, gender, address, adhr, pnr, DoJ, starting, destination, staus, seatNo, coach, mobl, email):
    addhar = 'XXXXXXXX'
    for i in str(adhr)[8:12]:
        addhar += i

    mobile = 'XXXXXX'
    for i in str(mobl)[6:10]:
        mobile += i

    from fpdf import FPDF
    
    document = FPDF(orientation='P', unit='mm', format='A4')
    document.add_page()
    
    document.set_margins(10, 5, 10)
    
    document.set_font("arial", 'U', size=28)
    document.cell(130, 25, txt=f"Indian Railways", ln=1, align='R')


    document.cell(1, 5, txt="", ln=10)
    document.set_font("arial", 'B', size=24)
    document.cell(130, 30, txt=train, ln=1, align='R')

    document.cell(1, 28, txt="", ln=10)
    document.set_font("Arial", "B", size=18)
    document.cell(5, 15, txt=f"PNR : {pnr}                  Aadhaar : {addhar}", ln=3)
    
    document.set_font_size(15)
    document.cell(15, 15, txt=f"Name : {name}                  DoB\\Gender : {age} {gender.capitalize()[0]}", ln=6)
    
    document.cell(25, 15, txt=f"Coach Number: {coach}                  Seat No : {seatNo}                  Status : {staus}", ln=9)
    document.cell(1, 30, txt="", ln=10)
    document.set_font("Arial", size=14)
    document.cell(35, 15, txt=f"Date of Journey : {DoJ}", ln=12)
    document.cell(45, 15, txt=f"Starting Junction : {starting}                  Destination Junction : {destination}", ln=15)

    document.cell(1, 30, txt="", ln=10)
    
    document.cell(55, 15, txt=f"Mobile Number : {mobile}                  E-Mail ID : {email}", ln=18)
    document.cell(65, 15, txt=f"Address : {address}", ln=21)
    
    document.output(f"{pnr}.pdf")
    
    return f"Your ticket have been Booked!! and would be send at {email}"