from .models import CityDetail
from web.models import Feeddback, Order
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import FeedbackForm, OrderForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from web.models import Image


# Create your views here.


def homegreek(request):

    feedbacks = Feeddback.objects.filter(deleted=False)
    restaurant_details = CityDetail.objects.all()


    try:
        
        ordersnumber = Order.objects.filter(user=request.user, deleted=False)
        feedbacks = Feeddback.objects.filter(deleted=False)  # όχι User εδω..
        restaurant_details = CityDetail.objects.all()
        return render(request, 'greek/home.html', {'ordersnumber': ordersnumber, 'feedbacks': feedbacks, 'restaurant_details': restaurant_details})
    except:
        feedbacks = Feeddback.objects.filter(deleted=False)  # όχι User εδω..
        restaurant_details = CityDetail.objects.all()
        return render(request, 'greek/home.html', {'feedbacks': feedbacks, 'restaurant_details': restaurant_details})
        # return redirect('homelogoutuser')


# def homelogoutuser(request):
#     feedbacks = Feeddback.objects.filter(deleted=False)
#     restaurant_details = CityDetail.objects.all()
#     return render(request, 'web/home.html', {'feedbacks': feedbacks, 'restaurant_details': restaurant_details})


def greeklogoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('homegreek')


def greeksignupuser(request):
    if request.method == 'GET':
        return render(request, 'greek/signupuser.html', {'form': UserCreationForm()})
    else:
        # create new user
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)

                # return render(request, 'greek/home.html', {'Thanks': 'Ο λογαρισμος σου μολις δημιουργηθηκε'})
                return redirect('homegreek')

            except IntegrityError:
                return render(request, 'greek/signupuser.html', {'form': UserCreationForm(),
                                                                 'error': 'Αυτό το UserName χρησιμοποιείται ήδη απο άλλον χρήστη. Παρακαλώ δοκιμάστε διαφορετικό UserName.'})

            except ValueError:
                return render(request, 'greek/signupuser.html', {'form': UserCreationForm(),
                                                                 'error': 'Παρακαλώ ελέγξτε ξανά τα στοιχεία που δώσατε.'})
        else:
            return render(request, 'greek/signupuser.html',
                          {'form': UserCreationForm(), 'error': 'Passwords Did Not Match'}) 


def greekloginuser(request):
    if request.method == 'GET':
        return render(request, 'greek/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'greek/loginuser.html',
                          {'error': 'Λάθος username ή password', 'form': AuthenticationForm()})
        else:
            login(request, user)
            return redirect('homegreek')


@login_required
def greekfeedback(request):

    deletedorders = Order.objects.filter(user=request.user, deleted=True)
    previus_feedback = Feeddback.objects.filter(user=request.user).all()
    feedbacks = Feeddback.objects.filter(deleted=False)
    feedbacksnumber = Feeddback.objects.filter(
        user=request.user, deleted=False)
    restaurant_details = CityDetail.objects.all()
    ordersnumber = Order.objects.filter(user=request.user, deleted=False)

    if request.method == 'GET':
        return render(request, 'greek/feedback.html', {'deletedorders': deletedorders, 'ordersnumber': ordersnumber,
                                                       'feedbacksnumber': feedbacksnumber, 'feedbacks': feedbacks,
                                                       'restaurant_details': restaurant_details, 'form': FeedbackForm()})
    else:
        try:
            form = FeedbackForm(data=request.POST, files=request.FILES)
            # το αποθηκεύουμε προσωρινά στο commend.
            commend = form.save(commit=False)
            commend.user = request.user  # Συνδέουμε τον User με το commend

            for data in previus_feedback:

                if ((request.POST['customer_first_name'] == data.customer_first_name) and (request.POST['customer_second_name'] == data.customer_second_name)
                        and (request.POST['feedback_description'] == data.feedback_description)):

                    return redirect('homegreek')
            commend.save()  # Τωρα κάνουμε save

            try:
                # όχι User εδω..
                feedbacks = Feeddback.objects.filter(deleted=False)
                # όχι User εδω..
                feedbacksnumber = Feeddback.objects.filter(
                    user=request.user, deleted=False)
                restaurant_details = CityDetail.objects.all()
                return render(request, 'greek/home.html', {'deletedorders': deletedorders, 'ordersnumber': ordersnumber,
                                                           'Thanks': "Ευχαριστουμε. Η Κριτικη σας, εχει αποσταλει και θα ληφθει υποψιν.",
                                                           'feedbacksnumber': feedbacksnumber, 'feedbacks': feedbacks, 'restaurant_details': restaurant_details})
            except TypeError:
                # όχι User εδω..
                feedbacks = Feeddback.objects.filter(deleted=False)
                restaurant_details = CityDetail.objects.all()
                return render(request, 'greek/home.html', {'deletedorders': deletedorders, 'ordersnumber': ordersnumber,
                                                           'feedbacks': feedbacks, 'restaurant_details': restaurant_details})

                # return redirect('homegreek')
        except ValueError:
            return render(request, 'greek/feddback.html', {'form': FeedbackForm(), 'error': 'Κάτι Πήγε Στραβά'})


