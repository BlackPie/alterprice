$ = require 'jquery'
Backbone = require 'backbone'
Marionette = require 'backbone.marionette'


module.exports = class ProductGalleryView extends Marionette.ItemView
    el: $('#product-gallery-view')

    template: false

    ui:
        imageLink: '.gallery-image-link'
        imagesNav: '.navigation'
        imageView: '.image'

    events:
        "click @ui.imageLink": "onClickImageLink"


    initialize: (options) =>
        @channel = options.channel


    onClickImageLink: (e) =>
        e.preventDefault()
        newActiveLink = @$(e.target)
        image = newActiveLink.attr 'data-image'
        activeLink = @$(@ui.imagesNav).find '.active'
        activeLink.removeClass 'active'
        newActiveLink.parent('li').addClass 'active'
        @$(@ui.imageView).css 'background-image', "url(#{image})"