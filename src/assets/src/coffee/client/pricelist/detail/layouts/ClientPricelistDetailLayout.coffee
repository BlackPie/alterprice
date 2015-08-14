$ = require 'jquery'
Marionette = require 'backbone.marionette'


module.exports = class ClientPricelistDetailLayout extends Marionette.LayoutView
    el: $('#client-pricelist-detail')

    regions:
        categoriesList:  "#client-pricelist-detail-categories-view"
        productsList:  "#client-pricelist-detail-products-view"
