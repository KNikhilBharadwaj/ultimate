from django.shortcuts import render,redirect
from django.db import connection
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# def login(request):
#     return render(request, "login.html")



# user and user for super admin pass and username 



def LoginPage(request):
    if request.method=="POST":
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            error_message = "Username or Password incorrect"
            messages.error(request, error_message)
            
        
    return render(request,'login.html')


from django.contrib import messages

def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        
        if pass1 != pass2:
            messages.error(request, "Your Password and confirm password are not the same")
        else: 
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            messages.success(request, "User created successfully!")
    
    return render(request, 'signup.html')



def LogoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    return render(request, "home.html")
#vendr form 
@login_required(login_url='login')
def index(request):
    return render(request, "index.html")
# =============================Vendor Form================================================
# def insert(request):
#     if request.method == "POST":
#         Vendor_Name = request.POST.get('Vendor_Name')  
#         Vendor_Address = request.POST.get('Vendor_Address')
#         GSTIN_Number = request.POST.get('GSTIN_Number')
#         Contact_Number = request.POST.get('Contact_Number')
#         Vendor_Email_ID = request.POST.get('Vendor_Email_ID')
#         print(Vendor_Name,  Vendor_Address, GSTIN_Number, Contact_Number, Vendor_Email_ID)

#         args = [Vendor_Name, Vendor_Address, GSTIN_Number, Contact_Number, Vendor_Email_ID]

#         try:
#             cursor = connection.cursor()
#             cursor.callproc('sp_creditors3', args)
#             results = cursor.fetchall()
#             cursor.close()

#             if results:
#                 message = results[0][0]
#             else:
#                 message = None

#             return render(request, 'index.html', {'message': message})

#         except Exception as e:
#             # Handle the exception or display the error message
#             error_message = str(e)
#             return render(request, 'index.html', {'error_message': error_message})

#     return render(request, "index.html")

from django.http import HttpResponse, JsonResponse
@login_required(login_url='login')
def Insertvendor(request):
    if request.method == 'POST':
        vendor_name = request.POST.get('vendor_name')
        # vendor_code = request.POST.get('vendor_code')
        vendor_address = request.POST.get('vendor_address')
        vendor_gstin = request.POST.get('vendor_gstin')
        contact_number = request.POST.get('contact_number')
        email_id = request.POST.get('email_id')
        
        # vendor = Vendor(vendor_name=vendor_name,vendor_address=vendor_address, vendor_gstin=vendor_gstin, contact_number=contact_number, email_id=email_id)
        # vendor.save()
        
        cursor = connection.cursor()
        args = [vendor_name, vendor_address, vendor_gstin, contact_number, email_id]
        cursor.callproc('sp_testing', args)
        
        # Fetch results if needed // CHANGED THE CODE ON 23-5-23
        results = cursor.fetchall()
        cursor.close()
        if results :
          
            message = results[0][0]
            print(message)  # Assuming the message is returned as the first column of the first row
        else:
            message = None

        return render(request, 'index.html', {'message': message})

    return render(request, 'index.html')


# =========================Sundrycreditors Form===========================================================


@login_required(login_url='login')  
def FormDetails(request):
    if request.method == 'POST':
        gst_no = request.POST.get('p_gstin_number')
        hsn_code = request.POST.get('p_hsn_code')
        inv_num = request.POST.get('p_invoice_number')
        inv_date = request.POST.get('p_invoice_date')
        inv_value = request.POST.get('p_invoice_value')
        paid_status = request.POST.get('p_paid_status')
        qty = request.POST.get('p_qty')
        cost = request.POST.get('p_cost')
        prj_batchcode = request.POST.get('p_project_batch_code')
        finacial_year = request.POST.get('p_financial_year')
        igst = request.POST.get('p_igst')
        cgst = request.POST.get('p_cgst')
        sgst = request.POST.get('p_sgst')
        
        
        cursor = connection.cursor()
        args = [gst_no,hsn_code,inv_num, inv_date ,inv_value,paid_status,qty ,cost,prj_batchcode ,finacial_year,igst ,cgst,sgst]
        cursor.callproc('prdtesting', args)
        
        # Fetch results if needed
        results = cursor.fetchall()
        cursor.close()
        if results:
            message = results[0][0]
            print(message)  # Assuming the message is returned as the first column of the first row
        else:
            message = None
        
        return render(request, 'page2.html', {'message': message})

    return render(request, 'page2.html')

# =====================================================================================================
                                    # To GET GSTIN DETAILS 
