template = (locals) =>
    return "<div class=\"counter-wrapper\">
        <div class=\"all-counter\"><div class=\"value\">0</div><span>Товаров в&nbsp;прайс-листе</span></div>
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