# @login_required
# def welcomefeedback(request):
#     if request.method == 'GET':
#         return render(request, 'web/welcomefeedback.html', {'form': FeedbackForm()})
#     else:
#         try:
#             # Files request files for uploading via USER and not ONLY via Admin.
#             form = FeedbackForm(request.POST, files=request.FILES)
#             # το αποθηκεύουμε προσωρινά στο commend.
#             commend = form.save(commit=False)
#             commend.user = request.user  # Συνδέουμε τον User με το commend.
#             commend.save()  # Τωρα κάνουμε save
#             return redirect('home')
#         except ValueError:
#             return render(request, 'web/feddback.html', {'form': FeedbackForm(), 'error': 'Bad information data'})


@login_required
def greekallmyfeedback(request):
    feedbacks = Feeddback.objects.filter(deleted=False)
    feedbacksnumber = Feeddback.objects.filter(
        user=request.user, deleted=False)
    restaurant_details = CityDetail.objects.all()
    feedbacks = Feeddback.objects.filter(user=request.user, deleted=False)
    deletedorders = Order.objects.filter(user=request.user, deleted=True)
    ordersnumber = Order.objects.filter(user=request.user, deleted=False)
    return render(request, 'greek/allmyfeedback.html', {'deletedorders': deletedorders, 'ordersnumber': ordersnumber, 'feedbacksnumber': feedbacksnumber, 'feedbacks': feedbacks,
                                                        'restaurant_details': restaurant_details, 'feeddbacks': feedbacks})


@login_required
def greekviewfeedback(request, feedback_pk):

    feedbacksnumber = Feeddback.objects.filter(
        user=request.user, deleted=False)
    restaurant_details = CityDetail.objects.all()

    feedbacks = Feeddback.objects.filter(user=request.user, deleted=False)
    viewfeedback = get_object_or_404(
        Feeddback, pk=feedback_pk, user=request.user)

    deletedorders = Order.objects.filter(user=request.user, deleted=True)
    ordersnumber = Order.objects.filter(user=request.user, deleted=False)

    if request.method == "GET":
        form = FeedbackForm(instance=viewfeedback)
        return render(request, 'greek/viewfeedback.html', {'deletedorders': deletedorders, 'ordersnumber': ordersnumber,
                                                           'feedbacksnumber': feedbacksnumber, 'feedbacks': feedbacks,
                                                           'restaurant_details': restaurant_details, 'viewfeeddbacks': viewfeedback, 'form': form})

    else:
        try:
            # Files request files for uploading via USER and not ONLY via Admin.
            form = FeedbackForm(
                request.POST, files=request.FILES, instance=viewfeedback)
            form.save()        # ΠΡΟΣΟΧΗ ΔΕΝ κάνει DELETE απο τον ADMIN ΜΟΝΟ απο τον USER

            return render(request, 'greek/allmyfeedback.html', {'feedbacksnumber': feedbacksnumber, 'feedbacks': feedbacks, 'restaurant_details': restaurant_details, 'feeddbacks': feedbacks, 'saved': 'ΟΙ ΑΛΛΑΓΕΣ ΑΠΟΘΗΚΕΥΤΗΚΑΝ'})

            # if viewfeedback.deleted is True:
            #     return redirect('deletedfeedback')
            # else:
            #     return redirect('allmyfeedback')
        except ValueError:
            return render(request, 'greek/viewfeedback.html', {'feedbacksnumber': feedbacksnumber, 'feedbacks': feedbacks, 'restaurant_details': restaurant_details, 'viewfeeddbacks': viewfeedback, 'form': form, 'error': 'Οπς Κάτι Πήγε Στραβά'})


