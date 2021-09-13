from .models import CityDetail, Feeddback, Order, ListOrNot
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import FeedbackForm, OrderForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


# Create your views here.

def mobile(request):
    lista_yes = False

    feedbacks = Feeddback.objects.filter(deleted=False)
    restaurant_details = CityDetail.objects.all()

    if request.method == 'GET':
        try:
            ordersnumber = Order.objects.filter(user=request.user, deleted=False)
            # όχι User εδω.. # όχι User εδω..
            feedbacks = Feeddback.objects.filter(deleted=False)
            return render(request, 'web/home.html', {'ordersnumber': ordersnumber, 'feedbacks': feedbacks, 'restaurant_details': restaurant_details, 'lista_yes': lista_yes})
        except TypeError:
            feedbacks = Feeddback.objects.filter(deleted=False)  # όχι User εδω..
            restaurant_details = CityDetail.objects.all()
            return render(request, 'web/home.html', {'feedbacks': feedbacks, 'restaurant_details': restaurant_details, 'lista_yes': lista_yes})
    else:
        return redirect('home')


def home(request):
    
    lista_yes = ListOrNot.lista

    feedbacks = Feeddback.objects.filter(deleted=False)
    restaurant_details = CityDetail.objects.all()

    if request.method == 'GET':
        try:
            ordersnumber = Order.objects.filter(user=request.user, deleted=False)
            # όχι User εδω.. # όχι User εδω..
            feedbacks = Feeddback.objects.filter(deleted=False)
            return render(request, 'web/home.html', {'ordersnumber': ordersnumber, 'feedbacks': feedbacks, 'restaurant_details': restaurant_details, 'lista_yes': lista_yes})
        except TypeError:
            feedbacks = Feeddback.objects.filter(deleted=False)  # όχι User εδω..
            restaurant_details = CityDetail.objects.all()
            return render(request, 'web/home.html', {'feedbacks': feedbacks, 'restaurant_details': restaurant_details, 'lista_yes': lista_yes})
    else:
        return redirect('mobile')


def homelogoutuser(request):
    feedbacks = Feeddback.objects.filter(deleted=False)
    restaurant_details = CityDetail.objects.all()
    return render(request, 'web/home.html', {'feedbacks': feedbacks, 'restaurant_details': restaurant_details})


def logoutuser(request):

    if request.method == "POST":
        logout(request)
        return redirect('home')


def signupuser(request):
    # deletedorders = Order.objects.filter(user=request.user, deleted=True)
    if request.method == 'GET':
        return render(request, 'web/signupuser.html', {'form': UserCreationForm()})
    else:
        # create new user
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)

                # return render(request, 'web/home.html', {'Thanks': 'Your Account Just Created'})
                return redirect('home')

            except IntegrityError:
                return render(request, 'web/signupuser.html', {'form': UserCreationForm(),
                                                               'error': 'This UserName already exist in our database. '
                                                                        'Please try another one.'})

            except ValueError:
                return render(request, 'web/signupuser.html', {'form': UserCreationForm(),
                                                               'error': 'Please fill in the spaces with the correct credentials.'})
        else:
            return render(request, 'web/signupuser.html',
                          {'form': UserCreationForm(), 'error': 'Passwords Did Not Match'})


def loginuser(request):
    # deletedorders = Order.objects.filter(user=request.user, deleted=True)
    if request.method == 'GET':
        return render(request, 'web/loginuser.html', {'deletedorders': deletedorders, 'form': AuthenticationForm()})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'web/loginuser.html',
                          {'error': 'Incorrect username or password', 'form': AuthenticationForm()})
        else:
            login(request, user)
            return redirect('home')


