Marionette   = require 'backbone.marionette'

CategoryCardTemplate = require 'templates/product/CategoryCard'
Events = require 'catalog/Events'


module.exports = class CatalogSearchCategoryView extends Marionette.ItemView
    ui:
        btn: ".btn"

    events:
        "click @ui.btn": "onClickBtn"

    serializeModel: (model) ->
        data = super(model)
        data.viewURL = model.getViewURL()
        return data

    initialize: (options) =>
        @channel = options.channel

    template: (object) ->
        return CategoryCardTemplate(object)

    onClickBtn: (e) =>
        e.preventDefault()
        if @$(e.target).hasClass 'active'
            categoryId = ''
        else
            categoryId = @$(@ui.btn).attr 'data-category'
        @channel.vent.trigger Events.SET_CATEGORY, categoryId
