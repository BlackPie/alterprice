PrettyPrice = require 'base/utils/PrettyPrice'

template = (locals) =>
    if locals.shop == undefined
        return null

    price = PrettyPrice.format locals.price

    rating = {}
    if not locals.rating
        locals.rating = 0
    for i in [0..5]
        if locals.rating >= i + 1
            rating[i + 1] = 'yellow'
        else
            rating[i + 1] = 'grey'

    deliveries = []

    if locals.delivery_cost > 0
        deliveries.push "Доставка: #{locals.delivery_cost}Р"
    if locals.delivery_cost == 0
        deliveries.push 'Доставка бесплатно'

    if locals.pickup
        deliveries.push 'Самовывоз'


#    for delivery of locals.productshopdelivery
#        if locals.productshopdelivery[delivery]
#            switch delivery
#                when "delivery" then deliveries.push 'Доставка'
#                when "pickup" then deliveries.push 'Самовывоз'
    deliveries = deliveries.join('/')

    return "<div class=\"pure-g offer-block\">
    <div class=\"pure-u-1-4\">
        <span class=\"shop\">#{locals.shop.name}</span>
    </div>
    <div class=\"pure-u-1-6\">
        <div class=\"rating\">
            <i class=\"icon-star-#{rating[1]}\"></i>
            <i class=\"icon-star-#{rating[2]}\"></i>
            <i class=\"icon-star-#{rating[3]}\"></i>
            <i class=\"icon-star-#{rating[4]}\"></i>
            <i class=\"icon-star-#{rating[5]}\"></i>
        </div>
    </div>
    <div class=\"pure-u-1-6\">
        <div class=\"price\"><span>#{price}</span> руб</div>
    </div>
    <div class=\"pure-u-1-4\">
        <div class=\"delivery\"><i class=\"icon-delivery\"></i> #{deliveries}</div>
    </div>
    <div class=\"pure-u-1-6\">
        <a href=\"#{locals.click_url}\" target=\"_blank\" class=\"btn btn-purple btn-full-width\">В магазин</a>
    </div>
</div>"


module.exports = template