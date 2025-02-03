from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import *
from django.http import JsonResponse
from django.utils.timezone import localtime

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from django.utils.timesince import timesince
from datetime import datetime
from reportlab.lib.units import inch
from reportlab.lib.colors import blue, gray, whitesmoke,white,black,skyblue
# PDF
def equipment_pdf(request, pk):
    # Get the specific Equipment item
    equipment = get_object_or_404(Equipment, id=pk)

    # Create an HTTP response with a PDF content type
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="equipment_{equipment.id}.pdf"'

    # Create a PDF document
    pdf = SimpleDocTemplate(response, pagesize=letter)
    elements = []  # List to hold elements for the PDF

    # Table data (headers + values)
    table_data = [
        ["Field", "Value"],  # Table Header
        ["Property Number", str(equipment.property_num)],
        ["Article Item", equipment.article_item],
        ["Description", equipment.description],
        ["Person Accountable", equipment.person_accountable],
        ["Cost", f"${equipment.cost:.2f}"],
        ["Remarks", equipment.remarks],
        ["Date Saved", equipment.date_save.strftime('%Y-%m-%d %H:%M:%S')],
        ["Last Updated", equipment.time_stamp.strftime('%Y-%m-%d %H:%M:%S')],
    ]

    # Create a table
    table = Table(table_data, colWidths=[150, 300])  # Adjust column widths

    # Add styling to the table
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Header background color
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Header text color
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),  # Align text to left
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Header font bold
        ('FONTSIZE', (0, 0), (-1, -1), 12),  # Font size
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),  # Padding for header
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),  # Background color for other rows
        ('GRID', (0, 0), (-1, -1), 1, colors.black)  # Grid lines
    ])

    table.setStyle(style)

    # Add the table to the elements list
    elements.append(table)

    # Build the PDF
    pdf.build(elements)

    return response 

def generate_repair_request_pdf(request):



        

       
    buf = io.BytesIO()
    c = canvas.Canvas(buf)
    response = HttpResponse(content_type='application/pdf')
    c.setTitle("SERVICE REQUEST")
    c.setPageSize((8.27*inch, 11.69*inch))
#Header

    c.setFont("Times-Bold", 15, leading=None)
    c.setFillColor("green")
    c.drawString(2.4*inch, 11.34*inch, "Bicol Region General Hospital and Geriatric Medical Center")
    c.setFont("Times-Roman", 11, leading=None)
    c.setFillColor("black")
    c.drawString(3.8*inch, 11.14*inch, "San Pedro, Cabusao Camarines Sur")
    c.drawString(3*inch, 10.99*inch, "Telephone Nos.: (054) 473-2244, 472-4422, 881-1033, 881-1761")
    c.drawString(3.1*inch, 10.85*inch, "E-mail Address:")
    c.setFillColor("Blue")
    c.drawString(4.2*inch, 10.85*inch, "bicolsan@gmail.com, brghgmc@gmail.com")
    c.drawString(4.1*inch, 10.66*inch, "Website: brghgmc.doh.gov.ph")
    c.setStrokeColorRGB(0, 0, 1, alpha=0.4)  # Blue color
    c.setLineWidth(2)
    c.line(0*inch,10.55*inch,9*inch,10.55*inch)

