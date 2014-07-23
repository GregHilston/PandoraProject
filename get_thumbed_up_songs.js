var section_counts = [].slice.call(document.getElementsByClassName('section_count')),
    counts = section_counts.map(function (e) {
        return e.textContent;
    }),
    total = counts.reduce(function (e, f) {
        return eval(e) + eval(f);
    }, 0);

var gettotal = function () {
    return document.querySelectorAll('.section.clearfix').length;
}
setTimeout(function repeater() {
    if (gettotal() < total) {
        var showmore = document.querySelector('.show_more');
        if (showmore) {
            showmore.click();
            showmore.parentElement.removeChild(showmore);
        }
        setTimeout(repeater, 100);
    }
});
