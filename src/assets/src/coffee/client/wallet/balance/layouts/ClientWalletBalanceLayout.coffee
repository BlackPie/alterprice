$ = require 'jquery'
Marionette = require 'backbone.marionette'


module.exports = class ClientWalletBalanceLayout extends Marionette.LayoutView
    el: $('#payments-page')

    regions:
        paymentsList: "#client-wallet-payments-layout"
        paymentsPager: ".client-wallet-payments-pager"
        billsList: "#client-wallet-bills-layout"
        billsPager: ".client-wallet-bills-pager"