#Body
    c.setFillColor("black")
    c.setFont("Times-Bold", 12, leading=None)
    c.drawString(3*inch, 10*inch, "IMIS SERVICE REQUEST FORM")
    
    c.setFillColor("black")
    c.setFont("Times-Roman", 10, leading=None)
    c.drawString(0.9*inch, 9.5*inch, "From: _________________________________________" )
    c.drawString(1.5*inch, 9.52*inch, "office" )
    c.drawString(4.46*inch, 9.5*inch, "Date: _______________________________" )
    c.drawString(5.3*inch, 9.52*inch, "date" )
    c.drawString(0.5*inch, 9*inch, "Kind of Work:" )
    c.drawString(0.7*inch, 8.75*inch, "_______________________________________" )
    c.drawString(1.7*inch, 8.75*inch, "kind_of_work" )
    c.drawString(1.3*inch, 8.80*inch, "Repair" )
    c.drawString(1.3*inch, 8.60*inch, "Layout Design" )
    c.drawString(1.3*inch, 8.40*inch, "Equipment Setup" )
    c.drawString(1.3*inch, 8.20*inch, "Data Entry" )
    c.drawString(1.3*inch, 8*inch, "Software Development" )
    c.drawString(3.2*inch, 8.80*inch, "Replacement" )
    c.drawString(3.2*inch, 8.60*inch, "Installation" )
    c.drawString(3.2*inch, 8.40*inch, "Technical Assistance" )
    c.drawString(3.2*inch, 8.20*inch, "Others" )

    c.drawString(4.5*inch, 9*inch, "Nature of Work and Site of Request:" )
    text_object = c.beginText(4.7*inch, 8.77*inch) 
    text_object.setFont("Times-Roman", 9)
   
        
    c.drawText(text_object)
    c.drawString(4.65*inch, 8.75*inch, "_______________________________________" )
    c.drawString(4.65*inch, 8.60*inch, "_______________________________________" )
    c.drawString(4.65*inch, 8.4832*inch, "_______________________________________" )
    c.drawString(0.5*inch, 7.5*inch, "Requested by: ________________________________" )
    c.drawString(1.8*inch, 7.5*inch, "first_name" )
    c.drawString(2.19*inch, 7.5*inch, "last_name" )
    c.drawString(4*inch, 7.5*inch, "Received by: _________________________________" )
    c.drawString(5*inch, 7.5*inch, "staff_fullname" )

    c.drawString(0*inch, 7*inch, "-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------" )
    c.setFillColor("black")
    c.setFont("Times-Bold", 10, leading=None)
    c.drawString(0.5*inch, 6.7*inch, "ASSESSMENT: " )
    c.setFillColor("black")
    c.setFont("Times-Roman", 10, leading=None)
    c.drawString(1.50*inch, 6.7*inch, "(Assessment of Project)" )
    c.drawString(0.65*inch, 6.4*inch, "Recommendation:" )
    c.setFont("Times-Bold", 10, leading=None)
    c.drawString(2.3*inch, 6.4*inch, "prerepair_inspection" )
    # c.drawString(2.3*inch, 6.2*inch, "Out-Source _______________________________________________________________________" )
    c.setFont("Times-Roman", 10, leading=None)
    c.drawString(0.5*inch, 5.8*inch, "Assessed by: ________________________________" )
    c.drawString(1.6*inch, 5.8*inch, "staff_fullname" )
    c.drawString(4*inch, 5.8*inch, "Noted by: _________________________________" )
    c.drawString(2.50*inch, 5.4*inch, " Approved by: _________________________________" )

