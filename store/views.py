from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models.product import Product
from .models.category import catergory
from .models.coustmer import coustmer
from .models.order import order
from .models.product import Product
from django.contrib.auth.hashers import make_password, check_password
from django.views import View


# Create your views here.


# index page which include the filter of the category and there product

# def index(request):
class Index(View):
    def post(self, request):
        product = request.POST.get("product")
        remove = request.POST.get("remove")
        cart = request.session.get("cart")

        if request.session != None:
            if cart:
                quantity = cart.get(product)
                if quantity:
                    if remove:
                        if quantity <= 1:
                            cart.pop(product)
                        else:
                            cart[product] = quantity - 1
                    else:
                        cart[product] = quantity + 1

                    cart = request.session["cart"]
                    print("cart:\t", cart)

                else:
                    cart[product] = 1

            else:
                cart = {}
                cart[product] = 1

        request.session["cart"] = cart
        print(cart)
        return redirect("mainpage")

    def get(self, request):
        cart = request.session.get("cart")
        if not cart:
            request.session["cart"] = {}
        item = None
        lst = catergory.objects.all()
        cat_id = request.GET.get("cat")

        if cat_id:
            item = Product.get_productby_cat_id(cat_id)
        else:
            item = Product.objects.all()

        shopname = "Digi Farm Pro"
        con = {"name": shopname, "item": item, "lst": lst}
        print("you are: ", request.session.get("email"))
        print("customer number : ", request.session.get("cust_id"))

        return render(request, "index.html", con)


# about page1
def about(request):
    print(request.session)
    return render(request, "about.html")


# need to design
def home(request):
    # return HttpResponse('<h1>this is home page</h1>')
    return render(request, "home.html")


def contact(request):
    return render(request, "contact.html")


# #########################################################
# sign up form


def signup(request):
    if request.method == "GET":
        return render(request, "signup.html")
    else:

        sendData = request.POST

        name = sendData.get("name")
        last_name = sendData.get("last_name")
        phone = sendData.get("contact")
        email = sendData.get("email")
        password = sendData.get("password")

        # dict holding the values
        value = {"name": name, "last_name": last_name}

        # validation
        # coustmer object created on the basis of input feild is submitted by the user
        cust = coustmer(
            name=name, last_name=last_name, phone=phone, email=email, password=password
        )
        
        err_msg = None
        # vallidation for input feild
        if not name or len(name) <= 3:
            err_msg = "please enter valid  First name  "

        # vallidation for input feild
        elif not last_name or len(last_name) <= 3:
            err_msg = "last name reruired "
        elif not phone or len(phone) != 10:
            err_msg = "provide correct contact details"

        # duplicate user not created in database which help to otimize our database
        elif cust.isExist():
            err_msg = "user already registed with same email"

        # data save if we got any kind of error in the input feild user does not need to input the data again if the data is correct this functionality work like google chrome
        if not err_msg:
            cust.password = make_password(cust.password)
            cust.register()

            return redirect("mainpage")
        else:
            data = {"error": err_msg, "values": value}
            return render(request, "signup.html", data)


# login form and validation class based views insted of if elif else ladder condiyion which helps achive the OPPS
class Login(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = coustmer.get_customer_by_email(email)
        err_msg = None
        print(user)
        if user:
            flag = check_password(password, user.password)
            print(" * " * 10)
            
            if flag:
                request.session["cust_id"] = user.id
                request.session["email"] = user.email
                request.session["name"] = user.name

                return redirect("mainpage")

            else:
                err_msg = "email or password is invalid"

                return render(request, "login.html", {"error": err_msg})
        else:
            err_msg = "email or password is invalid"
            return render(request, "login.html", {"error": err_msg})


def logout(request):
    request.session.clear()
    return redirect("mainpage")


def cart(request):
    name = request.session.get("name")
    ids = list(request.session.get("cart").keys())
    selection = Product.get_proby_id(ids)
    print("selected product:", ids)
    selected = {"name": name, "selection": selection}
    return render(request, "cart.html", selected)

# modal form

class checkout(View):
    def post(self, request):
        print(request.POST)
        address=request.POST.get('Address')
        mobile=request.POST.get('contact')
        cust=request.session.get('cust_id')  
        cart=request.session.get('cart')   #cart quantity 
        products=Product.get_proby_id(list(cart.keys())) #cart product
        print(cust,cart,products)
        
    
        for pr in products:
            x=None
            orders=order(custmer=coustmer(id=cust),
                         product=pr,
                         price=pr.price,
                         address=address,
                         phone_nu=mobile,
                         quantity=cart.get(str(pr.id)),
                         
                         )
            
            order.save(orders)
        request.session['cart']={}
        return render(request, "checkout.html")
            
            
        # return redirect('mainpage')

        #     orders=order(customer=coustmer(id=request.session['cust_id']),
        #                 product=pr,
        #                 price=pr.price,
        #                 address=address,
        #                 phone_nu=number,
        #                 quantity=cart.get(str(pr.id))
        #                 )
        #     orders.save()                         
        #     print("*******************************************",order.placeOrder)
        #     order.placeOrder()   
def my_order(request):
    name = request.session.get("name")
    imp={'name':name}
    return render(request, 'my_order.html',imp)

