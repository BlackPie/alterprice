$ = require 'jquery'
Backbone = require 'backbone'
Marionette = require 'backbone.marionette'
CatalogSearchCategoryView = require './CatalogSearchCategoryView'
CatalogSearchCategoriesListTpl = require 'templates/product/CatalogSearchCategoriesList'
DeclensionOfNumber = require 'base/utils/DeclensionOfNumber'


module.exports = class CatalogSearchCategoriesListView extends Marionette.CompositeView
    template: CatalogSearchCategoriesListTpl

    childViewContainer: '.category-tabs'

    categoriesWidth = 0

    ui:
        showAllBtn: '.show-all'
        categoriesWrapper: '.categories-filter'

    events:
        "click @ui.showAllBtn": "onClickShowAllBtn"

    initialize: (options) =>
        @channel = options.channel

    getChildView: (model) =>
        return CatalogSearchCategoryView

    childViewOptions: (model, index) =>
        return {channel: @channel}

    initMoreBtn: =>
        categoriesWrapper = @$(@ui.categoriesWrapper)
        maxWidth = categoriesWrapper.width()
        width = 0
        number = 0
        categoriesWrapper.find('a').each (i, el) =>
            width = width + $(el).outerWidth() + 5
            number = number + 1
        if width > maxWidth
            str = DeclensionOfNumber.run(number, ['категория', 'категории', 'категорий'])
            @$(@ui.showAllBtn).text("Все #{number} #{str}").fadeIn 'slow'

    onClickShowAllBtn: (e) =>
        e.preventDefault()
        @$(@ui.showAllBtn).hide()
        @$(@ui.categoriesWrapper).css 'height', 'auto'