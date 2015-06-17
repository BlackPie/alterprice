template = (locals) =>
    if locals.shop == undefined
        return null


    priceFormat = (_number) =>
        decimal= 0
        separator= ' '
        r = parseFloat(_number)
        exp10 =Math.pow(10,decimal)
        r = Math.round(r*exp10)/exp10
        rr = Number(r).toFixed(decimal).toString().split('.')
        b = rr[0].replace(/(\d{1,3}(?=(\d{3})+(?:\.\d|\b)))/g,"\$1"+separator)
        return b

    price = priceFormat locals.price

    rating = {}
    for i in [0..5]
        if locals.point >= i + 1
            rating[i + 1] = 'yellow'
        else
            rating[i + 1] = 'grey'

    deliveries = []
    for delivery of locals.productshopdelivery
        if locals.productshopdelivery[delivery]
            switch delivery
                when "delivery" then deliveries.push 'Доставка'
                when "pickup" then deliveries.push 'Самовывоз'
    deliveries = deliveries.join(', ')

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
        <a href=\"#\" class=\"btn btn-purple btn-full-width\">В магазин</a>
    </div>
</div>"


module.exports = template