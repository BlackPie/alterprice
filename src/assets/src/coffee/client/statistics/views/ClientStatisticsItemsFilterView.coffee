$ = require 'jquery'
Backbone = require 'backbone'
Marionette = require 'backbone.marionette'
Events = require 'client/Events'


module.exports = class ClientStatisticsItemsFilterView extends Marionette.ItemView
    el: $('#client-statistics-product-filter-view')

    template: false

    ui:
        typeSwitcher: '.type-switcher'
        periodDropdownBtn: '.choose-period-btn'
        periodWrapper: '.period-wrapper'
        periodOverlay: '.overlay'
        periodChoices: '.choices'
        periodChoiceLink: '.choice'
        periodInput: '#period-input'
        shopInput: '.current-shop'
        pricelistInput: '.current-pricelist'

    events:
        "change @ui.typeSwitcher": "onChangeTypeSwitcher"
        "click @ui.periodDropdownBtn": "onClickPeriodDropdownBtn"
        "click @ui.periodOverlay": "onClickOverlay"
        "click @ui.periodChoiceLink": "onClickPeriodChoiceLink"


    initialize: (options) =>
        @channel = options.channel


    onChangeTypeSwitcher: (e) =>
        el = @$(e.target)
        switchers = @$(@ui.typeSwitcher)
        switchers.closest('label').removeClass 'active'
        el.closest('label').addClass 'active'
        @channel.vent.trigger Events.STATISTICS_ITEMS_FILTERED


    onClickPeriodDropdownBtn: (e) =>
        e.preventDefault()
        @$(@ui.periodChoices).fadeIn 80
        @$(@ui.periodOverlay).show()


    onClickOverlay: (e) =>
        e.preventDefault()
        @$(@ui.periodOverlay).hide()
        @$(@ui.periodChoices).fadeOut 80


    onClickPeriodChoiceLink: (e) =>
        e.preventDefault()
        el = @$(e.target)
        value = el.attr 'data-value'
        text = el.text()
        @$(@ui.periodInput).val value
        @$(@ui.periodDropdownBtn).text text
        @$(@ui.periodOverlay).hide()
        @$(@ui.periodChoices).fadeOut 80, =>
            @$(@ui.periodWrapper).find('.active').removeClass 'active'
            el.closest('li').addClass 'active'
            @channel.vent.trigger Events.STATISTICS_ITEMS_FILTERED


    getFilterData: =>
        data =
            period: @$(@ui.periodInput).val()
        if @$(@ui.shopInput)
            data['shop'] = @$(@ui.shopInput).val()
        if @$(@ui.pricelistInput)
            data['pricelist'] = @$(@ui.pricelistInput).val()
        data['type'] = @$el.find('.header label.active').find('.type-switcher').val()
        return data
