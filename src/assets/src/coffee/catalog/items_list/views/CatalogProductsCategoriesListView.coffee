$ = require 'jquery'
Backbone = require 'backbone'
Marionette = require 'backbone.marionette'
Events = require 'catalog/Events'


module.exports = class CatalogProductsCategoriesListView extends Marionette.ItemView
    el: $('.categories-filter-wrapper')

    template: false

    ui:
        showAllBtn: '.show-all'
        categoriesWrapper: '.categories-filter'

    events:
        "click @ui.showAllBtn": "onClickShowAllBtn"


    initialize: (options) =>
        @channel = options.channel
        categoriesWrapper = @$(@ui.categoriesWrapper)
        maxWidth = categoriesWrapper.width()
        width = 0
        categoriesWrapper.find('a').each (i, el) =>
            width = width + $(el).outerWidth() + 8
        if width > maxWidth - @$(@ui.showAllBtn).outerWidth()
            @$(@ui.showAllBtn).fadeIn()



    onClickShowAllBtn: (e) =>
        e.preventDefault()
        @$(@ui.showAllBtn).hide()
        @$(@ui.categoriesWrapper).css 'height', 'auto'


    show: =>
        @$(@ui.showMoreBtn).show()

    hide: =>
        @$(@ui.showMoreBtn).hide()