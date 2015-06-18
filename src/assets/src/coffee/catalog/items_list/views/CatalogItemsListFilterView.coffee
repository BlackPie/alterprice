$ = require 'jquery'
Backbone = require 'backbone'
Marionette = require 'backbone.marionette'

Checkbox = require 'base/utils/Checkbox'


module.exports = class CatalogItemsListFilterView extends Marionette.ItemView
    el: $('.items-filter')

    template: false

    ui:
        checkboxLabel: 'label.checkbox'
        checkboxInput: 'label.checkbox input'
        submitBtn: '.submit'
        priceFromInput: '#price_from'
        priceTillInput: '#price_till'

    events:
        "change @ui.checkboxInput": "onChangeCheckboxInput"
        "focusin @ui.priceFromInput": "onFocusInPriceInput"
        "focusin @ui.priceTillInput": "onFocusInPriceInput"
        "focusout @ui.priceFromInput": "onFocusOutPriceInput"
        "focusout @ui.priceTillInput": "onFocusOutPriceInput"
        "change @ui.priceFromInput": "onChangePriceInput"
        "change @ui.priceTillInput": "onChangePriceInput"


    initialize: (options) =>
        @channel = options.channel

        Checkbox.init @$(@ui.checkboxLabel)


    onChangeCheckboxInput: (e) =>
        el = @$(e.target).closest('label')
        offset = el.position()
        submitBtn = @$(@ui.submitBtn)
        console.log offset.top
        submitBtn.css 'top', offset.top
        submitBtn.fadeIn()


    getFilterData: =>
        data =
            price_from: @$(@ui.priceFromInput).val()
            price_till: @$(@ui.priceTillInput).val()
        return data


    onFocusInPriceInput: (e) =>
        @$(e.target).closest('label').addClass 'focus'


    onFocusOutPriceInput: (e) =>
        @$(e.target).closest('label').removeClass 'focus'


    onChangePriceInput: (e) =>
        $.ajax
            url: '/api/product/list/count/'
            type: 'POST'