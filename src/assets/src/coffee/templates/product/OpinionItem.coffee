template = (locals) =>

    ratingHtml = ''
    for i in [1...6]
        if locals.grade >= i
            ratingHtml = ratingHtml + "<i class=\"icon-star-yellow\"></i>"
        else
            ratingHtml = ratingHtml + "<i class=\"icon-star-grey\"></i>"

    html = "
<header>
    <div class=\"pure-g\">
        <div class=\"pure-u-1-2\">
            <div class=\"name\">#{locals.author}</div>
            <div class=\"date\">#{locals.date}</div>
            <div class=\"rating\">#{ratingHtml}</div>
        </div>
        <div class=\"pure-u-1-2 text-right\">
            <span class=\"yandex-market-review\">Отзыв с Яндекс Маркет</span>
        </div>
    </div>
</header>
<div class=\"content\">
    <dl class=\"product-review-item__stat  product-review-item__stat_type_inline\">
        <dt class=\"product-review-item__title\">Достоинства:</dt>
        <dd class=\"product-review-item__text\">#{locals.pro}</dd>
    </dl>
    <dl class=\"product-review-item__stat  product-review-item__stat_type_inline\">
        <dt class=\"product-review-item__title\">Недостатки:</dt>
        <dd class=\"product-review-item__text\">#{locals.contra}</dd>
    </dl>
    <dl class=\"product-review-item__stat  product-review-item__stat_type_inline\">
        <dt class=\"product-review-item__title\">Комментарий:</dt>
        <dd class=\"product-review-item__text\">#{locals.comment}</dd>
    </dl>
</div>"
    return html


module.exports = template;