from django.shortcuts import render
from django.db import connection

# def Search_gstin(request):
#     if request.method == 'POST':
#         gstin_number = request.POST.get('gstin_number')

#         # Call the stored procedure to fetch data from the MySQL database
#         with connection.cursor() as cursor:
#             cursor.callproc('TESTING1', [gstin_number])  
#             result = cursor.fetchall()

#         # Pass the retrieved data to the template for rendering
#         return render(request, 'gstin.html', {'result': result})

#     return render(request, 'gstin.html')
from django.shortcuts import render
from django.db import connection

def Search_gstin(request):
    if request.method == 'POST':
        gstin_number = request.POST.get('gstin_number')
        with connection.cursor() as cursor:
            try:
                cursor.callproc('TESTING1', [gstin_number])
                result = cursor.fetchall()
                return render(request, 'gstin.html', {'result': result})
            except Exception as e:
                error_message = str(e)
                return render(request, 'gstin.html', {'error_message': error_message})
    return render(request, 'gstin.html')




# from django.contrib import messages

# def Search_gstin(request):
#     if request.method == 'POST':
#         gstin_number = request.POST.get('gstin_number')

#         with connection.cursor() as cursor:
#             cursor.callproc('sp_GetGSTINDetails', [gstin_number])
#             result = cursor.fetchall()

#             if cursor.description is not None:
#                 # Stored procedure executed successfully
#                 messages.success(request, 'Data retrieved successfully.')
#             elif result:
#                 # Stored procedure executed, but no data found
#                 messages.info(request, 'No data found for the provided GSTIN number.')
#             else:
#                 # Error occurred while executing the stored procedure
#                 messages.error(request, 'Error occurred while retrieving data from the database.')

#         return render(request, 'gstin.html', {'result': result})

#     return render(request, 'gstin.html')


# =====================================================================================================

#-------------------------------------------------------------------------------------------------------

    #     try:
    #         cursor = connection.cursor()
    #         cursor.callproc('tbl_productgenerator12345', args)
    #         results = cursor.fetchall()
    #         cursor.close()

    #         if results:
    #             message = results[0][0]
    #         else:
    #             message = None

    #         return render(request, 'page2.html', {'message': message})

    #     except Exception as e:
    #         # Handle the exception or display the error message
    #         error_message = str(e)
    #         return render(request, 'page2.html', {'error_message': error_message})

    # return render(request, "page2.html")
# ==========================================================================================================insert==============


# def fixednav(request):
#     return render(request, "fixednav.html")

# def page2(request):
#     return render(request, "page2.html")



# ==============================================================================
# from django.shortcuts import render
# # from .models import Ultimate
# from django.db import connection
# from django.contrib import messages


# def home(request):
#     return render(request, "home.html")

# def index(request):
#     return render(request, "index.html")

# def insert(request):
#     if request.method == "POST":
#         Vendor_Name = request.POST.get('Vendor_Name')  
#         Vendor_Code = request.POST.get('Vendor_Code')
#         Vendor_Address = request.POST.get('Vendor_Address')
#         GSTIN_Number = request.POST.get('GSTIN_Number')
#         Contact_Number = request.POST.get('Contact_Number')
#         Vendor_Email_ID = request.POST.get('Vendor_Email_ID')
#         print(Vendor_Name, Vendor_Code, Vendor_Address, GSTIN_Number, Contact_Number, Vendor_Email_ID)
          
#         # query = Ultimate(Vendor_Name=Vendor_Name, Vendor_Code=Vendor_Code, Vendor_Address=Vendor_Address, GSTIN_Number=GSTIN_Number, Contact_Number=Contact_Number, Vendor_Email_ID=Vendor_Email_ID)
#         # query.save()

#         args = [Vendor_Name, Vendor_Code, Vendor_Address, GSTIN_Number, Contact_Number, Vendor_Email_ID]
        
#         cursor = connection.cursor()
#         cursor.callproc('sp_creditors1', args) 
#         # res = cursor.callproc('sp_name', args)
#         results = cursor.fetchall()
#         cursor.close()
#         if results:
#             message = results[0][0]  # Assuming the message is returned as the first column of the first row
#         else:
#             message = None

#         return render(request, 'index.html', {'message': message})
#         # print(results)
#         # # messages.success(request,'Data is Submited Succefully...!!')

#     return render(request, "index.html")
    

# def page2(request):
#     return render(request, "page2.html")

# def fixednav(request):
#     return render(request, "fixednav.html")
