import streamlit as st
import pandas as pd
from io import StringIO
import random
import string
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Your book data
data = """Sr.No.,Title,Unit Price
1,Engineering Drawing (Group 4) -Hindi - Revised NSQF (1200) (9 Hindi + 1 English),120
2,Engineering Drawing (Group 7) -Hindi - Revised NSQF (1200),115
3,Engineering Drawing (Group 9) -Hindi - Revised NSQF (1200),140
4,Engineering Drawing (Group 13) -Hindi- Revised NSQF (1200),110
5,Engineering Drawing (Group 17) -Hindi - Revised NSQF (1200),125
6,Engineering Drawing 1st Year (Group 18) -Hindi - Revised NSQF (1200),130
7,Engineering Drawing 1st Year (Group 19) -Hindi - Revised NSQF (1200),110
8,Engineering Drawing 1st Year (Group 20) -Hindi - Revised NSQF (1200),105
9,Engineering Drawing 1st Year (Group 23) -Hindi - Revised NSQF (1200),85
10,Engineering Drawing 1st Year (Group 24) -Hindi - Revised NSQF (1200),125
11,Engineering Drawing 1st Year (Group 25) -Hindi - Revised NSQF (1200),130
12,Engineering Drawing 1st Year (Group 26) -Hindi - Revised NSQF (1200),90
13,Employability Skills - Student Workbook - Part 1 -Hindi (Revised NSQF) (1200),270
14,Employability Skills - Student Workbook - Part 2 -Hindi (Revised NSQF) (1200),245
15,Workshop Calculation & Science 1st Year (Draughtsman Civil) -Hindi - Revised NSQF (1200),150
16,Workshop Calculation & Science 1st Year (Draughtsman Mechanical) -Hindi - Revised NSQF (1200),145
17,Workshop Calculation & Science 1st Year (Electrician) -Hindi - Revised NSQF (1200),150
18,Workshop Calculation & Science 1st Year (Electronics Mechanic) -Hindi - Revised NSQF (1200),130
19,Workshop Calculation & Science 1st Year (Fitter) -Hindi - Revised NSQF (1200),155
20,Workshop Calculation & Science 1st Year (ICTSM) -Hindi - Revised NSQF (1200),120
21,Workshop Calculation & Science 1st Year (Machinist) -Hindi - Revised NSQF (1200),155
22,Workshop Calculation & Science (Mechanic Diesel & Mechanic Tractor) -Hindi - Revised NSQF (1200),180
23,Workshop Calculation & Science (Mechanic Auto Body Painting) -Hindi- Revised NSQF (1200),155
24,Workshop Calculation & Science 1st Year (MMV) -Hindi - Revised NSQF (1200),160
25,Workshop Calculation & Science (Plumber) - Hindi - Revised NSQF (1200),135
26,Workshop Calculation & Science 1st Year (R&ACT) -Hindi - Revised NSQF (1200),145
27,Workshop Calculation & Science 1st Year (TDM (D&M/PTJ&F) -Hindi - Revised NSQF (1200),160
28,Workshop Calculation & Science 1st Year (Turner) -Hindi - Revised NSQF (1200),155
29,Workshop Calculation & Science (Welder) -Hindi - Revised NSQF (1200),160
30,Workshop Calculation & Science 1st Year (Wireman) -Hindi - Revised NSQF (1200),150
31,Employability Skills - Student Workbook - 2nd Year -Hindi (Revised NSQF) (1200),190
32,Workshop Calculation & Science 2nd Year (Draughtsman Civil) -Hindi - Revised NSQF (1200),135
33,Workshop Calculation & Science 2nd Year (Electrician) -Hindi - Revised NSQF (1200),115
34,Workshop Calculation & Science 2nd Year (Fitter) -Hindi - Revised NSQF (1200),120
35,Workshop Calculation & Science 2nd Year (R&ACT) -Hindi - Revised NSQF (1200),125
36,Workshop Calculation & Science 2nd Year (Turner) -Hindi - Revised NSQF (1200),105
37,Workshop Calculation & Science 2nd Year (Wireman) -Hindi - Revised NSQF (1200),105
38,Carpenter Practical - Hindi - Revised NSQF LEVEL 3 (1200),475
39,Carpenter Theory - Hindi - Revised NSQF LEVEL 3 (1200),380
40,Cosmetology Practical - Hindi - Revised NSQF LEVEL 3 (1200),265
41,Cosmetology Theory Hindi - Revised NSQF LEVEL 3 (1200),185
42,COPA Theory - Hindi - Revised NSQF LEVEL 3 (1200),440
43,COPA - Practical (Volume II of II) Hindi Revised NSQF LEVEL 3 (1200),360
44,Draughtsman Civil 1st Year Practical - Hindi - Revised NSQF LEVEL 4 (1200),355
45,Draughtsman Civil 1st Year Theory - Hindi- Revised NSQF LEVEL 4 (1200),480
46,Draughtsman Civil 2nd Year Practical - Hindi Revised NSQF LEVEL 4 (1200),385
47,Draughtsman Civil 2nd Year Theory - Hindi - Revised NSQF LEVEL 4 (1200),495
48,Draughtsman Mechanical 1st Year Practical - Hindi - Revised NSQF LEVEL 4 (1200),440
49,Draughtsman Mechanical 1st Year Theory - Hindi - Revised NSQF LEVEL 4 (1200),415
50,Drone Technician Theory Hindi - Revised NSQF LEVEL 3 (1200),160
51,Dress Making Practical Hindi - Revised NSQF LEVEL 3 (1200),455
52,Dress Making Theory - Hindi Revised NSQF LEVEL 3 (1200),280
53,Electrician 1st Year Practical - Hindi - Revised NSQF LEVEL 4 (1200),335
54,Electrician 2nd Year Practical - Hindi - Revised NSQF LEVEL 4 (1200),345
55,Electrician 1st Year Theory - Hindi Revised NSQF LEVEL 4 (1200),390
56,Electronics Mechanic (Common for TPES) 1st Year Practical - Hindi - Revised NSQF LEVEL 4 (1200),330
57,Electronics Mechanic (Common for TPES) 1st Year Theory - Hindi Revised NSQF LEVEL 4 (1200),440
58,Fashion Design & Technology Practical - Hindi - Revised NSQF LEVEL 3 (1200),405
59,Fashion Design & Technology Theory Hindi - Revised NSQF LEVEL 3 (1200),300
60,Fitter 1st Year Practical - Hindi - Revised NSQF LEVEL 4 (1200),440
61,Fitter 1st Year Theory - Hindi - Revised NSQF LEVEL 4 (1200),450
62,Fitter 2nd Year Practical - Hindi - Revised NSQF LEVEL 4 (1200),305
63,Foundryman Practical - Hindi - Revised NSQF LEVEL 3 (1200),280
64,Foundryman Theory Hindi - Revised NSQF LEVEL 3 (1200),330
65,Health Sanitary Inspector Practical - Hindi - Revised NSQF LEVEL 3 (1200),320
66,Health Sanitary Inspector Theory Hindi - Revised NSQF LEVEL 3 (1200),250
67,Instrument Mechanic 1st Year Practical - Hindi - Revised NSQF LEVEL 4 (1200),435
68,Instrument Mechanic 1st Year Theory - Hindi - Revised NSQF LEVEL 4 (1200),425
69,Instrument Mechanic 2nd Year Practical Hindi Revised NSQF LEVEL 4 (1200),395
70,Instrument Mechanic 2nd Year Theory - Hindi - Revised NSQF LEVEL 4 (1200),345
71,ICTSM 1st Year Practical - Hindi - Revised NSQF LEVEL 4 (1200),440
72,ICTSM 1st Year Theory - Hindi - Revised NSQF LEVEL 4 (1200),410
73,Machinist 1st Year Practical - Hindi - Revised NSQF LEVEL 4 (1200),300
74,Machinist 1st Year Theory - Hindi - Revised NSQF LEVEL 4 (1200),360
75,Machinist 2nd Year Practical - Hindi - Revised NSQF LEVEL 4 (1200),420
76,Machinist 2nd Year Theory - Hindi - Revised NSQF LEVEL 4 (1200),400
77,Mechanic Diesel Theory - Hindi - Revised NSQF LEVEL 3 (1200),380
78,Mechanic Diesel Practical - Hindi Revised NSQF LEVEL 3 (1200),305
79,Mechanic Auto Electrical & Electronics Practical - Hindi Revised NSQF LEVEL 3 (1200),280
80,Mechanic Auto Electrical & Electronics Theory - Hindi Revised NSQF LEVEL 3 (1200),340
81,Machinist Grinder 1st Year Practical - Hindi - Revised NSQF LEVEL 4 (1200),325
82,Mechanic Auto Body Painting Practical - Hindi - Revised NSQF LEVEL 3 (1200),245
83,Mechanic Auto Body Painting Theory Hindi - Revised NSQF LEVEL 3 (1200),270
84,Mechanic Auto Body Repair Theory - Hindi - Revised NSQF LEVEL 3 (1200),330
85,MMV 1st Year Practical - Hindi - Revised NSQF LEVEL 4 (1200),280
86,MMV 1st Year Theory - Hindi - Revised NSQF LEVEL 4 (1200),300
87,MMV 2nd Year Practical - Hindi - Revised NSQF LEVEL 4 (1200),275
88,MMV 2nd Year Theory - Hindi - Revised NSQF LEVEL 4 (1200),305
89,Mechanic Two & Three Wheeler Practical - Hindi Revised NSQF LEVEL 3 (1200),335
90,Plumber Theory - Hindi Revised NSQF LEVEL 3 (1200),365
91,Plumber Practical Hindi - Revised NSQF LEVEL 3 (1200),310
92,Painter (General) 1st Year Practical - Hindi - Revised NSQF LEVEL 4 (1200),415
93,Physiotherapy Technician Theory - Hindi - Revised NSQF LEVEL 3 (1200),145
94,Refrigeration & Air Conditioning Technician 1st Year Practical - Hindi - Revised NSQF LEVEL 4 (1200),325
95,Refrigeration & Air Conditioning Technician 1st Year Theory - Hindi - Revised NSQF LEVEL 4 (1200),395
96,Refrigeration & Air Conditioning Technician 2nd Year Practical - Hindi - Revised NSQF LEVEL 4 (1200),390
97,Refrigeration & Air Conditioning Technician 2nd Year Theory - Hindi - Revised NSQF LEVEL 4 (1200),355
98,Solar Technician (Electrical) Practical Hindi - Revised NSQF LEVEL 3 (1200),365
99,Sheet Metal Worker Practical - Hindi Revised NSQF LEVEL 3 (1200),450
100,Sheet Metal Worker Theory - Hindi - Revised NSQF LEVEL 3 (1200),390
101,Surface Ornamentation Techniques (Embroidery) Practical - Hindi - Revised NSQF LEVEL 3 (1200),285
102,Surface Ornamentation Techniques (Embroidery) Theory - Hindi - Revised NSQF LEVEL 3 (1200),180
103,Stenographer Secretarial Assistant (Hindi) Practical - Hindi - Revised NSQF LEVEL 3 (1200),270
104,Stenographer Secretarial Assistant (Hindi) Theory - Hindi Revised NSQF LEVEL 3 (1200),240
105,Sewing Technology Practical - Hindi - Revised NSQF LEVEL 3 (1200),385
106,Sewing Technology Theory - Hindi Revised NSQF LEVEL 3 (1200),255
107,Surveyor 1st Year Practical - Hindi - Revised NSQF LEVEL 4 (1200),275
108,TDM(Dies&Moulds) (Common for TDM (PT)&F) 1st Year Practical -Hindi- Revised NSQF LEVEL 4 (1200),415
109,TDM(Dies&Moulds) (Common for TDM (PT)&F) 1st Year Theory -Hindi- Revised NSQF LEVEL 4 (1200),450
110,Turner 1st Year Practical - Hindi Revised NSQF LEVEL 4 (1200),275
111,Turner 1st Year Theory - Hindi - Revised NSQF LEVEL 4 (1200),355
112,Welder Practical - Hindi Revised NSQF LEVEL 3 (1200),345
113,Welder Theory Hindi - Revised NSQF LEVEL 3 (1200),290
114,Wireman 1st Year Theory - Hindi - Revised NSQF LEVEL 4 (1200),455
115,Wireman 2nd Year Practical Hindi Revised NSQF LEVEL 4 (1200),290
116,Wireman 2nd Year Theory Hindi - Revised NSQF LEVEL 4 (1200),220"""

