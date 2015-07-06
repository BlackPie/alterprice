$ = require 'jquery'
Backbone = require 'backbone'
Marionette   = require 'backbone.marionette'

PagerTemplate = require 'templates/pager'
Events = require 'client/Events'


module.exports = class ClientPricelistDetailProductsPagerView extends Marionette.ItemView
    el: $('#client-pricelist-detail-products-pager-view')

    ui:
        'links': 'a'
        'prevBtn': '.prev'
        'nextBtn': '.next'

    events:
        "click @ui.links": "onClickLink"


    initialize: (options) =>
        @channel = options.channel


    template: (object) ->
        return PagerTemplate(object)


    render: (response, options) =>
        locals = {
            pageSize: options.pageSize
            currentPage: options.currentPage
            count: response.count
            countPages: Math.ceil(response.count / options.pageSize)
        }
        @$el.html @template(locals)


    onClickLink: (e) =>
        e.preventDefault()
        @$el.find('.active').removeClass 'active'
        link = @$(e.target)
        page = parseInt link.attr('data-page')
        @$el.find("a.toPage[data-page=\"#{page}\"]").closest('li').addClass('active')

        if page > 1
            @$(@ui.prevBtn).removeClass 'hide'
        else
            @$(@ui.prevBtn).addClass 'hide'

        if page < @$el.find('.toPage').size()
            @$(@ui.nextBtn).removeClass 'hide'
        else
            @$(@ui.nextBtn).addClass 'hide'

        @$(@ui.prevBtn).find('a').attr 'data-page', page - 1
        @$(@ui.nextBtn).find('a').attr 'data-page', page + 1
        @channel.vent.trigger Events.PRICELIST_PRODUCTS_PAGER, page