#Box stroke
    c.setStrokeColorRGB(0, 0, 0)
    c.setLineWidth(1)
    c.setFillColor(white)#1
    c.rect(1.12*inch,8.80*inch,0.11*inch,0.11*inch,fill=1)
    c.setStrokeColorRGB(0, 0, 0)
    c.setLineWidth(1)
    c.setFillColor(white)#2
    c.rect(1.12*inch,8.60*inch,0.11*inch,0.11*inch,fill=1)
    c.setStrokeColorRGB(0, 0, 0)
    c.setLineWidth(1)
    c.setFillColor(white)#3
    c.rect(1.12*inch,8.40*inch,0.11*inch,0.11*inch,fill=1)
    c.setStrokeColorRGB(0, 0, 0)
    c.setLineWidth(1)
    c.setFillColor(white)#4
    c.rect(1.12*inch,8.20*inch,0.11*inch,0.11*inch,fill=1)
    c.setStrokeColorRGB(0, 0, 0)
    c.setLineWidth(1)
    c.setFillColor(white)#5
    c.rect(1.12*inch,8*inch,0.11*inch,0.11*inch,fill=1)
    c.setStrokeColorRGB(0, 0, 0)
    c.setLineWidth(1)
    c.setFillColor(white)#6
    c.rect(3*inch,8.80*inch,0.11*inch,0.11*inch,fill=1)
    c.setStrokeColorRGB(0, 0, 0)
    c.setLineWidth(1)
    c.setFillColor(white)#7
    c.rect(3*inch,8.60*inch,0.11*inch,0.11*inch,fill=1)
    c.setStrokeColorRGB(0, 0, 0)
    c.setLineWidth(1)
    c.setFillColor(white)#8
    c.rect(3*inch,8.40*inch,0.11*inch,0.11*inch,fill=1)
    c.setStrokeColorRGB(0, 0, 0)
    c.setLineWidth(1)
    c.setFillColor(white)#9
    c.rect(3*inch,8.20*inch,0.11*inch,0.11*inch,fill=1)
    c.setStrokeColorRGB(255, 0, 0)
    c.setLineWidth(1)
    c.setFillColor(white)#9
    c.rect(2.1*inch, 6.4*inch,0.11*inch,0.11*inch,fill=1)
    c.setStrokeColorRGB(255, 0, 0)
    c.setLineWidth(1)
    c.setFillColor(white)#9
    c.rect(2.1*inch, 6.2*inch,0.11*inch,0.11*inch,fill=1)

    
    c.setFillColor("black")
    c.setFont("Times-Bold", 11, leading=None)
    c.drawString(0*inch, 5.1*inch, "_____________________________________________________________________________________________________________________________________________" )
    c.drawString(2.45*inch, 4.85*inch, "Medical Center Chief I/Authorized Representative" )
    c.drawString(0*inch, 4.8*inch, "_____________________________________________________________________________________________________________________________________________" )




    
#table
    c.setStrokeColorRGB(0, 0, 0)
    c.setLineWidth(1)
    c.setFillColor(white)
    c.rect(0.9*inch, 4.29*inch, 6.417322*inch, 0.20*inch, fill=1)
    c.setFillColor(black) 
    c.drawString(0.95*inch, 4.33*inch, "ACTION TAKEN:")
    c.setFont("Times-Roman", 10, leading=None)
    c.drawString(2.3*inch, 4.34*inch, "(Use separate sheet if necessary)" )

    text_object = c.beginText(1.2*inch, 4*inch)
    text_object.setFont("Times-Roman", 10)
    text_object.setLeading(12)
#date
    c.setStrokeColorRGB(0, 0, 0)
    c.setLineWidth(1)
    c.setFillColor(white)
    c.rect(0.9*inch,2*inch,6.417322*inch,2.3*inch,fill=1)
    c.setFillColor(black) 
    c.drawText(text_object)
#time
    c.setStrokeColorRGB(0, 0, 0)
    c.setLineWidth(1)
    c.setFillColor(white)
    c.rect(1.50*inch,1.86*inch,.75*inch,2.43*inch,fill=1)
#action taken
    c.setStrokeColorRGB(0, 0, 0)
    c.setLineWidth(1)
    c.setFillColor(white)
    c.rect(2.25*inch,1.86*inch,2*inch,2.43*inch,fill=1)
#action officer
    c.setStrokeColorRGB(0, 0, 0)
    c.setLineWidth(1)
    c.setFillColor(white)
    c.rect(4.25*inch,1.86*inch,2*inch,2.43*inch,fill=1)
#signiture
    c.setStrokeColorRGB(0, 0, 0)
    c.setLineWidth(1)
    c.setFillColor(white)
    c.rect(6.25*inch,1.86*inch,1.25*inch,2.43*inch,fill=1)

#inspection 
    c.setFillColor("black")
    c.setFont("Times-Bold", 11, leading=None)
    c.drawString(.75*inch,1.60*inch, "INSPECTION: " )
    c.setFillColor("black")
    c.setFont("Times-Bold", 10, leading=None)
    c.drawString(1.80*inch,1.60*inch, "(Inspection of the Project)" )
    c.drawString(4*inch,1.60*inch, "Date: ____________________________________" )
    c.drawString(2.3*inch, 1.30*inch, "status" )
    c.drawString(2.3*inch, 1.10*inch, "Not Completed" )
    c.setStrokeColorRGB(255, 0, 0)
    c.setLineWidth(1)
    c.setFillColor(blue)
    c.rect(2.1*inch, 1.30*inch,0.1*inch,0.1*inch,fill=1)

    c.setStrokeColorRGB(0, 0, 0)
    c.setLineWidth(1)
    c.setFillColor(white)
    c.rect(2.1*inch, 1.10*inch,0.11*inch,0.11*inch,fill=1)
    
    c.setFillColor("black")
    c.setFont("Times-Roman", 10, leading=None)
    c.drawString(.50*inch,.8*inch, "Inspected by: ________________________________________        Received by: ______________________________" )
    c.drawString(2.2*inch, .8*inch, "staff_fullname")
    