@login_required
def feedback(request):

    deletedorders = Order.objects.filter(user=request.user, deleted=True)
    previus_feedback = Feeddback.objects.filter(user=request.user).all()
    feedbacks = Feeddback.objects.filter(deleted=False)
    feedbacksnumber = Feeddback.objects.filter(
        user=request.user, deleted=False)
    restaurant_details = CityDetail.objects.all()
    ordersnumber = Order.objects.filter(user=request.user, deleted=False)

    if request.method == 'GET':
        return render(request, 'web/feedback.html', {'deletedorders': deletedorders, 'ordersnumber': ordersnumber, 
        'feedbacksnumber': feedbacksnumber, 'feedbacks': feedbacks, 'restaurant_details': restaurant_details, 'form': FeedbackForm()})
    else:
        try:
            form = FeedbackForm(data=request.POST, files=request.FILES)
            # το αποθηκεύουμε προσωρινά στο commend.

            commend = form.save(commit=False)
            commend.user = request.user  # Συνδέουμε τον User με το commend

            for data in previus_feedback:

                if ((request.POST['customer_first_name'] == data.customer_first_name) and (request.POST['customer_second_name'] == data.customer_second_name)
                        and (request.POST['feedback_description'] == data.feedback_description)):

                    return redirect('home')

            commend.save()  # Τωρα κάνουμε save

            try:
                # όχι User εδω..
                feedbacks = Feeddback.objects.filter(deleted=False)
                # όχι User εδω..
                feedbacksnumber = Feeddback.objects.filter(
                    user=request.user, deleted=False)
                restaurant_details = CityDetail.objects.all()

                return render(request, 'web/home.html', {'deletedorders': deletedorders, 'Thanks': "Your feedback has been sent. Thank you.",
                                                         'feedbacksnumber': feedbacksnumber, 'feedbacks': feedbacks, 'restaurant_details': restaurant_details})

            except TypeError:
                # όχι User εδω..
                feedbacks = Feeddback.objects.filter(deleted=False)
                restaurant_details = CityDetail.objects.all()
                return render(request, 'web/home.html', {'deletedorders': deletedorders, 'feedbacks': feedbacks, 'restaurant_details': restaurant_details})

        except ValueError:
            return render(request, 'web/feddback.html', {'deletedorders': deletedorders, 'form': FeedbackForm(), 'error': 'Bad information data'})


@login_required
def welcomefeedback(request):
    deletedorders = Order.objects.filter(user=request.user, deleted=True)
    if request.method == 'GET':
        return render(request, 'web/welcomefeedback.html', {'deletedorders': deletedorders, 'form': FeedbackForm()})
    else:
        try:
            form = FeedbackForm(request.POST, files=request.FILES)
            # το αποθηκεύουμε προσωρινά στο commend.
            commend = form.save(commit=False)
            commend.user = request.user  # Συνδέουμε τον User με το commend.
            commend.save()  # Τωρα κάνουμε save
            return redirect('home')
        except ValueError:
            return render(request, 'web/feddback.html', {'deletedorders': deletedorders, 'form': FeedbackForm(), 'error': 'Bad information data'})


@login_required
def allmyfeedback(request):
    deletedorders = Order.objects.filter(user=request.user, deleted=True)
    ordersnumber = Order.objects.filter(user=request.user, deleted=False)
    feedbacksnumber = Feeddback.objects.filter(
        user=request.user, deleted=False)
    restaurant_details = CityDetail.objects.all()

    feedbacks = Feeddback.objects.filter(user=request.user, deleted=False)
    return render(request, 'web/allmyfeedback.html', {'ordersnumber': ordersnumber, 'deletedorders': deletedorders, 
    'feedbacksnumber': feedbacksnumber, 'feedbacks': feedbacks, 'restaurant_details': restaurant_details, 'feeddbacks': feedbacks})


