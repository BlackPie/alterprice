Marionette   = require 'backbone.marionette'

PricelistCategoryItemTemplate = require 'templates/client/PricelistCategoryItem'
Number = require 'base/utils/Number'


module.exports = class ClientPricelistDetailCategoriesItemView extends Marionette.ItemView
    tagName: 'tr'

    ui:
        numberEl: '.number-input-wrapper'

    serializeModel: (model) ->
        data = super(model)
        data.viewURL = model.getViewURL()
        return data

    initialize: (options) =>
        @channel = options.channel

    onRender: =>
        Number.init @$(@ui.numberEl)


    template: (object) ->
        return PricelistCategoryItemTemplate(object)