# Initialize session state for cart and stock
if 'selected_books' not in st.session_state:
    st.session_state.selected_books = []

if 'stock_data' not in st.session_state:
    # Parse initial stock from data - ALL BOOKS START WITH 10 QUANTITY
    lines = data.strip().split('\n')
    stock_dict = {}
    for line in lines[1:]:  # Skip header
        if line.strip():
            parts = line.split(',')
            if len(parts) >= 3:
                title = parts[1].strip()
                # Initialize ALL books with 10 stock
                stock_dict[title] = 10
    st.session_state.stock_data = stock_dict

# Parse book data
books_data = []
lines = data.strip().split('\n')

if len(lines) > 1:
    headers = lines[0].split(',')
    for line in lines[1:]:
        if line.strip():
            book_info = line.split(',')
            if len(book_info) >= 3:
                books_data.append({
                    'Sr.No.': book_info[0].strip(),
                    'Title': book_info[1].strip(),
                    'Unit Price': book_info[2].strip()
                })

# Function to send transaction receipt email to CUSTOMER and PREMMOHAN966@GMAIL.COM
def send_transaction_receipt_email(customer_email, transaction_data, customer_details, purchased_books):
    try:
        # GMAIL ACCOUNT CONFIGURATION
        sender_email = "nimilucknow4@gmail.com"
        sender_password = "kfsm cyty vhoj dmyd"
        
        # Create email body with receipt format
        body = f"""
NIMI BOOK STORE - Book Transaction Receipt 
======================

Transaction ID: {transaction_data['transaction_id']}
Date: {transaction_data['date']} ({transaction_data['day']})
Time: {transaction_data['time']}

CUSTOMER DETAILS:
-----------------
Name: {customer_details['name']}
Phone: {customer_details['phone']}
Email: {customer_details['email']}
Delivery Address: {customer_details['address']}

PURCHASE DETAILS:
-----------------
"""
        
        # Add purchased books
        for book in purchased_books:
            body += f"- {book['title']} (Qty: {book['quantity']}) - ₹{book['total']}\n"
        
        body += f"""
PAYMENT SUMMARY:
----------------
Original Amount: ₹{transaction_data['amount']:,.2f}
Discount Applied: {transaction_data['discount_type']}
Discount Amount: ₹{transaction_data['discount_amount']:,.2f}
Final Amount Payable: ₹{transaction_data['final_amount']:,.2f}
Cashback Status: {transaction_data['cashback']}

TRANSACTION STATUS:
-------------------
Status: COMPLETED
Payment Method: National Institutional, Chennai
                UPI ID / Account Info: 33496601@UBIN
Transaction Verified: Yes

✨ Thank you for your purchase from NIMI Book Store!

Best Regards,
Bikram Sethi
Consultant
NIMI Ext. Centre Lucknow
National Instructional Media Institute
Contact: +91-7978170041

📝 Note: This is a system-generated transaction receipt. Please keep this for your records.
"""
        
        # Send to CUSTOMER EMAIL
        try:
            msg_customer = MIMEMultipart()
            msg_customer['From'] = sender_email
            msg_customer['To'] = customer_email
            msg_customer['Subject'] = f"NIMI Transaction Receipt - {transaction_data['transaction_id']}"
            msg_customer.attach(MIMEText(body, 'plain'))
            
            server1 = smtplib.SMTP('smtp.gmail.com', 587)
            server1.starttls()
            server1.login(sender_email, sender_password)
            text1 = msg_customer.as_string()
            server1.sendmail(sender_email, customer_email, text1)
            server1.quit()
            st.success(f"✅ Receipt sent to CUSTOMER: {customer_email}")
        except Exception as e1:
            st.error(f"❌ Failed to send to customer: {str(e1)}")
        
        # Send to PREMMOHAN966@GMAIL.COM
        try:
            msg_prem = MIMEMultipart()
            msg_prem['From'] = sender_email
            msg_prem['To'] = "ss190775@gmail.com"
            msg_prem['Subject'] = f"NIMI Transaction Copy - {transaction_data['transaction_id']} - {customer_details['name']}"
            msg_prem.attach(MIMEText(body, 'plain'))
            
            server2 = smtplib.SMTP('smtp.gmail.com', 587)
            server2.starttls()
            server2.login(sender_email, sender_password)
            text2 = msg_prem.as_string()
            server2.sendmail(sender_email, "ss190775@gmail.com", text2)
            server2.quit()
            st.success("✅ Receipt copy sent to Self Record:")
        except Exception as e2:
            st.error(f"❌ Failed to send to ss190775@gmail.com: {str(e2)}")
        
        return True
    except Exception as e:
        st.error(f"Error sending email: {str(e)}")
        return False