@login_required
def viewfeedback(request, feedback_pk):
    ordersnumber = Order.objects.filter(user=request.user, deleted=False)
    deletedorders = Order.objects.filter(user=request.user, deleted=True)
    feedbacks = Feeddback.objects.filter(deleted=False)
    feedbacksnumber = Feeddback.objects.filter(
        user=request.user, deleted=False)
    restaurant_details = CityDetail.objects.all()

    feedbacks = Feeddback.objects.filter(user=request.user, deleted=False)
    viewfeedback = get_object_or_404(
        Feeddback, pk=feedback_pk, user=request.user)

    if request.method == "GET":
        form = FeedbackForm(instance=viewfeedback)
        return render(request, 'web/viewfeedback.html', {'ordersnumber': ordersnumber, 'deletedorders': deletedorders, 
        'feedbacksnumber': feedbacksnumber, 'feedbacks': feedbacks, 'restaurant_details': restaurant_details, 'viewfeeddbacks': viewfeedback, 'form': form})

    else:
        try:
            # Files request files for uploading via USER and not ONLY via Admin.
            form = FeedbackForm(
                request.POST, files=request.FILES, instance=viewfeedback)
            form.save()        # ΠΡΟΣΟΧΗ ΔΕΝ κάνει DELETE απο τον ADMIN ΜΟΝΟ απο τον USER

            return render(request, 'web/allmyfeedback.html', {'deletedorders': deletedorders, 'feedbacksnumber': feedbacksnumber, 
            'feedbacks': feedbacks, 'restaurant_details': restaurant_details, 'feeddbacks': feedbacks, 'saved': 'Changes Saved'})
        except ValueError:
            return render(request, 'web/viewfeedback.html', {'deletedorders': deletedorders, 'feedbacksnumber': feedbacksnumber, 
            'feedbacks': feedbacks, 'restaurant_details': restaurant_details, 'viewfeeddbacks': viewfeedback, 'form': form, 'error': 'Bad Info'})


@login_required
def deletefeedback(request, feedback_pk):
    viewfeedback = get_object_or_404(
        Feeddback, pk=feedback_pk, user=request.user)

    if request.method == "POST":
        viewfeedback.delete()        # ΠΡΟΣΟΧΗ ΔΕΝ κάνει DELETE απο τον ADMIN ΜΟΝΟ απο τον USER
        return redirect('allmyfeedback')
        # return render(request, 'web/allmyfeedback.html', {'viewfeeddbacks': viewfeedback, 'saved': 'Feedback Deleted Permanently'})
    else:
        return redirect('allmyfeedback')


@login_required
def deletedfeedback(request):

    ordersnumber = Order.objects.filter(user=request.user, deleted=False)
    deletedorders = Order.objects.filter(user=request.user, deleted=True)
    feedbacks = Feeddback.objects.filter(deleted=False)
    feedbacksnumber = Feeddback.objects.filter(
        user=request.user, deleted=False)
    restaurant_details = CityDetail.objects.all()

    feedbacks = Feeddback.objects.filter(user=request.user, deleted=True)
    return render(request, 'web/deletedfeedback.html', {'ordersnumber': ordersnumber, 'deletedorders': deletedorders, 
    'feedbacksnumber': feedbacksnumber, 'feedbacks': feedbacks, 'restaurant_details': restaurant_details, 'feeddbacks': feedbacks})


@login_required
def viewdeletedfeedback(request, feedback_pk):
    ordersnumber = Order.objects.filter(user=request.user, deleted=False)
    deletedorders = Order.objects.filter(user=request.user, deleted=True)
    viewfeedback = get_object_or_404(
        Feeddback, pk=feedback_pk, user=request.user)

    feedbacks = Feeddback.objects.filter(deleted=False)
    feedbacksnumber = Feeddback.objects.filter(
        user=request.user, deleted=False)
    restaurant_details = CityDetail.objects.all()

    if request.method == "GET":
        form = FeedbackForm(instance=viewfeedback)
        return render(request, 'web/viewfeedback.html', {'ordersnumber': ordersnumber, 'deletedorders': deletedorders, 'feedbacksnumber': feedbacksnumber,
        'feedbacks': feedbacks, 'restaurant_details': restaurant_details, 'viewfeeddbacks': viewfeedback, 'form': form})

    else:
        try:
            form = FeedbackForm(
                request.POST, files=request.FILES, instance=viewfeedback)
            form.save()        # ΠΡΟΣΟΧΗ ΔΕΝ κάνει DELETE απο τον ADMIN ΜΟΝΟ απο τον USER

            feedbacks = Feeddback.objects.filter(
                user=request.user, deleted=True)
            return render(request, 'web/deletedfeedback.html', {'ordersnumber': ordersnumber, 'deletedorders': deletedorders, 'feedbacksnumber': feedbacksnumber,
            'feedbacks': feedbacks, 'restaurant_details': restaurant_details, 'feeddbacks': feedbacks, 'saved': 'Changes Saved'})
        except ValueError:
            return render(request, 'web/viewfeedback.html', {'ordersnumber': ordersnumber, 'deletedorders': deletedorders, 'viewfeeddbacks': viewfeedback,
            'form': form, 'error': 'Bad Info'})