@login_required
def greekdeletefeedback(request, feedback_pk):

    # feedbacks = Feeddback.objects.filter(user=request.user, delete=False)
    viewfeedback = get_object_or_404(
        Feeddback, pk=feedback_pk, user=request.user)

    if request.method == "POST":
        viewfeedback.delete()        # ΠΡΟΣΟΧΗ ΔΕΝ κάνει DELETE απο τον ADMIN ΜΟΝΟ απο τον USER
        return redirect('greekallmyfeedback')
        # return render(request, 'web/allmyfeedback.html', {'viewfeeddbacks': viewfeedback, 'saved': 'Feedback Deleted Permanently'})
    else:
        return redirect('greekallmyfeedback')


@login_required
def greekdeletedfeedback(request):
    ordersnumber = Order.objects.filter(user=request.user, deleted=False)
    deletedorders = Order.objects.filter(user=request.user, deleted=True)
    feedbacks = Feeddback.objects.filter(deleted=False)
    feedbacksnumber = Feeddback.objects.filter(
        user=request.user, deleted=False)
    restaurant_details = CityDetail.objects.all()

    feedbacks = Feeddback.objects.filter(user=request.user, deleted=True)
    return render(request, 'greek/deletedfeedback.html', {'deletedorders': deletedorders, 'ordersnumber': ordersnumber,
                                                          'feedbacksnumber': feedbacksnumber, 'feedbacks': feedbacks,
                                                          'restaurant_details': restaurant_details, 'feeddbacks': feedbacks})


@login_required
def greekviewdeletedfeedback(request, feedback_pk):

    ordersnumber = Order.objects.filter(user=request.user, deleted=False)
    deletedorders = Order.objects.filter(user=request.user, deleted=True)
    feedbacks = Feeddback.objects.filter(deleted=False)
    feedbacksnumber = Feeddback.objects.filter(
        user=request.user, deleted=False)
    restaurant_details = CityDetail.objects.all()

    # feedbacks = Feeddback.objects.filter(user=request.user, deleted=False)
    viewfeedback = get_object_or_404(
        Feeddback, pk=feedback_pk, user=request.user)

    if request.method == "GET":
        form = FeedbackForm(instance=viewfeedback)
        return render(request, 'greek/viewfeedback.html', {'deletedorders': deletedorders, 'ordersnumber': ordersnumber,
                                                           'feedbacksnumber': feedbacksnumber, 'feedbacks': feedbacks,
                                                           'restaurant_details': restaurant_details, 'viewfeeddbacks': viewfeedback, 'form': form})

    else:
        try:
            # Files request files for uploading via USER and not ONLY via Admin.
            form = FeedbackForm(
                request.POST, files=request.FILES, instance=viewfeedback)
            form.save()        # ΠΡΟΣΟΧΗ ΔΕΝ κάνει DELETE απο τον ADMIN ΜΟΝΟ απο τον USER

            feedbacks = Feeddback.objects.filter(
                user=request.user, deleted=True)
            return render(request, 'greek/deletedfeedback.html', {'feedbacksnumber': feedbacksnumber, 'feedbacks': feedbacks, 'restaurant_details': restaurant_details, 'feeddbacks': feedbacks, 'saved': 'ΟΙ ΑΛΛΑΓΕΣ ΑΠΟΘΗΚΕΥΤΗΚΑΝ'})

            # if viewfeedback.deleted is True:
            # return redirect('deletedfeedback')
            # else:
            #     return redirect('allmyfeedback')
        except ValueError:
            return render(request, 'greek/viewfeedback.html', {'feedbacksnumber': feedbacksnumber, 'feedbacks': feedbacks, 'restaurant_details': restaurant_details, 'viewfeeddbacks': viewfeedback, 'form': form, 'error': 'Κάτι Πήγε Στραβά'})


# ORDERS