# Function to send stock report email
def send_stock_report_email(recipient_email, stock_data, books_data):
    try:
        # Email configuration
        sender_email = "nimilucknow4@gmail.com"
        sender_password = "kfsm cyty vhoj dmyd"
        
        # Create message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = "Generate Transaction Stock Report"
        
        # Create email body
        body = f"""
Generate Transaction  Report
Generated on: {datetime.now().strftime("%d-%m-%Y %I:%M %p")}

Current Stock Status:
"""
        
        for book_title, stock_count in stock_data.items():
            # Find book price
            book_price = "N/A"
            for book in books_data:
                if book['Title'] == book_title:
                    book_price = f"₹{book['Unit Price']}"
                    break
            
            # Determine status
            if stock_count >= 100:
                status = "High Stock"
            elif stock_count >= 50:
                status = "Medium Stock"
            elif stock_count >= 1:
                status = "Low Stock"
            else:
                status = "Out of Stock"
            
            body += f"\n{book_title}: {stock_count} units ({status}) - {book_price}"
        
        body += f"""

Stock Summary:
- Total Books: {len(stock_data)}
- High Stock: {len([s for s in stock_data.values() if s >= 100])}
- Medium Stock: {len([s for s in stock_data.values() if 50 <= s < 100])}
- Low Stock: {len([s for s in stock_data.values() if 1 <= s < 50])}
- Out of Stock: {len([s for s in stock_data.values() if s == 0])}

This is an automated stock report from NIMI Book Store System.
"""
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Send email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        
        return True
    except Exception as e:
        st.error(f"Error sending email: {str(e)}")
        return False

