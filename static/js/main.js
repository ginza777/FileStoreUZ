function search() {
    search_word = document.getElementById(`search-box`).value

    console.log(search_word)
    if (search_word != "") {


        var url = `search_book/`
        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({
                'search':search_word,

            })
        })
            .then((response) => {
                    response.json().then((data) => {
                        data = data['data']
                        console.log(data)







                    html=``

                    for(let i=0;i<data.length;i++){

                                     html2=`
                                    <div class="swiper-slide box">
                                            <div class="icons">
                                            <a href="#" class="fas fa-search"></a>
                                            <a href="#" class="fas fa-heart"></a>
                                            <a href="#" class="fas fa-eye"></a>
                                    </div>
                                    <div class="image">
                                        <img src=${data[i]['img']} alt="">
                                    </div>
                                    <div class="content">
                                         <h3>${data[i]['title'].slice(0,40)} ...</h3>
                                        <div class="price">Free <span style="color: red"> Premium</span></div>
                                        <a href="#" class="btn">download</a>
                                    </div>
                                    </div>`
                               html=html+html2



                    }







                        document.getElementById("natija").innerHTML = html
                         document.getElementById("search_div").hidden = false;




                    })

                }
            )
    }

    else {
        document.location.href = '/book/';



                      }



}