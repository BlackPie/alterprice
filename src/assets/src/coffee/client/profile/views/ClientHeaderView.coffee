$ = require 'jquery'
Backbone = require 'backbone'
Marionette = require 'backbone.marionette'


module.exports = class ClientHeaderView extends Marionette.ItemView
    el: $('#header-block')

    template: false

    ui:
        dropdownBtn: '.dropdown-btn'
        overlay: '.overlay'
        changeShopForm: '#change-shop-form'
        changeShopIdInput: '#change-shop-form-input'
        changeShopLink: '.choose-this-shop'

    events:
        "click @ui.dropdownBtn": "onClickDropdownBtn"
        "click @ui.overlay": "onClickOverlay"
        "click @ui.changeShopLink": "onClickChangeShopLink"


    initialize: (options) =>
        @channel = options.channel


    onClickDropdownBtn: (e) =>
        e.preventDefault()
        el = @$(e.target)
        wrapper = el.closest '.select-wrapper'
        wrapper.find('.overlay').show()
        wrapper.find('.choices').fadeIn 'fast'


    onClickOverlay: (e) =>
        e.preventDefault()
        el = @$(e.target)
        wrapper = el.closest '.select-wrapper'
        el.hide()
        wrapper.find('.choices').fadeOut 'fast'


    onClickChangeShopLink: (e) =>
        e.preventDefault()
        el = @$(e.target)
        shopId = el.attr 'data-id'
        @$(@ui.changeShopIdInput).val(shopId)
        @$(@ui.changeShopForm).submit()



