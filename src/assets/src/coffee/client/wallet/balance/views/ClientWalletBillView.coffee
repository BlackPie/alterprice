Marionette   = require 'backbone.marionette'

BillTrTemplate = require 'templates/client/BillTr'
Events = require 'catalog/Events'


module.exports = class ClientWalletBillView extends Marionette.ItemView
    tagName: 'tr'

    serializeModel: (model) ->
        data = super(model)
        data.viewURL = model.getViewURL()
        return data

    initialize: (options) =>
        @channel = options.channel

    template: (object) ->
        return BillTrTemplate(object)