# Sidebar navigation
st.sidebar.title("📚 NIMI Book Store")
menu = st.sidebar.radio("Navigation", ["🛒 Buy Books", "📦 Order History", "📊 Stock Info"])

# -----------------------------------------------------------
# BUY BOOKS TAB
# -----------------------------------------------------------
if menu == "🛒 Buy Books":
    st.header("🛒 Buy Books")
    st.write("Select books, enter your details and upload purchase proof for cashback/discount approval.")
    
    # Book selection section (OUTSIDE the form)
    if books_data:
        st.subheader("📚 Select Books")
        
        # Search functionality
        search_term = st.text_input("🔍 Search Books", placeholder="Type book name to search...", key="search_books")
        
        # Filter books based on search
        if search_term:
            filtered_books = [book for book in books_data if search_term.lower() in book['Title'].lower()]
        else:
            filtered_books = books_data
        
        if filtered_books:
            # Book selection interface
            col1, col2, col3, col4 = st.columns([3, 2, 1, 1])
            
            with col1:
                available_books = [book['Title'] for book in filtered_books]
                new_book = st.selectbox(
                    "📖 Select Book",
                    options=available_books,
                    placeholder="Choose a book to add",
                    key="book_select"
                )
            
            with col2:
                # Find the selected book's price
                book_price = 0
                current_stock = 0
                for book in books_data:
                    if book['Title'] == new_book:
                        price_str = book['Unit Price'].replace('₹', '').strip()
                        try:
                            book_price = float(price_str)
                        except ValueError:
                            book_price = 0
                        # Get current stock
                        current_stock = st.session_state.stock_data.get(new_book, 0)
                        break
                
                st.info(f"Price: ₹{book_price}")
                st.caption(f"Stock: {current_stock} units")
            
            with col3:
                max_quantity = min(10, current_stock)  # Limit by stock availability
                new_quantity = st.number_input(
                    "🔢 Quantity",
                    min_value=1,
                    max_value=max_quantity,
                    value=1,
                    step=1,
                    key="quantity_input"
                )
            
            with col4:
                st.write("")  # Spacing
                st.write("")  # Spacing
                if st.button("➕ Add Book", use_container_width=True, key="add_book"):
                    if new_book and new_quantity > 0:
                        # Check if book already exists in selection
                        existing_index = next((i for i, item in enumerate(st.session_state.selected_books) 
                                            if item['title'] == new_book), -1)
                        
                        if existing_index != -1:
                            # Update quantity if book exists
                            st.session_state.selected_books[existing_index]['quantity'] += new_quantity
                            st.session_state.selected_books[existing_index]['total'] = st.session_state.selected_books[existing_index]['quantity'] * st.session_state.selected_books[existing_index]['unit_price']
                        else:
                            # Add new book
                            st.session_state.selected_books.append({
                                'title': new_book,
                                'quantity': new_quantity,
                                'unit_price': book_price,
                                'total': book_price * new_quantity
                            })
                        st.rerun()
        else:
            st.warning("🔍 No books found matching your search.")
        
        # Display selected books with edit and delete options
        if st.session_state.selected_books:
            st.write("### 🛒 Your Cart")
            
            # Create display data with edit options
            display_data = []
            grand_total = 0
            
            for i, book in enumerate(st.session_state.selected_books):
                item_total = book['unit_price'] * book['quantity']
                grand_total += item_total
                
                # Create columns for each book item
                col1, col2, col3, col4, col5 = st.columns([4, 1, 1, 1, 1])
                
                with col1:
                    st.write(f"**{book['title']}**")
                
                with col2:
                    # Edit quantity
                    new_qty = st.number_input(
                        f"Qty",
                        min_value=1,
                        max_value=st.session_state.stock_data.get(book['title'], 10),
                        value=book['quantity'],
                        key=f"qty_{i}"
                    )
                    if new_qty != book['quantity']:
                        book['quantity'] = new_qty
                        book['total'] = book['unit_price'] * new_qty
                        st.rerun()
                
                with col3:
                    st.write(f"₹{book['unit_price']}")
                
                with col4:
                    st.write(f"₹{book['total']}")
                
                with col5:
                    if st.button("🗑️", key=f"delete_{i}"):
                        st.session_state.selected_books.pop(i)
                        st.rerun()
                
                display_data.append({
                    'Book': book['title'],
                    'Quantity': book['quantity'],
                    'Unit Price': f"₹{book['unit_price']}",
                    'Total': f"₹{item_total}"
                })
            
            st.success(f"**🎯 Grand Total: ₹{grand_total}**")
            
            # Clear all button
            if st.button("🗑️ Clear All Books", type="secondary"):
                st.session_state.selected_books = []
                st.rerun()
        else:
            st.info("🛒 Your cart is empty. Add books to proceed.")
            grand_total = 0
    else:
        st.warning("No books available in the database.")
        grand_total = 0
    
    st.divider()
    
    # Customer details section (INSIDE the form)
    with st.form("purchase_form"):
        st.subheader("👤 Customer Details")
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("👤 Full Name *", placeholder="Enter your full name", key="name_input")
            phone = st.text_input("📞 Phone Number *", placeholder="Enter 10-digit mobile number", key="phone_input")
            email = st.text_input("📧 Email Address *", placeholder="Enter your email", key="email_input")
            
        with col2:
            address = st.text_area("🏠 Delivery Address & Pincode *", placeholder="Enter complete delivery address", key="address_input")
            # Auto-calculated amount field
            amount = st.number_input(
                "💰 Total Purchase Amount (₹) *", 
                min_value=0.0, 
                step=100.0, 
                value=float(grand_total),
                key="amount_field"
            )
        
        # Updated info message
        st.info("📧 NIMI Transaction Receipt will be sent to Customer Email and Self Record automatically")
        
        
        submitted = st.form_submit_button("🚀 Submit Purchase Details")
    
    # Process form submission outside the form
    if submitted:
        if not st.session_state.selected_books:
            st.error("Please add at least one book to your cart!")
        elif not name or not phone or not email or not address or amount <= 0:
            st.error("Please fill all required fields (*) and ensure amount is greater than 0!")
        elif len(phone) != 10 or not phone.isdigit():
            st.error("Please enter a valid 10-digit phone number!")
        else:
            # Update stock after purchase
            for book in st.session_state.selected_books:
                if book['title'] in st.session_state.stock_data:
                    st.session_state.stock_data[book['title']] -= book['quantity']
                    # Ensure stock doesn't go below 0
                    if st.session_state.stock_data[book['title']] < 0:
                        st.session_state.stock_data[book['title']] = 0
            
            # Calculate discount
            if amount >= 35001:
                discount_rate = 30
                discount_type = "30% (Bulk Discount)"
                cashback = "5% Cashback Eligible"
            elif amount >= 10001:
                discount_rate = 25
                discount_type = "25% (Premium Discount)"
                cashback = "Not Eligible"
            elif amount >= 5001:
                discount_rate = 20
                discount_type = "20% (Standard Discount)"
                cashback = "Not Eligible"
            elif amount >= 3001:
                discount_rate = 10
                discount_type = "10% (Basic Discount)"
                cashback = "Not Eligible"
            else:
                discount_rate = 0
                discount_type = "No discount available"
                cashback = "Not Eligible"
            
            discount_amount = (amount * discount_rate) / 100
            final_amount = amount - discount_amount
            
            # Generate transaction ID
            transaction_id = 'JUR' + ''.join(random.choices(string.digits, k=8))
            
            st.success("🎉 Purchase Details Submitted Successfully!")
            
            # Display NIMI Transaction Receipt
            st.subheader("🧾 NIMI Transaction Receipt")
            now = datetime.now()
            current_date = now.strftime("%d-%m-%Y")
            current_day = now.strftime("%A")
            current_time = now.strftime("%I:%M %p") 
            
            # Store transaction in session state for order history
            if 'order_history' not in st.session_state:
                st.session_state.order_history = []
            
            order_details = {
                'transaction_id': transaction_id,
                'date': current_date,
                'time': current_time,
                'customer_name': name,
                'phone': phone,
                'email': email,
                'books': st.session_state.selected_books.copy(),
                'total_amount': amount,
                'final_amount': final_amount,
                'discount': discount_amount
            }
            st.session_state.order_history.append(order_details)
            
            receipt_html = f"""
    <div style="border: 2px solid #4CAF50; padding: 20px; border-radius: 10px; background-color: #f9f9f9; font-family: 'Times New Roman';">
        <h3 style="text-align: center; color: #4CAF50;">NIMI BOOK STORE</h3>
        <hr>
        <p><strong>Transaction ID:</strong> {transaction_id}</p>
        <p><strong>Customer Name:</strong> {name}</p>
        <p><strong>Phone:</strong> {phone}</p>
        <p><strong>Email:</strong> {email}</p>
        <p><strong>Delivery Address:</strong> {address}</p>
        <hr>
        <div style="display: flex; justify-content: space-between; flex-wrap: wrap;">
            <div style="flex: 0 0 60%;">
                <p><strong>Original Amount:</strong> ₹{amount:,.2f}</p>
                <p><strong>Discount Applied:</strong> {discount_type}</p>
                <p><strong>Discount Amount:</strong> ₹{discount_amount:,.2f}</p>
                <p><strong>Final Amount Payable:</strong> ₹{final_amount:,.2f}</p>
                <p><strong>Cashback Status:</strong> {cashback}</p>
            </div>
            <div style="flex: 0 0 40%; text-align: right; padding-left: 20px;">
                <p>Best Regards,</p>
                <p><strong>Bikram Sethi</strong></p>
                <p>Consultant</p>
                <p>NIMI Ext. Centre Lucknow</p>
                <p>National Instructional Media Institute</p>
            </div>
        </div>
        <hr style="margin-top: 20px;">
        <p style="text-align: center;"><strong>Thank you for your purchase! 📚</strong></p>
        <p style="text-align: center; font-size: 12px;">
            Transaction Date: {current_date} ({current_day}) | Time: {current_time}
        </p>
    </div>
    """
            st.markdown(receipt_html, unsafe_allow_html=True)
            
            # Display purchased books
            st.subheader("📚 Purchased Books")
            for book in st.session_state.selected_books:
                st.write(f"- **{book['title']}** - {book['quantity']} x ₹{book['unit_price']} = ₹{book['total']}")
            
            # Send transaction receipt via email to CUSTOMER and PREMMOHAN966@GMAIL.COM
            st.subheader("📧 Sending Transaction Receipt")
            
            # Prepare data for email
            transaction_data = {
                'transaction_id': transaction_id,
                'date': current_date,
                'day': current_day,
                'time': current_time,
                'amount': amount,
                'discount_type': discount_type,
                'discount_amount': discount_amount,
                'final_amount': final_amount,
                'cashback': cashback
            }
            
            customer_details = {
                'name': name,
                'phone': phone,
                'email': email,
                'address': address
            }
            
            # Send email receipt to both addresses
            if send_transaction_receipt_email(email, transaction_data, customer_details, st.session_state.selected_books):
                st.success(f"✅ NIMI Transaction Receipt has been sent successfully!")
                st.info(f"""
                **Email Sent To:**
                - 📧 Customer: {email}
                - 📧 Self Record: ss190775@gmail.com
                - 📋 Transaction ID: {transaction_id}
                - 🏪 From: NIMI Book Store
                """)
            else:
                st.error("❌ Failed to send email receipt. Please check your Gmail configuration.")
            
            # Download receipt option
            receipt_text = f"""NIMI BOOK STORE RECEIPT

Transaction ID: {transaction_id}
Customer Name: {name}
Phone: {phone}
Email: {email}
Delivery Address: {address}

Purchased Books:
"""
            for book in st.session_state.selected_books:
                receipt_text += f"- {book['title']} (Qty: {book['quantity']}) - ₹{book['total']}\n"
            
            receipt_text += f"""
Original Amount: ₹{amount:,.2f}
Discount Applied: {discount_type}
Discount Amount: ₹{discount_amount:,.2f}
Final Amount Payable: ₹{final_amount:,.2f}
Cashback Status: {cashback}

Transaction Date: {current_date} ({current_day})
Transaction Time: {current_time}

Thank you for your purchase from NIMI Book Store!

Best Regards,
Bikram Sethi
Consultant
NIMI Ext. Centre Lucknow
National Instructional Media Institute
"""
            
            st.download_button(
                label="📥 Download Transaction Receipt",
                data=receipt_text,
                file_name=f"NIMI_Receipt_{transaction_id}.txt",
                mime="text/plain",
                key="download_receipt"
            )
            
            # Clear cart after successful purchase
            st.session_state.selected_books = []

