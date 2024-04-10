from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("edit_listing/<int:listing_id>", views.edit_listing, name="edit_listing"),
    path("close_listing/<int:listing_id>", views.close_listing, name="close_listing"),
    path("delete_listing/<int:listing_id>", views.delete_listing, name="delete_listing"),
    path("success", views.success, name="success"),
    path("listing/<int:listing_id>", views.listing, name="listing"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("add_to_watchlist/<int:listing_id>", views.add_to_watchlist, name="add_to_watchlist"),
    path("remove_from_watchlist/<int:listing_id>", views.remove_from_watchlist, name="remove_from_watchlist"),
    path("categories", views.categories, name="categories"),
    path("category/<str:category>", views.category, name="category"),
    path("place_bid/<int:listing_id>", views.place_bid, name="place_bid"),
    path("bid_success", views.bid_success, name="bid_success"),
    path("add_comment/<int:listing_id>", views.add_comment, name="add_comment"),
    path("delete_comment/<int:comment_id>", views.delete_comment, name="delete_comment"),
    path("closed_listings", views.closed_listings, name="closed_listings"),
]
