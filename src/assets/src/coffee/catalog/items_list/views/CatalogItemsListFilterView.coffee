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
        brandInput: '.brand-input'
        categoryInput: '#category'
        searchInput: '#search'

    events:
        "change @ui.checkboxInput": "onChangeCheckboxInput"
        "focusin @ui.priceFromInput": "onFocusInPriceInput"
        "focusin @ui.priceTillInput": "onFocusInPriceInput"
        "focusout @ui.priceFromInput": "onFocusOutPriceInput"
        "focusout @ui.priceTillInput": "onFocusOutPriceInput"
        "change @ui.priceFromInput": "onChangePriceInput"
        "change @ui.priceTillInput": "onChangePriceInput"
        "submit @ui.filterForm": "onSubmitFilterForm"
        "keyup @ui.priceFromInput": "onKeyupPriceInput"
        "keyup @ui.priceTillInput": "onKeyupPriceInput"


    initialize: (options) =>
        @channel = options.channel

        Checkbox.init @$(@ui.checkboxLabel)


    onChangeCheckboxInput: (e) =>
        _ = @
        el = @$(e.target).closest('label')
        offset = el.position()

        $.ajax
            url: '/api/product/list/count/'
            type: 'POST'
            data: @getFilterData()
            success: (response) =>
                if response.status == 'success'
                    _.showSubmitBtn response.product_count, offset.top


    getFilterData: =>
        data =
            price_min: @$(@ui.priceFromInput).val()
            price_max: @$(@ui.priceTillInput).val()
            category: @$(@ui.categoryInput).val()
            search: @$(@ui.searchInput).val()
        brand = []
        @$(@ui.brandInput).filter(':checked').each (i, el) =>
            brand.push $(el).val()
        if brand.length > 0
            data['brand'] = brand
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
                    _.showSubmitBtn response.product_count, offset.top - 8


    showSubmitBtn: (count, offset) =>
        submitBtn = @$(@ui.submitBtn)
        submitBtn.find('span').text "(#{count})"
        submitBtn.css 'top', offset
        submitBtn.addClass 'show'


    onSubmitFilterForm: (e) =>
        e.preventDefault()
        @$(@ui.submitBtn).removeClass 'show'
        @channel.vent.trigger Events.SET_FILTER


    isNumeric: (number) =>
        if number in ['0', '1', '2', '3', '4', '5', '6', '7' , '8', '9']
            return true
        else
            return false


    onKeyupPriceInput: (e) =>
        el = @$(e.target)
        value = el.val()
        if not @isNumeric value.substring(value.length - 1) or value != ""
            value = value.substring 0, value.length - 1
            el.val value
        else
            @$(@ui.priceFromInput).change()


    setCategory: (categoryId) =>
        @$(@ui.categoryInput).val(categoryId)
