$ = require 'jquery'
Marionette = require 'backbone.marionette'


module.exports = class ClientWalletBalanceLayout extends Marionette.LayoutView
    el: $('#payments-page')

    regions:
        paymentsList:  "#client-wallet-payments-layout"