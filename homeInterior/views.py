from django.shortcuts import render
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .email_service import send_email 
# Create your views here.

@csrf_exempt
def enquiry(request):
    if request.method == "POST":

        data=json.loads(request.body)


        name=data.get("name1")
        email=data.get("email1")
        phone=data.get("phone1")
        project=data.get("project1")
        location=data.get("projectLocation1")
        message=data.get("message1")


        print("name:",name)
        print("email:",email)
        print("phone_number:",phone)
        print("project_type:",project)
        print("project_location:",location)
        print("message:",message)


        company_message = f"""
            Dear KD Interiors Team,

            A new interior design enquiry has been successfully submitted through the KD Interiors website.

            Customer Enquiry Details
            ----------------------------------------
            Name         : {name}
            Email Address: {email}
            Phone Number : {phone}
            Project Type : {project}
            Project Location :{location}
            Message      : {message}
            ----------------------------------------
            Action Required
            ----------------------------------------
            Please review the customer's enquiry details and contact them using
            the provided phone number or email address to discuss their project
            and the next steps.

            Thank you.

            Regards,
            KD Interiors
            """

        send_email(
                to_email="kprabu1512@gmail.com",
                to_name="KD Interiors Team",
                subject="New Interior Design Enquiry Received",
                message=company_message
            )


        user_message = f"""
            Dear {name},

            Thank you for contacting KD Interiors.

            We have successfully received your interior design enquiry. Our team
            will review your requirements and contact you shortly to discuss your
            project.

            Your Enquiry Details
            ----------------------------------------
            Name         : {name}
            Email Address: {email}
            Phone Number : {phone}
            Project Type : {project}
            Project Location :{location}
            Message      : {message}
            ----------------------------------------

            Our team will contact you using the phone number or email address
            provided in your enquiry.

            Thank you for choosing KD Interiors. We look forward to helping you
            create a beautiful space.

            Regards,
            KD Interiors
            """

        send_email(
                to_email=email,
                to_name=name,
                subject="Your Interior Design Enquiry Has Been Received",
                message=user_message
            )


        return JsonResponse({
            "message": "Enquiry submitted successfully "
        })



@csrf_exempt
def consultation(request):
    if request.method == "POST":

        data=json.loads(request.body)


        email=data.get("email")
        phone=data.get("phone")
        project=data.get("projectType")
        location=data.get("projectLocation")


        print("email:",email)
        print("phone_number:",phone)
        print("project_type:",project)
        print("project_location",location)
        



        company_message = f"""
                Dear KD Interiors Team,

                A new consultation request has been successfully submitted through the KD Interiors website.

                Consultation Details
                ----------------------------------------
                Email Address     : {email}
                Phone Number      : {phone}
                Project Type      : {project}
                Project Location  : {location}
                ----------------------------------------

                Action Required
                ----------------------------------------
                Please review the customer's consultation request and contact them
                using the provided phone number or email address to discuss their
                project and the next steps.

                Thank you.

                Regards,
                KD Interiors
                """

        send_email(
                    to_email="kprabu1512@gmail.com",
                    to_name="KD Interiors Team",
                    subject="New Consultation Request Received",
                    message=company_message
                )

        user_message = f"""
                Dear sir/madam,

                Thank you for requesting a consultation with KD Interiors.

                We have successfully received your consultation request. Our team
                will review your requirements and contact you shortly to discuss
                your project.

                Your Consultation Details
                ----------------------------------------
                Email Address     : {email}
                Phone Number      : {phone}
                Project Type      : {project}
                Project Location  : {location}
                ----------------------------------------

                Our team will contact you using the phone number or email address
                provided in your consultation request.

                Thank you for choosing KD Interiors. We look forward to helping
                you create a beautiful space.

                Regards,
                KD Interiors
                """

        send_email(
                    to_email=email,
                    to_name="website_visitor",
                    subject="Your KD Interiors Consultation Request Has Been Received",
                    message=user_message
                )

        return JsonResponse({
                    "message": "Consultation request submitted successfully"
                })

          



            


def home(request):
    return render(request, "interior/index.html")

def aboutUs(request):
    return render(request,"interior/aboutUs.html")

def contactUs(request):
    return render(request,"interior/contactUs.html")

def gallery(request):
    return render(request,"interior/gallery.html")

def videoGallery(request):
    return render(request,"interior/videoGallery.html")


def projectGallery(request):
    return render(request,"interior/projectGallery.html")


def livingRoom(request):
    return render(request,"interior/livingRoom.html")


def bedRoom(request):
    return render(request,"interior/bedRoom.html")


def kitchen(request):
    return render(request,"interior/kitchen.html")


def bathRoom(request):
    return render(request,"interior/bathRoom.html")


def homeOffice(request):
    return render(request,"interior/homeOffice.html")

def kidsRoom(request):
    return render(request,"interior/kidsRoom.html")