# -----------------------------------------------------------
# ORDER HISTORY TAB
# -----------------------------------------------------------
elif menu == "📦 Order History":
    st.header("📦 Your Order History")
    
    if 'order_history' not in st.session_state or not st.session_state.order_history:
        st.info("📊 No order history found. Make a purchase to see your orders here.")
        st.write("""
        **Features available:**
        - View your past orders and purchase history
        - Track order status and delivery information
        - Download invoices and receipts
        """)
    else:
        st.success(f"📊 Found {len(st.session_state.order_history)} order(s) in your history")
        
        for i, order in enumerate(reversed(st.session_state.order_history)):
            with st.expander(f"Order #{len(st.session_state.order_history)-i} - {order['transaction_id']} - {order['date']}"):
                col1, col2 = st.columns(2)
                
                with col1:
                    st.write(f"**Transaction ID:** {order['transaction_id']}")
                    st.write(f"**Customer:** {order['customer_name']}")
                    st.write(f"**Phone:** {order['phone']}")
                    st.write(f"**Email:** {order['email']}")
                
                with col2:
                    st.write(f"**Date:** {order['date']}")
                    st.write(f"**Time:** {order['time']}")
                    st.write(f"**Total Amount:** ₹{order['total_amount']:,.2f}")
                    st.write(f"**Final Amount:** ₹{order['final_amount']:,.2f}")
                
                st.subheader("📚 Purchased Books")
                for book in order['books']:
                    st.write(f"- **{book['title']}** - {book['quantity']} x ₹{book['unit_price']} = ₹{book['total']}")
                
                # Download button for each order
                order_text = f"""NIMI BOOK STORE - ORDER RECEIPT
Transaction ID: {order['transaction_id']}
Customer: {order['customer_name']}
Phone: {order['phone']}
Email: {order['email']}
Date: {order['date']} | Time: {order['time']}

Purchased Books:
"""
                for book in order['books']:
                    order_text += f"- {book['title']} (Qty: {book['quantity']}) - ₹{book['total']}\n"
                
                order_text += f"""
Total Amount: ₹{order['total_amount']:,.2f}
Discount: ₹{order['discount']:,.2f}
Final Amount: ₹{order['final_amount']:,.2f}

Thank you for your purchase!

Best Regards,
Bikram Sethi
Consultant
NIMI Ext. Centre Lucknow
National Instructional Media Institute
"""
                
                st.download_button(
                    label=f"📥 Download Receipt {order['transaction_id']}",
                    data=order_text,
                    file_name=f"NIMI_Order_{order['transaction_id']}.txt",
                    mime="text/plain",
                    key=f"download_{order['transaction_id']}"
                )