@login_required
def greekorder(request):

    feedbacksnumber = Feeddback.objects.filter(
        user=request.user, deleted=False)

    deletedorders = Order.objects.filter(user=request.user, deleted=True)
    previus_order = Order.objects.filter(user=request.user).all()
    orders = Order.objects.filter(deleted=False)
    ordersnumber = Order.objects.filter(user=request.user, deleted=False)

    restaurant_details = CityDetail.objects.all()

    english_order = f"order"
    greek_order = f"greekorder"

    if request.method == 'GET':
        # Προσοχή εδώ βάζεις και την () στο FeedbackForm γιατί είναι δική μας η Form.
        return render(request, 'greek/order.html', {'greek_order': greek_order, 'english_order': english_order,
                                                    'feedbacksnumber': feedbacksnumber, 'deletedorders': deletedorders,
                                                    'ordersnumber': ordersnumber, 'orders': orders, 'restaurant_details': restaurant_details,
                                                    'form': OrderForm()})
    else:
        try:
            form = OrderForm(data=request.POST, files=request.FILES)
            # το αποθηκεύουμε προσωρινά στο commend.
            commend = form.save(commit=False)
            commend.user = request.user  # Συνδέουμε τον User με το commend

            # Αυτό το κάνουμε για να μην σώζουμε το ίδιο πράγμα κάθε φορά που κάνει ανανέωση σελίδας ο χρήστης.
            for data in previus_order:

                if ((request.POST['customer_first_name'] == data.customer_first_name) and (request.POST['customer_second_name'] == data.customer_second_name)
                        and (request.POST['order_description'] == data.order_description)):

                    return redirect('homegreek')

            commend.save()  # Τωρα κάνουμε save
            try:
                orders = Order.objects.filter(deleted=False)
                ordersnumber = Order.objects.filter(
                    user=request.user, deleted=False)
                restaurant_details = CityDetail.objects.all()

                return render(request, 'greek/home.html', {'feedbacksnumber': feedbacksnumber, 'deletedorders': deletedorders,
                                                           'Thanks': "Η παραγγελια σας εχει σταλει. ευχαριστουμε που μας επιλεξατε.",
                                                           'ordersnumber': ordersnumber, 'orders': orders, 'restaurant_details': restaurant_details})

            except TypeError:
                # όχι User εδω..
                orders = Order.objects.filter(deleted=False)
                restaurant_details = CityDetail.objects.all()
                return render(request, 'greek/home.html', {'feedbacksnumber': feedbacksnumber, 'deletedorders': deletedorders,
                                                           'orders': orders, 'restaurant_details': restaurant_details})

        except ValueError:
            return render(request, 'greek/order.html', {'feedbacksnumber': feedbacksnumber, 'deletedorders': deletedorders,
                                                        'form': OrderForm(), 'error': 'Erro Κατι πηγε στραβα'})


@login_required
def greekallmyorders(request):

    feedbacksnumber = Feeddback.objects.filter(
        user=request.user, deleted=False)
    deletedorders = Order.objects.filter(user=request.user, deleted=True)
    ordersnumber = Order.objects.filter(user=request.user, deleted=False)
    restaurant_details = CityDetail.objects.all()

    orders = Order.objects.filter(user=request.user, deleted=False)

    english_order = f"allmyorders"
    greek_order = f"greekallmyorders"

    return render(request, 'greek/allmyorders.html', {'greek_order': greek_order, 'english_order': english_order,
                                                      'feedbacksnumber': feedbacksnumber, 'deletedorders': deletedorders,
                                                      'ordersnumber': ordersnumber, 'orders': orders,
                                                      'restaurant_details': restaurant_details, 'deletedorders': deletedorders})


@login_required
def greekvieworder(request, order_pk):

    feedbacksnumber = Feeddback.objects.filter(
        user=request.user, deleted=False)
    deletedorders = Order.objects.filter(user=request.user, deleted=True)

    orders = Order.objects.filter(deleted=False)
    ordersnumber = Order.objects.filter(user=request.user, deleted=False)
    restaurant_details = CityDetail.objects.all()

    orders = Order.objects.filter(user=request.user, deleted=False)

    vieworder = get_object_or_404(Order, pk=order_pk, user=request.user)
    english_order = f"vieworder"
    greek_order = f"greekvieworder"

    if request.method == "GET":
        form = OrderForm(instance=vieworder)
        return render(request, 'greek/vieworder.html', {'greek_order': greek_order, 'english_order': english_order,
                                                        'feedbacksnumber': feedbacksnumber, 'deletedorders': deletedorders,
                                                        'ordersnumber': ordersnumber, 'orders': orders, 'restaurant_details': restaurant_details,
                                                        'vieworders': vieworder, 'form': form})

    else:
        try:
            form = OrderForm(request.POST, files=request.FILES,
                             instance=vieworder)
            form.save()
            orders = Order.objects.filter(user=request.user, deleted=False)
            english_order = f"allmyorders"
            greek_order = f"greekallmyorders"
            return render(request, 'greek/allmyorders.html', {'greek_order': greek_order, 'english_order': english_order,
                                                              'feedbacksnumber': feedbacksnumber, 'deletedorders': deletedorders,
                                                              'ordersnumber': ordersnumber, 'orders': orders, 'restaurant_details': restaurant_details,
                                                              'saved': 'Οι αλλαγες αποθηκευτηκαν'})
        except ValueError:
            return render(request, 'greek/vieworder.html', {'greek_order': greek_order, 'english_order': english_order,
                                                            'feedbacksnumber': feedbacksnumber, 'deletedorders': deletedorders,
                                                            'ordersnumber': ordersnumber, 'orders': orders, 'restaurant_details': restaurant_details,
                                                            'vieworders': vieworder, 'form': form, 'error': 'Error Κατι πηγε στραβα'})