# ORDERS



@login_required
def order(request):
    feedbacksnumber = Feeddback.objects.filter(
        user=request.user, deleted=False)
    deletedorders = Order.objects.filter(user=request.user, deleted=True)
    previus_order = Order.objects.filter(user=request.user).all()

    # όχι User εδω.. # όχι User εδω..
    orders = Order.objects.filter(deleted=False)
    ordersnumber = Order.objects.filter(user=request.user, deleted=False)
    restaurant_details = CityDetail.objects.all()

    english_order = 'order'
    greek_order = 'greekorder'

    if request.method == 'GET':
        # Προσοχή εδώ βάζεις και την () στο FeedbackForm γιατί είναι δική μας η Form.
        return render(request, 'web/order.html', {'greek_order': greek_order, 'english_order': english_order, 
        'feedbacksnumber': feedbacksnumber, 'deletedorders': deletedorders,
        'ordersnumber': ordersnumber, 'orders': orders, 'restaurant_details': restaurant_details, 'form': OrderForm()})
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

                    return redirect('home')

            commend.save()  # Τωρα κάνουμε save
            try:
                orders = Order.objects.filter(deleted=False)
                ordersnumber = Order.objects.filter(
                    user=request.user, deleted=False)
                restaurant_details = CityDetail.objects.all()

                return render(request, 'web/home.html', {'feedbacksnumber': feedbacksnumber, 'deletedorders': deletedorders, 'Thanks': "Your order has been placed. Thank you.",
                                                         'ordersnumber': ordersnumber, 'orders': orders, 'restaurant_details': restaurant_details})

            except TypeError:
                # όχι User εδω..
                orders = Order.objects.filter(deleted=False)
                restaurant_details = CityDetail.objects.all()
                return render(request, 'web/home.html', {'feedbacksnumber': feedbacksnumber, 'deletedorders': deletedorders, 
                'orders': orders, 'restaurant_details': restaurant_details})

        except ValueError:
            return render(request, 'web/order.html', {'greek_order': greek_order, 'english_order': english_order,
            'feedbacksnumber': feedbacksnumber, 'deletedorders': deletedorders,
            'form': OrderForm(), 'error': 'Bad information data'})


@login_required
def allmyorders(request):
    feedbacksnumber = Feeddback.objects.filter(
        user=request.user, deleted=False)
    deletedorders = Order.objects.filter(user=request.user, deleted=True)
    ordersnumber = Order.objects.filter(user=request.user, deleted=False)
    restaurant_details = CityDetail.objects.all()

    orders = Order.objects.filter(user=request.user, deleted=False)

    english_order = 'allmyorders'
    greek_order = 'greekallmyorders'
    
    return render(request, 'web/allmyorders.html', {'greek_order': greek_order, 'english_order': english_order, 
    'feedbacksnumber': feedbacksnumber, 'deletedorders': deletedorders,
    'ordersnumber': ordersnumber, 'orders': orders, 'restaurant_details': restaurant_details, 'deletedorders': deletedorders})


