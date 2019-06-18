from django.shortcuts import render, redirect
from .models import CarDetailes
from django.core.files.storage import FileSystemStorage


def index(request):
    cardetailes = CarDetailes.objects.all()
    return render(request,"cardetails/index.html",{"carresults" : cardetailes})


def addcars(request):
    if request.method == 'POST':
        carname = request.POST["carname"]
        brand = request.POST["brand"]
        b_discription = request.POST["breifdiscription"]
        discription = request.POST["discription"]
        image = request.FILES["image"]
        fs = FileSystemStorage()
        fs.save(image.name, image)

        print(carname)
        print(brand)
        print(b_discription)
        print(discription)

        cardetailes = CarDetailes()
        cardetailes.name = carname
        cardetailes.brand = brand
        cardetailes.briefdiscriptions = b_discription
        cardetailes.discription = discription
        cardetailes.image = image
        cardetailes.save()


        return redirect("/cardetailes")

    return render(request, "cardetails/addcar.html")


def deletecars(request,id):
    CarDetailes.objects.filter(id=id).delete()
    return redirect("/cardetailes")


def editcars(request,id):
    if request.method == 'POST':
        id = request.POST["hdncarid"]
        carname = request.POST["carname"]
        brand = request.POST["brand"]
        b_discription = request.POST["breifdiscription"]
        discription = request.POST["discription"]


        print(id)
        print(carname)
        print(brand)
        print(b_discription)
        print(discription)

        editRecord = CarDetailes.objects.get(id=id)
        editRecord.name = carname
        editRecord.brand = brand
        editRecord.breifdiscription = b_discription
        editRecord.discription = discription
        editRecord.save()
        return redirect("/cardetailes")


    carDetailRecord = CarDetailes.objects.get(id=id)
    return render(request,"cardetails/editcars.html", {"editRecord": carDetailRecord})


def upload(request):
    if request.method == "POST":
        uploaded_file = request.FILES['document']
        print(uploaded_file.name)
        print(uploaded_file.size)
        fs = FileSystemStorage()
        fs.save(uploaded_file.name,uploaded_file)
    return render(request,"mediafiles/upload.html")