@login_required
def greekdeleteorder(request, order_pk):
    vieworder = get_object_or_404(
        Order, pk=order_pk, user=request.user)

    if request.method == "POST":
        vieworder.delete()
        return redirect('greekallmyorders')
        # return render(request, 'web/allmyfeedback.html', {'viewfeeddbacks': viewfeedback, 'saved': 'Feedback Deleted Permanently'})
    else:
        return redirect('greekallmyorders')


@login_required
def greekdeletedorders(request):

    feedbacksnumber = Feeddback.objects.filter(
        user=request.user, deleted=False)
    deletedorders = Order.objects.filter(user=request.user, deleted=True)

    restaurant_details = CityDetail.objects.all()
    orders = Order.objects.filter(user=request.user, deleted=True)
    ordersnumber = Order.objects.filter(user=request.user, deleted=False)

    if request.method == 'GET':
        return render(request, 'greek/deletedorders.html', {'feedbacksnumber': feedbacksnumber, 'deletedorders': deletedorders,
                                                            'ordersnumber': ordersnumber, 'orders': orders, 'restaurant_details': restaurant_details})
    else:
        return redirect('greekdeletedorders')


@login_required
def greekreviewdeletedorders(request, order_pk):
    feedbacksnumber = Feeddback.objects.filter(
        user=request.user, deleted=False)
    deletedorders = Order.objects.filter(user=request.user, deleted=True)
    vieworder = get_object_or_404(
        Order, pk=order_pk, user=request.user)

    orders = Order.objects.filter(
        user=request.user, deleted=True)
    ordersnumber = Order.objects.filter(user=request.user, deleted=False)
    restaurant_details = CityDetail.objects.all()

    if request.method == "GET":
        form = OrderForm(instance=vieworder)
        return render(request, 'greek/revieworder.html', {'feedbacksnumber': feedbacksnumber, 'deletedorders': deletedorders,
                                                          'ordersnumber': ordersnumber, 'orders': orders,
                                                          'restaurant_details': restaurant_details,
                                                          'vieworders': vieworder, 'form': form})

    else:
        try:
            form = OrderForm(
                request.POST, files=request.FILES, instance=vieworder)
            form.save()        # ΠΡΟΣΟΧΗ ΔΕΝ κάνει DELETE απο τον ADMIN ΜΟΝΟ απο τον USER

            orders = Order.objects.filter(
                user=request.user, deleted=True)
            return render(request, 'greek/deletedorders.html', {'feedbacksnumber': feedbacksnumber, 'deletedorders': deletedorders,
                                                                'ordersnumber': ordersnumber, 'orders': orders, 'restaurant_details': restaurant_details,
                                                                'saved': 'ΟΙ ΑΛΛΑΓΕΣ ΑΠΟΘΗΚΕΥΤΗΚΑΝ'})

        except ValueError:
            return render(request, 'greek/deletedorders.html', {'feedbacksnumber': feedbacksnumber, 'deletedorders': deletedorders,
                                                                'vieworders': vieworder, 'form': form, 'error': 'Error Κατι πηγε στραβα'})


@login_required
def greekdeletedeletedorder(request, order_pk):
    vieworder = get_object_or_404(
        Order, pk=order_pk, user=request.user)

    if request.method == "POST":
        vieworder.delete()
        return redirect('greekdeletedorders')

    else:
        return redirect('greekdeletedorders')
