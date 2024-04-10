from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Listing, User, Bid, Comment, CATEGORY_CHOICES
from .forms import ListingForm

from decimal import Decimal



def index(request):
    listings = Listing.objects.filter(is_open=True)
    context = { 'listings' : listings }
    return render(request, "auctions/index.html", context)

def closed_listings(request):
    listings = Listing.objects.filter(is_open=False)
    context = { 'listings' : listings }
    return render(request, "auctions/index.html", context)

def create_listing(request):
    if request.method == 'POST':

        form = ListingForm(request.POST)
        if form.is_valid():
            # Process the form data
            listing = form.save(commit=False)  # create new listing object but don't officially save yet
            listing.created_by = request.user  
            listing.save()  # Save to DB now
            return redirect('success')

    else:
        form = ListingForm()

    return render(request, 'auctions/new.html', {'form': form})

def edit_listing(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            return redirect('listing', listing_id=listing_id)
    else:
        form = ListingForm(instance=listing)
    return render(request, 'auctions/edit.html', {'form': form})

def delete_listing(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    listing.delete()
    return redirect('index')
#untested
def close_listing(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    listing.is_open = False
    listing.save()
    return redirect('index')

def success(request):
    return render(request, 'auctions/success.html')

def listing(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    return render(request, 'auctions/listing.html', {'listing': listing})

def watchlist(request):
    user = request.user
    watchlist = user.watchlist.all()
    return render(request, 'auctions/watchlist.html', {'watchlist': watchlist})

def add_to_watchlist(request, listing_id):
    user = request.user
    listing = Listing.objects.get(pk=listing_id)
    user.watchlist.add(listing)
    referer = request.META.get('HTTP_REFERER')
    return redirect(referer) if referer else HttpResponseBadRequest("Invalid Referer")

def remove_from_watchlist(request, listing_id):
    user = request.user
    listing = Listing.objects.get(pk=listing_id)
    user.watchlist.remove(listing)
    referer = request.META.get('HTTP_REFERER')
    return redirect(referer) if referer else HttpResponseBadRequest("Invalid Referer")

def categories(request):
    return render(request, 'auctions/categories.html', {'CATEGORY_CHOICES': CATEGORY_CHOICES})

def category(request, category):
    listings = Listing.objects.filter(category=category)
    category_dict = dict(CATEGORY_CHOICES)
    return render(request, 'auctions/category.html', {'listings': listings, 'category': category, 'category_name': category_dict[category]})

def place_bid(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    if listing.is_open == False:
        error_message = "Bidding for this item is closed."
        return render(request, 'auctions/listing.html', {'listing': listing, 'error_message': error_message})

    if request.method == 'POST':
        amount_str = request.POST['amount']
        amount = Decimal(amount_str)
        if amount > listing.starting_bid and (listing.highest_bid == None or amount > listing.highest_bid.amount):
            new_bid = Bid(created_by=request.user, listing=listing, amount=amount)
            new_bid.save()
            listing.highest_bid = new_bid
            listing.save()
            return redirect('bid_success')
        else:
            error_message = "Bid must be higher than the current highest bid and the starting bid."
            return render(request, 'auctions/listing.html', {'listing': listing, 'error_message': error_message})
        
    referer = request.META.get('HTTP_REFERER')
    return redirect(referer) if referer else HttpResponseBadRequest("Invalid Referer")

def bid_success(request):
    return render(request, 'auctions/bid_success.html')


def add_comment(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    if request.method == 'POST':
        content = request.POST['content']
        comment = Comment(created_by=request.user, listing=listing, content=content)
        comment.save()
        return render(request, 'auctions/listing.html', {'listing': listing })
    else:
        return render(request, 'auctions/listing.html', {'listing': listing})
#untested 
def delete_comment(request, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    listing = comment.listing
    comment.delete()
    return render(request, 'auctions/listing.html', {'listing': listing})

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