#footer
    c.setStrokeColorRGB(0, 0, 1, alpha=0.4) # Blue color
    c.setLineWidth(2)
    c.line(0*inch,.6*inch,9*inch,.6*inch)
    c.setFillColor("black")
    c.setFont("Times-Roman", 10, leading=None)
    c.drawString(0.25*inch, .4*inch, "BRGHGMC-F-HOPSS-IMIS-013                      Rev .0             Effectivity Date: " )
    c.drawString(4.7*inch, .4*inch, "Duration" )
  
    
    

    c.showPage()
    c.save()
    pdf = buf.getvalue()
    buf.close()
    response.write(pdf)
    return response

@login_required(login_url="user_login")
@admin_only
def admin_page(request):
    user_list = User.objects.all()

    return render(request, 'base/admin/home.html', {'user_list':user_list})

@allowed_users(allowed_roles="employee")
def employee_page(request):
    return render(request, 'base/employee/home.html')

@login_required(login_url="user_login")
def item_list(request):
    items = Equipment.objects.all().order_by('-time_stamp')
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfuly Save')
            return redirect('item_list')
        
    context = {
        'form':form,
        'items':items
    }
    return render(request, 'base/items.html', context)

def edit_item(request, pk):
    item = get_object_or_404(Equipment, id=pk)

    if request.method == 'POST':
        edit_form = ItemForm(request.POST, instance=item)
        if edit_form.is_valid():
            edit_form.save()
            return JsonResponse({"success": True}, status=200)

    return JsonResponse({"success": False}, status=400)

def add_item(request):
    if request.method == "POST":
        property_num = request.POST.get("property_num")
        article_item = request.POST.get("article_item")
        description = request.POST.get("description")
        person_accountable = request.POST.get("person_accountable")
        cost = request.POST.get("cost")
        remarks = request.POST.get("remarks")

        if not property_num or not article_item or not description:
            return JsonResponse({"success": False, "error": "Missing fields"}, status=400)

        try:
            equipment = Equipment.objects.create(
                property_num=property_num,
                article_item=article_item,
                description=description,
                person_accountable=person_accountable,
                cost=cost,
                remarks=remarks
            )
            return JsonResponse({
                "success": True,
                "id": equipment.id,
                "property_num": equipment.property_num,
                "article_item": equipment.article_item,
                "description": equipment.description,
                "person_accountable": equipment.person_accountable,
                "cost": str(equipment.cost),  # Convert Decimal to string
                "remarks": equipment.remarks,
                "time_stamp": equipment.time_stamp.strftime("%Y-%m-%dT%H:%M:%S")
            })
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)}, status=400)
    
    return JsonResponse({"success": False, "error": "Invalid request"}, status=400)

def user_list(request):
    list_user = User.objects.filter(is_superuser=False)
    return render(request, 'base/admin/user_list.html', {'list_user': list_user})
    
@unauthorized_user
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None

        if user is not None and user.check_password(password):
            login(request, user)
            return redirect('home')
        else:
            if user is None:
                messages.error(request, 'Username not exist')
            else:
                messages.error(request, 'Password Incorrect')

    return render(request, 'base/authentication/login.html')

def user_logout(request):
    logout(request)
    return redirect('user_login')

@unauthorized_user
def user_register(request):
    if request.method == 'POST':
        reg_form = RegForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            messages.success(request, 'You successfuly registered!')
            return redirect('user_login')
        else:
            messages.error(request, 'Please correct the error below')
    else:
        reg_form = RegForm()
    context = {
        'reg_form': reg_form
    }
    return render(request, 'base/authentication/register.html', context)