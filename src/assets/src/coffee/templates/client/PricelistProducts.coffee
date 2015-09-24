template = (locals) =>
    return "<div class=\"counter-wrapper\">
        <div class=\"all-counter with-card\"><div class=\"value\">0</div><span>Товаров с карточкой</span></div>
        <div class=\"all-counter without-card\"><div class=\"value\">0</div><span>Товаров без карточки</span></div>
    </div>
    <table>
    <thead>
        <tr>
            <th>Название товара</th>
            <th class=\"text-center\" width=\"170px\">Ставка, р</th>
        </tr>
    </thead>
    <tbody>
    </tbody>
</table>"


module.exports = template