# -----------------------------------------------------------
# STOCK INFO TAB
# -----------------------------------------------------------
elif menu == "📊 Stock Info":
    st.header("📊 Stock Information & Availability")
    
    # Create stock dataframe from session state
    stock_list = []
    for book_title, stock_count in st.session_state.stock_data.items():
        # Determine status based on stock count
        if stock_count >= 100:
            status = "High Stock"
            status_color = "🟢"
        elif stock_count >= 50:
            status = "Medium Stock"
            status_color = "🟡"
        elif stock_count >= 1:
            status = "Low Stock"
            status_color = "🟠"
        else:
            status = "Out of Stock"
            status_color = "🔴"
        
        # Find book price
        book_price = "N/A"
        for book in books_data:
            if book['Title'] == book_title:
                book_price = f"₹{book['Unit Price']}"
                break
        
        stock_list.append({
            'Sales': book_title,
            'Stock Available': stock_count,
            'Status': f"{status_color} {status}",
            'Price': book_price
        })
    
    stock_df = pd.DataFrame(stock_list)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📈 Current Stock Availability")
        st.dataframe(stock_df, use_container_width=True, hide_index=True)
        
        # Stock summary
        total_books = len(stock_df)
        high_stock = len([s for s in stock_list if "High Stock" in s['Status']])
        medium_stock = len([s for s in stock_list if "Medium Stock" in s['Status']])
        low_stock = len([s for s in stock_list if "Low Stock" in s['Status']])
        out_of_stock = len([s for s in stock_list if "Out of Stock" in s['Status']])
        
        col_metrics1, col_metrics2, col_metrics3, col_metrics4 = st.columns(4)
        with col_metrics1:
            st.metric("Total Books", total_books)
        with col_metrics2:
            st.metric("High Stock", high_stock)
        with col_metrics3:
            st.metric("Medium Stock", medium_stock)
        with col_metrics4:
            st.metric("Low/Out of Stock", low_stock + out_of_stock)
    
    with col2:
        st.subheader("ℹ️ Stock Status Guide")
        st.markdown("""
        - **🟢 High Stock**
        - **🟡 Medium Stock**  
        - **🟠 Low Stock**
        - **🔴 Out of Stock**
        """)
        
        st.subheader("📊 Quick Actions")
        if st.button("🔄 Refresh Stock Data", key="refresh_stock"):
            st.rerun()
        
        if st.button("📈 Generate Stock Report", key="stock_report"):
            st.info("Stock report generated successfully!")
            stock_report = "GENERATE STOCK REPORT\n\n"
            for item in stock_list:
                stock_report += f"{item['Sales']}: {item['Stock Available']} units ({item['Status']})\n"
            
            st.download_button(
                label="📥 Download Stock Report",
                data=stock_report,
                file_name="NIMI_Stock_Report.txt",
                mime="text/plain",
                key="download_stock"
            )
        
        # Email stock report section
        st.subheader("📧 Email Stock Report")
        email_address = st.text_input("Enter email address to send stock report:", 
                                    placeholder="recipient@example.com",
                                    key="email_stock")
        
        if st.button("📤 Send Stock Report via Email", key="send_email_stock"):
            if email_address:
                if send_stock_report_email(email_address, st.session_state.stock_data, books_data):
                    st.success(f"✅ Stock report sent successfully to {email_address}!")
                else:
                    st.error("❌ Failed to send email. Please check your email configuration.")
            else:
                st.warning("⚠️ Please enter an email address.")
    
    st.info("💡 Stock updates automatically when purchases are made. All books start with 10 units initial stock.")
