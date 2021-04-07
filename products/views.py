from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone
from .models import Product

def home(request):
    products=Product.objects
    return render(request,'products/home.html',{'products':products})

@login_required(login_url="/accounts/signup")
def create(request):
    if request.method=="POST":
        if request.POST['title'] and request.POST['description'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
        # create a new product object
            product = Product()
            # set all properties of this objects
            product.title = request.POST['title']
            product.description=request.POST['description']
            """ with the URL we have to make sure that it has the appropriate beginning on it. if the user already
            provided http or https then we can leave it, and if it is not provided then we should go ahead and
            add that on there. """
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                product.url=request.POST['url']
            else:
                product.url="http://" + request.POST['url'] # remember, when we work with a tag then http is worked very helpful
                # in case of icon and image the method is little bit different.
            product.icon=request.FILES['icon']
            product.image=request.FILES['image']
            # then we add some fields which will be auto generated.
            product.pub_date = timezone.datetime.now() # for timezone we have to import timezone utils
            # now we have to get the current user
            product.hunter=request.user
            product.save()
            # then we want to see the product in detail
            return redirect('home')
        else:
            return render(request,'products/create.hmtl',{'error':'All Fields are required'})
    else:
        return render(request,'products/create.html')

def productDetail(request,product_id):
    product_detail=get_object_or_404(Product,pk=product_id)
    return render(request,'products/productDetail.html',{'product_detail':product_detail})
@login_required(login_url="/accounts/signup")
def upvote(request,product_id):
    if request.method=="POST":
        product_detail=get_object_or_404(Product,pk=product_id)
        product_detail.votes+=1
        product_detail.save()
        return redirect('/products/'+str(product_detail.id)) # we can also use product_id
