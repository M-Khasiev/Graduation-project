let searchForm = document.getElementById('search');
let pageLink = document.querySelectorAll('.pages-link');

if (searchForm){
    for(let i = 0; pageLink.length > i; i++) {
        pageLink[i].addEventListener('click', function(e){
            e.preventDefault()

            let page = this.dataset.page;

            searchForm.innerHTML += `<input value=${page} name="page" type="hidden">`

            searchForm.submit()
        })
    }
}