@login_required
def vieworder(request, order_pk):
    feedbacksnumber = Feeddback.objects.filter(
        user=request.user, deleted=False)
    deletedorders = Order.objects.filter(user=request.user, deleted=True) 

    # orders = Order.objects.filter(deleted=False)
    ordersnumber = Order.objects.filter(user=request.user, deleted=False)
    restaurant_details = CityDetail.objects.all()

    orders = Order.objects.filter(user=request.user, deleted=False)
    vieworder = get_object_or_404(Order, pk=order_pk, user=request.user)

    english_order = f"vieworder"
    greek_order = f"greekvieworder"

    if request.method == "GET":
        form = OrderForm(instance=vieworder)
        return render(request, 'web/vieworder.html', {'greek_order': greek_order, 'english_order': english_order,
        'feedbacksnumber': feedbacksnumber, 'deletedorders': deletedorders,
        'ordersnumber': ordersnumber, 'orders': orders, 
        'restaurant_details': restaurant_details, 'vieworders': vieworder, 'form': form})

    else:
        try:
            form = OrderForm(request.POST, files=request.FILES,
                             instance=vieworder)
            form.save()
            orders = Order.objects.filter(user=request.user, deleted=False)

            english_order = f"allmyorders"
            greek_order = f"greekallmyorders"

            return render(request, 'web/allmyorders.html', {'greek_order': greek_order, 'english_order': english_order,
            'feedbacksnumber': feedbacksnumber, 'deletedorders': deletedorders,
            'ordersnumber': ordersnumber, 'orders': orders, 'restaurant_details': restaurant_details, 'saved': 'Changes Saved'})
        except ValueError:
            return render(request, 'web/vieworder.html', {'greek_order': greek_order, 'english_order': english_order, 
            'feedbacksnumber': feedbacksnumber, 'deletedorders': deletedorders,
            'ordersnumber': ordersnumber, 'orders': orders, 'restaurant_details': restaurant_details, 'vieworders': vieworder, 'form': form, 'error': 'Bad Info'})


@login_required
def deleteorder(request, order_pk):
    vieworder = get_object_or_404(
        Order, pk=order_pk, user=request.user)

    if request.method == "POST":
        vieworder.delete()
        return redirect('allmyorders')
        # return render(request, 'web/allmyfeedback.html', {'viewfeeddbacks': viewfeedback, 'saved': 'Feedback Deleted Permanently'})
    else:
        return redirect('allmyorders')


@login_required
def deletedorders(request):
    feedbacksnumber = Feeddback.objects.filter(
        user=request.user, deleted=False)
    deletedorders = Order.objects.filter(user=request.user, deleted=True)

    restaurant_details = CityDetail.objects.all()
    orders = Order.objects.filter(user=request.user, deleted=True)
    ordersnumber = Order.objects.filter(user=request.user, deleted=False)

    if request.method == 'GET':
        return render(request, 'web/deletedorders.html', {'feedbacksnumber': feedbacksnumber, 'deletedorders': deletedorders, 
        'ordersnumber': ordersnumber, 'orders': orders, 'restaurant_details': restaurant_details})
    else:
        return redirect('deletedorders')


@login_required
def reviewdeletedorders(request, order_pk):
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
        return render(request, 'web/revieworder.html', {'feedbacksnumber': feedbacksnumber, 'deletedorders': deletedorders, 
        'ordersnumber': ordersnumber, 'orders': orders, 'restaurant_details': restaurant_details, 'vieworders': vieworder, 'form': form})

    else:
        try:
            form = OrderForm(
                request.POST, files=request.FILES, instance=vieworder)
            form.save()        # ΠΡΟΣΟΧΗ ΔΕΝ κάνει DELETE απο τον ADMIN ΜΟΝΟ απο τον USER

            orders = Order.objects.filter(
                user=request.user, deleted=True)
            return render(request, 'web/deletedorders.html', {'feedbacksnumber': feedbacksnumber, 'deletedorders': deletedorders, 
            'ordersnumber': ordersnumber, 'orders': orders, 'restaurant_details': restaurant_details, 'saved': 'Changes Saved'})

        except ValueError:
            return render(request, 'web/deletedorders.html', {'feedbacksnumber': feedbacksnumber, 'deletedorders': deletedorders, 
            'vieworders': vieworder, 'form': form, 'error': 'Bad Info'})


@login_required
def deletedeletedorder(request, order_pk):
    vieworder = get_object_or_404(
        Order, pk=order_pk, user=request.user)

    if request.method == "POST":
        vieworder.delete()
        return redirect('deletedorders')
        # return render(request, 'web/allmyfeedback.html', {'viewfeeddbacks': viewfeedback, 'saved': 'Feedback Deleted Permanently'})
    else:
        return redirect('deletedorders')
