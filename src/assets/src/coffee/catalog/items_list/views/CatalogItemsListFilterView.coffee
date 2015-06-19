$ = require 'jquery'
Backbone = require 'backbone'
Marionette = require 'backbone.marionette'
Events = require 'catalog/Events'
Checkbox = require 'base/utils/Checkbox'


module.exports = class CatalogItemsListFilterView extends Marionette.ItemView
    el: $('#catalog-products-filter-view')

    template: false

    ui:
        checkboxLabel: 'label.checkbox'
        checkboxInput: 'label.checkbox input'
        submitBtn: '.submit'
        priceFromInput: '#price_from'
        priceTillInput: '#price_till'
        filterForm: 'form.items-filter'

    events:
        "change @ui.checkboxInput": "onChangeCheckboxInput"
        "focusin @ui.priceFromInput": "onFocusInPriceInput"
        "focusin @ui.priceTillInput": "onFocusInPriceInput"
        "focusout @ui.priceFromInput": "onFocusOutPriceInput"
        "focusout @ui.priceTillInput": "onFocusOutPriceInput"
        "change @ui.priceFromInput": "onChangePriceInput"
        "change @ui.priceTillInput": "onChangePriceInput"
        "submit @ui.filterForm": "onSubmitFilterForm"


    initialize: (options) =>
        @channel = options.channel

        Checkbox.init @$(@ui.checkboxLabel)


    onChangeCheckboxInput: (e) =>
        _ = @
        el = @$(e.target).closest('label')
        offset = el.position()
        priceFromInput = @$(@ui.priceFromInput)

        $.ajax
            url: '/api/product/list/count/'
            type: 'POST'
            data: @getFilterData()
            success: (response) =>
                if response.status == 'success'
                    _.showSubmitBtn response.data.product_count, offset.top


    getFilterData: =>
        data =
            price_min: @$(@ui.priceFromInput).val()
            price_max: @$(@ui.priceTillInput).val()
        return data


    onFocusInPriceInput: (e) =>
        @$(e.target).closest('label').addClass 'focus'


    onFocusOutPriceInput: (e) =>
        @$(e.target).closest('label').removeClass 'focus'


    onChangePriceInput: (e) =>
        _ = @
        priceFromInput = @$(@ui.priceFromInput)
        $.ajax
            url: '/api/product/list/count/'
            type: 'POST'
            data: @getFilterData()
            success: (response) =>
                if response.status == 'success'
                    offset = priceFromInput.position()
                    _.showSubmitBtn response.data.product_count, offset.top - 8


    showSubmitBtn: (count, offset) =>
        submitBtn = @$(@ui.submitBtn)
        submitBtn.find('span').text "(#{count})"
        submitBtn.css 'top', offset
        submitBtn.addClass 'show'


    onSubmitFilterForm: (e) =>
        e.preventDefault()
        @channel.vent.trigger Events.SET_FILTER