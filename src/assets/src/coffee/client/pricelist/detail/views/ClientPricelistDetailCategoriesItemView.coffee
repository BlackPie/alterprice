Marionette   = require 'backbone.marionette'
$ = require 'jquery'

PricelistCategoryItemTemplate = require 'templates/client/PricelistCategoryItem'
Number = require 'base/utils/Number'


module.exports = class ClientPricelistDetailCategoriesItemView extends Marionette.ItemView
    tagName: 'tr'

    ui:
        numberEl: '.number-input-wrapper'
        numberInput: '.number-input'

    events:
        "change @ui.numberInput": "onChangeNumber"


    serializeModel: (model) ->
        data = super(model)
        data.viewURL = model.getViewURL()
        return data


    initialize: (options) =>
        @channel = options.channel


    onRender: =>
        Number.init @$(@ui.numberEl), 3


    template: (object) ->
        return PricelistCategoryItemTemplate(object)


    onChangeNumber: (e) =>
        el = @$(e.target)
        categoryId = parseInt el.attr 'data-id'
        price = parseInt el.val()

        $.ajax
            type: 'PUT'
            dataType: 'json'
            url: "/api/shop/category/#{categoryId}/update/"
            data:
                'price': price
