$ = require 'jquery'
Backbone = require 'backbone'
Marionette = require 'backbone.marionette'


module.exports = class ClientHeaderView extends Marionette.ItemView
    el: $('#header-block')

    template: false

    ui:
        dropdownBtn: '.dropdown-btn'
        overlay: '.overlay'

    events:
        "click @ui.dropdownBtn": "onClickDropdownBtn"
        "click @ui.overlay": "onClickOverlay"


    initialize: (options) =>
        @channel = options.channel


    onClickDropdownBtn: (e) =>
        console.log 'sdf'
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

