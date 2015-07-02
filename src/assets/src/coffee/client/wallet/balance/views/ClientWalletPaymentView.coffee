Marionette   = require 'backbone.marionette'

PaymentTrTemplate = require 'templates/client/PaymentTr'
Events = require 'catalog/Events'


module.exports = class ClientWalletPaymentView extends Marionette.ItemView
    #ui:
    #    btn: ".btn"

    tagName: 'tr'

    serializeModel: (model) ->
        data = super(model)
        data.viewURL = model.getViewURL()
        return data

    initialize: (options) =>
        @channel = options.channel

    template: (object) ->
        return PaymentTrTemplate(object)
