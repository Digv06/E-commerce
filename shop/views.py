from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Orders, UpdateOrder
from math import ceil
import json

def index(request):
    allprods = []
    catprods = Product.objects.values('category','id')
    cats = { item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n=len(prod)
        nslides = n // 4 + ceil((n / 4) - (n // 4))
        allprods.append([prod,range(1,nslides),nslides])
    # params = {'no_of_slides': nslides, 'range':range(1,nslides),'products':products}
    params = {'allprods':allprods}
    return render(request,'shop/index.html',params)

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    thank =False
    if request.method == 'POST':
        name = request.POST.get("name",'')
        email = request.POST.get("email",'')
        phone = request.POST.get("phone",'')
        desc = request.POST.get("desc",'')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank = True
    return render(request,'shop/contact.html',{'thank' : thank})

def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = UpdateOrder.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps(updates, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'shop/tracker.html')

def search(request):
    return render(request,'shop/search.html')

def checkout(request):
    if request.method == "POST":
        items = request.POST.get('itemJson')
        name=request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        city=request.POST.get('city')
        state=request.POST.get('state')
        zip=request.POST.get('zip')
        order = Orders(items=items,name=name,email=email,address=address,phone=phone,city=city,state=state,zip=zip)
        order.save()
        update = UpdateOrder(order_id=order.order_id,update_desc="Your Order has been Placed!!!")
        update.save()
        thank = True
        id = order.order_id
        return render(request,'shop/CheckOut.html', {'thank':thank , 'id':id})
    return render(request,'shop/CheckOut.html')

def productview(request, myid):
    product = Product.objects.filter(id=myid)
    return render(request, 'shop/prodview.html', {'product': product[0]})