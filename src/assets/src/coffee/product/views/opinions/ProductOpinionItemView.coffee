Marionette   = require 'backbone.marionette'

OpinionItemTemplate = require 'templates/product/OfferItem'


module.exports = class ProductOpinionItemView extends Marionette.ItemView

    tagName: 'div'

    className: 'comment-block'

    serializeModel: (model) ->
        data = super(model)
        data.viewURL = model.getViewURL()
        return data

    initialize: (options) =>
        @channel = options.channel

    template: (object) ->
        return OpinionItemTemplate(object)