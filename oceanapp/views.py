from webbrowser import get
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from .models import profile, principal, accured, history, otp
from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from datetime import date, timedelta
from datetime import datetime
import random

# multiply ethereum value by 1000000000000000000 then send it to frontend
# Create your views here.

@login_required
def portfolio_wallet_connect(request):
    return render(request, 'oceanapp/port.html', {})

def index(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        subject = request.POST['subject']
        body = request.POST['message']

        email_mess = EmailMessage (
            f'Ocean Fortunes - {subject}',
            f'This is a contact message from ocean fortunes. This message is from {fname} {lname}. Body: \n \n {body}. \n \n Good day.',
            settings.EMAIL_HOST_USER,
            [email]
        )
        email_mess.fail_silently = True
        email_mess.send()
        messages.success(request, 'We have received your message')
        return render(request, 'oceanapp/home.html', {})

    return render(request, 'oceanapp/home.html', {})


def notify(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            user_name = User.objects.all()
            check = str(datetime.now()).split("-")[1]
            
            for i in user_name:
                get_accure = accured.objects.filter(user=i)
                for j in get_accure:
                    f_date = str(j.date).split("-")[1]
                    l_date = str(j.new_date).split("-")[1]

                    if int(check) >= int(l_date):
                        get_principle = principal.objects.get(user=i)
                        percent = get_principle.percentage
                        principal_value = get_principle.principal
                        calc = percent * principal_value * 1 + principal_value 
                        
                        result = str(calc)
                        v_accured = accured.objects.get(user=i)
                        v_accured.value = result
                        v_accured.save()
                    else:
                        pass
    else:
        return render('home')

    return render(request, 'oceanapp/notify.html', {})

@login_required
def principal1(request):
    check_otp = otp.objects.filter(user=request.user)
    if check_otp:
        messages.error(request, 'Enter OTP to login')
        return redirect('otp')
        
    get_data = principal.objects.filter(user=request.user)
    if get_data:
        data = principal.objects.get(user=request.user)
        data.principal +=200
        data.percentage = 9
        data.save()
        new_history = history(user=request.user, buy_sold=True, status=True, amount=200)
        new_history.save()
        return redirect('home')
    else:
        get_principal = principal(user=request.user, principal=200, percentage=9)
        get_principal.save()
        new_history = history(user=request.user, buy_sold=True, status=True, amount=200)
        new_history.save()
        return redirect('home')

@login_required  
def principal2(request):
    check_otp = otp.objects.filter(user=request.user)
    if check_otp:
        messages.error(request, 'Enter OTP to login')
        return redirect('otp')
    
   
        
    get_data = principal.objects.filter(user=request.user)
    if get_data:
        data = principal.objects.get(user=request.user)
        data.principal +=350
        data.percentage = 12
        data.save()
        new_history = history(user=request.user, buy_sold=True, status=True, amount=350)
        new_history.save()
        return redirect('home')
    else:
        get_principal = principal(user=request.user, principal=350, percentage=12)
        get_principal.save()
        new_history = history(user=request.user, buy_sold=True, status=True, amount=350)
        new_history.save()
        return redirect('home')
    get_principal.save()
    return redirect('home')

@login_required
def wc_error(request):
    messages.error(request, 'There was an error processing your transaction. Please try again')
    return render(request, 'oceanapp/port1.html', {})

@login_required
def principal3(request):
    check_otp = otp.objects.filter(user=request.user)
    if check_otp:
        messages.error(request, 'Enter OTP to login')
        return redirect('otp')
    
   
        
    get_data = principal.objects.filter(user=request.user)
    if get_data:
        data = principal.objects.get(user=request.user)
        data.principal +=500
        data.percentage = 17
        data.save()
        new_history = history(user=request.user, buy_sold=True, status=True, amount=500)
        new_history.save()
        return redirect('home')
    else:
        get_principal = principal(user=request.user, principal=500, percentage=17)
        get_principal.save()
        new_history = history(user=request.user, buy_sold=True, status=True, amount=500)
        new_history.save()
        return redirect('home')

@login_required
def home(request):
    check_otp = otp.objects.filter(user=request.user)
    if check_otp:
        messages.error(request, 'Enter OTP to login')
        return redirect('otp')
    
   
        
    data2 = principal.objects.get(user=request.user)
    principall = data2.principal
    percent = data2.percentage /100
    percent2 = data2.percentage
    cards = principall/4
    expected_income=(principall * percent) + principall
    acc = accured.objects.get(user=request.user)
    
    acc_value= acc.value

    context = {
        'data': data2.principal, 
        'card':cards, 
        'percent':percent2,
        'ex': expected_income,
        'acc': acc_value,
        }
    
    return render(request, 'oceanapp/index.html', context)

def email_veri(request, username):
    if request.method == 'POST':
        print(username)
        user = User.objects.get(username=username)
        update_profile = profile.objects.get(user=user)
        update_profile.email_verify = True
        update_profile.save()

        messages.success(request, 'Profile Verified. Proceed to Login')
        return redirect('login')
    return render(request, 'oceanapp/email_veri.html', {})

def Register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('uname')
        name = request.POST.get('name')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        phone = request.POST.get('phone')

        try:
            name.split()[1]
            
        except:
            messages.error(request, 'Enter your first and last names')
            return render(request, 'oceanapp/reg.html', {})

        check = User.objects.filter(username=username)
        check_email = User.objects.filter(email=email)
        if check:
            messages.error(request, 'Username is taken, try another')
            return render(request, 'oceanapp/reg.html', {})

        if check_email:
            messages.error(request, 'Email is taken, try another')
            return render(request, 'oceanapp/reg.html', {})

        if len(pass1) < 8:
            messages.error(request, 'Password must be equal to or greater than 8 characters')
            return render(request, 'oceanapp/reg.html', {})

        fin = 0
        nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']   
        for i in nums:
            if i in pass1:
                fin +=1

        if fin > 0: 
            pass
        else:
            messages.error(request, 'Password must contain at least one number and special character')
            return render(request, 'oceanapp/reg.html', {})

        special = ['!', '@', '#', '$ ''', '%', '^', '&', '*', '(', ')', '-', '+', '?', '_', '=', ',', '<', '>', '/']

        tot = 0
        for i in special:
            if i in pass1:
                tot+=1
        if tot == 0:
            messages.error(request, 'Password must contain at least one number and special character')
            return render(request, 'oceanapp/reg.html', {})

        split_name = name.split()
        first = split_name[0]
        second = split_name[1]

        new_user = User.objects.create_user(username=username, email=email, password=pass1)
        new_user.first_name = first
        new_user.last_name = second
        new_user.save()
        new_profile = profile(user=new_user, num=phone)
        new_profile.save()
        new_principal = principal(user=new_user, principal=0)
        new_principal.save()

        start_date = datetime.now()
        end_date = start_date + timedelta(days=30)
        new_accured = accured(user=new_user, date=start_date, new_date=end_date)
        new_accured.save()

        email_templat_name = 'oceanapp/emailconfirm.html'

        c = {
            'username': username
        }
        emaill = render_to_string(email_templat_name, c)     

        email_mess = EmailMessage (
            'Ocean Fortunes Email Verification',
            emaill,
            settings.EMAIL_HOST_USER,
            [email]
        )
        email_mess.fail_silently = True
        email_mess.content_subtype = 'html'
        email_mess.send()

        messages.success(request, 'User Created Successfully. Check your email to verify account')
        return redirect('create')
        

        
    return render(request, 'oceanapp/reg.html', {})

def created(request):
    return render(request, 'oceanapp/created.html')

# referal registeration view
def Register2(request, user):
    if request.user.is_authenticated:
            return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('uname')
        name = request.POST.get('name')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        phone = request.POST.get('phone')

        try:
            name.split()[1]
            
        except:
            messages.error(request, 'Enter your first and last names')
            return render(request, 'oceanapp/reg.html', {})

        check = User.objects.filter(username=username)
        check_email = User.objects.filter(email=email)
        if check:
            messages.error(request, 'Username is taken, try another')
            return render(request, 'oceanapp/reg.html', {})

        if check_email:
            messages.error(request, 'Email is taken, try another')
            return render(request, 'oceanapp/reg.html', {})

        if len(pass1) < 8:
            messages.error(request, 'Password must be equal to or greater than 8 characters')
            return render(request, 'oceanapp/reg.html', {})

        fin = 0
        nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']   
        for i in nums:
            if i in pass1:
                fin +=1

        if fin > 0: 
            pass
        else:
            messages.error(request, 'Password must contain at least one number and special character')
            return render(request, 'oceanapp/reg.html', {})

        special = ['!', '@', '#', '$ ''', '%', '^', '&', '*', '(', ')', '-', '+', '?', '_', '=', ',', '<', '>', '/']

        tot = 0
        for i in special:
            if i in pass1:
                tot+=1
        if tot == 0:
            messages.error(request, 'Password must contain at least one number and special character')
            return render(request, 'oceanapp/reg.html', {})

        split_name = name.split()
        first = split_name[0]
        second = split_name[1]

        new_user = User.objects.create_user(username=username, email=email, password=pass1)
        new_user.first_name = first
        new_user.last_name = second
        new_user.save()
        new_profile = profile(user=new_user, num=phone)
        new_profile.save()
        new_principal = principal(user=new_user, principal=0)
        new_principal.save()

        email_templat_name = 'oceanapp/emailconfirm.html'

        c = {
            'username': username
        }
        emaill = render_to_string(email_templat_name, c)     

        email_mess = EmailMessage (
            'Ocean Fortunes Email Verification',
            emaill,
            settings.EMAIL_HOST_USER,
            [email]
        )
        email_mess.fail_silently = True
        email_mess.content_subtype = 'html'
        email_mess.send()
        get_user = User.objects.get(username=user)
        get_user = profile.objects.get(user=get_user)
        get_user.credit+=10
        get_user.refer_num+=1
        get_user.save()
        
        messages.success(request, 'User Created Successfully. Check your email to verify account')
        return redirect('create')
        

        
    return render(request, 'oceanapp/reg.html', {})

def Login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('uname')
        pass1 = request.POST.get('pass')
        
        get_user = User.objects.filter(username=username)
        if get_user:
            user = User.objects.get(username=username)
            get_prof = profile.objects.get(user=user)
            if get_prof.email_verify == True:
                pass
            else:
                messages.error(request, 'Verify your email before you can login')
                return render(request, 'oceanapp/login.html')
        else:
            messages.error(request, f'Error, wrong user details or user does not exist')
            return render(request, 'oceanapp/login.html', {})
        auth_user = authenticate(username=username, password=pass1)
        if auth_user is not None:
            login(request, auth_user)
            final = ''
            nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
            while len(final) < 6:
                pick = random.choice(nums)
                final+=pick
            new_otp = otp(user=request.user, value=final)
            new_otp.save()

            email_templat_name = 'oceanapp/send_otp.html'

            c = {
                'otp': final
            }
            emaill = render_to_string(email_templat_name, c)     

            email_mess = EmailMessage (
                'Your Verification Code: Ocean Fortunes',
                emaill,
                settings.EMAIL_HOST_USER,
                [request.user.email]
            )
            email_mess.fail_silently = True
            email_mess.content_subtype = 'html'
            email_mess.send()

            messages.success(request, 'We have sent a 6 digit code to your email. Use it to login')
            return redirect('otp')
        else:
            messages.error(request, f'Error, wrong user details or user does not exist')
            return render(request, 'oceanapp/login.html', {})

    return render(request, 'oceanapp/login.html', {})

def re_send(request):
    get_otp = otp.objects.filter(user=request.user)
    if get_otp:
        del_otp = otp.objects.get(user=request.user)
        del_otp.delete()
    final = ''
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
    while len(final) < 6:
            pick = random.choice(nums)
            final+=pick
    new_otp = otp(user=request.user, value=final)
    new_otp.save()

    email_templat_name = 'oceanapp/send_otp.html'

    c = {
            'otp': final
        }
    emaill = render_to_string(email_templat_name, c)     

    email_mess = EmailMessage (
                'Your Verification Code: Ocean Fortunes',
                emaill,
                settings.EMAIL_HOST_USER,
                [request.user.email]
            )
    email_mess.fail_silently = True
    email_mess.content_subtype = 'html'
    email_mess.send()

    messages.success(request, 'We have re-sent the 6 digit code to your email. Use it to login')
    return redirect('otp')

def send_otp(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    if request.method == 'POST':
        otp_value = request.POST['otp']
        get_otp = otp.objects.filter(user=request.user, value=otp_value)
        if get_otp:
            del_otp = otp.objects.get(user=request.user, value=otp_value)
            del_otp.delete()
            return redirect('home')
        else:
            messages.error(request, 'You have entered a wrong OTP')
            return render(request, 'oceanapp/otp.html', {})
    return render(request, 'oceanapp/otp.html', {})

def LogoutView(request):
    logout(request)
    return redirect('login')

@login_required
def portfolio(request):
    check_otp = otp.objects.filter(user=request.user)
    if check_otp:
        messages.error(request, 'Enter OTP to login')
        return redirect('otp')
    em_veri = profile.objects.filter(user=request.user)
   
        
    return render(request, 'oceanapp/portfolio.html', {})

@login_required
def account(request):
    check_otp = otp.objects.filter(user=request.user)
    if check_otp:
        messages.error(request, 'Enter OTP to login')
        return redirect('otp')
    
   
        
    if request.method == 'POST':
        sel = request.POST['select']
        print(sel)
    last_logged = get_user_model().objects.get(username=request.user)
    log=last_logged.last_login
    get_profile = profile.objects.get(user=request.user)
    verify =get_profile.verified
    email = get_profile.email_verify
    credit = get_profile.credit
    get_history = history.objects.filter(user=request.user)
    prince = principal.objects.get(user=request.user)
    get_acc = accured.objects.get(user=request.user)
    context = {
        'log': log,
        'verify':verify,
        'email': email,
        'credit':credit,
        'history': get_history,
        'pri': prince,
        'acc': get_acc,
        'prof': get_profile,
    }
    return render(request, 'oceanapp/accounts.html', context)

@login_required
def profileimg(request):
    check_otp = otp.objects.filter(user=request.user)
    if check_otp:
        messages.error(request, 'Enter OTP to login')
        return redirect('otp')
    
   
        
    if request.method == 'POST':
        file = request.POST.get('upload')    
        if file:
            print('yes')
        update_profile = profile.objects.get(user=request.user)
        update_profile.file = file
        update_profile.save()
        return redirect('settings')

    return render(request, 'oceanapp/verify.html')

@login_required
def thank(request):
    check_otp = otp.objects.filter(user=request.user)
    if check_otp:
        messages.error(request, 'Enter OTP to login')
        return redirect('otp')
    
   
        
    return render(request, 'oceanapp/verify-step-3.html')
    
@login_required
def setting(request):
    get_profile = profile.objects.get(user=request.user)
    check_otp = otp.objects.filter(user=request.user)
    if check_otp:
        messages.error(request, 'Enter OTP to login')
        return redirect('otp')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        file = request.FILES.get('file-upload-field')
        name = request.POST.get('fullname')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        address = request.POST.get('presentaddress')
        city = request.POST.get('city')
        postal = request.POST.get('postal')
        country = request.POST.get('country')

        if username:
            new_username = User.objects.get(user=request.user)
            new_username.username = username
            new_username.save()
        
        if file:
            new_prof = profile.objects.get(user=request.user)
            new_prof.file=file
            new_prof.save()

        if name:
            try:
                name.split()[1]
            
            except:
                messages.error(request, 'Enter your first and last names')
                return redirect('setting')
                
            split_name = name.split()
            first = split_name[0]
            second = split_name[1]
            new_name = User.objects.get(username=request.user)
            new_name.first_name = first
            new_name.last_name = second
            new_name.save()

        if email:
            new_email = User.objects.get(username=request.user)
            new_email.email = email
            new_email.save()

        if dob:
            #dob
            new_data = profile.objects.get(user=request.user)
            new_data.dob = dob
            new_data.save()
        if address:
            #address
            new_data = profile.objects.get(user=request.user)
            new_data.address = address
            new_data.save()
        if city:
            #city
            new_data = profile.objects.get(user=request.user)
            new_data.city = city
            new_data.save()
        if postal:
            #postal
            new_data = profile.objects.get(user=request.user)
            new_data.postal = postal
            new_data.save()
        if country:
            #country
            new_data = profile.objects.get(user=request.user)
            new_data.country = country
            new_data.save()
        # if file:
        #     #file
        #     new_data = profile.objects.get(user=request.user)
        #     new_data.file = file
        #     new_data.save()

        messages.success(request, f'Profile Successfully Updated')
        return redirect('setting')

        
    img = profile.objects.get(user=request.user)
    return render(request, 'oceanapp/settings.html', {"img":img, 'prof': get_profile,})

@login_required
def faq(request):
    check_otp = otp.objects.filter(user=request.user)
    if check_otp:
        messages.error(request, 'Enter OTP to login')
        return redirect('otp')
    
   
        
    return render(request, 'oceanapp/faq.html', {})

@login_required
def prefrence(request):
    check_otp = otp.objects.filter(user=request.user)
    if check_otp:
        messages.error(request, 'Enter OTP to login')
        return redirect('otp')
    
   
        
    return render(request, 'oceanapp/settings-preferences.html', {})

@login_required
def security(request):
    check_otp = otp.objects.filter(user=request.user)
    if check_otp:
        messages.error(request, 'Enter OTP to login')
        return redirect('otp')
    
   
        
    if request.method == 'POST':
        num = request.POST.get('num2')    
        update_profile = profile.objects.get(user=request.user)
        update_profile.num2 = num
        update_profile.save()

        get_profile = profile.objects.get(user=request.user)
        verify =get_profile.email_verify

        messages.success(request, f'Number Successfully Added!')
        return render(request, 'oceanapp/settings-security.html', {'verify':verify})

    get_profile = profile.objects.get(user=request.user)
    verify =get_profile.email_verify
    verify2 = get_profile.verified
    
    return render(request, 'oceanapp/settings-security.html', {'verify':verify, 'verify2':verify2, 'prof':get_profile})

def v1(request):
    return render(request, 'oceanapp/verify-step-1.html')

@login_required
def verify1(request):
    check_otp = otp.objects.filter(user=request.user)
    if check_otp:
        messages.error(request, 'Enter OTP to login')
        return redirect('otp')
    
    if request.method == 'POST':
        file1 = request.FILES.get('upload1')
        file2 = request.FILES.get('upload2')
        update_profile = profile.objects.get(user=request.user)
        update_profile.file2 = file1
        update_profile.back = file2
        update_profile.save()
        
        return redirect('thank')
    return render(request, 'oceanapp/verify-step-2.html')

@login_required
def verify2(request):
    check_otp = otp.objects.filter(user=request.user)
    if check_otp:
        messages.error(request, 'Enter OTP to login')
        return redirect('otp')
    
   
        
    return render(request, 'oceanapp/verify-step-2.html', {})


@login_required
def accured_income_withdraw(request):
    user = User.objects.get(username=request.user.username)
    get_profile = profile.objects.get(user=user)
    if get_profile.refer_num < 10:
        messages.success(request, 'You must have 10 referalls before you can withdraw accured income')
        return redirect('account')
    else:
        email = request.user.email
        email_mess = EmailMessage (
            f'Ocean Fortunes: Early Withdraw: {request.user.first_name} {request.user.last_name}',
            f'Purpose: Request for early withdrawal \n \n From: {request.user.first_name} {request.user.last_name}', 
            settings.EMAIL_HOST_USER,
            ['oceanfortunes@gmail.com']
        )
        email_mess.fail_silently = True
        email_mess.send()
        messages.success(request, 'Your request has been received and is being processed')
        return redirect('account')

@login_required
def withdraw_referral_credit(request):
    email = request.user.email
    email_mess = EmailMessage (
        f'Ocean Fortunes: Referral Credit Withdraw: {request.user.first_name} {request.user.last_name}',
        f'Purpose: Request for referral credit withdrawal \n \n From: {request.user.first_name} {request.user.last_name}', 
        settings.EMAIL_HOST_USER,
        ['oceanfortunes@gmail.com']
    )
    email_mess.fail_silently = True
    email_mess.send()
    messages.success(request, 'Your request has been received and is being processed')
    return redirect('account')

@login_required
def principle_withdraw(request):
    email = request.user.email
    email_mess = EmailMessage (
        f'Ocean Fortunes: Principle Withdraw: {request.user.first_name} {request.user.last_name}',
        f'Purpose: Request for principle withdrawal \n \n From: {request.user.first_name} {request.user.last_name}', 
        settings.EMAIL_HOST_USER,
        ['theprotonguy@yahoo.com']
    )
    email_mess.fail_silently = True
    email_mess.send()
    messages.success(request, 'Your request has been received and is being processed')
    return redirect('account')
       

def email_reset_check(request):
    if request.method == 'POST':
        email = request.POST['email']
        check = User.objects.filter(email=email)
        if check:
            user=User.objects.get(email=email)
            email_templat_name = 'oceanapp/email_template.html'

            c = {
                'username': user.username
            }
            emaill = render_to_string(email_templat_name, c)     

            email_mess = EmailMessage (
                'Ocean Fortunes Password Reset',
                emaill,
                settings.EMAIL_HOST_USER,
                [email]
            )
            email_mess.fail_silently = True
            email_mess.content_subtype = 'html'
            email_mess.send()
            return redirect('reset-sent')
        else:
            messages.error('No user with that email exists')
            return redirect('reset-form')    

    return render(request, 'oceanapp/email_change.html', {})    

def password_reset_form(request, user):
    if request.method == 'POST':
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 != pass2:
            messages.error(request, 'Passwords do not match')
            return render(request, 'oceanapp/email_password_reset.html', {})

        if len(pass1) < 8:
            messages.error(request, 'Password must be equal to or greater than 8 characters')
            return render(request, 'oceanapp/email_password_reset.html', {})
        fin = 0
        nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']   
        for i in nums:
            if i in pass1:
                fin +=1

        if fin > 0: 
            pass
        else:
            messages.error(request, 'Password must contain at least one number and special character')
            return render(request, 'oceanapp/email_password_reset.html', {})

        special = ['!', '@', '#', '$ ''', '%', '^', '&', '*', '(', ')', '-', '+', '?', '_', '=', ',', '<', '>', '/']

        tot = 0
        for i in special:
            if i in pass1:
                tot+=1
        if tot == 0:
            messages.error(request, 'Password must contain at least one number and special character')
            return render(request, 'oceanapp/email_password_reset.html', {})

        user = User.objects.get(username=user)
        user.set_password(pass1)
        user.save()
        messages.success(request, 'Password changed successfully. Login')
        return redirect('login') 
    return render(request, 'oceanapp/email_password_reset.html', {})

def password_reset_sent(request):
    return render(request, 'oceanapp/email_reset_sent.html', {})