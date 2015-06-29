$ = require 'jquery'
Backbone = require 'backbone'
Marionette = require 'backbone.marionette'

Number = require 'base/utils/Number'


module.exports = class ClientPricelistDetailManagmentView extends Marionette.ItemView
    el: $('#client-pricelist-detail-managment-view')

    template: false

    ui:
        numberWrapper: '.number-input-wrapper'


    initialize: (options) =>
        @channel = options.channel
        Number.init @$(@ui.numberWrapper)
